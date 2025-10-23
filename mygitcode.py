# 在终端打印一个红色爱心图案

def print_heart(width=60, height=30):
    for y in range(int(height/2), -int(height/2), -1):
        line = ''
        for x in range(-int(width/2), int(width/2)):
            xp = x * 2.0 / width
            yp = y * 2.0 / height
            # 心形隐式方程 (x^2 + y^2 - 1)^3 - x^2 * y^3 <= 0
            if (xp**2 + yp**2 - 1)**3 - xp**2 * yp**3 <= 0:
                line += '\x1b[31m♥\x1b[0m'  # 红色心形（ANSI）
            else:
                line += '  '
        print(line)

if __name__ == "__main__":
    print_heart(60, 30)