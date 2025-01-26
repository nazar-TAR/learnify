import os
import time


def scary_reboot():
    print("Що це? Щось сталося...")
    time.sleep(2)

    for i in range(3):
        print(f"Перезавантаження через {3 - i} секунди...")
        time.sleep(1)

    print("\nНесподівано комп'ютер перезавантажується...")
    time.sleep(1)
    os.system('shutdown -r now')  # Перезавантаження комп'ютера без попередження


scary_reboot()

