const obj ={
	"created": 1673359559.742664,
	"duration": 0.05684399604797363,
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
		"failed": 5,
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
				"duration": 0.00019013499968423275,
				"outcome": "passed"
			},
			"call": {
				"duration": 0.00033153600088553503,
				"outcome": "failed",
				"crash": {
					"path": "/home/nik/Desktop/TDSOM_UPDATED/webapp/script_test/test/test_ft_isalnum.py",
					"lineno": 43,
					"message": "assert 9213 == 8"
				},
				"traceback": [
					{
						"path": "script_test/test/test_ft_isalnum.py",
						"lineno": 43,
						"message": "in test1_ft_isalnum"
					}
				],
				"longrepr": "script_test/test/test_ft_isalnum.py:43: in test1_ft_isalnum\n    assert result == original_result\nE   assert 9213 == 8"
			},
			"teardown": {
				"duration": 0.0002780189997793059,
				"outcome": "passed"
			}
		},
		{
			"nodeid": "script_test/test/test_ft_isalnum.py::test2_ft_isalnum",
			"lineno": 44,
			"outcome": "failed",
			"keywords": [
				"test2_ft_isalnum",
				"script_test/test/test_ft_isalnum.py",
				"webapp"
			],
			"setup": {
				"duration": 0.00020468999991862802,
				"outcome": "passed"
			},
			"call": {
				"duration": 0.00033436500052630436,
				"outcome": "failed",
				"crash": {
					"path": "/home/nik/Desktop/TDSOM_UPDATED/webapp/script_test/test/test_ft_isalnum.py",
					"lineno": 74,
					"message": "assert 9213 == 0"
				},
				"traceback": [
					{
						"path": "script_test/test/test_ft_isalnum.py",
						"lineno": 74,
						"message": "in test2_ft_isalnum"
					}
				],
				"longrepr": "script_test/test/test_ft_isalnum.py:74: in test2_ft_isalnum\n    assert result == original_result\nE   assert 9213 == 0"
			},
			"teardown": {
				"duration": 0.000209198000447941,
				"outcome": "passed"
			}
		},
		{
			"nodeid": "script_test/test/test_ft_isalnum.py::test3_ft_isalnum",
			"lineno": 75,
			"outcome": "failed",
			"keywords": [
				"test3_ft_isalnum",
				"script_test/test/test_ft_isalnum.py",
				"webapp"
			],
			"setup": {
				"duration": 0.00018657700002222555,
				"outcome": "passed"
			},
			"call": {
				"duration": 0.0002969560000565252,
				"outcome": "failed",
				"crash": {
					"path": "/home/nik/Desktop/TDSOM_UPDATED/webapp/script_test/test/test_ft_isalnum.py",
					"lineno": 105,
					"message": "assert 9213 == 0"
				},
				"traceback": [
					{
						"path": "script_test/test/test_ft_isalnum.py",
						"lineno": 105,
						"message": "in test3_ft_isalnum"
					}
				],
				"longrepr": "script_test/test/test_ft_isalnum.py:105: in test3_ft_isalnum\n    assert result == original_result\nE   assert 9213 == 0"
			},
			"teardown": {
				"duration": 0.00018265200014866423,
				"outcome": "passed"
			}
		},
		{
			"nodeid": "script_test/test/test_ft_isalnum.py::test4_ft_isalnum",
			"lineno": 106,
			"outcome": "failed",
			"keywords": [
				"test4_ft_isalnum",
				"script_test/test/test_ft_isalnum.py",
				"webapp"
			],
			"setup": {
				"duration": 0.00017856399972515646,
				"outcome": "passed"
			},
			"call": {
				"duration": 0.000278395999885106,
				"outcome": "failed",
				"crash": {
					"path": "/home/nik/Desktop/TDSOM_UPDATED/webapp/script_test/test/test_ft_isalnum.py",
					"lineno": 136,
					"message": "assert 9213 == 0"
				},
				"traceback": [
					{
						"path": "script_test/test/test_ft_isalnum.py",
						"lineno": 136,
						"message": "in test4_ft_isalnum"
					}
				],
				"longrepr": "script_test/test/test_ft_isalnum.py:136: in test4_ft_isalnum\n    assert result == original_result\nE   assert 9213 == 0"
			},
			"teardown": {
				"duration": 0.0001823249995140941,
				"outcome": "passed"
			}
		},
		{
			"nodeid": "script_test/test/test_ft_isalnum.py::test5_ft_isalnum",
			"lineno": 137,
			"outcome": "failed",
			"keywords": [
				"test5_ft_isalnum",
				"script_test/test/test_ft_isalnum.py",
				"webapp"
			],
			"setup": {
				"duration": 0.00017777700031729182,
				"outcome": "passed"
			},
			"call": {
				"duration": 0.00028601099984371103,
				"outcome": "failed",
				"crash": {
					"path": "/home/nik/Desktop/TDSOM_UPDATED/webapp/script_test/test/test_ft_isalnum.py",
					"lineno": 167,
					"message": "assert 9213 == 8"
				},
				"traceback": [
					{
						"path": "script_test/test/test_ft_isalnum.py",
						"lineno": 167,
						"message": "in test5_ft_isalnum"
					}
				],
				"longrepr": "script_test/test/test_ft_isalnum.py:167: in test5_ft_isalnum\n    assert result == original_result\nE   assert 9213 == 8"
			},
			"teardown": {
				"duration": 0.0001706590001049335,
				"outcome": "passed"
			}
		},
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
				"duration": 0.00019013499968423275,
				"outcome": "passed"
			},
			"call": {
				"duration": 0.00033153600088553503,
				"outcome": "failed",
				"crash": {
					"path": "/home/nik/Desktop/TDSOM_UPDATED/webapp/script_test/test/test_ft_isalnum.py",
					"lineno": 43,
					"message": "assert 9213 == 8"
				},
				"traceback": [
					{
						"path": "script_test/test/test_ft_isalnum.py",
						"lineno": 43,
						"message": "in test1_ft_isalnum"
					}
				],
				"longrepr": "script_test/test/test_ft_isalnum.py:43: in test1_ft_isalnum\n    assert result == original_result\nE   assert 9213 == 8"
			},
			"teardown": {
				"duration": 0.0002780189997793059,
				"outcome": "passed"
			}
		},
		{
			"nodeid": "script_test/test/test_ft_isalnum.py::test2_ft_isalnum",
			"lineno": 44,
			"outcome": "failed",
			"keywords": [
				"test2_ft_isalnum",
				"script_test/test/test_ft_isalnum.py",
				"webapp"
			],
			"setup": {
				"duration": 0.00020468999991862802,
				"outcome": "passed"
			},
			"call": {
				"duration": 0.00033436500052630436,
				"outcome": "failed",
				"crash": {
					"path": "/home/nik/Desktop/TDSOM_UPDATED/webapp/script_test/test/test_ft_isalnum.py",
					"lineno": 74,
					"message": "assert 9213 == 0"
				},
				"traceback": [
					{
						"path": "script_test/test/test_ft_isalnum.py",
						"lineno": 74,
						"message": "in test2_ft_isalnum"
					}
				],
				"longrepr": "script_test/test/test_ft_isalnum.py:74: in test2_ft_isalnum\n    assert result == original_result\nE   assert 9213 == 0"
			},
			"teardown": {
				"duration": 0.000209198000447941,
				"outcome": "passed"
			}
		},
		{
			"nodeid": "script_test/test/test_ft_isalnum.py::test3_ft_isalnum",
			"lineno": 75,
			"outcome": "failed",
			"keywords": [
				"test3_ft_isalnum",
				"script_test/test/test_ft_isalnum.py",
				"webapp"
			],
			"setup": {
				"duration": 0.00018657700002222555,
				"outcome": "passed"
			},
			"call": {
				"duration": 0.0002969560000565252,
				"outcome": "failed",
				"crash": {
					"path": "/home/nik/Desktop/TDSOM_UPDATED/webapp/script_test/test/test_ft_isalnum.py",
					"lineno": 105,
					"message": "assert 9213 == 0"
				},
				"traceback": [
					{
						"path": "script_test/test/test_ft_isalnum.py",
						"lineno": 105,
						"message": "in test3_ft_isalnum"
					}
				],
				"longrepr": "script_test/test/test_ft_isalnum.py:105: in test3_ft_isalnum\n    assert result == original_result\nE   assert 9213 == 0"
			},
			"teardown": {
				"duration": 0.00018265200014866423,
				"outcome": "passed"
			}
		},
		{
			"nodeid": "script_test/test/test_ft_isalnum.py::test4_ft_isalnum",
			"lineno": 106,
			"outcome": "failed",
			"keywords": [
				"test4_ft_isalnum",
				"script_test/test/test_ft_isalnum.py",
				"webapp"
			],
			"setup": {
				"duration": 0.00017856399972515646,
				"outcome": "passed"
			},
			"call": {
				"duration": 0.000278395999885106,
				"outcome": "failed",
				"crash": {
					"path": "/home/nik/Desktop/TDSOM_UPDATED/webapp/script_test/test/test_ft_isalnum.py",
					"lineno": 136,
					"message": "assert 9213 == 0"
				},
				"traceback": [
					{
						"path": "script_test/test/test_ft_isalnum.py",
						"lineno": 136,
						"message": "in test4_ft_isalnum"
					}
				],
				"longrepr": "script_test/test/test_ft_isalnum.py:136: in test4_ft_isalnum\n    assert result == original_result\nE   assert 9213 == 0"
			},
			"teardown": {
				"duration": 0.0001823249995140941,
				"outcome": "passed"
			}
		},
		{
			"nodeid": "script_test/test/test_ft_isalnum.py::test5_ft_isalnum",
			"lineno": 137,
			"outcome": "failed",
			"keywords": [
				"test5_ft_isalnum",
				"script_test/test/test_ft_isalnum.py",
				"webapp"
			],
			"setup": {
				"duration": 0.00017777700031729182,
				"outcome": "passed"
			},
			"call": {
				"duration": 0.00028601099984371103,
				"outcome": "failed",
				"crash": {
					"path": "/home/nik/Desktop/TDSOM_UPDATED/webapp/script_test/test/test_ft_isalnum.py",
					"lineno": 167,
					"message": "assert 9213 == 8"
				},
				"traceback": [
					{
						"path": "script_test/test/test_ft_isalnum.py",
						"lineno": 167,
						"message": "in test5_ft_isalnum"
					}
				],
				"longrepr": "script_test/test/test_ft_isalnum.py:167: in test5_ft_isalnum\n    assert result == original_result\nE   assert 9213 == 8"
			},
			"teardown": {
				"duration": 0.0001706590001049335,
				"outcome": "passed"
			}
		},
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
				"duration": 0.00019013499968423275,
				"outcome": "passed"
			},
			"call": {
				"duration": 0.00033153600088553503,
				"outcome": "failed",
				"crash": {
					"path": "/home/nik/Desktop/TDSOM_UPDATED/webapp/script_test/test/test_ft_isalnum.py",
					"lineno": 43,
					"message": "assert 9213 == 8"
				},
				"traceback": [
					{
						"path": "script_test/test/test_ft_isalnum.py",
						"lineno": 43,
						"message": "in test1_ft_isalnum"
					}
				],
				"longrepr": "script_test/test/test_ft_isalnum.py:43: in test1_ft_isalnum\n    assert result == original_result\nE   assert 9213 == 8"
			},
			"teardown": {
				"duration": 0.0002780189997793059,
				"outcome": "passed"
			}
		},
		{
			"nodeid": "script_test/test/test_ft_isalnum.py::test2_ft_isalnum",
			"lineno": 44,
			"outcome": "failed",
			"keywords": [
				"test2_ft_isalnum",
				"script_test/test/test_ft_isalnum.py",
				"webapp"
			],
			"setup": {
				"duration": 0.00020468999991862802,
				"outcome": "passed"
			},
			"call": {
				"duration": 0.00033436500052630436,
				"outcome": "failed",
				"crash": {
					"path": "/home/nik/Desktop/TDSOM_UPDATED/webapp/script_test/test/test_ft_isalnum.py",
					"lineno": 74,
					"message": "assert 9213 == 0"
				},
				"traceback": [
					{
						"path": "script_test/test/test_ft_isalnum.py",
						"lineno": 74,
						"message": "in test2_ft_isalnum"
					}
				],
				"longrepr": "script_test/test/test_ft_isalnum.py:74: in test2_ft_isalnum\n    assert result == original_result\nE   assert 9213 == 0"
			},
			"teardown": {
				"duration": 0.000209198000447941,
				"outcome": "passed"
			}
		},
		{
			"nodeid": "script_test/test/test_ft_isalnum.py::test3_ft_isalnum",
			"lineno": 75,
			"outcome": "failed",
			"keywords": [
				"test3_ft_isalnum",
				"script_test/test/test_ft_isalnum.py",
				"webapp"
			],
			"setup": {
				"duration": 0.00018657700002222555,
				"outcome": "passed"
			},
			"call": {
				"duration": 0.0002969560000565252,
				"outcome": "failed",
				"crash": {
					"path": "/home/nik/Desktop/TDSOM_UPDATED/webapp/script_test/test/test_ft_isalnum.py",
					"lineno": 105,
					"message": "assert 9213 == 0"
				},
				"traceback": [
					{
						"path": "script_test/test/test_ft_isalnum.py",
						"lineno": 105,
						"message": "in test3_ft_isalnum"
					}
				],
				"longrepr": "script_test/test/test_ft_isalnum.py:105: in test3_ft_isalnum\n    assert result == original_result\nE   assert 9213 == 0"
			},
			"teardown": {
				"duration": 0.00018265200014866423,
				"outcome": "passed"
			}
		},
		{
			"nodeid": "script_test/test/test_ft_isalnum.py::test4_ft_isalnum",
			"lineno": 106,
			"outcome": "failed",
			"keywords": [
				"test4_ft_isalnum",
				"script_test/test/test_ft_isalnum.py",
				"webapp"
			],
			"setup": {
				"duration": 0.00017856399972515646,
				"outcome": "passed"
			},
			"call": {
				"duration": 0.000278395999885106,
				"outcome": "failed",
				"crash": {
					"path": "/home/nik/Desktop/TDSOM_UPDATED/webapp/script_test/test/test_ft_isalnum.py",
					"lineno": 136,
					"message": "assert 9213 == 0"
				},
				"traceback": [
					{
						"path": "script_test/test/test_ft_isalnum.py",
						"lineno": 136,
						"message": "in test4_ft_isalnum"
					}
				],
				"longrepr": "script_test/test/test_ft_isalnum.py:136: in test4_ft_isalnum\n    assert result == original_result\nE   assert 9213 == 0"
			},
			"teardown": {
				"duration": 0.0001823249995140941,
				"outcome": "passed"
			}
		},
		{
			"nodeid": "script_test/test/test_ft_isalnum.py::test5_ft_isalnum",
			"lineno": 137,
			"outcome": "failed",
			"keywords": [
				"test5_ft_isalnum",
				"script_test/test/test_ft_isalnum.py",
				"webapp"
			],
			"setup": {
				"duration": 0.00017777700031729182,
				"outcome": "passed"
			},
			"call": {
				"duration": 0.00028601099984371103,
				"outcome": "failed",
				"crash": {
					"path": "/home/nik/Desktop/TDSOM_UPDATED/webapp/script_test/test/test_ft_isalnum.py",
					"lineno": 167,
					"message": "assert 9213 == 8"
				},
				"traceback": [
					{
						"path": "script_test/test/test_ft_isalnum.py",
						"lineno": 167,
						"message": "in test5_ft_isalnum"
					}
				],
				"longrepr": "script_test/test/test_ft_isalnum.py:167: in test5_ft_isalnum\n    assert result == original_result\nE   assert 9213 == 8"
			},
			"teardown": {
				"duration": 0.0001706590001049335,
				"outcome": "passed"
			}
		},
	]
}
