import os
from resources import Resources
path = os.path.dirname(os.path.abspath(__file__))


characters = []
for character_name in ['right_ray', 'R'] :
    characters.append(
        {
          "name" = character_name,
          "latex" = Resources(path=path).get(character_name + '.tex').read().decode('UTF-8-')
        })

hypotheses = set()

# todo: use jinja for this
goal = f"no proper subset of {characters[1].latex}_{{{characters[0].latex}}} is {{chara
fulltext = f"Prove that {goal}"
proof = None
No proper subset of \mathbbm{R}_{\mathcal{RR}} is \mathcal{RR}-clopen
