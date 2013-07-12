
letter_stats = {}

str = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque tempor odio a turpis consectetur, sed pellentesque metus blandit. Fusce iaculis, leo sed vehicula rutrum, massa lacus suscipit turpis, vel rhoncus purus ligula ornare lectus. Aliquam erat volutpat. Vestibulum posuere enim urna, in sollicitudin eros imperdiet vel. Vestibulum sit amet libero consequat, lobortis nulla nec, placerat dui. Morbi dapibus diam ac neque interdum, ut tincidunt leo pellentesque. Curabitur et ornare mauris, vitae vulputate enim. Quisque pretium, quam et vehicula ullamcorper, sem mi bibendum tortor, id aliquam sem metus eu urna. Donec consectetur suscipit venenatis. Donec vitae molestie nisl. Sed rutrum, turpis sit amet commo
"""

i = 0
while i < len(str):
    if not str[i].isspace():
        if str[i] in letter_stats:
          letter_stats[str[i]] += 1
        else:
    	    letter_stats[str[i]] = 1
    i += 1

for key, value in sorted(letter_stats.iteritems()):
	print("%s %d" % (key, value))


