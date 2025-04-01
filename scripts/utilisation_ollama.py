import ollama

stream = ollama.chat(
    model = 'llama3.1',
    messages=[{'role':'user', 'content':f"""Style à utiliser : 'video 1' : "Cathy, fallait que je me pose là pour te faire un message. Parce que à la salle tout à l'heure, t'as fait un beau travail. Ok, t'as versé quelques larmes à la fin. Mais c'est parce que t'es passé en mode Spartan. Et parce que tu sais, tu sais pourquoi tu te bats Cathy. Tu sais pourquoi tu te bats. Ton bouti est en train de se structurer. Ton bouti devient juicy Cathy. La vie de moi je pèse mes mots. Ton bouti devient juicy. Donc ne lâche rien. T'es assa ton summer body. Ton travail sur tes ikkyo il était mais above the top. Donc demain on se retrouve, même mindset. Je prends mon checker. Ça va passer crème. Cathy, juste n'oublie pas que t'es belle. T'es belle. Allez je te fais des bisous.",
    "video 2": " Je sens de la salle, je suis juste bien là. J'ai dépassé mes limites en mode Spartan comme tous les soirs. C'est du plaisir. Devant moi j'étais à la barre, il y avait une femme très belle qui faisait des squats. Très belle plastique, sculptée, calbée, un bouti extrêmement juicy, un yoga pants nickel, un crop top d'une très grande classe. Et j'ai énormément de respect, la vie de moi, pour ces femmes qui prennent soin d'elles, qui travaillent, qui sont belles tout simplement. Moi ça me donne des ailes et je leur tire ma révérence de gentleman.",
    "video 3": " Pour moi c'est des matins qui chantent. Hier j'ai bien travaillé mes pecs à la salle, totalement Spartan. Le cardio est là aussi, tiens viens. Et puis voilà j'ai encore le coeur qui bat la chamade. J'ai des étoiles plein les yeux parce qu'il y avait deux femmes cette fois, deux jeunes femmes avec des bouties d'une très très grande qualité. Travailler, juicy et forcément c'est des émotions qui remontent. C'est la fierté pour cette femme féminine qui se donne. Ça fait plaisir, ça m'honore. J'ai qu'une impatience c'est de retourner."
"
Rédige un commentaire qu'on pourrait poster sur google maps pour mettre 5 étoiles à une boulangerie, en t'inspirant du style à utiliser.
"""}],
    stream=True,
)

for chunk in stream:
    print(chunk['message']['content'], end='', flush=True)