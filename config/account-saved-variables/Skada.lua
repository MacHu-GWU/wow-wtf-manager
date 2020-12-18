
SkadaDB = {
	["profileKeys"] = {
		{% for character in all_characters %}
		["{{ character.char }} - {{ character.realm}}"] = "MyDefault",
		{% endfor %}
	},
	["profiles"] = {
		["MyDefault"] = {
			["windows"] = {
				{
					["point"] = "RIGHT",
					["barmax"] = 10,
					["scale"] = 1,
					["barfontsize"] = 14,
					["barslocked"] = true,
					["y"] = -250.9176266810352,
					["x"] = -39.15925548453697,
					["title"] = {
						["fontsize"] = 14,
					},
				}, -- [1]
			},
			["reset"] = {
				["join"] = 1,
			},
		},
	},
}
