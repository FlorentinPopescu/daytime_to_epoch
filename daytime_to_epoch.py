""" epoch time script """

# imports
import os
from datetime import datetime
from time import strptime, mktime

from flask import Flask

# ==================================

APP = Flask(__name__)
# ---------------------------------

# APP.secret_key = b"\xe0\x95\xf2`W8'X,2\xfc\x88Z\x8c\x97\xad~1\xd8k\xbb\xaf\xd7\xab"
# APP.secret_key = os.environ.get('SECRET_KEY').encode()
# ------------------------------------------

def local_to_epoch():
    """ response -> current time converted to epoch time """
    local_time = str(datetime.now())
    pattern = "%Y-%m-%d %H:%M:%S.%f"
    epoch = int(mktime(strptime(local_time, pattern)))

    return (str(epoch), local_time)

# ---------------------------------
@APP.route('/', methods=["GET", "POST"])
def epoch_tm():
    """ application """
    page = """
        <b>{0}</b>
        <hr></hr>
        <b><i>this is the epoch time corresponding to {1}</i></b> 
    """.format(*local_to_epoch())
    return page

# =================================
if __name__ == "__main__":
    # PORT = int(os.environ.get("POST", 6738))
    PORT = process.env.PORT || 5000
    APP.run(host="0.0.0.0", port=PORT)
    # APP.run(debug=True)
