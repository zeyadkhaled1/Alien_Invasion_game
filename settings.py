class Settings:
    """A class to store all settings for alien Invasion"""

    def __init__(self):
        """Initialize the game's static settings"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed = 1.5
        self.ship_limit = 3

        # Bullet Settings
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction of 1 representts  right;-1 represents left.
        self.fleet_direction = 1

        # How quickly  the game speeds up
        self.speedup_sclae = 1.1
        self.initialize_dynamic_settings()
        # How quickly the alien pont values increase
        self.score_scale = 1.5

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0
        # fleet_direction of 1 represents right;-1 represents left.
        self.fleet_direction = 1

        # Scoring
        self.alien_point = 50

    def increase_speed(self):
        """Increase speed settings and aliens point value"""
        self.ship_speed *= self.speedup_sclae
        self.bullet_speed *= self.speedup_sclae
        self.alien_speed *= self.speedup_sclae

        self.alien_point = int(self.alien_point*self.score_scale)
