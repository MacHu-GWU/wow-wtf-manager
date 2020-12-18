
RatingBusterDB = {
	["namespaces"] = {
		["LibDualSpec-1.0"] = {
		},
	},
	["profileKeys"] = {
		{% for character in all_characters %}
		["{{ character.char }} - {{ character.realm}}"] = "MyDefault",
		{% endfor %}
	},
	["profiles"] = {
		["MyDefault"] = {
			["showItemID"] = true,
		},
	},
}
