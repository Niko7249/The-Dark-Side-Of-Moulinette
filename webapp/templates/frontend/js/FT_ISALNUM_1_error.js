const obj ={
	"created": 1673354607.242164,
	"duration": 0.051103830337524414,
	"exitcode": 1,
	"root": "/home/nik/Desktop/TDSOM_UPDATED/webapp",
	"environment": {
		"Python": "3.8.10",
		"Platform": "Linux-5.15.0-57-generic-x86_64-with-glibc2.29",
		"Packages": {
			"pytest": "7.2.0",
			"pluggy": "1.0.0"
		},
		"Plugins": {
			"json-report": "1.5.0",
			"metadata": "2.0.4"
		}
	},
	"summary": {
		"failed": 1,
		"passed": 4,
		"total": 5,
		"collected": 5
	},
	"collectors": [
		{
			"nodeid": "",
			"outcome": "passed",
			"result": [
				{
					"nodeid": "script_test/test/test_ft_isalnum.py",
					"type": "Module"
				}
			]
		},
		{
			"nodeid": "script_test/test/test_ft_isalnum.py",
			"outcome": "passed",
			"result": [
				{
					"nodeid": "script_test/test/test_ft_isalnum.py::test1_ft_isalnum",
					"type": "Function",
					"lineno": 13
				},
				{
					"nodeid": "script_test/test/test_ft_isalnum.py::test2_ft_isalnum",
					"type": "Function",
					"lineno": 44
				},
				{
					"nodeid": "script_test/test/test_ft_isalnum.py::test3_ft_isalnum",
					"type": "Function",
					"lineno": 75
				},
				{
					"nodeid": "script_test/test/test_ft_isalnum.py::test4_ft_isalnum",
					"type": "Function",
					"lineno": 106
				},
				{
					"nodeid": "script_test/test/test_ft_isalnum.py::test5_ft_isalnum",
					"type": "Function",
					"lineno": 137
				}
			]
		}
	],
	"tests": [
		{
			"nodeid": "script_test/test/test_ft_isalnum.py::test1_ft_isalnum",
			"lineno": 13,
			"outcome": "failed",
			"keywords": [
				"test1_ft_isalnum",
				"script_test/test/test_ft_isalnum.py",
				"webapp"
			],
			"setup": {
				"duration": 0.0001838730004237732,
				"outcome": "passed"
			},
			"call": {
				"duration": 0.0003082039997934771,
				"outcome": "failed",
				"crash": {
					"path": "/home/nik/Desktop/TDSOM_UPDATED/webapp/script_test/test/test_ft_isalnum.py",
					"lineno": 43,
					"message": "assert 0 == 8"
				},
				"traceback": [
					{
						"path": "script_test/test/test_ft_isalnum.py",
						"lineno": 43,
						"message": "in test1_ft_isalnum"
					}
				],
				"longrepr": "script_test/test/test_ft_isalnum.py:43: in test1_ft_isalnum\n    assert result == original_result\nE   assert 0 == 8"
			},
			"teardown": {
				"duration": 0.00032291099978465354,
				"outcome": "passed"
			}
		},
		{
			"nodeid": "script_test/test/test_ft_isalnum.py::test2_ft_isalnum",
			"lineno": 44,
			"outcome": "passed",
			"keywords": [
				"test2_ft_isalnum",
				"script_test/test/test_ft_isalnum.py",
				"webapp"
			],
			"setup": {
				"duration": 0.00033463999989180593,
				"outcome": "passed"
			},
			"call": {
				"duration": 0.00025217400025212555,
				"outcome": "passed"
			},
			"teardown": {
				"duration": 0.0002031029998761369,
				"outcome": "passed"
			}
		},
		{
			"nodeid": "script_test/test/test_ft_isalnum.py::test3_ft_isalnum",
			"lineno": 75,
			"outcome": "passed",
			"keywords": [
				"test3_ft_isalnum",
				"script_test/test/test_ft_isalnum.py",
				"webapp"
			],
			"setup": {
				"duration": 0.00022622799997407128,
				"outcome": "passed"
			},
			"call": {
				"duration": 0.0002278219999425346,
				"outcome": "passed"
			},
			"teardown": {
				"duration": 0.0002238800002487551,
				"outcome": "passed"
			}
		},
		{
			"nodeid": "script_test/test/test_ft_isalnum.py::test4_ft_isalnum",
			"lineno": 106,
			"outcome": "passed",
			"keywords": [
				"test4_ft_isalnum",
				"script_test/test/test_ft_isalnum.py",
				"webapp"
			],
			"setup": {
				"duration": 0.00021070100001452374,
				"outcome": "passed"
			},
			"call": {
				"duration": 0.00022848299977340503,
				"outcome": "passed"
			},
			"teardown": {
				"duration": 0.0001920869999594288,
				"outcome": "passed"
			}
		},
		{
			"nodeid": "script_test/test/test_ft_isalnum.py::test5_ft_isalnum",
			"lineno": 137,
			"outcome": "passed",
			"keywords": [
				"test5_ft_isalnum",
				"script_test/test/test_ft_isalnum.py",
				"webapp"
			],
			"setup": {
				"duration": 0.00021107800012032385,
				"outcome": "passed"
			},
			"call": {
				"duration": 0.00022633100024904707,
				"outcome": "passed"
			},
			"teardown": {
				"duration": 0.0001908580002236704,
				"outcome": "passed"
			}
		}
	]
}
