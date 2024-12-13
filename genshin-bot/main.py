import pyautogui
import cv2
import win32gui
import win32ui
import win32con
import numpy as np
from PIL import Image
import time


def capture_game_window(window_title="Genshin Impact"):
    hwnd = win32gui.FindWindow(None, window_title)
    if hwnd == 0:
        print("Окно игры не найдено!")
        return None, None

    left, top, right, bottom = win32gui.GetWindowRect(hwnd)
    width, height = right - left, bottom - top

    hwindc = win32gui.GetWindowDC(hwnd)
    srcdc = win32ui.CreateDCFromHandle(hwindc)
    memdc = srcdc.CreateCompatibleDC()

    bmp = win32ui.CreateBitmap()
    bmp.CreateCompatibleBitmap(srcdc, width, height)
    memdc.SelectObject(bmp)
    memdc.BitBlt((0, 0), (width, height), srcdc, (0, 0), win32con.SRCCOPY)

    bmpinfo = bmp.GetInfo()
    bmpstr = bmp.GetBitmapBits(True)

    img = Image.frombuffer(
        'RGB',
        (bmpinfo['bmWidth'], bmpinfo['bmHeight']),
        bmpstr, 'raw', 'BGRX', 0, 1
    )

    win32gui.DeleteObject(bmp.GetHandle())
    memdc.DeleteDC()
    srcdc.DeleteDC()
    win32gui.ReleaseDC(hwnd, hwindc)

    return np.array(img), (left, top, right, bottom)


def find_marker_on_screen(screen, marker_template_path, threshold=0.8):
    template = cv2.imread(marker_template_path, cv2.IMREAD_UNCHANGED)
    result = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    if max_val >= threshold:
        return max_loc  # Координаты маркера
    return None


def move_to_and_click(x, y, offset=(0, 0)):
    real_x, real_y = x + offset[0], y + offset[1]
    pyautogui.moveTo(real_x, real_y, duration=0.5)
    pyautogui.click()


def perform_daily_quests():
    print("Начинаем выполнение дейликов...")
    time.sleep(5)

    while True:
        screen, bounds = capture_game_window()
        if screen is None:
            print("Игра не запущена. Ожидаю...")
            time.sleep(5)
            continue

        # Ищем маркер миссии
        marker_pos = find_marker_on_screen(screen, "mission_marker.jpg")
        if marker_pos:
            print("Маркер миссии найден. Переход к выполнению.")
            left, top, _, _ = bounds
            move_to_and_click(marker_pos[0] + left, marker_pos[1] + top)

            # Ждём перехода на место задания
            time.sleep(10)
            continue

        print("Все миссии выполнены!")
        break


if __name__ == "__main__":
    perform_daily_quests()
