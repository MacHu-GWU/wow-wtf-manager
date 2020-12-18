
ParrotDB = {
	["profileKeys"] = {
		{% for character in all_characters %}
		["{{ character.char }} - {{ character.realm}}"] = "MyDefault",
		{% endfor %}
	},
	["namespaces"] = {
		["CombatEvents"] = {
			["profiles"] = {
				["Default"] = {
					["dbver"] = 3,
				},
				["MyDefault"] = {
					["dbver"] = 3,
					["disable_in_10man"] = true,
					["disable_in_25man"] = true,
				},
			},
		},
		["Debug"] = {
		},
		["Suppressions"] = {
		},
		["Display"] = {
		},
		["Cooldowns"] = {
		},
		["ScrollAreas"] = {
			["profiles"] = {
				["MyDefault"] = {
					["areas"] = {
						["Notification"] = {
							["stickyDirection"] = "UP;CENTER",
							["direction"] = "UP;CENTER",
							["stickyAnimationStyle"] = "Pow",
							["xOffset"] = 0,
							["size"] = 150,
							["animationStyle"] = "Straight",
							["yOffset"] = 175,
						},
						["Incoming"] = {
							["stickyDirection"] = "RIGHT",
							["direction"] = "DOWN;LEFT",
							["stickyAnimationStyle"] = "Horizontal",
							["iconSide"] = "RIGHT",
							["xOffset"] = 170,
							["size"] = 260,
							["animationStyle"] = "Straight",
							["yOffset"] = -30,
						},
						["Outgoing"] = {
							["stickyDirection"] = "LEFT",
							["direction"] = "UP;RIGHT",
							["stickyAnimationStyle"] = "Horizontal",
							["xOffset"] = -180,
							["size"] = 260,
							["animationStyle"] = "Straight",
							["yOffset"] = -30,
						},
					},
				},
			},
		},
		["Triggers"] = {
			["profiles"] = {
				["Default"] = {
					["dbver"] = 3,
				},
				["MyDefault"] = {
					["dbver"] = 3,
				},
			},
		},
	},
	["profiles"] = {
		["MyDefault"] = {
		},
	},
}
