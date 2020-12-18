
CombuctorDB2 = {
	["global"] = {
		["maxScale"] = 1.5,
	},
	["version"] = "2.2.2",
	["profiles"] = {
		{% for character in all_characters %}
		["{{ character.char }} - {{ character.realm}}"] = {
			["inventory"] = {
				["exclude"] = {
					["All"] = {
						"All", -- [1]
						"Ammo", -- [2]
					},
				},
				["h"] = 639.0606460091157,
				["position"] = {
					"RIGHT", -- [1]
					nil, -- [2]
					"RIGHT", -- [3]
					-9.609731121206739, -- [4]
					-37.9045673854006, -- [5]
				},
				["showBags"] = false,
				["bags"] = {
					-2, -- [1]
					0, -- [2]
					1, -- [3]
					2, -- [4]
					3, -- [5]
					4, -- [6]
				},
				["sets"] = {
					"All", -- [1]
					"Equipment", -- [2]
					"Usable", -- [3]
					"Quest", -- [4]
					"Trade Goods", -- [5]
					"Projectile", -- [6]
					"Soul Shard", -- [7]
					"Miscellaneous", -- [8]
				},
				["w"] = 544.1597635333388,
				["leftSideFilter"] = true,
			},
			["bank"] = {
				["h"] = 512,
				["showBags"] = false,
				["exclude"] = {
					["All"] = {
						"All", -- [1]
						"Shards", -- [2]
						"Ammo", -- [3]
						"Keys", -- [4]
					},
				},
				["sets"] = {
					"All", -- [1]
					"Equipment", -- [2]
					"Trade Goods", -- [3]
					"Miscellaneous", -- [4]
					"Usable", -- [5]
					"Quest", -- [6]
					"Projectile", -- [7]
					"Soul Shard", -- [8]
				},
				["w"] = 512,
				["bags"] = {
					-1, -- [1]
					5, -- [2]
					6, -- [3]
					7, -- [4]
					8, -- [5]
					9, -- [6]
					10, -- [7]
					11, -- [8]
				},
			},
		},
		{% endfor %}
	},
}
CombuctorVersion = nil
