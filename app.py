from flask import Flask, request
import match
import threading
import time

app = Flask(__name__)


users = {}
'''
users will look like {
    userId1: {
        question1: A,
        question2: B
    },
    userId2: {
        questton3: B
    }

}
'''

locked_data_arr = []
locked_data_dic = {}
'''
locked_data_arr will look like this
sorted from unlocked soonest to last so always consistent search of O(1) since we are 
only unlocking first of the arr everytime if we do do need to unlock
[
    {userID1: unlockTime},
    {userID3: unlockTime},
    {userID2: unlockTime},
]
locked_data_dic {
  userID: lockedTil
}
'''

def check_locks():
    while True:
        while len(locked_data_arr) > 0:
            # only need to first valu of arr
            userID = list(locked_data_arr[0].keys())[0]
            lockedTil = locked_data_arr[0][userID]
            now = int(time.time())

            if lockedTil <= now:
                locked_data_arr = locked_data_arr[1:]
                del locked_data_dic[userID]
            else:
                break    # no need to look at rest since sortd by time     

@app.route('/answers',  methods=['POST'])
def create_answer():
    data = request.get_json()
    users[data["user_id"]][data["question_id"]] = data["score"]
    
    return True, 200


@app.route('/users/compatibility', methods=['POST'])
def compatibility():
    data = request.get_json()
    if data["from_id"] in locked_data_dic or data["to_id"] in locked_data_dic:
        return "Record not found", 400
    else:
        locked_til = int(time.time()) + 3
        locked_data_dic[data["to_id"]]: locked_til
        locked_data_dic[data["from_id"]]: locked_til
        locked_data_arr.append({data["from_id"]: locked_til})
        locked_data_arr.append({data["to_id"]: locked_til})

        score = match.compatibility(data["from_id"], data["to_id"])

        if score is None:
            return "no responses in common", 400

        return score, 200


if __name__ == "__main__":
    x =  threading.Thread(target=check_locks, daemon=True).start()
    x.start()
    user_1 = {
        "question_1": 1,
        "question_2": 1,
        "question_3": 1
    }

    user_2 = {
        "question_1": 1,
        "question_2": 2,
        "question_3": 3
    }

    score = match.compatibility(user_1, user_2)

    print(score)
