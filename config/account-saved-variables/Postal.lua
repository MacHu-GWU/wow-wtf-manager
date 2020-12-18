
Postal3DB = {
	["global"] = {
		["BlackBook"] = {
			["alts"] = {
			},
		},
	},
	["profileKeys"] = {
		{% for character in all_characters %}
		["{{ character.char }} - {{ character.realm}}"] = "MyDefault",
		{% endfor %}
	},
	["profiles"] = {
		["MyDefault"] = {
			["BlackBook"] = {
				["recent"] = {
					{% for character in all_characters %}
					"{{ character.char }}",
					{% endfor %}
				},
			},
		},
	},
}
