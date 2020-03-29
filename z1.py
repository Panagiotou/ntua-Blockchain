 * Serving Flask app "Rest" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://127.0.0.5:5000/ (Press CTRL+C to quit)
127.0.0.1 - - [29/Mar/2020 21:05:16] "GET /Live HTTP/1.1" 200 -
	 	 I am transaction (460bf54d4ac5d31a74940a58e43f4c003540569e) giving 100 $ from node 0 to node 4
previous block
	 I am block with index 0
	 My Transaction list contains:
	 	 I am transaction (3e7bdd1cd8cb19b6242bb2a1ea1e6df90b2d1f94) giving 500 $ from node genesis to node 0
4 5
127.0.0.1 - - [29/Mar/2020 21:05:16] "POST /ValidateTransaction HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:16] "GET /Live HTTP/1.1" 200 -
{'id': 1, 'ip': '127.0.0.2', 'port': 5000, 'public_key': <_RSAobj @0x7fd1e884b2b0 n(2048),e>, 'balance': 0}
{'id': 2, 'ip': '127.0.0.3', 'port': 5000, 'public_key': <_RSAobj @0x7fd1e884b278 n(2048),e>, 'balance': 0}
{'id': 3, 'ip': '127.0.0.4', 'port': 5000, 'public_key': <_RSAobj @0x7fd1e884b240 n(2048),e>, 'balance': 0}
127.0.0.1 - - [29/Mar/2020 21:05:16] "POST /UpdateRing HTTP/1.1" 200 -
Reading input transactions from txt
[{'balance': 0, 'id': 0, 'ip': '127.0.0.1', 'port': '5000', 'public_key': <_RSAobj @0x7fd1e8abd128 n(2048),e>}, {'id': 1, 'ip': '127.0.0.2', 'port': 5000, 'public_key': <_RSAobj @0x7fd1e884b2b0 n(2048),e>, 'balance': 0}, {'id': 2, 'ip': '127.0.0.3', 'port': 5000, 'public_key': <_RSAobj @0x7fd1e884b278 n(2048),e>, 'balance': 0}, {'id': 3, 'ip': '127.0.0.4', 'port': 5000, 'public_key': <_RSAobj @0x7fd1e884b240 n(2048),e>, 'balance': 0}]
	 	 I am transaction (75c07dde241ab0c64c451d2489a22b7b5142fd1d) giving 1 $ from node 4 to node 3
previous block
	 I am block with index 0
	 My Transaction list contains:
	 	 I am transaction (3e7bdd1cd8cb19b6242bb2a1ea1e6df90b2d1f94) giving 500 $ from node genesis to node 0
5 5
I have to mine
Mining block
	 I am block with index 1
	 My Transaction list contains:
	 	 I am transaction (bd970252d6402238b21478516ec1cf5698c9fae5) giving 100 $ from node 0 to node 1
	 	 I am transaction (82baab665489b6d523721fec9fad6f1e9e281c13) giving 100 $ from node 0 to node 2
	 	 I am transaction (cc4040036b22cb128a93a3f7d6d59090d47a7a9f) giving 100 $ from node 0 to node 3
	 	 I am transaction (460bf54d4ac5d31a74940a58e43f4c003540569e) giving 100 $ from node 0 to node 4
	 	 I am transaction (75c07dde241ab0c64c451d2489a22b7b5142fd1d) giving 1 $ from node 4 to node 3
127.0.0.1 - - [29/Mar/2020 21:05:17] "POST /AddBlock HTTP/1.1" 200 -
Done
127.0.0.1 - - [29/Mar/2020 21:05:18] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:18] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:18] "GET /Chain HTTP/1.1" 200 -
chain changed for node 4 my chain length was 2
Other chain lengths are:
	 node 0 , len 2
	 node 1 , len 2
	 node 2 , len 2
	 node 3 , len 3
3 4 4
selected node 3 , len 3
127.0.0.1 - - [29/Mar/2020 21:05:18] "POST /AddBlock HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:18] "POST /ValidateTransaction HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:18] "POST /ValidateTransaction HTTP/1.1" 200 -
	 	 I am transaction (4f200d0e54c1cfedc572c9e9e228eda13a934c32) giving 1 $ from node 3 to node 2
127.0.0.1 - - [29/Mar/2020 21:05:18] "POST /ValidateTransaction HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:18] "POST /ValidateTransaction HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:18] "POST /ValidateTransaction HTTP/1.1" 200 -
previous block
	 I am block with index 2
	 My Transaction list contains:
	 	 I am transaction (71207f946085d739fb93ff5b157ffef092f8c4c4) giving 2 $ from node 2 to node 3
	 	 I am transaction (4c80bcdabc9bc47adf485f88aa16b95b0e984da3) giving 3 $ from node 2 to node 0
	 	 I am transaction (4f22f058a18d952b39131b5d6e122c3bf2626205) giving 4 $ from node 2 to node 4
	 	 I am transaction (82813a1a2f499f2246235103faedb2f9920bd6c1) giving 5 $ from node 2 to node 3
	 	 I am transaction (1d62677497dfe519db820ed3d61e65fd1d1f037a) giving 2 $ from node 3 to node 4
1 5
127.0.0.1 - - [29/Mar/2020 21:05:18] "POST /ValidateTransaction HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:18] "POST /ValidateTransaction HTTP/1.1" 200 -
	 	 I am transaction (7d389fd7c85d438ff86bcff8e79c6f5987fc82b8) giving 1 $ from node 1 to node 3
previous block
	 I am block with index 2
	 My Transaction list contains:
	 	 I am transaction (71207f946085d739fb93ff5b157ffef092f8c4c4) giving 2 $ from node 2 to node 3
	 	 I am transaction (4c80bcdabc9bc47adf485f88aa16b95b0e984da3) giving 3 $ from node 2 to node 0
	 	 I am transaction (4f22f058a18d952b39131b5d6e122c3bf2626205) giving 4 $ from node 2 to node 4
	 	 I am transaction (82813a1a2f499f2246235103faedb2f9920bd6c1) giving 5 $ from node 2 to node 3
	 	 I am transaction (1d62677497dfe519db820ed3d61e65fd1d1f037a) giving 2 $ from node 3 to node 4
2 5
127.0.0.1 - - [29/Mar/2020 21:05:18] "POST /ValidateTransaction HTTP/1.1" 200 -
	 	 I am transaction (a5c4853d6e0428c43001baab2e4f9f2bdeadc2c8) giving 1 $ from node 0 to node 1
previous block
	 I am block with index 2
	 My Transaction list contains:
	 	 I am transaction (71207f946085d739fb93ff5b157ffef092f8c4c4) giving 2 $ from node 2 to node 3
	 	 I am transaction (4c80bcdabc9bc47adf485f88aa16b95b0e984da3) giving 3 $ from node 2 to node 0
	 	 I am transaction (4f22f058a18d952b39131b5d6e122c3bf2626205) giving 4 $ from node 2 to node 4
	 	 I am transaction (82813a1a2f499f2246235103faedb2f9920bd6c1) giving 5 $ from node 2 to node 3
	 	 I am transaction (1d62677497dfe519db820ed3d61e65fd1d1f037a) giving 2 $ from node 3 to node 4
3 5
127.0.0.1 - - [29/Mar/2020 21:05:18] "POST /ValidateTransaction HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:18] "POST /ValidateTransaction HTTP/1.1" 200 -
	 	 I am transaction (939490a4e6686c59c923121ed717a06c67b1af97) giving 6 $ from node 2 to node 1
previous block
	 I am block with index 2
	 My Transaction list contains:
	 	 I am transaction (71207f946085d739fb93ff5b157ffef092f8c4c4) giving 2 $ from node 2 to node 3
	 	 I am transaction (4c80bcdabc9bc47adf485f88aa16b95b0e984da3) giving 3 $ from node 2 to node 0
	 	 I am transaction (4f22f058a18d952b39131b5d6e122c3bf2626205) giving 4 $ from node 2 to node 4
127.0.0.1 - - [29/Mar/2020 21:05:19] "GET /Chain HTTP/1.1" 200 -
	 	 I am transaction (82813a1a2f499f2246235103faedb2f9920bd6c1) giving 5 $ from node 2 to node 3
	 	 I am transaction (1d62677497dfe519db820ed3d61e65fd1d1f037a) giving 2 $ from node 3 to node 4
4 5
127.0.0.1 - - [29/Mar/2020 21:05:19] "POST /ValidateTransaction HTTP/1.1" 200 -
	 	 I am transaction (645b10978b756e500f0ab25a54f0b8f887126959) giving 3 $ from node 3 to node 0
previous block
	 I am block with index 2
	 My Transaction list contains:
	 	 I am transaction (71207f946085d739fb93ff5b157ffef092f8c4c4) giving 2 $ from node 2 to node 3
	 	 I am transaction (4c80bcdabc9bc47adf485f88aa16b95b0e984da3) giving 3 $ from node 2 to node 0
	 	 I am transaction (4f22f058a18d952b39131b5d6e122c3bf2626205) giving 4 $ from node 2 to node 4
	 	 I am transaction (82813a1a2f499f2246235103faedb2f9920bd6c1) giving 5 $ from node 2 to node 3
	 	 I am transaction (1d62677497dfe519db820ed3d61e65fd1d1f037a) giving 2 $ from node 3 to node 4
5 5
I have to mine
Mining block
	 I am block with index 2
	 My Transaction list contains:
	 	 I am transaction (4f200d0e54c1cfedc572c9e9e228eda13a934c32) giving 1 $ from node 3 to node 2
	 	 I am transaction (7d389fd7c85d438ff86bcff8e79c6f5987fc82b8) giving 1 $ from node 1 to node 3
	 	 I am transaction (a5c4853d6e0428c43001baab2e4f9f2bdeadc2c8) giving 1 $ from node 0 to node 1
	 	 I am transaction (939490a4e6686c59c923121ed717a06c67b1af97) giving 6 $ from node 2 to node 1
	 	 I am transaction (645b10978b756e500f0ab25a54f0b8f887126959) giving 3 $ from node 3 to node 0
127.0.0.1 - - [29/Mar/2020 21:05:19] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:19] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:19] "GET /Chain HTTP/1.1" 200 -
chain changed for node 4 my chain length was 3
Other chain lengths are:
	 node 0 , len 2
127.0.0.1 - - [29/Mar/2020 21:05:19] "GET /Chain HTTP/1.1" 200 -
	 node 1 , len 2
	 node 2 , len 3
	 node 3 , len 3
3 4 4
selected node 3 , len 3
127.0.0.1 - - [29/Mar/2020 21:05:19] "POST /AddBlock HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:19] "GET /Chain HTTP/1.1" 200 -
chain changed for node 4 my chain length was 3
Other chain lengths are:
	 node 0 , len 2
	 node 1 , len 2
	 node 2 , len 3
	 node 3 , len 3
3 4 4
selected node 3 , len 3
127.0.0.1 - - [29/Mar/2020 21:05:19] "POST /AddBlock HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:19] "GET /Chain HTTP/1.1" 200 -
Done
127.0.0.1 - - [29/Mar/2020 21:05:19] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:19] "GET /Chain HTTP/1.1" 200 -
chain changed for node 4 my chain length was 3
Other chain lengths are:
	 node 0 , len 2
	 node 1 , len 3
	 node 2 , len 3
	 node 3 , len 3
127.0.0.1 - - [29/Mar/2020 21:05:19] "GET /Chain HTTP/1.1" 200 -
2 4 4
selected node 2 , len 3
127.0.0.1 - - [29/Mar/2020 21:05:19] "POST /AddBlock HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:19] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:19] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:19] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:20] "GET /Chain HTTP/1.1" 200 -
chain changed for node 4 my chain length was 3
127.0.0.1 - - [29/Mar/2020 21:05:20] "GET /Chain HTTP/1.1" 200 -
Other chain lengths are:
	 node 0 , len 3
	 node 1 , len 3
	 node 2 , len 3
	 node 3 , len 3
1 4 4
selected node 1 , len 3
127.0.0.1 - - [29/Mar/2020 21:05:20] "POST /AddBlock HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:20] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:20] "GET /Chain HTTP/1.1" 200 -
chain changed for node 4 my chain length was 3
Other chain lengths are:
	 node 0 , len 3
	 node 1 , len 3
	 node 2 , len 3
	 node 3 , len 3
1 4 4
selected node 1 , len 3
127.0.0.1 - - [29/Mar/2020 21:05:20] "POST /AddBlock HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:20] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:20] "POST /AddBlock HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:20] "GET /Chain HTTP/1.1" 200 -
chain changed for node 4 my chain length was 4
Other chain lengths are:
	 node 0 , len 3
	 node 1 , len 3
	 node 2 , len 3
	 node 3 , len 4
3 4 4
selected node 3 , len 4
127.0.0.1 - - [29/Mar/2020 21:05:20] "POST /AddBlock HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:20] "POST /ValidateTransaction HTTP/1.1" 200 -
	 	 I am transaction (44febccc946afb1c181d5891a7e5424e16d41331) giving 2 $ from node 4 to node 0
previous block
	 I am block with index 3
	 My Transaction list contains:
	 	 I am transaction (7d389fd7c85d438ff86bcff8e79c6f5987fc82b8) giving 1 $ from node 1 to node 3
	 	 I am transaction (645b10978b756e500f0ab25a54f0b8f887126959) giving 3 $ from node 3 to node 0
	 	 I am transaction (a5c4853d6e0428c43001baab2e4f9f2bdeadc2c8) giving 1 $ from node 0 to node 1
	 	 I am transaction (75c07dde241ab0c64c451d2489a22b7b5142fd1d) giving 1 $ from node 4 to node 3
	 	 I am transaction (939490a4e6686c59c923121ed717a06c67b1af97) giving 6 $ from node 2 to node 1
1 5
127.0.0.1 - - [29/Mar/2020 21:05:20] "POST /ValidateTransaction HTTP/1.1" 200 -
	 	 I am transaction (6b83923d8f733a16046365dab263659e0fa5c883) giving 2 $ from node 1 to node 0
previous block
	 I am block with index 3
	 My Transaction list contains:
	 	 I am transaction (7d389fd7c85d438ff86bcff8e79c6f5987fc82b8) giving 1 $ from node 1 to node 3
	 	 I am transaction (645b10978b756e500f0ab25a54f0b8f887126959) giving 3 $ from node 3 to node 0
	 	 I am transaction (a5c4853d6e0428c43001baab2e4f9f2bdeadc2c8) giving 1 $ from node 0 to node 1
	 	 I am transaction (75c07dde241ab0c64c451d2489a22b7b5142fd1d) giving 1 $ from node 4 to node 3
	 	 I am transaction (939490a4e6686c59c923121ed717a06c67b1af97) giving 6 $ from node 2 to node 1
2 5
127.0.0.1 - - [29/Mar/2020 21:05:20] "POST /ValidateTransaction HTTP/1.1" 200 -
	 	 I am transaction (a2f6ff0062fda6662c2bb32d553b50a17dbc46c6) giving 4 $ from node 3 to node 2
previous block
	 I am block with index 3
	 My Transaction list contains:
	 	 I am transaction (7d389fd7c85d438ff86bcff8e79c6f5987fc82b8) giving 1 $ from node 1 to node 3
	 	 I am transaction (645b10978b756e500f0ab25a54f0b8f887126959) giving 3 $ from node 3 to node 0
	 	 I am transaction (a5c4853d6e0428c43001baab2e4f9f2bdeadc2c8) giving 1 $ from node 0 to node 1
	 	 I am transaction (75c07dde241ab0c64c451d2489a22b7b5142fd1d) giving 1 $ from node 4 to node 3
	 	 I am transaction (939490a4e6686c59c923121ed717a06c67b1af97) giving 6 $ from node 2 to node 1
3 5
127.0.0.1 - - [29/Mar/2020 21:05:20] "POST /ValidateTransaction HTTP/1.1" 200 -
	 	 I am transaction (f8b7b41fcf0a9263d50dfc08e4de4f81a453cb6e) giving 7 $ from node 2 to node 1
previous block
	 I am block with index 3
	 My Transaction list contains:
	 	 I am transaction (7d389fd7c85d438ff86bcff8e79c6f5987fc82b8) giving 1 $ from node 1 to node 3
	 	 I am transaction (645b10978b756e500f0ab25a54f0b8f887126959) giving 3 $ from node 3 to node 0
	 	 I am transaction (a5c4853d6e0428c43001baab2e4f9f2bdeadc2c8) giving 1 $ from node 0 to node 1
	 	 I am transaction (75c07dde241ab0c64c451d2489a22b7b5142fd1d) giving 1 $ from node 4 to node 3
	 	 I am transaction (939490a4e6686c59c923121ed717a06c67b1af97) giving 6 $ from node 2 to node 1
4 5
127.0.0.1 - - [29/Mar/2020 21:05:20] "POST /ValidateTransaction HTTP/1.1" 200 -
	 	 I am transaction (159563e55122dba87932dbdb76a15787c31cec23) giving 2 $ from node 0 to node 2
previous block
	 I am block with index 3
	 My Transaction list contains:
	 	 I am transaction (7d389fd7c85d438ff86bcff8e79c6f5987fc82b8) giving 1 $ from node 1 to node 3
	 	 I am transaction (645b10978b756e500f0ab25a54f0b8f887126959) giving 3 $ from node 3 to node 0
	 	 I am transaction (a5c4853d6e0428c43001baab2e4f9f2bdeadc2c8) giving 1 $ from node 0 to node 1
	 	 I am transaction (75c07dde241ab0c64c451d2489a22b7b5142fd1d) giving 1 $ from node 4 to node 3
	 	 I am transaction (939490a4e6686c59c923121ed717a06c67b1af97) giving 6 $ from node 2 to node 1
5 5
I have to mine
Mining block
	 I am block with index 3
	 My Transaction list contains:
	 	 I am transaction (44febccc946afb1c181d5891a7e5424e16d41331) giving 2 $ from node 4 to node 0
	 	 I am transaction (6b83923d8f733a16046365dab263659e0fa5c883) giving 2 $ from node 1 to node 0
	 	 I am transaction (a2f6ff0062fda6662c2bb32d553b50a17dbc46c6) giving 4 $ from node 3 to node 2
	 	 I am transaction (f8b7b41fcf0a9263d50dfc08e4de4f81a453cb6e) giving 7 $ from node 2 to node 1
	 	 I am transaction (159563e55122dba87932dbdb76a15787c31cec23) giving 2 $ from node 0 to node 2
chain changed for node 4 my chain length was 4
Other chain lengths are:
	 node 0 , len 3
	 node 1 , len 3
	 node 2 , len 3
	 node 3 , len 4
3 4 4
selected node 3 , len 4
127.0.0.1 - - [29/Mar/2020 21:05:20] "POST /AddBlock HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:21] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:21] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:21] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:21] "GET /Chain HTTP/1.1" 200 -
chain changed for node 4 my chain length was 4
Other chain lengths are:
	 node 0 , len 3
	 node 1 , len 4
	 node 2 , len 4
	 node 3 , len 4
2 4 4
selected node 2 , len 4
127.0.0.1 - - [29/Mar/2020 21:05:21] "POST /AddBlock HTTP/1.1" 200 -
Done
127.0.0.1 - - [29/Mar/2020 21:05:21] "GET /Chain HTTP/1.1" 200 -
chain changed for node 4 my chain length was 4
Other chain lengths are:
	 node 0 , len 3
	 node 1 , len 4
	 node 2 , len 4
	 node 3 , len 4
2 4 4
selected node 2 , len 4
127.0.0.1 - - [29/Mar/2020 21:05:21] "POST /AddBlock HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:21] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:21] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:21] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:22] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:22] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:22] "GET /Chain HTTP/1.1" 200 -
chain changed for node 4 my chain length was 4
Other chain lengths are:
	 node 0 , len 4
	 node 1 , len 4
	 node 2 , len 4
	 node 3 , len 4
1 4 4
selected node 1 , len 4
127.0.0.1 - - [29/Mar/2020 21:05:22] "POST /AddBlock HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:22] "POST /ValidateTransaction HTTP/1.1" 200 -
	 	 I am transaction (83969789c2ff95aeedc412263b42b2a9d2eee8bd) giving 5 $ from node 3 to node 1
previous block
	 I am block with index 3
	 My Transaction list contains:
	 	 I am transaction (7d389fd7c85d438ff86bcff8e79c6f5987fc82b8) giving 1 $ from node 1 to node 3
	 	 I am transaction (645b10978b756e500f0ab25a54f0b8f887126959) giving 3 $ from node 3 to node 0
	 	 I am transaction (a5c4853d6e0428c43001baab2e4f9f2bdeadc2c8) giving 1 $ from node 0 to node 1
	 	 I am transaction (75c07dde241ab0c64c451d2489a22b7b5142fd1d) giving 1 $ from node 4 to node 3
	 	 I am transaction (939490a4e6686c59c923121ed717a06c67b1af97) giving 6 $ from node 2 to node 1
1 5
	 	 I am transaction (30bd82c3d48d9fa710030ed74e1cd6a59072bb02) giving 8 $ from node 2 to node 1
previous block
	 I am block with index 3
	 My Transaction list contains:
	 	 I am transaction (7d389fd7c85d438ff86bcff8e79c6f5987fc82b8) giving 1 $ from node 1 to node 3
	 	 I am transaction (645b10978b756e500f0ab25a54f0b8f887126959) giving 3 $ from node 3 to node 0
	 	 I am transaction (a5c4853d6e0428c43001baab2e4f9f2bdeadc2c8) giving 1 $ from node 0 to node 1
	 	 I am transaction (75c07dde241ab0c64c451d2489a22b7b5142fd1d) giving 1 $ from node 4 to node 3
	 	 I am transaction (939490a4e6686c59c923121ed717a06c67b1af97) giving 6 $ from node 2 to node 1
2 5
127.0.0.1 - - [29/Mar/2020 21:05:22] "POST /ValidateTransaction HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:22] "POST /ValidateTransaction HTTP/1.1" 200 -
	 	 I am transaction (d71e8736a2103e95bca4006cb8d810033f9828ba) giving 3 $ from node 4 to node 1
previous block
	 I am block with index 3
	 My Transaction list contains:
	 	 I am transaction (7d389fd7c85d438ff86bcff8e79c6f5987fc82b8) giving 1 $ from node 1 to node 3
	 	 I am transaction (645b10978b756e500f0ab25a54f0b8f887126959) giving 3 $ from node 3 to node 0
	 	 I am transaction (a5c4853d6e0428c43001baab2e4f9f2bdeadc2c8) giving 1 $ from node 0 to node 1
	 	 I am transaction (75c07dde241ab0c64c451d2489a22b7b5142fd1d) giving 1 $ from node 4 to node 3
	 	 I am transaction (939490a4e6686c59c923121ed717a06c67b1af97) giving 6 $ from node 2 to node 1
3 5
127.0.0.1 - - [29/Mar/2020 21:05:22] "POST /ValidateTransaction HTTP/1.1" 200 -
	 	 I am transaction (f7eed2a451f5d842e201f7e787cbd228b42d589d) giving 3 $ from node 1 to node 3
previous block
	 I am block with index 3
	 My Transaction list contains:
	 	 I am transaction (7d389fd7c85d438ff86bcff8e79c6f5987fc82b8) giving 1 $ from node 1 to node 3
	 	 I am transaction (645b10978b756e500f0ab25a54f0b8f887126959) giving 3 $ from node 3 to node 0
	 	 I am transaction (a5c4853d6e0428c43001baab2e4f9f2bdeadc2c8) giving 1 $ from node 0 to node 1
	 	 I am transaction (75c07dde241ab0c64c451d2489a22b7b5142fd1d) giving 1 $ from node 4 to node 3
	 	 I am transaction (939490a4e6686c59c923121ed717a06c67b1af97) giving 6 $ from node 2 to node 1
4 5
127.0.0.1 - - [29/Mar/2020 21:05:22] "POST /ValidateTransaction HTTP/1.1" 200 -
	 	 I am transaction (89d2257e48865caf5d053bda708e4d053eda1e78) giving 4 $ from node 4 to node 0
127.0.0.1 - - [29/Mar/2020 21:05:22] "GET /Chain HTTP/1.1" 200 -
previous block
	 I am block with index 3
	 My Transaction list contains:
	 	 I am transaction (7d389fd7c85d438ff86bcff8e79c6f5987fc82b8) giving 1 $ from node 1 to node 3
	 	 I am transaction (645b10978b756e500f0ab25a54f0b8f887126959) giving 3 $ from node 3 to node 0
	 	 I am transaction (a5c4853d6e0428c43001baab2e4f9f2bdeadc2c8) giving 1 $ from node 0 to node 1
	 	 I am transaction (75c07dde241ab0c64c451d2489a22b7b5142fd1d) giving 1 $ from node 4 to node 3
	 	 I am transaction (939490a4e6686c59c923121ed717a06c67b1af97) giving 6 $ from node 2 to node 1
5 5
I have to mine
Mining block
	 I am block with index 4
	 My Transaction list contains:
	 	 I am transaction (83969789c2ff95aeedc412263b42b2a9d2eee8bd) giving 5 $ from node 3 to node 1
	 	 I am transaction (30bd82c3d48d9fa710030ed74e1cd6a59072bb02) giving 8 $ from node 2 to node 1
	 	 I am transaction (d71e8736a2103e95bca4006cb8d810033f9828ba) giving 3 $ from node 4 to node 1
	 	 I am transaction (f7eed2a451f5d842e201f7e787cbd228b42d589d) giving 3 $ from node 1 to node 3
	 	 I am transaction (89d2257e48865caf5d053bda708e4d053eda1e78) giving 4 $ from node 4 to node 0
127.0.0.1 - - [29/Mar/2020 21:05:22] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:22] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:22] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:23] "GET /Chain HTTP/1.1" 200 -
chain changed for node 4 my chain length was 4
Other chain lengths are:
	 node 0 , len 4
	 node 1 , len 4
	 node 2 , len 4
	 node 3 , len 4
1 4 4
selected node 1 , len 4
127.0.0.1 - - [29/Mar/2020 21:05:23] "POST /AddBlock HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:23] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:23] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:23] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:23] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:23] "GET /Chain HTTP/1.1" 200 -
chain changed for node 4 my chain length was 4
Other chain lengths are:
	 node 0 , len 4
	 node 1 , len 4
	 node 2 , len 4
	 node 3 , len 4
1 4 4
selected node 1 , len 4
127.0.0.1 - - [29/Mar/2020 21:05:24] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:24] "POST /AddBlock HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:24] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:25] "POST /AddBlock HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:25] "POST /AddBlock HTTP/1.1" 200 -
Done
127.0.0.1 - - [29/Mar/2020 21:05:25] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:25] "GET /Chain HTTP/1.1" 200 -
chain changed for node 4 my chain length was 6
Other chain lengths are:
	 node 0 , len 6
	 node 1 , len 6
	 node 2 , len 6
	 node 3 , len 6
1 4 4
selected node 1 , len 6
127.0.0.1 - - [29/Mar/2020 21:05:26] "POST /AddBlock HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:26] "POST /ValidateTransaction HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:26] "POST /ValidateTransaction HTTP/1.1" 200 -
	 	 I am transaction (190058e49bff6cc69fbad2d6881f0f74cb2bbca0) giving 10 $ from node 2 to node 3
previous block
	 I am block with index 5
	 My Transaction list contains:
	 	 I am transaction (159563e55122dba87932dbdb76a15787c31cec23) giving 2 $ from node 0 to node 2
	 	 I am transaction (a6b44eb0a4e1691b3ad2548bca4c3cea0948da97) giving 9 $ from node 2 to node 0
	 	 I am transaction (83969789c2ff95aeedc412263b42b2a9d2eee8bd) giving 5 $ from node 3 to node 1
	 	 I am transaction (44febccc946afb1c181d5891a7e5424e16d41331) giving 2 $ from node 4 to node 0
	 	 I am transaction (f7eed2a451f5d842e201f7e787cbd228b42d589d) giving 3 $ from node 1 to node 3
1 5
127.0.0.1 - - [29/Mar/2020 21:05:26] "POST /ValidateTransaction HTTP/1.1" 200 -
	 	 I am transaction (d1be3e179e7bb47463351d66834833b90e4c0dd8) giving 6 $ from node 3 to node 2
previous block
	 I am block with index 5
	 My Transaction list contains:
	 	 I am transaction (159563e55122dba87932dbdb76a15787c31cec23) giving 2 $ from node 0 to node 2
	 	 I am transaction (a6b44eb0a4e1691b3ad2548bca4c3cea0948da97) giving 9 $ from node 2 to node 0
	 	 I am transaction (83969789c2ff95aeedc412263b42b2a9d2eee8bd) giving 5 $ from node 3 to node 1
	 	 I am transaction (44febccc946afb1c181d5891a7e5424e16d41331) giving 2 $ from node 4 to node 0
	 	 I am transaction (f7eed2a451f5d842e201f7e787cbd228b42d589d) giving 3 $ from node 1 to node 3
2 5
127.0.0.1 - - [29/Mar/2020 21:05:26] "POST /ValidateTransaction HTTP/1.1" 200 -
	 	 I am transaction (e280394356a2c8c334594372ab324e1fc30eeda5) giving 7 $ from node 3 to node 2
previous block
	 I am block with index 5
	 My Transaction list contains:
	 	 I am transaction (159563e55122dba87932dbdb76a15787c31cec23) giving 2 $ from node 0 to node 2
	 	 I am transaction (a6b44eb0a4e1691b3ad2548bca4c3cea0948da97) giving 9 $ from node 2 to node 0
	 	 I am transaction (83969789c2ff95aeedc412263b42b2a9d2eee8bd) giving 5 $ from node 3 to node 1
	 	 I am transaction (44febccc946afb1c181d5891a7e5424e16d41331) giving 2 $ from node 4 to node 0
	 	 I am transaction (f7eed2a451f5d842e201f7e787cbd228b42d589d) giving 3 $ from node 1 to node 3
3 5
127.0.0.1 - - [29/Mar/2020 21:05:26] "POST /ValidateTransaction HTTP/1.1" 200 -
	 	 I am transaction (fe0e06244e1fd41cd661ce9cd378f5e1c75dd1d5) giving 4 $ from node 1 to node 0
previous block
	 I am block with index 5
	 My Transaction list contains:
	 	 I am transaction (159563e55122dba87932dbdb76a15787c31cec23) giving 2 $ from node 0 to node 2
	 	 I am transaction (a6b44eb0a4e1691b3ad2548bca4c3cea0948da97) giving 9 $ from node 2 to node 0
	 	 I am transaction (83969789c2ff95aeedc412263b42b2a9d2eee8bd) giving 5 $ from node 3 to node 1
	 	 I am transaction (44febccc946afb1c181d5891a7e5424e16d41331) giving 2 $ from node 4 to node 0
	 	 I am transaction (f7eed2a451f5d842e201f7e787cbd228b42d589d) giving 3 $ from node 1 to node 3
4 5
127.0.0.1 - - [29/Mar/2020 21:05:26] "POST /ValidateTransaction HTTP/1.1" 200 -
	 	 I am transaction (cfc0e275f96d316e7c252266c37f0e607c54037d) giving 5 $ from node 4 to node 2
127.0.0.1 - - [29/Mar/2020 21:05:26] "GET /Chain HTTP/1.1" 200 -
previous block
	 I am block with index 5
	 My Transaction list contains:
	 	 I am transaction (159563e55122dba87932dbdb76a15787c31cec23) giving 2 $ from node 0 to node 2
	 	 I am transaction (a6b44eb0a4e1691b3ad2548bca4c3cea0948da97) giving 9 $ from node 2 to node 0
	 	 I am transaction (83969789c2ff95aeedc412263b42b2a9d2eee8bd) giving 5 $ from node 3 to node 1
	 	 I am transaction (44febccc946afb1c181d5891a7e5424e16d41331) giving 2 $ from node 4 to node 0
	 	 I am transaction (f7eed2a451f5d842e201f7e787cbd228b42d589d) giving 3 $ from node 1 to node 3
5 5
I have to mine
Mining block
	 I am block with index 5
	 My Transaction list contains:
	 	 I am transaction (190058e49bff6cc69fbad2d6881f0f74cb2bbca0) giving 10 $ from node 2 to node 3
	 	 I am transaction (d1be3e179e7bb47463351d66834833b90e4c0dd8) giving 6 $ from node 3 to node 2
	 	 I am transaction (e280394356a2c8c334594372ab324e1fc30eeda5) giving 7 $ from node 3 to node 2
	 	 I am transaction (fe0e06244e1fd41cd661ce9cd378f5e1c75dd1d5) giving 4 $ from node 1 to node 0
	 	 I am transaction (cfc0e275f96d316e7c252266c37f0e607c54037d) giving 5 $ from node 4 to node 2
Done
127.0.0.1 - - [29/Mar/2020 21:05:27] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:27] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:27] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:27] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:27] "POST /AddBlock HTTP/1.1" 200 -
chain changed for node 4 my chain length was 7
Other chain lengths are:
	 node 0 , len 6
	 node 1 , len 6
	 node 2 , len 6
	 node 3 , len 6
1 4 4
selected node 1 , len 6
127.0.0.1 - - [29/Mar/2020 21:05:27] "POST /AddBlock HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:27] "GET /Chain HTTP/1.1" 200 -
chain changed for node 4 my chain length was 6
Other chain lengths are:
	 node 0 , len 6
	 node 1 , len 6
	 node 2 , len 6
	 node 3 , len 6
1 4 4
selected node 1 , len 6
127.0.0.1 - - [29/Mar/2020 21:05:27] "POST /AddBlock HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:28] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:28] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:28] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:28] "GET /Chain HTTP/1.1" 200 -
chain changed for node 4 my chain length was 6
Other chain lengths are:
	 node 0 , len 6
	 node 1 , len 6
	 node 2 , len 7
	 node 3 , len 6
2 4 4
selected node 2 , len 7
127.0.0.1 - - [29/Mar/2020 21:05:28] "POST /AddBlock HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:28] "POST /ValidateTransaction HTTP/1.1" 200 -
	 	 I am transaction (4cff59508d420428cffac2f5efde19054668ba46) giving 3 $ from node 0 to node 2
previous block
	 I am block with index 6
	 My Transaction list contains:
	 	 I am transaction (d71e8736a2103e95bca4006cb8d810033f9828ba) giving 3 $ from node 4 to node 1
	 	 I am transaction (190058e49bff6cc69fbad2d6881f0f74cb2bbca0) giving 10 $ from node 2 to node 3
	 	 I am transaction (d1be3e179e7bb47463351d66834833b90e4c0dd8) giving 6 $ from node 3 to node 2
	 	 I am transaction (e280394356a2c8c334594372ab324e1fc30eeda5) giving 7 $ from node 3 to node 2
	 	 I am transaction (fe0e06244e1fd41cd661ce9cd378f5e1c75dd1d5) giving 4 $ from node 1 to node 0
1 5
127.0.0.1 - - [29/Mar/2020 21:05:28] "POST /ValidateTransaction HTTP/1.1" 200 -
	 	 I am transaction (f9d99ad4403adf5603f765f374b600696f1fc3c1) giving 6 $ from node 4 to node 1
previous block
	 I am block with index 6
	 My Transaction list contains:
	 	 I am transaction (d71e8736a2103e95bca4006cb8d810033f9828ba) giving 3 $ from node 4 to node 1
	 	 I am transaction (190058e49bff6cc69fbad2d6881f0f74cb2bbca0) giving 10 $ from node 2 to node 3
	 	 I am transaction (d1be3e179e7bb47463351d66834833b90e4c0dd8) giving 6 $ from node 3 to node 2
	 	 I am transaction (e280394356a2c8c334594372ab324e1fc30eeda5) giving 7 $ from node 3 to node 2
	 	 I am transaction (fe0e06244e1fd41cd661ce9cd378f5e1c75dd1d5) giving 4 $ from node 1 to node 0
2 5
127.0.0.1 - - [29/Mar/2020 21:05:28] "POST /ValidateTransaction HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:28] "GET /Chain HTTP/1.1" 200 -
	 	 I am transaction (37a465516989adaf7593f9d0aa2154b7d09b889b) giving 8 $ from node 3 to node 4
previous block
	 I am block with index 6
	 My Transaction list contains:
	 	 I am transaction (d71e8736a2103e95bca4006cb8d810033f9828ba) giving 3 $ from node 4 to node 1
	 	 I am transaction (190058e49bff6cc69fbad2d6881f0f74cb2bbca0) giving 10 $ from node 2 to node 3
	 	 I am transaction (d1be3e179e7bb47463351d66834833b90e4c0dd8) giving 6 $ from node 3 to node 2
	 	 I am transaction (e280394356a2c8c334594372ab324e1fc30eeda5) giving 7 $ from node 3 to node 2
	 	 I am transaction (fe0e06244e1fd41cd661ce9cd378f5e1c75dd1d5) giving 4 $ from node 1 to node 0
3 5
	 	 I am transaction (bedf943b483e382c24bbb76c8a3b5a0719ef7205) giving 7 $ from node 4 to node 0
127.0.0.1 - - [29/Mar/2020 21:05:28] "POST /ValidateTransaction HTTP/1.1" 200 -
previous block
	 I am block with index 6
	 My Transaction list contains:
	 	 I am transaction (d71e8736a2103e95bca4006cb8d810033f9828ba) giving 3 $ from node 4 to node 1
	 	 I am transaction (190058e49bff6cc69fbad2d6881f0f74cb2bbca0) giving 10 $ from node 2 to node 3
	 	 I am transaction (d1be3e179e7bb47463351d66834833b90e4c0dd8) giving 6 $ from node 3 to node 2
	 	 I am transaction (e280394356a2c8c334594372ab324e1fc30eeda5) giving 7 $ from node 3 to node 2
	 	 I am transaction (fe0e06244e1fd41cd661ce9cd378f5e1c75dd1d5) giving 4 $ from node 1 to node 0
4 5
127.0.0.1 - - [29/Mar/2020 21:05:28] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:28] "POST /ValidateTransaction HTTP/1.1" 200 -
	 	 I am transaction (d3df646fcee36fd7be1ab1b4736648263928e847) giving 8 $ from node 4 to node 3
previous block
	 I am block with index 6
127.0.0.1 - - [29/Mar/2020 21:05:28] "GET /Chain HTTP/1.1" 200 -
	 My Transaction list contains:
	 	 I am transaction (d71e8736a2103e95bca4006cb8d810033f9828ba) giving 3 $ from node 4 to node 1
	 	 I am transaction (190058e49bff6cc69fbad2d6881f0f74cb2bbca0) giving 10 $ from node 2 to node 3
	 	 I am transaction (d1be3e179e7bb47463351d66834833b90e4c0dd8) giving 6 $ from node 3 to node 2
	 	 I am transaction (e280394356a2c8c334594372ab324e1fc30eeda5) giving 7 $ from node 3 to node 2
	 	 I am transaction (fe0e06244e1fd41cd661ce9cd378f5e1c75dd1d5) giving 4 $ from node 1 to node 0
5 5
I have to mine
Mining block
	 I am block with index 6
	 My Transaction list contains:
	 	 I am transaction (4cff59508d420428cffac2f5efde19054668ba46) giving 3 $ from node 0 to node 2
	 	 I am transaction (f9d99ad4403adf5603f765f374b600696f1fc3c1) giving 6 $ from node 4 to node 1
	 	 I am transaction (37a465516989adaf7593f9d0aa2154b7d09b889b) giving 8 $ from node 3 to node 4
	 	 I am transaction (bedf943b483e382c24bbb76c8a3b5a0719ef7205) giving 7 $ from node 4 to node 0
	 	 I am transaction (d3df646fcee36fd7be1ab1b4736648263928e847) giving 8 $ from node 4 to node 3
127.0.0.1 - - [29/Mar/2020 21:05:28] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:29] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:29] "GET /Chain HTTP/1.1" 200 -
chain changed for node 4 my chain length was 7
Other chain lengths are:
	 node 0 , len 6
	 node 1 , len 6
	 node 2 , len 7
	 node 3 , len 7
3 4 4
selected node 3 , len 7
127.0.0.1 - - [29/Mar/2020 21:05:29] "POST /AddBlock HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:29] "GET /Chain HTTP/1.1" 200 -
Done
127.0.0.1 - - [29/Mar/2020 21:05:29] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:29] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:30] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:30] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:30] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:30] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:30] "POST /AddBlock HTTP/1.1" 200 -
chain changed for node 4 my chain length was 8
Other chain lengths are:
	 node 0 , len 7
	 node 1 , len 7
	 node 2 , len 7
	 node 3 , len 7
1 4 4
selected node 1 , len 7
127.0.0.1 - - [29/Mar/2020 21:05:30] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:30] "POST /AddBlock HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:30] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:31] "GET /Chain HTTP/1.1" 200 -
chain changed for node 4 my chain length was 7
Other chain lengths are:
	 node 0 , len 7
	 node 1 , len 7
	 node 2 , len 8
	 node 3 , len 7
2 4 4
selected node 2 , len 8
127.0.0.1 - - [29/Mar/2020 21:05:31] "POST /AddBlock HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:31] "GET /Chain HTTP/1.1" 200 -
chain changed for node 4 my chain length was 8
Other chain lengths are:
	 node 0 , len 7
	 node 1 , len 7
	 node 2 , len 7
	 node 3 , len 7
1 4 4
selected node 1 , len 7
127.0.0.1 - - [29/Mar/2020 21:05:31] "POST /AddBlock HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:31] "GET /Chain HTTP/1.1" 200 -
chain changed for node 4 my chain length was 7
Other chain lengths are:
	 node 0 , len 7
	 node 1 , len 8
	 node 2 , len 7
	 node 3 , len 7
1 4 4
selected node 1 , len 8
127.0.0.1 - - [29/Mar/2020 21:05:31] "POST /AddBlock HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:31] "POST /ValidateTransaction HTTP/1.1" 200 -
	 	 I am transaction (42e233fac0c2863e0954453dbb999ed13f965169) giving 5 $ from node 1 to node 4
previous block
	 I am block with index 7
	 My Transaction list contains:
	 	 I am transaction (89d2257e48865caf5d053bda708e4d053eda1e78) giving 4 $ from node 4 to node 0
	 	 I am transaction (4cff59508d420428cffac2f5efde19054668ba46) giving 3 $ from node 0 to node 2
	 	 I am transaction (f9d99ad4403adf5603f765f374b600696f1fc3c1) giving 6 $ from node 4 to node 1
	 	 I am transaction (cfc0e275f96d316e7c252266c37f0e607c54037d) giving 5 $ from node 4 to node 2
	 	 I am transaction (37a465516989adaf7593f9d0aa2154b7d09b889b) giving 8 $ from node 3 to node 4
1 5
127.0.0.1 - - [29/Mar/2020 21:05:31] "POST /ValidateTransaction HTTP/1.1" 200 -
	 	 I am transaction (61fc13eedfc95f97b00ac67e2ca23deea291a2dd) giving 4 $ from node 0 to node 2
previous block
	 I am block with index 7
	 My Transaction list contains:
	 	 I am transaction (89d2257e48865caf5d053bda708e4d053eda1e78) giving 4 $ from node 4 to node 0
	 	 I am transaction (4cff59508d420428cffac2f5efde19054668ba46) giving 3 $ from node 0 to node 2
	 	 I am transaction (f9d99ad4403adf5603f765f374b600696f1fc3c1) giving 6 $ from node 4 to node 1
	 	 I am transaction (cfc0e275f96d316e7c252266c37f0e607c54037d) giving 5 $ from node 4 to node 2
	 	 I am transaction (37a465516989adaf7593f9d0aa2154b7d09b889b) giving 8 $ from node 3 to node 4
2 5
127.0.0.1 - - [29/Mar/2020 21:05:31] "POST /ValidateTransaction HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:31] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:31] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:31] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:31] "GET /Chain HTTP/1.1" 200 -
	 	 I am transaction (9343a7a380a17666ba9caf9fcd9d067b28064051) giving 9 $ from node 4 to node 3
previous block
	 I am block with index 7
	 My Transaction list contains:
	 	 I am transaction (89d2257e48865caf5d053bda708e4d053eda1e78) giving 4 $ from node 4 to node 0
	 	 I am transaction (4cff59508d420428cffac2f5efde19054668ba46) giving 3 $ from node 0 to node 2
	 	 I am transaction (f9d99ad4403adf5603f765f374b600696f1fc3c1) giving 6 $ from node 4 to node 1
	 	 I am transaction (cfc0e275f96d316e7c252266c37f0e607c54037d) giving 5 $ from node 4 to node 2
	 	 I am transaction (37a465516989adaf7593f9d0aa2154b7d09b889b) giving 8 $ from node 3 to node 4
3 5
127.0.0.1 - - [29/Mar/2020 21:05:31] "POST /ValidateTransaction HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:31] "GET /Chain HTTP/1.1" 200 -
	 	 I am transaction (eda3c5d830659d25a7bcf4a3f89d1dc61fa75e35) giving 10 $ from node 4 to node 0
previous block
	 I am block with index 7
	 My Transaction list contains:
	 	 I am transaction (89d2257e48865caf5d053bda708e4d053eda1e78) giving 4 $ from node 4 to node 0
	 	 I am transaction (4cff59508d420428cffac2f5efde19054668ba46) giving 3 $ from node 0 to node 2
	 	 I am transaction (f9d99ad4403adf5603f765f374b600696f1fc3c1) giving 6 $ from node 4 to node 1
	 	 I am transaction (cfc0e275f96d316e7c252266c37f0e607c54037d) giving 5 $ from node 4 to node 2
	 	 I am transaction (37a465516989adaf7593f9d0aa2154b7d09b889b) giving 8 $ from node 3 to node 4
4 5
127.0.0.1 - - [29/Mar/2020 21:05:32] "POST /ValidateTransaction HTTP/1.1" 200 -
	 	 I am transaction (9b82f809ef144bf147392189ae454d9e2865b4dd) giving 9 $ from node 3 to node 4
previous block
	 I am block with index 7
	 My Transaction list contains:
	 	 I am transaction (89d2257e48865caf5d053bda708e4d053eda1e78) giving 4 $ from node 4 to node 0
	 	 I am transaction (4cff59508d420428cffac2f5efde19054668ba46) giving 3 $ from node 0 to node 2
	 	 I am transaction (f9d99ad4403adf5603f765f374b600696f1fc3c1) giving 6 $ from node 4 to node 1
	 	 I am transaction (cfc0e275f96d316e7c252266c37f0e607c54037d) giving 5 $ from node 4 to node 2
	 	 I am transaction (37a465516989adaf7593f9d0aa2154b7d09b889b) giving 8 $ from node 3 to node 4
5 5
I have to mine
	 	 I am transaction (9fc0474368e0edf92519b875b240e0f9646cf37c) giving 5 $ from node 0 to node 1
previous block
	 I am block with index 7
	 My Transaction list contains:
	 	 I am transaction (89d2257e48865caf5d053bda708e4d053eda1e78) giving 4 $ from node 4 to node 0
	 	 I am transaction (4cff59508d420428cffac2f5efde19054668ba46) giving 3 $ from node 0 to node 2
	 	 I am transaction (f9d99ad4403adf5603f765f374b600696f1fc3c1) giving 6 $ from node 4 to node 1
	 	 I am transaction (cfc0e275f96d316e7c252266c37f0e607c54037d) giving 5 $ from node 4 to node 2
	 	 I am transaction (37a465516989adaf7593f9d0aa2154b7d09b889b) giving 8 $ from node 3 to node 4
6 5
ERROR-----------
	 I am block with index 7
	 My Transaction list contains:
	 	 I am transaction (42e233fac0c2863e0954453dbb999ed13f965169) giving 5 $ from node 1 to node 4
	 	 I am transaction (61fc13eedfc95f97b00ac67e2ca23deea291a2dd) giving 4 $ from node 0 to node 2
	 	 I am transaction (9343a7a380a17666ba9caf9fcd9d067b28064051) giving 9 $ from node 4 to node 3
	 	 I am transaction (eda3c5d830659d25a7bcf4a3f89d1dc61fa75e35) giving 10 $ from node 4 to node 0
	 	 I am transaction (9b82f809ef144bf147392189ae454d9e2865b4dd) giving 9 $ from node 3 to node 4
	 	 I am transaction (9fc0474368e0edf92519b875b240e0f9646cf37c) giving 5 $ from node 0 to node 1
Mining block
	 I am block with index 7
	 My Transaction list contains:
	 	 I am transaction (42e233fac0c2863e0954453dbb999ed13f965169) giving 5 $ from node 1 to node 4
	 	 I am transaction (61fc13eedfc95f97b00ac67e2ca23deea291a2dd) giving 4 $ from node 0 to node 2
	 	 I am transaction (9343a7a380a17666ba9caf9fcd9d067b28064051) giving 9 $ from node 4 to node 3
	 	 I am transaction (eda3c5d830659d25a7bcf4a3f89d1dc61fa75e35) giving 10 $ from node 4 to node 0
	 	 I am transaction (9b82f809ef144bf147392189ae454d9e2865b4dd) giving 9 $ from node 3 to node 4
	 	 I am transaction (9fc0474368e0edf92519b875b240e0f9646cf37c) giving 5 $ from node 0 to node 1
127.0.0.1 - - [29/Mar/2020 21:05:32] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:32] "POST /ValidateTransaction HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:32] "POST /AddBlock HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:32] "GET /Chain HTTP/1.1" 200 -
Done
127.0.0.1 - - [29/Mar/2020 21:05:33] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:33] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:33] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:33] "GET /Chain HTTP/1.1" 200 -
chain changed for node 4 my chain length was 9
Other chain lengths are:
	 node 0 , len 8
	 node 1 , len 9
	 node 2 , len 8
	 node 3 , len 9
3 4 4
selected node 3 , len 9
127.0.0.1 - - [29/Mar/2020 21:05:33] "POST /AddBlock HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:34] "GET /Chain HTTP/1.1" 200 -
chain changed for node 4 my chain length was 9
Other chain lengths are:
	 node 0 , len 9
	 node 1 , len 9
	 node 2 , len 9
	 node 3 , len 9
1 4 4
selected node 1 , len 9
127.0.0.1 - - [29/Mar/2020 21:05:34] "POST /AddBlock HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:34] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:34] "GET /Chain HTTP/1.1" 200 -
chain changed for node 4 my chain length was 9
Other chain lengths are:
	 node 0 , len 9
	 node 1 , len 9
	 node 2 , len 9
	 node 3 , len 9
1 4 4
selected node 1 , len 9
127.0.0.1 - - [29/Mar/2020 21:05:34] "POST /AddBlock HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:34] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:34] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:35] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:35] "GET /Chain HTTP/1.1" 200 -
chain changed for node 4 my chain length was 9
Other chain lengths are:
	 node 0 , len 9
	 node 1 , len 9
	 node 2 , len 9
	 node 3 , len 9
1 4 4
selected node 1 , len 9
127.0.0.1 - - [29/Mar/2020 21:05:35] "POST /AddBlock HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:35] "POST /ValidateTransaction HTTP/1.1" 200 -
	 	 I am transaction (2a5a123cf68bb77589b47a3cbd6c91de5c279187) giving 6 $ from node 1 to node 3
previous block
	 I am block with index 8
	 My Transaction list contains:
	 	 I am transaction (bedf943b483e382c24bbb76c8a3b5a0719ef7205) giving 7 $ from node 4 to node 0
	 	 I am transaction (42e233fac0c2863e0954453dbb999ed13f965169) giving 5 $ from node 1 to node 4
	 	 I am transaction (61fc13eedfc95f97b00ac67e2ca23deea291a2dd) giving 4 $ from node 0 to node 2
	 	 I am transaction (d3df646fcee36fd7be1ab1b4736648263928e847) giving 8 $ from node 4 to node 3
	 	 I am transaction (9343a7a380a17666ba9caf9fcd9d067b28064051) giving 9 $ from node 4 to node 3
1 5
127.0.0.1 - - [29/Mar/2020 21:05:35] "POST /ValidateTransaction HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:35] "GET /Chain HTTP/1.1" 200 -
	 	 I am transaction (5dddd18c84a479a9332a06c20a90b8507469348f) giving 10 $ from node 3 to node 0
previous block
	 I am block with index 8
	 My Transaction list contains:
	 	 I am transaction (bedf943b483e382c24bbb76c8a3b5a0719ef7205) giving 7 $ from node 4 to node 0
	 	 I am transaction (42e233fac0c2863e0954453dbb999ed13f965169) giving 5 $ from node 1 to node 4
	 	 I am transaction (61fc13eedfc95f97b00ac67e2ca23deea291a2dd) giving 4 $ from node 0 to node 2
	 	 I am transaction (d3df646fcee36fd7be1ab1b4736648263928e847) giving 8 $ from node 4 to node 3
	 	 I am transaction (9343a7a380a17666ba9caf9fcd9d067b28064051) giving 9 $ from node 4 to node 3
2 5
127.0.0.1 - - [29/Mar/2020 21:05:35] "POST /ValidateTransaction HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:35] "GET /Chain HTTP/1.1" 200 -
	 	 I am transaction (73e127c92d9bfee56763acea8eaa9bfde374a4d5) giving 7 $ from node 1 to node 2
previous block
	 I am block with index 8
	 My Transaction list contains:
	 	 I am transaction (bedf943b483e382c24bbb76c8a3b5a0719ef7205) giving 7 $ from node 4 to node 0
	 	 I am transaction (42e233fac0c2863e0954453dbb999ed13f965169) giving 5 $ from node 1 to node 4
	 	 I am transaction (61fc13eedfc95f97b00ac67e2ca23deea291a2dd) giving 4 $ from node 0 to node 2
	 	 I am transaction (d3df646fcee36fd7be1ab1b4736648263928e847) giving 8 $ from node 4 to node 3
	 	 I am transaction (9343a7a380a17666ba9caf9fcd9d067b28064051) giving 9 $ from node 4 to node 3
3 5
127.0.0.1 - - [29/Mar/2020 21:05:36] "POST /ValidateTransaction HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:36] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:36] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:36] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:36] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:36] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:36] "POST /AddBlock HTTP/1.1" 200 -
chain changed for node 4 my chain length was 10
Other chain lengths are:
	 node 0 , len 9
	 node 1 , len 9
	 node 2 , len 9
	 node 3 , len 9
1 4 4
selected node 1 , len 9
127.0.0.1 - - [29/Mar/2020 21:05:36] "POST /AddBlock HTTP/1.1" 200 -
	 	 I am transaction (42b7f21b26a8166f07ef11c1012c8a624fcfea4a) giving 6 $ from node 0 to node 3
previous block
	 I am block with index 8
	 My Transaction list contains:
	 	 I am transaction (bedf943b483e382c24bbb76c8a3b5a0719ef7205) giving 7 $ from node 4 to node 0
	 	 I am transaction (42e233fac0c2863e0954453dbb999ed13f965169) giving 5 $ from node 1 to node 4
	 	 I am transaction (61fc13eedfc95f97b00ac67e2ca23deea291a2dd) giving 4 $ from node 0 to node 2
	 	 I am transaction (d3df646fcee36fd7be1ab1b4736648263928e847) giving 8 $ from node 4 to node 3
	 	 I am transaction (9343a7a380a17666ba9caf9fcd9d067b28064051) giving 9 $ from node 4 to node 3
4 5
127.0.0.1 - - [29/Mar/2020 21:05:37] "POST /ValidateTransaction HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:37] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:37] "GET /Chain HTTP/1.1" 200 -
	 	 I am transaction (06cc26e81af6e1fc4614e2718c1b36e30b8b4af6) giving 7 $ from node 0 to node 1
previous block
	 I am block with index 8
	 My Transaction list contains:
	 	 I am transaction (bedf943b483e382c24bbb76c8a3b5a0719ef7205) giving 7 $ from node 4 to node 0
	 	 I am transaction (42e233fac0c2863e0954453dbb999ed13f965169) giving 5 $ from node 1 to node 4
	 	 I am transaction (61fc13eedfc95f97b00ac67e2ca23deea291a2dd) giving 4 $ from node 0 to node 2
	 	 I am transaction (d3df646fcee36fd7be1ab1b4736648263928e847) giving 8 $ from node 4 to node 3
	 	 I am transaction (9343a7a380a17666ba9caf9fcd9d067b28064051) giving 9 $ from node 4 to node 3
5 5
I have to mine
Mining block
	 I am block with index 8
	 My Transaction list contains:
	 	 I am transaction (2a5a123cf68bb77589b47a3cbd6c91de5c279187) giving 6 $ from node 1 to node 3
	 	 I am transaction (5dddd18c84a479a9332a06c20a90b8507469348f) giving 10 $ from node 3 to node 0
	 	 I am transaction (73e127c92d9bfee56763acea8eaa9bfde374a4d5) giving 7 $ from node 1 to node 2
	 	 I am transaction (42b7f21b26a8166f07ef11c1012c8a624fcfea4a) giving 6 $ from node 0 to node 3
	 	 I am transaction (06cc26e81af6e1fc4614e2718c1b36e30b8b4af6) giving 7 $ from node 0 to node 1
Done
127.0.0.1 - - [29/Mar/2020 21:05:37] "GET /Chain HTTP/1.1" 200 -
chain changed for node 4 my chain length was 9
Other chain lengths are:
	 node 0 , len 9
	 node 1 , len 9
	 node 2 , len 10
	 node 3 , len 10
3 4 4
selected node 3 , len 10
127.0.0.1 - - [29/Mar/2020 21:05:37] "POST /AddBlock HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:37] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:37] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:38] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:38] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:38] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:38] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:38] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:38] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:38] "GET /Chain HTTP/1.1" 200 -
chain changed for node 4 my chain length was 10
Other chain lengths are:
	 node 0 , len 10
	 node 1 , len 9
	 node 2 , len 9
	 node 3 , len 10
3 4 4
selected node 3 , len 10
127.0.0.1 - - [29/Mar/2020 21:05:38] "POST /AddBlock HTTP/1.1" 200 -
chain changed for node 4 my chain length was 10
Other chain lengths are:
	 node 0 , len 10
	 node 1 , len 10
	 node 2 , len 9
	 node 3 , len 10
1 4 4
selected node 1 , len 10
127.0.0.1 - - [29/Mar/2020 21:05:38] "POST /AddBlock HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:38] "POST /ValidateTransaction HTTP/1.1" 200 -
	 	 I am transaction (49ebde5f5b35a949fe84a1dfcc9de5765acc4996) giving 9 $ from node 1 to node 0
previous block
	 I am block with index 9
	 My Transaction list contains:
	 	 I am transaction (eda3c5d830659d25a7bcf4a3f89d1dc61fa75e35) giving 10 $ from node 4 to node 0
	 	 I am transaction (9fc0474368e0edf92519b875b240e0f9646cf37c) giving 5 $ from node 0 to node 1
	 	 I am transaction (9b82f809ef144bf147392189ae454d9e2865b4dd) giving 9 $ from node 3 to node 4
	 	 I am transaction (2a5a123cf68bb77589b47a3cbd6c91de5c279187) giving 6 $ from node 1 to node 3
	 	 I am transaction (5dddd18c84a479a9332a06c20a90b8507469348f) giving 10 $ from node 3 to node 0
1 5
	 	 I am transaction (1c5d41b868b561ecc155cdc744afbefa88e39f53) giving 8 $ from node 1 to node 2
previous block
	 I am block with index 9
	 My Transaction list contains:
	 	 I am transaction (eda3c5d830659d25a7bcf4a3f89d1dc61fa75e35) giving 10 $ from node 4 to node 0
	 	 I am transaction (9fc0474368e0edf92519b875b240e0f9646cf37c) giving 5 $ from node 0 to node 1
	 	 I am transaction (9b82f809ef144bf147392189ae454d9e2865b4dd) giving 9 $ from node 3 to node 4
	 	 I am transaction (2a5a123cf68bb77589b47a3cbd6c91de5c279187) giving 6 $ from node 1 to node 3
	 	 I am transaction (5dddd18c84a479a9332a06c20a90b8507469348f) giving 10 $ from node 3 to node 0
2 5
	 	 I am transaction (5cae6373e65118d595100f127af09a853784e50d) giving 10 $ from node 1 to node 2
previous block
	 I am block with index 9
	 My Transaction list contains:
	 	 I am transaction (eda3c5d830659d25a7bcf4a3f89d1dc61fa75e35) giving 10 $ from node 4 to node 0
	 	 I am transaction (9fc0474368e0edf92519b875b240e0f9646cf37c) giving 5 $ from node 0 to node 1
	 	 I am transaction (9b82f809ef144bf147392189ae454d9e2865b4dd) giving 9 $ from node 3 to node 4
	 	 I am transaction (2a5a123cf68bb77589b47a3cbd6c91de5c279187) giving 6 $ from node 1 to node 3
	 	 I am transaction (5dddd18c84a479a9332a06c20a90b8507469348f) giving 10 $ from node 3 to node 0
3 5
127.0.0.1 - - [29/Mar/2020 21:05:38] "POST /ValidateTransaction HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:38] "POST /ValidateTransaction HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:39] "POST /ValidateTransaction HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:39] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:39] "POST /AddBlock HTTP/1.1" 200 -
	 	 I am transaction (285eb60f4f8d0c7b8f19ff6f623aa7b97e0a14ca) giving 8 $ from node 0 to node 4
previous block
	 I am block with index 10
	 My Transaction list contains:
	 	 I am transaction (73e127c92d9bfee56763acea8eaa9bfde374a4d5) giving 7 $ from node 1 to node 2
	 	 I am transaction (42b7f21b26a8166f07ef11c1012c8a624fcfea4a) giving 6 $ from node 0 to node 3
	 	 I am transaction (06cc26e81af6e1fc4614e2718c1b36e30b8b4af6) giving 7 $ from node 0 to node 1
	 	 I am transaction (1c5d41b868b561ecc155cdc744afbefa88e39f53) giving 8 $ from node 1 to node 2
	 	 I am transaction (49ebde5f5b35a949fe84a1dfcc9de5765acc4996) giving 9 $ from node 1 to node 0
4 5
127.0.0.1 - - [29/Mar/2020 21:05:39] "POST /ValidateTransaction HTTP/1.1" 200 -
	 	 I am transaction (ce2b3ac10a7b0667a9e67668da279bd158c74022) giving 9 $ from node 0 to node 4
previous block
	 I am block with index 10
	 My Transaction list contains:
	 	 I am transaction (73e127c92d9bfee56763acea8eaa9bfde374a4d5) giving 7 $ from node 1 to node 2
	 	 I am transaction (42b7f21b26a8166f07ef11c1012c8a624fcfea4a) giving 6 $ from node 0 to node 3
	 	 I am transaction (06cc26e81af6e1fc4614e2718c1b36e30b8b4af6) giving 7 $ from node 0 to node 1
	 	 I am transaction (1c5d41b868b561ecc155cdc744afbefa88e39f53) giving 8 $ from node 1 to node 2
	 	 I am transaction (49ebde5f5b35a949fe84a1dfcc9de5765acc4996) giving 9 $ from node 1 to node 0
5 5
I have to mine
Mining block
	 I am block with index 9
	 My Transaction list contains:
	 	 I am transaction (49ebde5f5b35a949fe84a1dfcc9de5765acc4996) giving 9 $ from node 1 to node 0
	 	 I am transaction (1c5d41b868b561ecc155cdc744afbefa88e39f53) giving 8 $ from node 1 to node 2
	 	 I am transaction (5cae6373e65118d595100f127af09a853784e50d) giving 10 $ from node 1 to node 2
	 	 I am transaction (285eb60f4f8d0c7b8f19ff6f623aa7b97e0a14ca) giving 8 $ from node 0 to node 4
	 	 I am transaction (ce2b3ac10a7b0667a9e67668da279bd158c74022) giving 9 $ from node 0 to node 4
Done
127.0.0.1 - - [29/Mar/2020 21:05:40] "GET /Chain HTTP/1.1" 200 -
chain changed for node 4 my chain length was 11
Other chain lengths are:
	 node 0 , len 10
	 node 1 , len 10
	 node 2 , len 11
	 node 3 , len 11
3 4 4
selected node 3 , len 11
127.0.0.1 - - [29/Mar/2020 21:05:40] "POST /AddBlock HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:40] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:41] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:41] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:41] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:41] "GET /Chain HTTP/1.1" 200 -
chain changed for node 4 my chain length was 11
Other chain lengths are:
	 node 0 , len 10
	 node 1 , len 11
	 node 2 , len 11
	 node 3 , len 11
2 4 4
selected node 2 , len 11
127.0.0.1 - - [29/Mar/2020 21:05:41] "POST /AddBlock HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:41] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:41] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:41] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:41] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:41] "GET /Chain HTTP/1.1" 200 -
chain changed for node 4 my chain length was 11
Other chain lengths are:
	 node 0 , len 11
	 node 1 , len 11
	 node 2 , len 10
	 node 3 , len 11
1 4 4
selected node 1 , len 11
127.0.0.1 - - [29/Mar/2020 21:05:41] "POST /AddBlock HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:42] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:42] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:42] "GET /Chain HTTP/1.1" 200 -
chain changed for node 4 my chain length was 11
Other chain lengths are:
	 node 0 , len 11
	 node 1 , len 11
	 node 2 , len 10
	 node 3 , len 11
1 4 4
selected node 1 , len 11
127.0.0.1 - - [29/Mar/2020 21:05:42] "POST /AddBlock HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:42] "POST /ValidateTransaction HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:42] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:42] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:43] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:43] "GET /Chain HTTP/1.1" 200 -
	 	 I am transaction (2f8b50fb0668f69c5b165154c15053aad2a04082) giving 10 $ from node 0 to node 4
previous block
	 I am block with index 10
	 My Transaction list contains:
	 	 I am transaction (73e127c92d9bfee56763acea8eaa9bfde374a4d5) giving 7 $ from node 1 to node 2
	 	 I am transaction (42b7f21b26a8166f07ef11c1012c8a624fcfea4a) giving 6 $ from node 0 to node 3
	 	 I am transaction (06cc26e81af6e1fc4614e2718c1b36e30b8b4af6) giving 7 $ from node 0 to node 1
	 	 I am transaction (1c5d41b868b561ecc155cdc744afbefa88e39f53) giving 8 $ from node 1 to node 2
	 	 I am transaction (49ebde5f5b35a949fe84a1dfcc9de5765acc4996) giving 9 $ from node 1 to node 0
1 5
127.0.0.1 - - [29/Mar/2020 21:05:43] "POST /ValidateTransaction HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:43] "GET /Chain HTTP/1.1" 200 -
chain changed for node 4 my chain length was 11
Other chain lengths are:
	 node 0 , len 11
	 node 1 , len 11
	 node 2 , len 11
	 node 3 , len 11
1 4 4
selected node 1 , len 11
127.0.0.1 - - [29/Mar/2020 21:05:43] "POST /AddBlock HTTP/1.1" 200 -
	 	 I am transaction (7d06049a50784a67fb7510c37dd5a9a2c6e06256) giving 10 $ from node 0 to node 4
previous block
	 I am block with index 10
	 My Transaction list contains:
	 	 I am transaction (73e127c92d9bfee56763acea8eaa9bfde374a4d5) giving 7 $ from node 1 to node 2
	 	 I am transaction (42b7f21b26a8166f07ef11c1012c8a624fcfea4a) giving 6 $ from node 0 to node 3
	 	 I am transaction (06cc26e81af6e1fc4614e2718c1b36e30b8b4af6) giving 7 $ from node 0 to node 1
	 	 I am transaction (1c5d41b868b561ecc155cdc744afbefa88e39f53) giving 8 $ from node 1 to node 2
	 	 I am transaction (49ebde5f5b35a949fe84a1dfcc9de5765acc4996) giving 9 $ from node 1 to node 0
2 5
127.0.0.1 - - [29/Mar/2020 21:05:43] "POST /ValidateTransaction HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:43] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:43] "POST /ValidateTransaction HTTP/1.1" 400 -
127.0.0.1 - - [29/Mar/2020 21:05:44] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:44] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:44] "GET /Chain HTTP/1.1" 200 -
chain changed for node 4 my chain length was 11
Other chain lengths are:
	 node 0 , len 11
	 node 1 , len 11
	 node 2 , len 11
	 node 3 , len 11
1 4 4
selected node 1 , len 11
127.0.0.1 - - [29/Mar/2020 21:05:44] "POST /AddBlock HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:44] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:44] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:44] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:44] "GET /Chain HTTP/1.1" 200 -
chain changed for node 4 my chain length was 11
Other chain lengths are:
	 node 0 , len 11
	 node 1 , len 11
	 node 2 , len 11
127.0.0.1 - - [29/Mar/2020 21:05:44] "GET /Chain HTTP/1.1" 200 -
	 node 3 , len 11
1 4 4
selected node 1 , len 11
127.0.0.1 - - [29/Mar/2020 21:05:44] "POST /AddBlock HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2020 21:05:46] "POST /AddBlock HTTP/1.1" 200 -
