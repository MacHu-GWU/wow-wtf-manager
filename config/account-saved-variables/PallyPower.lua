
PallyPowerDB = {
	["profiles"] = {
		["MyDefault"] = {
			["display"] = {
				["frameLocked"] = true,
			},
			["disable"] = false,
		},
		["class/Paladin"] = {
		},
	},
	["currentProfile"] = {
		{% for character in all_characters %}
		["{{ character.char }} - {{ character.realm}}"] = "MyDefault",
		{% endfor %}
	},
}
PallyPower_Assignments = {
	["Batlefury"] = {
		3, -- [1]
		3, -- [2]
		3, -- [3]
		3, -- [4]
		4, -- [5]
		3, -- [6]
		3, -- [7]
		3, -- [8]
		3, -- [9]
		4, -- [10]
		3, -- [11]
	},
	["Glowyy"] = {
		2, -- [1]
		2, -- [2]
		1, -- [3]
		1, -- [4]
		1, -- [5]
		1, -- [6]
		1, -- [7]
		1, -- [8]
		1, -- [9]
		2, -- [10]
		2, -- [11]
	},
}
PallyPower_NormalAssignments = {
}
PallyPower_AuraAssignments = {
	["Batlefury"] = 1,
	["Glowyy"] = 3,
}
PallyPower_SavedPresets = {
}
