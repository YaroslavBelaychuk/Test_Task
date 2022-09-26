from functools import lru_cache

import numpy as np
import pandas as pd

from app import db
from app.models.user import User


@lru_cache
def get_solve(type):
    if type == "1":
        return pd.DataFrame(data={"a": [1, 1, 2], "b": [1, 1, 1], "c": [3, 2, 1]})
    if type == "2":
        users = db.session.query(User.id, User.login, ).all()
        return pd.DataFrame(users)
    if type == "3":
        return pd.DataFrame(np.random.randint(0, 100, size=(100, 4)), columns=list('ABCD'))
