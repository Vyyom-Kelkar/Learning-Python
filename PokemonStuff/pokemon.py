import json

TYPE_LIST = {
	'normal', 'flying', 'fighting', 'fairy',
	'rock', 'ground', 'steel',
	'water', 'ice',
	'fire', 'electric', 'dragon',
	'dark', 'ghost', 'psychic',
	'grass', 'bug', 'poison'
}

data = {}

for i in range(18):
	attacker = raw_input('Enter attacker type: ')

	strongDefenders = {n for n in raw_input('Enter strong defenders (not very effective): ').split(' ')}
	strongDefenders.discard('')
	weakDefenders = {n for n in raw_input('Enter weak defenders (super effective): ').split(' ')}
	weakDefenders.discard('')
	immuneDefenders = {n for n in raw_input('Enter immune defenders (does not effect): ').split(' ')}
	immuneDefenders.discard('')

	nonNormalDefenders = strongDefenders.union(weakDefenders, immuneDefenders)
	normalDefenders = TYPE_LIST.difference(nonNormalDefenders)

	data[attacker] = {}
	data[attacker]["super_effective"] = list(weakDefenders)
	data[attacker]["not_very_effective"] = list(strongDefenders)
	data[attacker]["does_not_effect"] = list(immuneDefenders)
	data[attacker]["normal_damage"] = list(normalDefenders)

with open("types.json", "w") as f:
	print >> f, json.dumps(data, indent=1)

