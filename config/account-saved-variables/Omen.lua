
Omen3DB = {
	["profileKeys"] = {
		{% for character in all_characters %}
		["{{ character.char }} - {{ character.realm}}"] = "MyDefault",
		{% endfor %}
	},
	["profiles"] = {
		["MyDefault"] = {
			["PositionW"] = 221.3526829100494,
			["PositionH"] = 103.3512956065097,
			["VGrip2"] = 127.2777944450514,
			["PositionY"] = 393.8524456405221,
			["Locked"] = true,
			["ShowWith"] = {
				["Alone"] = true,
			},
			["VGrip1"] = 94.07489154634233,
			["PositionX"] = 1636.410517382976,
		},
	},
}
