from matplotlib import pyplot as plt
import pandas as pd

d = {"equipment": [
    {
        "date": "2022-02-25",
        "day": 2,
        "aircraft": 10,
        "helicopter": 7,
        "tank": 80,
        "APC": 516,
        "field artillery": 49,
        "MRL": 4,
        "military auto": 100,
        "fuel tank": 60,
        "drone": 0,
        "naval ship": 2,
        "anti-aircraft warfare": 0
    },
    {
        "date": "2022-02-26",
        "day": 3,
        "aircraft": 27,
        "helicopter": 26,
        "tank": 146,
        "APC": 706,
        "field artillery": 49,
        "MRL": 4,
        "military auto": 130,
        "fuel tank": 60,
        "drone": 2,
        "naval ship": 2,
        "anti-aircraft warfare": 0
    },
    {
        "date": "2022-02-27",
        "day": 4,
        "aircraft": 27,
        "helicopter": 26,
        "tank": 150,
        "APC": 706,
        "field artillery": 50,
        "MRL": 4,
        "military auto": 130,
        "fuel tank": 60,
        "drone": 2,
        "naval ship": 2,
        "anti-aircraft warfare": 0
    },
    {
        "date": "2022-02-28",
        "day": 5,
        "aircraft": 29,
        "helicopter": 29,
        "tank": 150,
        "APC": 816,
        "field artillery": 74,
        "MRL": 21,
        "military auto": 291,
        "fuel tank": 60,
        "drone": 3,
        "naval ship": 2,
        "anti-aircraft warfare": 5
    },
    {
        "date": "2022-03-01",
        "day": 6,
        "aircraft": 29,
        "helicopter": 29,
        "tank": 198,
        "APC": 846,
        "field artillery": 77,
        "MRL": 24,
        "military auto": 305,
        "fuel tank": 60,
        "drone": 3,
        "naval ship": 2,
        "anti-aircraft warfare": 7
    },
    {
        "date": "2022-03-02",
        "day": 7,
        "aircraft": 30,
        "helicopter": 31,
        "tank": 211,
        "APC": 862,
        "field artillery": 85,
        "MRL": 40,
        "military auto": 355,
        "fuel tank": 60,
        "drone": 3,
        "naval ship": 2,
        "anti-aircraft warfare": 9
    },
    {
        "date": "2022-03-03",
        "day": 8,
        "aircraft": 30,
        "helicopter": 31,
        "tank": 217,
        "APC": 900,
        "field artillery": 90,
        "MRL": 42,
        "military auto": 374,
        "fuel tank": 60,
        "drone": 3,
        "naval ship": 2,
        "anti-aircraft warfare": 11
    },
    {
        "date": "2022-03-04",
        "day": "9",
        "aircraft": 33,
        "helicopter": 37,
        "tank": 251,
        "APC": 939,
        "field artillery": 105,
        "MRL": 50,
        "military auto": 404,
        "fuel tank": 60,
        "drone": 3,
        "naval ship": 2,
        "anti-aircraft warfare": 18
    },
    {
        "date": "2022-03-05",
        "day": 10,
        "aircraft": 39,
        "helicopter": 40,
        "tank": 269,
        "APC": 945,
        "field artillery": 105,
        "MRL": 50,
        "military auto": 409,
        "fuel tank": 60,
        "drone": 3,
        "naval ship": 2,
        "anti-aircraft warfare": 19
    },
    {
        "date": "2022-03-06",
        "day": 11,
        "aircraft": 44,
        "helicopter": 48,
        "tank": 285,
        "APC": 985,
        "field artillery": 109,
        "MRL": 50,
        "military auto": 447,
        "fuel tank": 60,
        "drone": 4,
        "naval ship": 2,
        "anti-aircraft warfare": 21
    },
    {
        "date": "2022-03-07",
        "day": 12,
        "aircraft": 46,
        "helicopter": 68,
        "tank": 290,
        "APC": 999,
        "field artillery": 117,
        "MRL": 50,
        "military auto": 454,
        "fuel tank": 60,
        "drone": 7,
        "naval ship": 3,
        "anti-aircraft warfare": 23
    },
    {
        "date": "2022-03-08",
        "day": 13,
        "aircraft": 48,
        "helicopter": 80,
        "tank": 303,
        "APC": 1036,
        "field artillery": 120,
        "MRL": 56,
        "military auto": 474,
        "fuel tank": 60,
        "drone": 7,
        "naval ship": 3,
        "anti-aircraft warfare": 27
    },
    {
        "date": "2022-03-09",
        "day": 14,
        "aircraft": 49,
        "helicopter": 81,
        "tank": 317,
        "APC": 1070,
        "field artillery": 120,
        "MRL": 56,
        "military auto": 482,
        "fuel tank": 60,
        "drone": 7,
        "naval ship": 3,
        "anti-aircraft warfare": 28
    },
    {
        "date": "2022-03-10",
        "day": 15,
        "aircraft": 49,
        "helicopter": 81,
        "tank": 335,
        "APC": 1105,
        "field artillery": 123,
        "MRL": 56,
        "military auto": 526,
        "fuel tank": 60,
        "drone": 7,
        "naval ship": 3,
        "anti-aircraft warfare": 29
    },
    {
        "date": "2022-03-11",
        "day": 16,
        "aircraft": 57,
        "helicopter": 83,
        "tank": 353,
        "APC": 1165,
        "field artillery": 125,
        "MRL": 58,
        "military auto": 558,
        "fuel tank": 60,
        "drone": 7,
        "naval ship": 3,
        "anti-aircraft warfare": 31
    },
    {
        "date": "2022-03-12",
        "day": 17,
        "aircraft": 58,
        "helicopter": 83,
        "tank": 362,
        "APC": 1205,
        "field artillery": 135,
        "MRL": 62,
        "military auto": 585,
        "fuel tank": 60,
        "drone": 7,
        "naval ship": 3,
        "anti-aircraft warfare": 33
    },
    {
        "date": "2022-03-13",
        "day": 18,
        "aircraft": 74,
        "helicopter": 86,
        "tank": 374,
        "APC": 1226,
        "field artillery": 140,
        "MRL": 62,
        "military auto": 600,
        "fuel tank": 60,
        "drone": 7,
        "naval ship": 3,
        "anti-aircraft warfare": 34
    },
    {
        "date": "2022-03-14",
        "day": 19,
        "aircraft": 77,
        "helicopter": 90,
        "tank": 389,
        "APC": 1249,
        "field artillery": 150,
        "MRL": 64,
        "military auto": 617,
        "fuel tank": 60,
        "drone": 8,
        "naval ship": 3,
        "anti-aircraft warfare": 34
    },
    {
        "date": "2022-03-15",
        "day": 20,
        "aircraft": 81,
        "helicopter": 95,
        "tank": 404,
        "APC": 1279,
        "field artillery": 150,
        "MRL": 64,
        "military auto": 640,
        "fuel tank": 60,
        "drone": 9,
        "naval ship": 3,
        "anti-aircraft warfare": 36
    },
    {
        "date": "2022-03-16",
        "day": "21",
        "aircraft": 84,
        "helicopter": 108,
        "tank": 430,
        "APC": 1375,
        "field artillery": 190,
        "MRL": 70,
        "military auto": 819,
        "fuel tank": 60,
        "drone": 11,
        "naval ship": 3,
        "anti-aircraft warfare": 43,
        "special equipment": 10
    },
    {
        "date": "2022-03-17",
        "day": 22,
        "aircraft": 86,
        "helicopter": 108,
        "tank": 444,
        "APC": 1435,
        "field artillery": 201,
        "MRL": 72,
        "military auto": 864,
        "fuel tank": 60,
        "drone": 11,
        "naval ship": 3,
        "anti-aircraft warfare": 43,
        "special equipment": 10
    },
    {
        "date": "2022-03-18",
        "day": 23,
        "aircraft": 93,
        "helicopter": 112,
        "tank": 450,
        "APC": 1448,
        "field artillery": 205,
        "MRL": 72,
        "military auto": 879,
        "fuel tank": 60,
        "drone": 12,
        "naval ship": 3,
        "anti-aircraft warfare": 43,
        "special equipment": 11
    },
    {
        "date": "2022-03-19",
        "day": 24,
        "aircraft": 95,
        "helicopter": 115,
        "tank": 466,
        "APC": 1470,
        "field artillery": 213,
        "MRL": 72,
        "military auto": 914,
        "fuel tank": 60,
        "drone": 17,
        "naval ship": 3,
        "anti-aircraft warfare": 44,
        "special equipment": 11
    },
    {
        "date": "2022-03-20",
        "day": 25,
        "aircraft": 96,
        "helicopter": 118,
        "tank": 476,
        "APC": 1487,
        "field artillery": 230,
        "MRL": 74,
        "military auto": 947,
        "fuel tank": 60,
        "drone": 21,
        "naval ship": 3,
        "anti-aircraft warfare": 44,
        "special equipment": 12
    },
    {
        "date": "2022-03-21",
        "day": 26,
        "aircraft": 97,
        "helicopter": 121,
        "tank": 498,
        "APC": 1535,
        "field artillery": 240,
        "MRL": 80,
        "military auto": 969,
        "fuel tank": 60,
        "drone": 24,
        "naval ship": 3,
        "anti-aircraft warfare": 45,
        "special equipment": 13
    },
    {
        "date": "2022-03-22",
        "day": 27,
        "aircraft": 99,
        "helicopter": 123,
        "tank": 509,
        "APC": 1556,
        "field artillery": 252,
        "MRL": 80,
        "military auto": 1000,
        "fuel tank": 70,
        "drone": 35,
        "naval ship": 3,
        "anti-aircraft warfare": 45,
        "special equipment": 15
    },
    {
        "date": "2022-03-23",
        "day": 28,
        "aircraft": 101,
        "helicopter": 124,
        "tank": 517,
        "APC": 1578,
        "field artillery": 267,
        "MRL": 80,
        "military auto": 1008,
        "fuel tank": 70,
        "drone": 42,
        "naval ship": 4,
        "anti-aircraft warfare": 47,
        "special equipment": 15
    },
    {
        "date": "2022-03-24",
        "day": 29,
        "aircraft": 108,
        "helicopter": 124,
        "tank": 530,
        "APC": 1597,
        "field artillery": 280,
        "MRL": 82,
        "military auto": 1033,
        "fuel tank": 72,
        "drone": 50,
        "naval ship": 4,
        "anti-aircraft warfare": 47,
        "special equipment": 16
    },
    {
        "date": "2022-03-25",
        "day": 30,
        "aircraft": 115,
        "helicopter": 125,
        "tank": 561,
        "APC": 1625,
        "field artillery": 291,
        "MRL": 90,
        "military auto": 1089,
        "fuel tank": 72,
        "drone": 53,
        "naval ship": 5,
        "anti-aircraft warfare": 49,
        "special equipment": 18
    },
    {
        "date": "2022-03-26",
        "day": 31,
        "aircraft": 117,
        "helicopter": 127,
        "tank": 575,
        "APC": 1640,
        "field artillery": 293,
        "MRL": 91,
        "military auto": 1131,
        "fuel tank": 73,
        "drone": 56,
        "naval ship": 7,
        "anti-aircraft warfare": 51,
        "special equipment": 19,
        "mobile SRBM system": 2
    },
    {
        "date": "2022-03-27",
        "day": 32,
        "aircraft": 121,
        "helicopter": 127,
        "tank": 582,
        "APC": 1664,
        "field artillery": 294,
        "MRL": 93,
        "military auto": 1144,
        "fuel tank": 73,
        "drone": 56,
        "naval ship": 7,
        "anti-aircraft warfare": 52,
        "special equipment": 21,
        "mobile SRBM system": 4
    },
    {
        "date": "2022-03-28",
        "day": 33,
        "aircraft": 123,
        "helicopter": 127,
        "tank": 586,
        "APC": 1694,
        "field artillery": 302,
        "MRL": 95,
        "military auto": 1150,
        "fuel tank": 73,
        "drone": 66,
        "naval ship": 7,
        "anti-aircraft warfare": 54,
        "special equipment": 21,
        "mobile SRBM system": 4
    },
    {
        "date": "2022-03-29",
        "day": 34,
        "aircraft": 127,
        "helicopter": 129,
        "tank": 597,
        "APC": 1710,
        "field artillery": 303,
        "MRL": 96,
        "military auto": 1178,
        "fuel tank": 73,
        "drone": 71,
        "naval ship": 7,
        "anti-aircraft warfare": 54,
        "special equipment": 21,
        "mobile SRBM system": 4
    },
    {
        "date": "2022-03-30",
        "day": 35,
        "aircraft": 131,
        "helicopter": 131,
        "tank": 605,
        "APC": 1723,
        "field artillery": 305,
        "MRL": 96,
        "military auto": 1184,
        "fuel tank": 75,
        "drone": 81,
        "naval ship": 7,
        "anti-aircraft warfare": 54,
        "special equipment": 21,
        "mobile SRBM system": 4
    },
    {
        "date": "2022-03-31",
        "day": 36,
        "aircraft": 135,
        "helicopter": 131,
        "tank": 614,
        "APC": 1735,
        "field artillery": 311,
        "MRL": 96,
        "military auto": 1201,
        "fuel tank": 75,
        "drone": 83,
        "naval ship": 7,
        "anti-aircraft warfare": 54,
        "special equipment": 22,
        "mobile SRBM system": 4
    },
    {
        "date": "2022-04-01",
        "day": 37,
        "aircraft": 143,
        "helicopter": 131,
        "tank": 625,
        "APC": 1751,
        "field artillery": 316,
        "MRL": 96,
        "military auto": 1220,
        "fuel tank": 76,
        "drone": 85,
        "naval ship": 7,
        "anti-aircraft warfare": 54,
        "special equipment": 24,
        "mobile SRBM system": 4
    },
    {
        "date": "2022-04-02",
        "day": 38,
        "aircraft": 143,
        "helicopter": 134,
        "tank": 631,
        "APC": 1776,
        "field artillery": 317,
        "MRL": 100,
        "military auto": 1236,
        "fuel tank": 76,
        "drone": 87,
        "naval ship": 7,
        "anti-aircraft warfare": 54,
        "special equipment": 24,
        "mobile SRBM system": 4
    },
    {
        "date": "2022-04-03",
        "day": 39,
        "aircraft": 143,
        "helicopter": 134,
        "tank": 644,
        "APC": 1830,
        "field artillery": 325,
        "MRL": 105,
        "military auto": 1249,
        "fuel tank": 76,
        "drone": 89,
        "naval ship": 7,
        "anti-aircraft warfare": 54,
        "special equipment": 24,
        "mobile SRBM system": 4
    },
    {
        "date": "2022-04-04",
        "day": 40,
        "aircraft": 147,
        "helicopter": 134,
        "tank": 647,
        "APC": 1844,
        "field artillery": 330,
        "MRL": 107,
        "military auto": 1273,
        "fuel tank": 76,
        "drone": 91,
        "naval ship": 7,
        "anti-aircraft warfare": 54,
        "special equipment": 25,
        "mobile SRBM system": 4
    },
    {
        "date": "2022-04-05",
        "day": 41,
        "aircraft": 150,
        "helicopter": 134,
        "tank": 676,
        "APC": 1858,
        "field artillery": 332,
        "MRL": 107,
        "military auto": 1322,
        "fuel tank": 76,
        "drone": 94,
        "naval ship": 7,
        "anti-aircraft warfare": 55,
        "special equipment": 25,
        "mobile SRBM system": 4
    },
    {
        "date": "2022-04-06",
        "day": 42,
        "aircraft": 150,
        "helicopter": 135,
        "tank": 684,
        "APC": 1861,
        "field artillery": 332,
        "MRL": 107,
        "military auto": 1324,
        "fuel tank": 76,
        "drone": 96,
        "naval ship": 7,
        "anti-aircraft warfare": 55,
        "special equipment": 25,
        "mobile SRBM system": 4
    },
    {
        "date": "2022-04-07",
        "day": 43,
        "aircraft": 150,
        "helicopter": 135,
        "tank": 698,
        "APC": 1891,
        "field artillery": 332,
        "MRL": 108,
        "military auto": 1358,
        "fuel tank": 76,
        "drone": 111,
        "naval ship": 7,
        "anti-aircraft warfare": 55,
        "special equipment": 25,
        "mobile SRBM system": 4
    },
    {
        "date": "2022-04-08",
        "day": 44,
        "aircraft": 150,
        "helicopter": 135,
        "tank": 700,
        "APC": 1891,
        "field artillery": 333,
        "MRL": 108,
        "military auto": 1361,
        "fuel tank": 76,
        "drone": 112,
        "naval ship": 7,
        "anti-aircraft warfare": 55,
        "special equipment": 25,
        "mobile SRBM system": 4
    },
    {
        "date": "2022-04-09",
        "day": 45,
        "aircraft": 151,
        "helicopter": 136,
        "tank": 705,
        "APC": 1895,
        "field artillery": 335,
        "MRL": 108,
        "military auto": 1363,
        "fuel tank": 76,
        "drone": 112,
        "naval ship": 7,
        "anti-aircraft warfare": 55,
        "special equipment": 25,
        "mobile SRBM system": 4
    },
    {
        "date": "2022-04-10",
        "day": 46,
        "aircraft": 152,
        "helicopter": 137,
        "tank": 722,
        "APC": 1911,
        "field artillery": 342,
        "MRL": 108,
        "military auto": 1384,
        "fuel tank": 76,
        "drone": 112,
        "naval ship": 7,
        "anti-aircraft warfare": 55,
        "special equipment": 25,
        "mobile SRBM system": 4
    },
    {
        "date": "2022-04-11",
        "day": 47,
        "aircraft": 154,
        "helicopter": 137,
        "tank": 725,
        "APC": 1923,
        "field artillery": 347,
        "MRL": 111,
        "military auto": 1387,
        "fuel tank": 76,
        "drone": 119,
        "naval ship": 7,
        "anti-aircraft warfare": 55,
        "special equipment": 25,
        "mobile SRBM system": 4
    },
    {
        "date": "2022-04-12",
        "day": 48,
        "aircraft": 157,
        "helicopter": 140,
        "tank": 732,
        "APC": 1946,
        "field artillery": 349,
        "MRL": 111,
        "military auto": 1406,
        "fuel tank": 76,
        "drone": 124,
        "naval ship": 7,
        "anti-aircraft warfare": 63,
        "special equipment": 25,
        "mobile SRBM system": 4
    },
    {
        "date": "2022-04-13",
        "day": 49,
        "aircraft": 158,
        "helicopter": 143,
        "tank": 739,
        "APC": 1964,
        "field artillery": 358,
        "MRL": 115,
        "military auto": 1429,
        "fuel tank": 76,
        "drone": 132,
        "naval ship": 7,
        "anti-aircraft warfare": 64,
        "special equipment": 25,
        "mobile SRBM system": 4
    },
    {
        "date": "2022-04-14",
        "day": 50,
        "aircraft": 160,
        "helicopter": 144,
        "tank": 753,
        "APC": 1968,
        "field artillery": 366,
        "MRL": 122,
        "military auto": 1437,
        "fuel tank": 76,
        "drone": 134,
        "naval ship": 7,
        "anti-aircraft warfare": 64,
        "special equipment": 25,
        "mobile SRBM system": 4
    },
    {
        "date": "2022-04-15",
        "day": 51,
        "aircraft": 163,
        "helicopter": 144,
        "tank": 756,
        "APC": 1976,
        "field artillery": 366,
        "MRL": 122,
        "military auto": 1443,
        "fuel tank": 76,
        "drone": 135,
        "naval ship": 8,
        "anti-aircraft warfare": 66,
        "special equipment": 25,
        "mobile SRBM system": 4
    },
    {
        "date": "2022-04-16",
        "day": 52,
        "aircraft": 163,
        "helicopter": 145,
        "tank": 762,
        "APC": 1982,
        "field artillery": 371,
        "MRL": 125,
        "military auto": 1458,
        "fuel tank": 76,
        "drone": 138,
        "naval ship": 8,
        "anti-aircraft warfare": 66,
        "special equipment": 26,
        "mobile SRBM system": 4
    },
    {
        "date": "2022-04-17",
        "day": 53,
        "aircraft": 165,
        "helicopter": 146,
        "tank": 773,
        "APC": 2002,
        "field artillery": 376,
        "MRL": 127,
        "military auto": 1471,
        "fuel tank": 76,
        "drone": 148,
        "naval ship": 8,
        "anti-aircraft warfare": 66,
        "special equipment": 27,
        "mobile SRBM system": 4
    },
    {
        "date": "2022-04-18",
        "day": 54,
        "aircraft": 167,
        "helicopter": 147,
        "tank": 790,
        "APC": 2041,
        "field artillery": 381,
        "MRL": 130,
        "military auto": 1487,
        "fuel tank": 76,
        "drone": 155,
        "naval ship": 8,
        "anti-aircraft warfare": 67,
        "special equipment": 27,
        "mobile SRBM system": 4
    },
    {
        "date": "2022-04-19",
        "day": 55,
        "aircraft": 169,
        "helicopter": 150,
        "tank": 802,
        "APC": 2063,
        "field artillery": 386,
        "MRL": 132,
        "military auto": 1495,
        "fuel tank": 76,
        "drone": 158,
        "naval ship": 8,
        "anti-aircraft warfare": 67,
        "special equipment": 27,
        "mobile SRBM system": 4
    },
    {
        "date": "2022-04-20",
        "day": 56,
        "aircraft": 171,
        "helicopter": 150,
        "tank": 815,
        "APC": 2087,
        "field artillery": 391,
        "MRL": 136,
        "military auto": 1504,
        "fuel tank": 76,
        "drone": 165,
        "naval ship": 8,
        "anti-aircraft warfare": 67,
        "special equipment": 27,
        "mobile SRBM system": 4
    },
    {
        "date": "2022-04-21",
        "day": 57,
        "aircraft": 172,
        "helicopter": 151,
        "tank": 829,
        "APC": 2118,
        "field artillery": 393,
        "MRL": 136,
        "military auto": 1508,
        "fuel tank": 76,
        "drone": 166,
        "naval ship": 8,
        "anti-aircraft warfare": 67,
        "special equipment": 27,
        "mobile SRBM system": 4
    },
    {
        "date": "2022-04-22",
        "day": 58,
        "aircraft": 176,
        "helicopter": 153,
        "tank": 838,
        "APC": 2162,
        "field artillery": 397,
        "MRL": 138,
        "military auto": 1523,
        "fuel tank": 76,
        "drone": 172,
        "naval ship": 8,
        "anti-aircraft warfare": 69,
        "special equipment": 27,
        "mobile SRBM system": 4
    },
    {
        "date": "2022-04-23",
        "day": 59,
        "aircraft": 177,
        "helicopter": 154,
        "tank": 854,
        "APC": 2205,
        "field artillery": 403,
        "MRL": 143,
        "military auto": 1543,
        "fuel tank": 76,
        "drone": 182,
        "naval ship": 8,
        "anti-aircraft warfare": 69,
        "special equipment": 27,
        "mobile SRBM system": 4
    },
    {
        "date": "2022-04-24",
        "day": 60,
        "aircraft": 179,
        "helicopter": 154,
        "tank": 873,
        "APC": 2238,
        "field artillery": 408,
        "MRL": 147,
        "military auto": 1557,
        "fuel tank": 76,
        "drone": 191,
        "naval ship": 8,
        "anti-aircraft warfare": 69,
        "special equipment": 28,
        "mobile SRBM system": 4
    },
    {
        "date": "2022-04-25",
        "day": 61,
        "aircraft": 181,
        "helicopter": 154,
        "tank": 884,
        "APC": 2258,
        "field artillery": 411,
        "MRL": 149,
        "military auto": 1566,
        "fuel tank": 76,
        "drone": 201,
        "naval ship": 8,
        "anti-aircraft warfare": 69,
        "special equipment": 28,
        "mobile SRBM system": 4
    },
    {
        "date": "2022-04-26",
        "day": 62,
        "aircraft": 184,
        "helicopter": 154,
        "tank": 918,
        "APC": 2308,
        "field artillery": 416,
        "MRL": 149,
        "military auto": 1643,
        "fuel tank": 76,
        "drone": 205,
        "naval ship": 8,
        "anti-aircraft warfare": 69,
        "special equipment": 31,
        "mobile SRBM system": 4
    },
    {
        "date": "2022-04-27",
        "day": 63,
        "aircraft": 185,
        "helicopter": 155,
        "tank": 939,
        "APC": 2342,
        "field artillery": 421,
        "MRL": 149,
        "military auto": 1666,
        "fuel tank": 76,
        "drone": 207,
        "naval ship": 8,
        "anti-aircraft warfare": 71,
        "special equipment": 31,
        "mobile SRBM system": 4
    },
    {
        "date": "2022-04-28",
        "day": 64,
        "aircraft": 187,
        "helicopter": 155,
        "tank": 970,
        "APC": 2389,
        "field artillery": 431,
        "MRL": 151,
        "military auto": 1688,
        "fuel tank": 76,
        "drone": 215,
        "naval ship": 8,
        "anti-aircraft warfare": 72,
        "special equipment": 31,
        "mobile SRBM system": 4
    },
    {
        "date": "2022-04-29",
        "day": 65,
        "aircraft": 189,
        "helicopter": 155,
        "tank": 986,
        "APC": 2418,
        "field artillery": 435,
        "MRL": 151,
        "military auto": 1695,
        "fuel tank": 76,
        "drone": 229,
        "naval ship": 8,
        "anti-aircraft warfare": 73,
        "special equipment": 31,
        "mobile SRBM system": 4
    }
]}

df = pd.DataFrame(d['equipment'])
print(df)
df.plot(x='day', y='tank', kind='scatter') #change values here
plt.show()
