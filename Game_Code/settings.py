class Settings:
    """存储游戏《外星人入侵》所有设置的类"""

    def __init__(self):
        """初始化游戏的设置"""
        #屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        #飞船设置
        self.ship_speed = 1.5
        self.ship_limit = 3

        #子弹设置
        self.bullet_speed = 1.0
        self.bullet_width = 100
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3

        #设置外星人的移动速递
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        #fleet_direction为1表示向右移动，-1表示向左移动
        self.fleet_direction = 1
