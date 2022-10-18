pmcdir = input("Your PolyMC root directory: ") + '/polymc.cfg'

lines = open(pmcdir).read().splitlines()
lines[37] = 'MetaURLOverride=https://meta.prismlauncher.org/v1/'
lines[32] = 'MSAClientIDOverride=c36a9fb6-4f2a-41ff-90bd-ae7cc92031eb'
open(pmcdir, 'w').write('\n'.join(lines))

print("Done")
