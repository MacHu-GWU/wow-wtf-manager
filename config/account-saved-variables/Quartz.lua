
Quartz3DB = {
	["profileKeys"] = {
		{% for character in all_characters %}
		["{{ character.char }} - {{ character.realm}}"] = "MyDefault",
		{% endfor %}
	},
	["namespaces"] = {
		["Swing"] = {
		},
		["Buff"] = {
		},
		["Interrupt"] = {
		},
		["Flight"] = {
		},
		["Pet"] = {
			["profiles"] = {
				["MyDefault"] = {
					["y"] = 255.1550707325798,
					["x"] = 941.9335619336382,
				},
			},
		},
		["Player"] = {
			["profiles"] = {
				["MyDefault"] = {
					["y"] = 280.3670408793614,
					["x"] = 822.5259491618837,
				},
			},
		},
		["GCD"] = {
		},
		["Focus"] = {
			["profiles"] = {
				["MyDefault"] = {
					["y"] = 334.3510917441489,
					["x"] = 839.4306970212091,
				},
			},
		},
		["Target"] = {
			["profiles"] = {
				["MyDefault"] = {
					["y"] = 311.4348494943892,
					["x"] = 840.6774149979098,
				},
			},
		},
		["Range"] = {
		},
		["Mirror"] = {
		},
		["Latency"] = {
		},
	},
	["profiles"] = {
		["MyDefault"] = {
			["modules"] = {
				["Buff"] = false,
			},
		},
	},
}
