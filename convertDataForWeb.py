import numpy as np
import json
gameArr = []
answerArr = []
for i in range(200):
    game = np.load("training_ds/g-66-" + str(i) + ".npy")
    answer = np.load("training_ds/a-66-" + str(i) + ".npy")
    gameArr.append(game.tolist())
    answerArr.append(answer.tolist())


print(len(gameArr))
web_game = {
    'puzzle': gameArr,
    'answer': answerArr,
}
with open('trained_ds.json', 'w') as json_file:
    json.dump(web_game, json_file)
print("Done!")
