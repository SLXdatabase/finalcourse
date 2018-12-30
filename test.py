#!/usr/bin/python2
# -*- coding: utf-8 -*-

from orm import execute_raw_sql
from model import UserModel, ScoreModel, MovieModel
import unittest


def create_user_instance(
        userid,
        username,
        password,
        record
    ):
    user = UserModel()

    user.userid = userid
    user.username = username
    user.password = password
    user.record = record

    user.save()
    return user

def create_score_instance(
        userid,
        movieid,
        comDate,
        value,
        content,
        watched,
        star
    ):
    score = ScoreModel()

    score.userid = userid
    score.movieid = movieid
    score.comDate = comDate
    score.value = value
    score.content = content
    score.watched = watched
    score.star = star

    score.save()
    return score

def create_movie_instance(
        movieid,
        mname,
        director,
        editor,
        actor,
        mtype,
        countryOrLocation,
        language,
        date,
        duration,
        othername,
        IMDb,
        introduction,
        allActors,
        numOfEvaluator,
        star5,
        star4,
        star3,
        star2,
        star1
    ):
    movie = MovieModel()

    movie.movieid = movieid
    movie.mname = mname
    movie.director = director
    movie.editor = editor
    movie.actor = actor
    movie.mtype = mtype
    movie.countryOrLocation = countryOrLocation
    movie.language = language
    movie.date = date
    movie.duration = duration
    movie.othername = othername
    movie.IMDb = IMDb
    movie.introduction = introduction
    movie.allActors = allActors
    movie.numOfEvaluator = numOfEvaluator
    movie.star5 = star5
    movie.star4 = star4
    movie.star3 = star3
    movie.star2 = star2
    movie.star1 = star1

    movie.save()
    return movie


class TestUserModel(unittest.TestCase):

    def setUp(self):
        if list(UserModel.where(userid=1314).select()) == []:
            create_user_instance(
                1314,
                "lolo",
                "bobo",
                "520"
            )
        if list(UserModel.where(userid=1315).select()) == []:
            create_user_instance(
                1315,
                "lolo",
                "bobo",
                "520"
            )
        if list(UserModel.where(userid=1316).select()) == []:
            create_user_instance(
                1316,
                "lolo",
                "bobo",
                "520"
            )

    def tearDown(self):
        execute_raw_sql("truncate table User;")

    def test_instance(self):
        user = UserModel.where(userid=1314).select().next()

        self.assertEquals(user.userid, "1314")
        self.assertEquals(user.username, "lolo")
        self.assertEquals(user.password, "bobo")
        self.assertEquals(user.record, "520")

    def test_select(self):
        users = UserModel.where().select()

        for user in users:
            if user.userid == "1314":
                pass
            elif user.userid == "1315":
                pass
            else:
                pass

    def test_update(self):
        UserModel.where(userid=1314).update(record="1314")
        user = UserModel.where(userid=1314).select().next()

        self.assertEquals(user.userid, "1314")
        self.assertEquals(user.username, "lolo")
        self.assertEquals(user.password, "bobo")
        self.assertEquals(user.record, "1314")

    def test_limit(self):
        users = UserModel.where(username="lolo").limit(2).select()

        cnt = 0
        for user in users: cnt += 1
        self.assertEquals(2, cnt)

    def test_count(self):
        cnt = UserModel.where(username="lolo").count()

        self.assertEquals(3, cnt)


class TestScoreModel(unittest.TestCase):

    def test_instance(self):
        pass

    def test_select(self):
        pass

    def test_update(self):
        pass

    def test_limit(self):
        pass

    def test_count(self):
        pass


class TestMovieModel(unittest.TestCase):

    def test_instance(self):
        pass

    def test_select(self):
        pass

    def test_update(self):
        pass

    def test_limit(self):
        pass

    def test_count(self):
        pass


if __name__ == "__main__":
    unittest.main()
