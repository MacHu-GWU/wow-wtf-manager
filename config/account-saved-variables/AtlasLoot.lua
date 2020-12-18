
AtlasLootOptions = nil
AtlasLootDB = {
	["profileKeys"] = {
		{% for character in all_characters %}
		["{{ character.char }} - {{ character.realm}}"] = "MyDefault",
		{% endfor %}
	},
	["profiles"] = {
		["MyDefault"] = {
			["CraftingLink"] = 2,
			["ItemIDs"] = 1,
			["AllLinks"] = false,
			["AtlasLootVersion"] = "51103",
		},
	},
}
AtlasLootWishList = {
	["Options"] = {
	},
	["Shared"] = {
	},
	["Own"] = {
	},
}
