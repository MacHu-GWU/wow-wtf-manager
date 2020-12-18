
DominosDB = {
	["profileKeys"] = {
		{% for character in all_characters %}
		["{{ character.char }} - {{ character.realm}}"] = "MyDefault",
		{% endfor %}
	},
	["profiles"] = {
		["MyDefault"] = {
			["frames"] = {
				{
					["point"] = "BOTTOMLEFT",
					["scale"] = 1,
					["y"] = 0,
					["x"] = 482.8569256201919,
					["spacing"] = 2,
					["padH"] = 2,
					["numButtons"] = 12,
					["pages"] = {
						["WARRIOR"] = {
							["[bar:2]"] = 1,
							["[bar:3]"] = 2,
							["[bar:4]"] = 3,
							["[bar:5]"] = 4,
							["[bar:6]"] = 5,
							["[bonusbar:1]"] = 6,
							["[bonusbar:2]"] = 7,
							["[bonusbar:3]"] = 8,
						},
						["PALADIN"] = {
							["[bar:2]"] = 1,
							["[bar:3]"] = 2,
							["[bar:4]"] = 3,
							["[bar:5]"] = 4,
							["[bar:6]"] = 5,
						},
						["DEATHKNIGHT"] = {
							["[bar:2]"] = 1,
							["[bar:3]"] = 2,
							["[bar:4]"] = 3,
							["[bar:5]"] = 4,
							["[bar:6]"] = 5,
						},
						["SHAMAN"] = {
							["[bar:2]"] = 1,
							["[bar:3]"] = 2,
							["[bar:4]"] = 3,
							["[bar:5]"] = 4,
							["[bar:6]"] = 5,
						},
						["HUNTER"] = {
							["[bar:2]"] = 1,
							["[bar:3]"] = 2,
							["[bar:4]"] = 3,
							["[bar:5]"] = 4,
							["[bar:6]"] = 5,
						},
						["ROGUE"] = {
							["[bar:2]"] = 1,
							["[bar:3]"] = 2,
							["[bar:4]"] = 3,
							["[bar:5]"] = 4,
							["[bar:6]"] = 5,
							["[bonusbar:1]"] = 6,
							["[form:3]"] = 6,
						},
						["DRUID"] = {
							["[bar:2]"] = 1,
							["[bar:3]"] = 2,
							["[bar:4]"] = 3,
							["[bar:5]"] = 4,
							["[bar:6]"] = 5,
							["[bonusbar:1]"] = 6,
							["[bonusbar:2]"] = 7,
							["[bonusbar:3]"] = 8,
							["[bonusbar:4]"] = 9,
						},
						["MAGE"] = {
							["[bar:2]"] = 1,
							["[bar:3]"] = 2,
							["[bar:4]"] = 3,
							["[bar:5]"] = 4,
							["[bar:6]"] = 5,
						},
						["WARLOCK"] = {
							["[bar:2]"] = 1,
							["[bar:3]"] = 2,
							["[bar:4]"] = 3,
							["[bar:5]"] = 4,
							["[bar:6]"] = 5,
						},
						["PRIEST"] = {
							["[bonusbar:1]"] = 6,
							["[bar:6]"] = 5,
							["[bar:5]"] = 4,
							["[bar:3]"] = 2,
							["[bar:4]"] = 3,
							["[bar:2]"] = 1,
						},
					},
					["padW"] = 2,
				}, -- [1]
				{
					["point"] = "BOTTOMLEFT",
					["y"] = 30.00000041032344,
					["x"] = 489.2629607667195,
					["padW"] = 2,
					["spacing"] = 2,
					["anchor"] = "1TL",
					["numButtons"] = 12,
					["pages"] = {
						["DEATHKNIGHT"] = {
						},
						["WARRIOR"] = {
						},
						["WARLOCK"] = {
						},
						["SHAMAN"] = {
						},
						["MAGE"] = {
						},
						["DRUID"] = {
						},
						["PALADIN"] = {
						},
					},
					["padH"] = 2,
				}, -- [2]
				{
					["point"] = "BOTTOMLEFT",
					["y"] = 106.6935036430908,
					["x"] = 481.7885703175719,
					["padW"] = 2,
					["spacing"] = 2,
					["anchor"] = "2TC",
					["numButtons"] = 12,
					["pages"] = {
						["DEATHKNIGHT"] = {
						},
						["WARRIOR"] = {
						},
						["WARLOCK"] = {
						},
						["SHAMAN"] = {
						},
						["MAGE"] = {
						},
						["DRUID"] = {
						},
						["PALADIN"] = {
						},
					},
					["padH"] = 2,
				}, -- [3]
				{
					["point"] = "BOTTOMLEFT",
					["y"] = 146.6935129437554,
					["x"] = 481.7885703175719,
					["padW"] = 2,
					["spacing"] = 2,
					["anchor"] = "3TC",
					["numButtons"] = 12,
					["pages"] = {
						["DEATHKNIGHT"] = {
						},
						["WARRIOR"] = {
						},
						["WARLOCK"] = {
						},
						["SHAMAN"] = {
						},
						["MAGE"] = {
						},
						["DRUID"] = {
						},
						["PALADIN"] = {
						},
					},
					["padH"] = 2,
				}, -- [4]
				{
					["point"] = "BOTTOMLEFT",
					["y"] = 186.6935134908533,
					["x"] = 481.7885703175719,
					["padW"] = 2,
					["spacing"] = 2,
					["anchor"] = "4TL",
					["numButtons"] = 12,
					["pages"] = {
						["DEATHKNIGHT"] = {
						},
						["WARRIOR"] = {
						},
						["WARLOCK"] = {
						},
						["SHAMAN"] = {
						},
						["MAGE"] = {
						},
						["DRUID"] = {
						},
						["PALADIN"] = {
						},
					},
					["padH"] = 2,
				}, -- [5]
				{
					["point"] = "BOTTOMRIGHT",
					["padW"] = 2,
					["x"] = -472.8815361360566,
					["spacing"] = 2,
					["padH"] = 2,
					["y"] = 0,
					["numButtons"] = 12,
					["pages"] = {
						["DEATHKNIGHT"] = {
						},
						["WARRIOR"] = {
						},
						["WARLOCK"] = {
						},
						["SHAMAN"] = {
						},
						["MAGE"] = {
						},
						["DRUID"] = {
						},
						["PALADIN"] = {
						},
					},
				}, -- [6]
				{
					["point"] = "BOTTOMRIGHT",
					["y"] = 78.77212079292816,
					["x"] = -399.5730064897439,
					["padW"] = 2,
					["spacing"] = 2,
					["anchor"] = "6TC",
					["numButtons"] = 12,
					["pages"] = {
						["DEATHKNIGHT"] = {
						},
						["WARRIOR"] = {
						},
						["WARLOCK"] = {
						},
						["SHAMAN"] = {
						},
						["MAGE"] = {
						},
						["DRUID"] = {
						},
						["PALADIN"] = {
						},
					},
					["padH"] = 2,
				}, -- [7]
				{
					["point"] = "BOTTOMRIGHT",
					["y"] = 118.7721300935927,
					["x"] = -399.5730064897439,
					["padW"] = 2,
					["spacing"] = 2,
					["anchor"] = "7TC",
					["numButtons"] = 12,
					["pages"] = {
						["DEATHKNIGHT"] = {
						},
						["WARRIOR"] = {
						},
						["WARLOCK"] = {
						},
						["SHAMAN"] = {
						},
						["MAGE"] = {
						},
						["DRUID"] = {
						},
						["PALADIN"] = {
						},
					},
					["padH"] = 2,
				}, -- [8]
				{
					["point"] = "BOTTOMRIGHT",
					["y"] = 158.7721393942573,
					["x"] = -399.5730064897439,
					["padW"] = 2,
					["spacing"] = 2,
					["anchor"] = "8TC",
					["numButtons"] = 12,
					["pages"] = {
						["DEATHKNIGHT"] = {
						},
						["WARRIOR"] = {
						},
						["WARLOCK"] = {
						},
						["SHAMAN"] = {
						},
						["MAGE"] = {
						},
						["DRUID"] = {
						},
						["PALADIN"] = {
						},
					},
					["padH"] = 2,
				}, -- [9]
				{
					["point"] = "BOTTOMRIGHT",
					["y"] = 198.7721399413552,
					["x"] = -399.5730064897439,
					["padW"] = 2,
					["spacing"] = 2,
					["anchor"] = "9TC",
					["numButtons"] = 12,
					["pages"] = {
						["DEATHKNIGHT"] = {
						},
						["WARRIOR"] = {
						},
						["WARLOCK"] = {
						},
						["SHAMAN"] = {
						},
						["MAGE"] = {
						},
						["DRUID"] = {
						},
						["PALADIN"] = {
						},
					},
					["padH"] = 2,
				}, -- [10]
				["totem1"] = {
					["y"] = 362.5002511521369,
					["x"] = 603.5703954649413,
					["point"] = "BOTTOMLEFT",
					["spacing"] = 0,
					["showTotems"] = true,
					["scale"] = 0.8,
					["showRecall"] = false,
					["anchor"] = "vehicleTL",
				},
				["bags"] = {
					["hideKeyring"] = true,
					["point"] = "BOTTOMRIGHT",
					["scale"] = 1,
					["y"] = 31.66666855871362,
					["x"] = -2.334284431526612e-005,
					["spacing"] = 0,
					["anchor"] = "menuTR",
					["numButtons"] = 5,
				},
				["xp"] = {
					["point"] = "TOPLEFT",
					["scale"] = 1,
					["width"] = 0.24,
					["y"] = 0,
					["x"] = 0,
					["height"] = 14,
					["alwaysShowText"] = true,
					["texture"] = "blizzard",
				},
				["totem3"] = {
					["y"] = 398.5002744037984,
					["x"] = 603.5703954649413,
					["point"] = "BOTTOMLEFT",
					["spacing"] = 0,
					["showTotems"] = true,
					["scale"] = 0.8,
					["showRecall"] = false,
					["anchor"] = "totem1TC",
				},
				["roll"] = {
					["columns"] = 1,
					["scale"] = 0.84,
					["y"] = 0,
					["x"] = -309.9539644393717,
					["spacing"] = 2,
					["anchor"] = "6RB",
					["numButtons"] = 4,
					["point"] = "BOTTOMRIGHT",
				},
				["pet"] = {
					["y"] = 230.0002088546293,
					["x"] = 482.8563653919263,
					["point"] = "BOTTOMLEFT",
					["spacing"] = 6,
				},
				["class"] = {
					["y"] = 226.6935315450845,
					["x"] = 481.7885703175719,
					["point"] = "BOTTOMLEFT",
					["spacing"] = 2,
					["anchor"] = "5TL",
					["numButtons"] = 6,
				},
				["vehicle"] = {
					["y"] = 286.6934360764982,
					["x"] = 481.7885703175719,
					["point"] = "BOTTOMLEFT",
					["anchor"] = "petTL",
					["numButtons"] = 3,
				},
				["menu"] = {
					["y"] = 0,
					["x"] = 0.0001400570663463441,
					["point"] = "BOTTOMRIGHT",
					["spacing"] = 0,
					["scale"] = 1,
					["padW"] = 0,
					["padH"] = 0,
				},
				["totem2"] = {
					["point"] = "BOTTOMLEFT",
					["scale"] = 0.8,
					["showRecall"] = false,
					["y"] = 434.5002976554598,
					["x"] = 603.5703954649413,
					["spacing"] = 0,
					["showTotems"] = true,
					["anchor"] = "totem3TC",
				},
			},
			["showgrid"] = 1,
		},
	},
}
DominosVersion = "1.18.6"
