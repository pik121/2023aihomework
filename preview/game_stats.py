class GameStats():

    def __init__(self, ai_settings):
        #初始化
        self.ai_settings = ai_settings
        self.reset_stats()

        # 游戏状态.
        self.game_active = False

        # 最高分.
        self.high_score = 0

    def reset_stats(self):
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
