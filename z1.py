Created transaction
	 	 I am transaction (22638dedb224898aa6cae8cbd7cafb03ff303edc) giving 500 $ from node genesis to node 0
1 2
Block added to blockchain!
	 I am block with index 0
	 My Transaction list contains:
	 	 I am transaction (22638dedb224898aa6cae8cbd7cafb03ff303edc) giving 500 $ from node genesis to node 0


Blockchain:
	 I am block with index 0
	 My Transaction list contains:
	 	 I am transaction (22638dedb224898aa6cae8cbd7cafb03ff303edc) giving 500 $ from node genesis to node 0


0

 * Serving Flask app "BootstrapRest" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
127.0.0.1 - - [23/Mar/2020 20:57:31] "POST /nodes/register HTTP/1.1" 200 -
Validating Transaction
	 	 I am transaction (f3f596d61dfa65e51ff1c749ed8d9e39f4227f3a) giving 100 $ from node 0 to node 1
Result True
Trani f3f596d61dfa65e51ff1c749ed8d9e39f4227f3a
	 I am block with index 1
	 My Transaction list contains:
False
False
1 2
127.0.0.1 - - [23/Mar/2020 20:57:32] "POST /ValidateTransaction HTTP/1.1" 200 -
Created transaction
	 	 I am transaction (f3f596d61dfa65e51ff1c749ed8d9e39f4227f3a) giving 100 $ from node 0 to node 1
127.0.0.1 - - [23/Mar/2020 20:57:32] "POST /nodes/register HTTP/1.1" 200 -
Validating Transaction
	 	 I am transaction (4d4366153409aaf2ea130d97affea9bf6c91c2bb) giving 100 $ from node 0 to node 2
Result True
Trani 4d4366153409aaf2ea130d97affea9bf6c91c2bb
	 I am block with index 1
	 My Transaction list contains:
	 	 I am transaction (f3f596d61dfa65e51ff1c749ed8d9e39f4227f3a) giving 100 $ from node 0 to node 1
False
False
2 2
AAAA
127.0.0.1 - - [23/Mar/2020 20:57:32] "POST /nodes/register HTTP/1.1" 200 -
Validating Transaction
	 	 I am transaction (01662993795fb5fd8093c5eb4414af9516606e8e) giving 100 $ from node 0 to node 3
Result True
Trani 01662993795fb5fd8093c5eb4414af9516606e8e
	 I am block with index 2
	 My Transaction list contains:
False
False
1 2
127.0.0.1 - - [23/Mar/2020 20:57:32] "POST /ValidateTransaction HTTP/1.1" 200 -
Created transaction
	 	 I am transaction (01662993795fb5fd8093c5eb4414af9516606e8e) giving 100 $ from node 0 to node 3
Validate own block
Block added to blockchain!
	 I am block with index 1
	 My Transaction list contains:
	 	 I am transaction (f3f596d61dfa65e51ff1c749ed8d9e39f4227f3a) giving 100 $ from node 0 to node 1
	 	 I am transaction (4d4366153409aaf2ea130d97affea9bf6c91c2bb) giving 100 $ from node 0 to node 2


Blockchain:
	 I am block with index 0
	 My Transaction list contains:
	 	 I am transaction (22638dedb224898aa6cae8cbd7cafb03ff303edc) giving 500 $ from node genesis to node 0
	 I am block with index 1
	 My Transaction list contains:
	 	 I am transaction (f3f596d61dfa65e51ff1c749ed8d9e39f4227f3a) giving 100 $ from node 0 to node 1
	 	 I am transaction (4d4366153409aaf2ea130d97affea9bf6c91c2bb) giving 100 $ from node 0 to node 2


0 1

127.0.0.1 - - [23/Mar/2020 20:57:32] "POST /AddBlock HTTP/1.1" 200 -
Done
127.0.0.1 - - [23/Mar/2020 20:57:32] "POST /ValidateTransaction HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:32] "POST /nodes/register HTTP/1.1" 200 -
Created transaction
	 	 I am transaction (4d4366153409aaf2ea130d97affea9bf6c91c2bb) giving 100 $ from node 0 to node 2
Validating Transaction
	 	 I am transaction (c41568a85d921ed060a5f30a8ec96b7f255fec7e) giving 100 $ from node 0 to node 4
Result True
Trani c41568a85d921ed060a5f30a8ec96b7f255fec7e
	 I am block with index 2
	 My Transaction list contains:
	 	 I am transaction (01662993795fb5fd8093c5eb4414af9516606e8e) giving 100 $ from node 0 to node 3
False
False
2 2
AAAA
Validate own block
Block added to blockchain!
	 I am block with index 2
	 My Transaction list contains:
	 	 I am transaction (01662993795fb5fd8093c5eb4414af9516606e8e) giving 100 $ from node 0 to node 3
	 	 I am transaction (c41568a85d921ed060a5f30a8ec96b7f255fec7e) giving 100 $ from node 0 to node 4


Blockchain:
	 I am block with index 0
	 My Transaction list contains:
	 	 I am transaction (22638dedb224898aa6cae8cbd7cafb03ff303edc) giving 500 $ from node genesis to node 0
	 I am block with index 1
	 My Transaction list contains:
	 	 I am transaction (f3f596d61dfa65e51ff1c749ed8d9e39f4227f3a) giving 100 $ from node 0 to node 1
	 	 I am transaction (4d4366153409aaf2ea130d97affea9bf6c91c2bb) giving 100 $ from node 0 to node 2
	 I am block with index 2
	 My Transaction list contains:
	 	 I am transaction (01662993795fb5fd8093c5eb4414af9516606e8e) giving 100 $ from node 0 to node 3
	 	 I am transaction (c41568a85d921ed060a5f30a8ec96b7f255fec7e) giving 100 $ from node 0 to node 4


0 1 2

127.0.0.1 - - [23/Mar/2020 20:57:33] "POST /AddBlock HTTP/1.1" 200 -
Done
127.0.0.1 - - [23/Mar/2020 20:57:33] "POST /ValidateTransaction HTTP/1.1" 200 -
Created transaction
	 	 I am transaction (c41568a85d921ed060a5f30a8ec96b7f255fec7e) giving 100 $ from node 0 to node 4
127.0.0.1 - - [23/Mar/2020 20:57:33] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:33] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:33] "POST /AddBlock HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:33] "POST /AddBlock HTTP/1.1" 200 -
Validating Transaction
	 	 I am transaction (d5cf3a50e4feb2818a4ed54398d0374cef6ba6a4) giving 1 $ from node 1 to node 3
Result True
Trani d5cf3a50e4feb2818a4ed54398d0374cef6ba6a4
	 I am block with index 3
	 My Transaction list contains:
False
False
1 2
127.0.0.1 - - [23/Mar/2020 20:57:33] "POST /ValidateTransaction HTTP/1.1" 200 -
Validating Transaction
	 	 I am transaction (e3179905507f5ad52fc3922bfcfd435f3e8e4c53) giving 2 $ from node 1 to node 0
Result True
Trani e3179905507f5ad52fc3922bfcfd435f3e8e4c53
127.0.0.1 - - [23/Mar/2020 20:57:33] "GET /Chain HTTP/1.1" 200 -
	 I am block with index 3
	 My Transaction list contains:
	 	 I am transaction (d5cf3a50e4feb2818a4ed54398d0374cef6ba6a4) giving 1 $ from node 1 to node 3
False
False
2 2
AAAA
127.0.0.1 - - [23/Mar/2020 20:57:33] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:33] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:33] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:33] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:34] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:34] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:34] "POST /AddBlock HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:34] "POST /AddBlock HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:34] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:34] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:34] "POST /AddBlock HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:34] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:34] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:34] "GET /Chain HTTP/1.1" 200 -
Block added to blockchain!
	 I am block with index 3
Validating Transaction
127.0.0.1 - - [23/Mar/2020 20:57:34] "POST /AddBlock HTTP/1.1" 200 -
	 My Transaction list contains:
	 	 I am transaction (6b03130364cdbc9e6eb53eec293ac2168eae92e8) giving 3 $ from node 1 to node 3
	 	 I am transaction (e3179905507f5ad52fc3922bfcfd435f3e8e4c53) giving 2 $ from node 1 to node 0
Result True
Trani 6b03130364cdbc9e6eb53eec293ac2168eae92e8
	 I am block with index 4
	 My Transaction list contains:
False
Validating Transaction
127.0.0.1 - - [23/Mar/2020 20:57:34] "GET /Chain HTTP/1.1" 200 -
False
	 	 I am transaction (f693990b4ba97ffa45974d842489e70d62b887e8) giving 4 $ from node 1 to node 0
1 2
127.0.0.1 - - [23/Mar/2020 20:57:34] "POST /ValidateTransaction HTTP/1.1" 200 -
Result True
127.0.0.1 - - [23/Mar/2020 20:57:34] "GET /Chain HTTP/1.1" 200 -
Trani f693990b4ba97ffa45974d842489e70d62b887e8
	 	 I am transaction (6b03130364cdbc9e6eb53eec293ac2168eae92e8) giving 3 $ from node 1 to node 3
127.0.0.1 - - [23/Mar/2020 20:57:34] "GET /Chain HTTP/1.1" 200 -
	 I am block with index 4
Validating Transaction
	 My Transaction list contains:
	 	 I am transaction (52775aa21764f8c923c71c3aab103ac49444697c) giving 5 $ from node 1 to node 4
	 	 I am transaction (6b03130364cdbc9e6eb53eec293ac2168eae92e8) giving 3 $ from node 1 to node 3
Result True
False
Validating Transaction
False

	 	 I am transaction (72f01b7c9ccea94888b00ed9ecaafe6d4ccb3eef) giving 6 $ from node 1 to node 3
Validate own block
2 2

AAAA
Blockchain:
	 I am block with index 0
127.0.0.1 - - [23/Mar/2020 20:57:34] "POST /AddBlock HTTP/1.1" 200 -
	 My Transaction list contains:
Trani 52775aa21764f8c923c71c3aab103ac49444697c
127.0.0.1 - - [23/Mar/2020 20:57:34] "GET /Chain HTTP/1.1" 200 -
Result True
127.0.0.1 - - [23/Mar/2020 20:57:34] "POST /AddBlock HTTP/1.1" 200 -
Validate own block
Done
127.0.0.1 - - [23/Mar/2020 20:57:34] "POST /ValidateTransaction HTTP/1.1" 200 -
	 	 I am transaction (22638dedb224898aa6cae8cbd7cafb03ff303edc) giving 500 $ from node genesis to node 0
Block added to blockchain!
	 I am block with index 1
	 My Transaction list contains:
	 I am block with index 4
127.0.0.1 - - [23/Mar/2020 20:57:34] "GET /Chain HTTP/1.1" 200 -
	 I am block with index 4
	 My Transaction list contains:
Block added to blockchain!
Validating Transaction
	 My Transaction list contains:
	 I am block with index 4
	 	 I am transaction (d5cf3a50e4feb2818a4ed54398d0374cef6ba6a4) giving 1 $ from node 1 to node 3
	 	 I am transaction (6b03130364cdbc9e6eb53eec293ac2168eae92e8) giving 3 $ from node 1 to node 3
	 My Transaction list contains:
	 	 I am transaction (6b03130364cdbc9e6eb53eec293ac2168eae92e8) giving 3 $ from node 1 to node 3
	 	 I am transaction (f693990b4ba97ffa45974d842489e70d62b887e8) giving 4 $ from node 1 to node 0
	 	 I am transaction (f3f596d61dfa65e51ff1c749ed8d9e39f4227f3a) giving 100 $ from node 0 to node 1
	 	 I am transaction (4d4366153409aaf2ea130d97affea9bf6c91c2bb) giving 100 $ from node 0 to node 2
	 	 I am transaction (6b03130364cdbc9e6eb53eec293ac2168eae92e8) giving 3 $ from node 1 to node 3
False
	 	 I am transaction (f693990b4ba97ffa45974d842489e70d62b887e8) giving 4 $ from node 1 to node 0


	 I am block with index 2
	 	 I am transaction (1077a03e809bd5e682b27629a21afe6f8ade4df4) giving 7 $ from node 1 to node 2
Blockchain:
False
	 I am block with index 0
Result True
	 My Transaction list contains:
	 My Transaction list contains:
OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
	 	 I am transaction (01662993795fb5fd8093c5eb4414af9516606e8e) giving 100 $ from node 0 to node 3

	 	 I am transaction (22638dedb224898aa6cae8cbd7cafb03ff303edc) giving 500 $ from node genesis to node 0
127.0.0.1 - - [23/Mar/2020 20:57:34] "GET /Chain HTTP/1.1" 200 -
Trani 72f01b7c9ccea94888b00ed9ecaafe6d4ccb3eef
127.0.0.1 - - [23/Mar/2020 20:57:34] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:34] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:34] "GET /Chain HTTP/1.1" 200 -
	 	 I am transaction (c41568a85d921ed060a5f30a8ec96b7f255fec7e) giving 100 $ from node 0 to node 4
Validate own block
	 I am block with index 1
	 My Transaction list contains:
127.0.0.1 - - [23/Mar/2020 20:57:34] "POST /AddBlock HTTP/1.1" 200 -

Blockchain:
	 I am block with index 0
Validating Transaction
	 	 I am transaction (f3f596d61dfa65e51ff1c749ed8d9e39f4227f3a) giving 100 $ from node 0 to node 1
	 	 I am transaction (4d4366153409aaf2ea130d97affea9bf6c91c2bb) giving 100 $ from node 0 to node 2
	 I am block with index 2
	 My Transaction list contains:
	 I am block with index 5
	 My Transaction list contains:
False
	 My Transaction list contains:
False
	 	 I am transaction (22638dedb224898aa6cae8cbd7cafb03ff303edc) giving 500 $ from node genesis to node 0
	 	 I am transaction (0ad25cbffd27da14df38a4ae2aaf87cea69eb18d) giving 8 $ from node 1 to node 2
	 I am block with index 3
	 I am block with index 1
	 My Transaction list contains:
127.0.0.1 - - [23/Mar/2020 20:57:35] "GET /Chain HTTP/1.1" 200 -
	 My Transaction list contains:
127.0.0.1 - - [23/Mar/2020 20:57:35] "POST /AddBlock HTTP/1.1" 200 -
	 	 I am transaction (e3179905507f5ad52fc3922bfcfd435f3e8e4c53) giving 2 $ from node 1 to node 0
	 	 I am transaction (f3f596d61dfa65e51ff1c749ed8d9e39f4227f3a) giving 100 $ from node 0 to node 1
	 	 I am transaction (01662993795fb5fd8093c5eb4414af9516606e8e) giving 100 $ from node 0 to node 3
	 	 I am transaction (6b03130364cdbc9e6eb53eec293ac2168eae92e8) giving 3 $ from node 1 to node 3
	 	 I am transaction (4d4366153409aaf2ea130d97affea9bf6c91c2bb) giving 100 $ from node 0 to node 2
Done
127.0.0.1 - - [23/Mar/2020 20:57:35] "POST /ValidateTransaction HTTP/1.1" 200 -
	 I am block with index 4
Result True
1 2
127.0.0.1 - - [23/Mar/2020 20:57:35] "POST /ValidateTransaction HTTP/1.1" 200 -
	 My Transaction list contains:
	 I am block with index 2
	 	 I am transaction (c41568a85d921ed060a5f30a8ec96b7f255fec7e) giving 100 $ from node 0 to node 4
	 	 I am transaction (6b03130364cdbc9e6eb53eec293ac2168eae92e8) giving 3 $ from node 1 to node 3
	 My Transaction list contains:
Trani 1077a03e809bd5e682b27629a21afe6f8ade4df4
	 	 I am transaction (01662993795fb5fd8093c5eb4414af9516606e8e) giving 100 $ from node 0 to node 3
	 	 I am transaction (c41568a85d921ed060a5f30a8ec96b7f255fec7e) giving 100 $ from node 0 to node 4
	 I am block with index 5
	 I am block with index 3
	 I am block with index 3
	 	 I am transaction (f693990b4ba97ffa45974d842489e70d62b887e8) giving 4 $ from node 1 to node 0
	 My Transaction list contains:
	 I am block with index 4
	 My Transaction list contains:
	 	 I am transaction (e3179905507f5ad52fc3922bfcfd435f3e8e4c53) giving 2 $ from node 1 to node 0
	 My Transaction list contains:
	 	 I am transaction (e3179905507f5ad52fc3922bfcfd435f3e8e4c53) giving 2 $ from node 1 to node 0
	 	 I am transaction (6b03130364cdbc9e6eb53eec293ac2168eae92e8) giving 3 $ from node 1 to node 3
	 My Transaction list contains:
	 I am block with index 4
	 My Transaction list contains:
	 	 I am transaction (72f01b7c9ccea94888b00ed9ecaafe6d4ccb3eef) giving 6 $ from node 1 to node 3
	 	 I am transaction (d5cf3a50e4feb2818a4ed54398d0374cef6ba6a4) giving 1 $ from node 1 to node 3
	 	 I am transaction (6b03130364cdbc9e6eb53eec293ac2168eae92e8) giving 3 $ from node 1 to node 3
	 	 I am transaction (6b03130364cdbc9e6eb53eec293ac2168eae92e8) giving 3 $ from node 1 to node 3
False
	 	 I am transaction (6b03130364cdbc9e6eb53eec293ac2168eae92e8) giving 3 $ from node 1 to node 3
	 I am block with index 4
	 My Transaction list contains:
	 	 I am transaction (f693990b4ba97ffa45974d842489e70d62b887e8) giving 4 $ from node 1 to node 0

False

2 2
0 1 2 3 4 4
AAAA
	 	 I am transaction (6b03130364cdbc9e6eb53eec293ac2168eae92e8) giving 3 $ from node 1 to node 3

127.0.0.1 - - [23/Mar/2020 20:57:35] "POST /AddBlock HTTP/1.1" 200 -
	 I am block with index 4
RESOLVE conflicts chain updated
	 	 I am transaction (f693990b4ba97ffa45974d842489e70d62b887e8) giving 4 $ from node 1 to node 0
	 My Transaction list contains:
	 I am block with index 4
RESOLVE conflicts chain updated
	 	 I am transaction (d5cf3a50e4feb2818a4ed54398d0374cef6ba6a4) giving 1 $ from node 1 to node 3
	 My Transaction list contains:
	 	 I am transaction (6b03130364cdbc9e6eb53eec293ac2168eae92e8) giving 3 $ from node 1 to node 3
	 	 I am transaction (d5cf3a50e4feb2818a4ed54398d0374cef6ba6a4) giving 1 $ from node 1 to node 3


0 1 2 3 4 4
Trani 0ad25cbffd27da14df38a4ae2aaf87cea69eb18d

127.0.0.1 - - [23/Mar/2020 20:57:35] "POST /AddBlock HTTP/1.1" 200 -
	 I am block with index 5
	 	 I am transaction (6b03130364cdbc9e6eb53eec293ac2168eae92e8) giving 3 $ from node 1 to node 3
127.0.0.1 - - [23/Mar/2020 20:57:35] "GET /Chain HTTP/1.1" 200 -


0 1 2 3 4 4

127.0.0.1 - - [23/Mar/2020 20:57:35] "POST /AddBlock HTTP/1.1" 200 -
Done
127.0.0.1 - - [23/Mar/2020 20:57:35] "POST /ValidateTransaction HTTP/1.1" 200 -
	 My Transaction list contains:
False
127.0.0.1 - - [23/Mar/2020 20:57:35] "GET /Chain HTTP/1.1" 200 -
False
1 2
Validate own block
RESOLVE conflicts chain updated
127.0.0.1 - - [23/Mar/2020 20:57:35] "POST /ValidateTransaction HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:35] "GET /Chain HTTP/1.1" 200 -
Block added to blockchain!
	 I am block with index 5
	 My Transaction list contains:
	 	 I am transaction (72f01b7c9ccea94888b00ed9ecaafe6d4ccb3eef) giving 6 $ from node 1 to node 3
	 	 I am transaction (52775aa21764f8c923c71c3aab103ac49444697c) giving 5 $ from node 1 to node 4


Blockchain:
	 I am block with index 0
	 My Transaction list contains:
	 	 I am transaction (22638dedb224898aa6cae8cbd7cafb03ff303edc) giving 500 $ from node genesis to node 0
	 I am block with index 1
	 My Transaction list contains:
	 	 I am transaction (f3f596d61dfa65e51ff1c749ed8d9e39f4227f3a) giving 100 $ from node 0 to node 1
	 	 I am transaction (4d4366153409aaf2ea130d97affea9bf6c91c2bb) giving 100 $ from node 0 to node 2
	 I am block with index 2
	 My Transaction list contains:
	 	 I am transaction (01662993795fb5fd8093c5eb4414af9516606e8e) giving 100 $ from node 0 to node 3
	 	 I am transaction (c41568a85d921ed060a5f30a8ec96b7f255fec7e) giving 100 $ from node 0 to node 4
	 I am block with index 3
	 My Transaction list contains:
	 	 I am transaction (e3179905507f5ad52fc3922bfcfd435f3e8e4c53) giving 2 $ from node 1 to node 0
	 	 I am transaction (6b03130364cdbc9e6eb53eec293ac2168eae92e8) giving 3 $ from node 1 to node 3
	 I am block with index 4
	 My Transaction list contains:
	 	 I am transaction (f693990b4ba97ffa45974d842489e70d62b887e8) giving 4 $ from node 1 to node 0
	 	 I am transaction (52775aa21764f8c923c71c3aab103ac49444697c) giving 5 $ from node 1 to node 4
	 I am block with index 5
	 My Transaction list contains:
	 	 I am transaction (72f01b7c9ccea94888b00ed9ecaafe6d4ccb3eef) giving 6 $ from node 1 to node 3
	 	 I am transaction (52775aa21764f8c923c71c3aab103ac49444697c) giving 5 $ from node 1 to node 4


0 1 2 3 4 5

127.0.0.1 - - [23/Mar/2020 20:57:35] "POST /AddBlock HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:35] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:35] "POST /AddBlock HTTP/1.1" 200 -
Done
127.0.0.1 - - [23/Mar/2020 20:57:35] "POST /ValidateTransaction HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:35] "GET /Chain HTTP/1.1" 200 -
RESOLVE conflicts chain updated
127.0.0.1 - - [23/Mar/2020 20:57:35] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:35] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:36] "GET /Chain HTTP/1.1" 200 -
Old chain


Blockchain:
	 I am block with index 0
	 My Transaction list contains:
	 	 I am transaction (22638dedb224898aa6cae8cbd7cafb03ff303edc) giving 500 $ from node genesis to node 0
	 I am block with index 1
	 My Transaction list contains:
	 	 I am transaction (f3f596d61dfa65e51ff1c749ed8d9e39f4227f3a) giving 100 $ from node 0 to node 1
	 	 I am transaction (4d4366153409aaf2ea130d97affea9bf6c91c2bb) giving 100 $ from node 0 to node 2
	 I am block with index 2
	 My Transaction list contains:
	 	 I am transaction (01662993795fb5fd8093c5eb4414af9516606e8e) giving 100 $ from node 0 to node 3
	 	 I am transaction (c41568a85d921ed060a5f30a8ec96b7f255fec7e) giving 100 $ from node 0 to node 4
	 I am block with index 3
	 My Transaction list contains:
	 	 I am transaction (e3179905507f5ad52fc3922bfcfd435f3e8e4c53) giving 2 $ from node 1 to node 0
	 	 I am transaction (6b03130364cdbc9e6eb53eec293ac2168eae92e8) giving 3 $ from node 1 to node 3
	 I am block with index 4
	 My Transaction list contains:
	 	 I am transaction (6b03130364cdbc9e6eb53eec293ac2168eae92e8) giving 3 $ from node 1 to node 3
	 	 I am transaction (f693990b4ba97ffa45974d842489e70d62b887e8) giving 4 $ from node 1 to node 0
	 I am block with index 4
	 My Transaction list contains:
	 	 I am transaction (d5cf3a50e4feb2818a4ed54398d0374cef6ba6a4) giving 1 $ from node 1 to node 3
	 	 I am transaction (6b03130364cdbc9e6eb53eec293ac2168eae92e8) giving 3 $ from node 1 to node 3


0 1 2 3 4 4

New Chain


Blockchain:
	 I am block with index 0
	 My Transaction list contains:
	 	 I am transaction (22638dedb224898aa6cae8cbd7cafb03ff303edc) giving 500 $ from node genesis to node 0
	 I am block with index 1
	 My Transaction list contains:
	 	 I am transaction (f3f596d61dfa65e51ff1c749ed8d9e39f4227f3a) giving 100 $ from node 0 to node 1
	 	 I am transaction (4d4366153409aaf2ea130d97affea9bf6c91c2bb) giving 100 $ from node 0 to node 2
	 I am block with index 2
	 My Transaction list contains:
	 	 I am transaction (01662993795fb5fd8093c5eb4414af9516606e8e) giving 100 $ from node 0 to node 3
	 	 I am transaction (c41568a85d921ed060a5f30a8ec96b7f255fec7e) giving 100 $ from node 0 to node 4
	 I am block with index 3
	 My Transaction list contains:
	 	 I am transaction (e3179905507f5ad52fc3922bfcfd435f3e8e4c53) giving 2 $ from node 1 to node 0
	 	 I am transaction (6b03130364cdbc9e6eb53eec293ac2168eae92e8) giving 3 $ from node 1 to node 3
	 I am block with index 4
	 My Transaction list contains:
	 	 I am transaction (6b03130364cdbc9e6eb53eec293ac2168eae92e8) giving 3 $ from node 1 to node 3
	 	 I am transaction (e3179905507f5ad52fc3922bfcfd435f3e8e4c53) giving 2 $ from node 1 to node 0
	 I am block with index 5
	 My Transaction list contains:
	 	 I am transaction (72f01b7c9ccea94888b00ed9ecaafe6d4ccb3eef) giving 6 $ from node 1 to node 3
	 	 I am transaction (52775aa21764f8c923c71c3aab103ac49444697c) giving 5 $ from node 1 to node 4


0 1 2 3 4 5

old curr
	 I am block with index 5
	 My Transaction list contains:
	 	 I am transaction (72f01b7c9ccea94888b00ed9ecaafe6d4ccb3eef) giving 6 $ from node 1 to node 3
	 	 I am transaction (1077a03e809bd5e682b27629a21afe6f8ade4df4) giving 7 $ from node 1 to node 2
new curr
	 I am block with index 6
	 My Transaction list contains:
127.0.0.1 - - [23/Mar/2020 20:57:36] "GET /Chain HTTP/1.1" 200 -
Old chain


Blockchain:
	 I am block with index 0
	 My Transaction list contains:
	 	 I am transaction (22638dedb224898aa6cae8cbd7cafb03ff303edc) giving 500 $ from node genesis to node 0
	 I am block with index 1
127.0.0.1 - - [23/Mar/2020 20:57:36] "GET /Chain HTTP/1.1" 200 -
	 My Transaction list contains:
	 	 I am transaction (f3f596d61dfa65e51ff1c749ed8d9e39f4227f3a) giving 100 $ from node 0 to node 1
	 	 I am transaction (4d4366153409aaf2ea130d97affea9bf6c91c2bb) giving 100 $ from node 0 to node 2
127.0.0.1 - - [23/Mar/2020 20:57:36] "GET /Chain HTTP/1.1" 200 -
	 I am block with index 2
	 My Transaction list contains:
	 	 I am transaction (01662993795fb5fd8093c5eb4414af9516606e8e) giving 100 $ from node 0 to node 3
127.0.0.1 - - [23/Mar/2020 20:57:36] "GET /Chain HTTP/1.1" 200 -
	 	 I am transaction (c41568a85d921ed060a5f30a8ec96b7f255fec7e) giving 100 $ from node 0 to node 4
	 I am block with index 3
	 My Transaction list contains:
	 	 I am transaction (e3179905507f5ad52fc3922bfcfd435f3e8e4c53) giving 2 $ from node 1 to node 0
127.0.0.1 - - [23/Mar/2020 20:57:36] "POST /AddBlock HTTP/1.1" 200 -
Old chain
	 	 I am transaction (6b03130364cdbc9e6eb53eec293ac2168eae92e8) giving 3 $ from node 1 to node 3


Blockchain:
	 I am block with index 0
	 My Transaction list contains:
	 	 I am transaction (22638dedb224898aa6cae8cbd7cafb03ff303edc) giving 500 $ from node genesis to node 0
	 I am block with index 1
	 My Transaction list contains:
	 	 I am transaction (f3f596d61dfa65e51ff1c749ed8d9e39f4227f3a) giving 100 $ from node 0 to node 1
	 	 I am transaction (4d4366153409aaf2ea130d97affea9bf6c91c2bb) giving 100 $ from node 0 to node 2
	 I am block with index 2
	 My Transaction list contains:
	 	 I am transaction (01662993795fb5fd8093c5eb4414af9516606e8e) giving 100 $ from node 0 to node 3
	 	 I am transaction (c41568a85d921ed060a5f30a8ec96b7f255fec7e) giving 100 $ from node 0 to node 4
	 I am block with index 3
	 My Transaction list contains:
	 	 I am transaction (e3179905507f5ad52fc3922bfcfd435f3e8e4c53) giving 2 $ from node 1 to node 0
	 	 I am transaction (6b03130364cdbc9e6eb53eec293ac2168eae92e8) giving 3 $ from node 1 to node 3
	 I am block with index 4
	 My Transaction list contains:
	 	 I am transaction (6b03130364cdbc9e6eb53eec293ac2168eae92e8) giving 3 $ from node 1 to node 3
	 	 I am transaction (f693990b4ba97ffa45974d842489e70d62b887e8) giving 4 $ from node 1 to node 0
	 I am block with index 4
	 My Transaction list contains:
	 	 I am transaction (d5cf3a50e4feb2818a4ed54398d0374cef6ba6a4) giving 1 $ from node 1 to node 3
	 	 I am transaction (6b03130364cdbc9e6eb53eec293ac2168eae92e8) giving 3 $ from node 1 to node 3


0 1 2 3 4 4

New Chain


Blockchain:
	 I am block with index 0
	 My Transaction list contains:
	 	 I am transaction (22638dedb224898aa6cae8cbd7cafb03ff303edc) giving 500 $ from node genesis to node 0
	 I am block with index 1
	 My Transaction list contains:
	 	 I am transaction (f3f596d61dfa65e51ff1c749ed8d9e39f4227f3a) giving 100 $ from node 0 to node 1
	 	 I am transaction (4d4366153409aaf2ea130d97affea9bf6c91c2bb) giving 100 $ from node 0 to node 2
	 I am block with index 2
	 My Transaction list contains:
	 	 I am transaction (01662993795fb5fd8093c5eb4414af9516606e8e) giving 100 $ from node 0 to node 3
	 	 I am transaction (c41568a85d921ed060a5f30a8ec96b7f255fec7e) giving 100 $ from node 0 to node 4
	 I am block with index 3
	 My Transaction list contains:
	 	 I am transaction (e3179905507f5ad52fc3922bfcfd435f3e8e4c53) giving 2 $ from node 1 to node 0
	 	 I am transaction (6b03130364cdbc9e6eb53eec293ac2168eae92e8) giving 3 $ from node 1 to node 3
	 I am block with index 4
	 My Transaction list contains:
	 	 I am transaction (6b03130364cdbc9e6eb53eec293ac2168eae92e8) giving 3 $ from node 1 to node 3
	 	 I am transaction (e3179905507f5ad52fc3922bfcfd435f3e8e4c53) giving 2 $ from node 1 to node 0
	 I am block with index 5
	 My Transaction list contains:
	 	 I am transaction (72f01b7c9ccea94888b00ed9ecaafe6d4ccb3eef) giving 6 $ from node 1 to node 3
	 	 I am transaction (52775aa21764f8c923c71c3aab103ac49444697c) giving 5 $ from node 1 to node 4


0 1 2 3 4 5

old curr
	 I am block with index 4
	 My Transaction list contains:
	 	 I am transaction (6b03130364cdbc9e6eb53eec293ac2168eae92e8) giving 3 $ from node 1 to node 3
	 	 I am transaction (f693990b4ba97ffa45974d842489e70d62b887e8) giving 4 $ from node 1 to node 0
new curr
	 I am block with index 6
	 My Transaction list contains:
	 I am block with index 4
	 My Transaction list contains:
	 	 I am transaction (6b03130364cdbc9e6eb53eec293ac2168eae92e8) giving 3 $ from node 1 to node 3
	 	 I am transaction (f693990b4ba97ffa45974d842489e70d62b887e8) giving 4 $ from node 1 to node 0
	 I am block with index 4
	 My Transaction list contains:
	 	 I am transaction (d5cf3a50e4feb2818a4ed54398d0374cef6ba6a4) giving 1 $ from node 1 to node 3
	 	 I am transaction (6b03130364cdbc9e6eb53eec293ac2168eae92e8) giving 3 $ from node 1 to node 3


0 1 2 3 4 4

New Chain


Blockchain:
	 I am block with index 0
	 My Transaction list contains:
	 	 I am transaction (22638dedb224898aa6cae8cbd7cafb03ff303edc) giving 500 $ from node genesis to node 0
	 I am block with index 1
	 My Transaction list contains:
	 	 I am transaction (f3f596d61dfa65e51ff1c749ed8d9e39f4227f3a) giving 100 $ from node 0 to node 1
	 	 I am transaction (4d4366153409aaf2ea130d97affea9bf6c91c2bb) giving 100 $ from node 0 to node 2
	 I am block with index 2
	 My Transaction list contains:
	 	 I am transaction (01662993795fb5fd8093c5eb4414af9516606e8e) giving 100 $ from node 0 to node 3
	 	 I am transaction (c41568a85d921ed060a5f30a8ec96b7f255fec7e) giving 100 $ from node 0 to node 4
	 I am block with index 3
	 My Transaction list contains:
	 	 I am transaction (e3179905507f5ad52fc3922bfcfd435f3e8e4c53) giving 2 $ from node 1 to node 0
	 	 I am transaction (6b03130364cdbc9e6eb53eec293ac2168eae92e8) giving 3 $ from node 1 to node 3
	 I am block with index 4
	 My Transaction list contains:
	 	 I am transaction (6b03130364cdbc9e6eb53eec293ac2168eae92e8) giving 3 $ from node 1 to node 3
	 	 I am transaction (e3179905507f5ad52fc3922bfcfd435f3e8e4c53) giving 2 $ from node 1 to node 0
	 I am block with index 5
	 My Transaction list contains:
	 	 I am transaction (72f01b7c9ccea94888b00ed9ecaafe6d4ccb3eef) giving 6 $ from node 1 to node 3
	 	 I am transaction (52775aa21764f8c923c71c3aab103ac49444697c) giving 5 $ from node 1 to node 4


0 1 2 3 4 5

old curr
	 I am block with index 5
	 My Transaction list contains:
	 	 I am transaction (72f01b7c9ccea94888b00ed9ecaafe6d4ccb3eef) giving 6 $ from node 1 to node 3
	 	 I am transaction (1077a03e809bd5e682b27629a21afe6f8ade4df4) giving 7 $ from node 1 to node 2
new curr
	 I am block with index 6
	 My Transaction list contains:
127.0.0.1 - - [23/Mar/2020 20:57:36] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:36] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:36] "POST /AddBlock HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:36] "GET /Chain HTTP/1.1" 200 -
Block added to blockchain!
	 I am block with index 6
	 My Transaction list contains:
	 	 I am transaction (0ad25cbffd27da14df38a4ae2aaf87cea69eb18d) giving 8 $ from node 1 to node 2
	 	 I am transaction (9970a5c0a373b7858e01a02a59859ad880278031) giving 9 $ from node 1 to node 0


Blockchain:
	 I am block with index 0
	 My Transaction list contains:
	 	 I am transaction (22638dedb224898aa6cae8cbd7cafb03ff303edc) giving 500 $ from node genesis to node 0
	 I am block with index 1
	 My Transaction list contains:
	 	 I am transaction (f3f596d61dfa65e51ff1c749ed8d9e39f4227f3a) giving 100 $ from node 0 to node 1
	 	 I am transaction (4d4366153409aaf2ea130d97affea9bf6c91c2bb) giving 100 $ from node 0 to node 2
	 I am block with index 2
	 My Transaction list contains:
	 	 I am transaction (01662993795fb5fd8093c5eb4414af9516606e8e) giving 100 $ from node 0 to node 3
	 	 I am transaction (c41568a85d921ed060a5f30a8ec96b7f255fec7e) giving 100 $ from node 0 to node 4
	 I am block with index 3
	 My Transaction list contains:
	 	 I am transaction (e3179905507f5ad52fc3922bfcfd435f3e8e4c53) giving 2 $ from node 1 to node 0
	 	 I am transaction (6b03130364cdbc9e6eb53eec293ac2168eae92e8) giving 3 $ from node 1 to node 3
	 I am block with index 4
	 My Transaction list contains:
	 	 I am transaction (6b03130364cdbc9e6eb53eec293ac2168eae92e8) giving 3 $ from node 1 to node 3
	 	 I am transaction (e3179905507f5ad52fc3922bfcfd435f3e8e4c53) giving 2 $ from node 1 to node 0
	 I am block with index 5
	 My Transaction list contains:
	 	 I am transaction (72f01b7c9ccea94888b00ed9ecaafe6d4ccb3eef) giving 6 $ from node 1 to node 3
	 	 I am transaction (52775aa21764f8c923c71c3aab103ac49444697c) giving 5 $ from node 1 to node 4
	 I am block with index 6
	 My Transaction list contains:
	 	 I am transaction (0ad25cbffd27da14df38a4ae2aaf87cea69eb18d) giving 8 $ from node 1 to node 2
	 	 I am transaction (9970a5c0a373b7858e01a02a59859ad880278031) giving 9 $ from node 1 to node 0


0 1 2 3 4 5 6

127.0.0.1 - - [23/Mar/2020 20:57:36] "POST /AddBlock HTTP/1.1" 200 -
Validating Transaction
	 	 I am transaction (9970a5c0a373b7858e01a02a59859ad880278031) giving 9 $ from node 1 to node 0
Result True
Trani 9970a5c0a373b7858e01a02a59859ad880278031
	 I am block with index 6
	 My Transaction list contains:
False
True
Transaction was already in chain or in block
	 	 I am transaction (9970a5c0a373b7858e01a02a59859ad880278031) giving 9 $ from node 1 to node 0
127.0.0.1 - - [23/Mar/2020 20:57:36] "POST /ValidateTransaction HTTP/1.1" 200 -
Validating Transaction
	 	 I am transaction (bd941fffb39ab64ccdf305905d114a455a315c74) giving 10 $ from node 1 to node 2
Result True
Trani bd941fffb39ab64ccdf305905d114a455a315c74
	 I am block with index 6
	 My Transaction list contains:
False
False
1 2
127.0.0.1 - - [23/Mar/2020 20:57:36] "POST /ValidateTransaction HTTP/1.1" 200 -
Validating Transaction
	 	 I am transaction (1798cccfb048481cb904b2a0d7343f90941b9953) giving 1 $ from node 2 to node 4
Result True
Trani 1798cccfb048481cb904b2a0d7343f90941b9953
	 I am block with index 6
	 My Transaction list contains:
	 	 I am transaction (bd941fffb39ab64ccdf305905d114a455a315c74) giving 10 $ from node 1 to node 2
False
False
2 2
AAAA
127.0.0.1 - - [23/Mar/2020 20:57:37] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:37] "POST /AddBlock HTTP/1.1" 200 -
RESOLVE conflicts chain updated
127.0.0.1 - - [23/Mar/2020 20:57:37] "POST /AddBlock HTTP/1.1" 200 -
Validating Transaction
	 	 I am transaction (4592016452dc7215913bea7029f2a6ff0c3cb2bb) giving 2 $ from node 2 to node 3
Result True
Trani 4592016452dc7215913bea7029f2a6ff0c3cb2bb
	 I am block with index 8
	 My Transaction list contains:
False
True
Transaction was already in chain or in block
	 	 I am transaction (4592016452dc7215913bea7029f2a6ff0c3cb2bb) giving 2 $ from node 2 to node 3
127.0.0.1 - - [23/Mar/2020 20:57:37] "POST /ValidateTransaction HTTP/1.1" 200 -
Old chain


Blockchain:
	 I am block with index 0
	 My Transaction list contains:
	 	 I am transaction (22638dedb224898aa6cae8cbd7cafb03ff303edc) giving 500 $ from node genesis to node 0
	 I am block with index 1
	 My Transaction list contains:
	 	 I am transaction (f3f596d61dfa65e51ff1c749ed8d9e39f4227f3a) giving 100 $ from node 0 to node 1
	 	 I am transaction (4d4366153409aaf2ea130d97affea9bf6c91c2bb) giving 100 $ from node 0 to node 2
	 I am block with index 2
	 My Transaction list contains:
	 	 I am transaction (01662993795fb5fd8093c5eb4414af9516606e8e) giving 100 $ from node 0 to node 3
	 	 I am transaction (c41568a85d921ed060a5f30a8ec96b7f255fec7e) giving 100 $ from node 0 to node 4
	 I am block with index 3
	 My Transaction list contains:
	 	 I am transaction (e3179905507f5ad52fc3922bfcfd435f3e8e4c53) giving 2 $ from node 1 to node 0
	 	 I am transaction (6b03130364cdbc9e6eb53eec293ac2168eae92e8) giving 3 $ from node 1 to node 3
	 I am block with index 4
	 My Transaction list contains:
	 	 I am transaction (6b03130364cdbc9e6eb53eec293ac2168eae92e8) giving 3 $ from node 1 to node 3
	 	 I am transaction (e3179905507f5ad52fc3922bfcfd435f3e8e4c53) giving 2 $ from node 1 to node 0
	 I am block with index 5
	 My Transaction list contains:
	 	 I am transaction (72f01b7c9ccea94888b00ed9ecaafe6d4ccb3eef) giving 6 $ from node 1 to node 3
	 	 I am transaction (52775aa21764f8c923c71c3aab103ac49444697c) giving 5 $ from node 1 to node 4
	 I am block with index 6
	 My Transaction list contains:
	 	 I am transaction (0ad25cbffd27da14df38a4ae2aaf87cea69eb18d) giving 8 $ from node 1 to node 2
	 	 I am transaction (9970a5c0a373b7858e01a02a59859ad880278031) giving 9 $ from node 1 to node 0
Validating Transaction


	 	 I am transaction (22b1776df3cd11faed623a33f0143d0497ed9af4) giving 3 $ from node 2 to node 0
0 1 2 3 4 5 6
Result True

Trani 22b1776df3cd11faed623a33f0143d0497ed9af4
New Chain


	 I am block with index 8
	 My Transaction list contains:
False
Blockchain:
	 I am block with index 0
	 My Transaction list contains:
False
	 	 I am transaction (22638dedb224898aa6cae8cbd7cafb03ff303edc) giving 500 $ from node genesis to node 0
	 I am block with index 1
1 2
127.0.0.1 - - [23/Mar/2020 20:57:38] "POST /ValidateTransaction HTTP/1.1" 200 -
	 My Transaction list contains:
	 	 I am transaction (f3f596d61dfa65e51ff1c749ed8d9e39f4227f3a) giving 100 $ from node 0 to node 1
	 	 I am transaction (4d4366153409aaf2ea130d97affea9bf6c91c2bb) giving 100 $ from node 0 to node 2
	 I am block with index 2
	 My Transaction list contains:
	 	 I am transaction (01662993795fb5fd8093c5eb4414af9516606e8e) giving 100 $ from node 0 to node 3
	 	 I am transaction (c41568a85d921ed060a5f30a8ec96b7f255fec7e) giving 100 $ from node 0 to node 4
	 I am block with index 3
	 My Transaction list contains:
	 	 I am transaction (e3179905507f5ad52fc3922bfcfd435f3e8e4c53) giving 2 $ from node 1 to node 0
	 	 I am transaction (6b03130364cdbc9e6eb53eec293ac2168eae92e8) giving 3 $ from node 1 to node 3
	 I am block with index 4
	 My Transaction list contains:
	 	 I am transaction (f693990b4ba97ffa45974d842489e70d62b887e8) giving 4 $ from node 1 to node 0
	 	 I am transaction (52775aa21764f8c923c71c3aab103ac49444697c) giving 5 $ from node 1 to node 4
	 I am block with index 5
	 My Transaction list contains:
	 	 I am transaction (72f01b7c9ccea94888b00ed9ecaafe6d4ccb3eef) giving 6 $ from node 1 to node 3
	 	 I am transaction (1077a03e809bd5e682b27629a21afe6f8ade4df4) giving 7 $ from node 1 to node 2
	 I am block with index 6
	 My Transaction list contains:
	 	 I am transaction (0ad25cbffd27da14df38a4ae2aaf87cea69eb18d) giving 8 $ from node 1 to node 2
	 	 I am transaction (9970a5c0a373b7858e01a02a59859ad880278031) giving 9 $ from node 1 to node 0
	 I am block with index 7
	 My Transaction list contains:
	 	 I am transaction (1798cccfb048481cb904b2a0d7343f90941b9953) giving 1 $ from node 2 to node 4
	 	 I am transaction (4592016452dc7215913bea7029f2a6ff0c3cb2bb) giving 2 $ from node 2 to node 3


0 1 2 3 4 5 6 7

old curr
	 I am block with index 7
	 My Transaction list contains:
new curr
	 I am block with index 8
	 My Transaction list contains:
	 	 I am transaction (22b1776df3cd11faed623a33f0143d0497ed9af4) giving 3 $ from node 2 to node 0
Validate own block
127.0.0.1 - - [23/Mar/2020 20:57:38] "POST /AddBlock HTTP/1.1" 200 -
Done
127.0.0.1 - - [23/Mar/2020 20:57:38] "POST /ValidateTransaction HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:38] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:38] "POST /AddBlock HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:38] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:38] "POST /AddBlock HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:38] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:38] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:38] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:38] "POST /AddBlock HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:38] "GET /Chain HTTP/1.1" 200 -
Block added to blockchain!
	 I am block with index 8
	 My Transaction list contains:
	 	 I am transaction (22b1776df3cd11faed623a33f0143d0497ed9af4) giving 3 $ from node 2 to node 0
	 	 I am transaction (8c2bd3d8acb1610a994d972003f85122057739ff) giving 4 $ from node 2 to node 4


127.0.0.1 - - [23/Mar/2020 20:57:38] "GET /Chain HTTP/1.1" 200 -
Blockchain:
	 I am block with index 0
	 My Transaction list contains:
	 	 I am transaction (22638dedb224898aa6cae8cbd7cafb03ff303edc) giving 500 $ from node genesis to node 0
	 I am block with index 1
	 My Transaction list contains:
127.0.0.1 - - [23/Mar/2020 20:57:38] "GET /Chain HTTP/1.1" 200 -
Validating Transaction
	 	 I am transaction (f3f596d61dfa65e51ff1c749ed8d9e39f4227f3a) giving 100 $ from node 0 to node 1
	 	 I am transaction (8c2bd3d8acb1610a994d972003f85122057739ff) giving 4 $ from node 2 to node 4
127.0.0.1 - - [23/Mar/2020 20:57:38] "GET /Chain HTTP/1.1" 200 -
	 	 I am transaction (4d4366153409aaf2ea130d97affea9bf6c91c2bb) giving 100 $ from node 0 to node 2
	 I am block with index 2
	 My Transaction list contains:
	 	 I am transaction (01662993795fb5fd8093c5eb4414af9516606e8e) giving 100 $ from node 0 to node 3
127.0.0.1 - - [23/Mar/2020 20:57:38] "POST /AddBlock HTTP/1.1" 200 -
	 	 I am transaction (c41568a85d921ed060a5f30a8ec96b7f255fec7e) giving 100 $ from node 0 to node 4
	 I am block with index 3
	 My Transaction list contains:
Result True
Trani 8c2bd3d8acb1610a994d972003f85122057739ff
	 I am block with index 8
	 My Transaction list contains:
	 	 I am transaction (e3179905507f5ad52fc3922bfcfd435f3e8e4c53) giving 2 $ from node 1 to node 0
	 	 I am transaction (22b1776df3cd11faed623a33f0143d0497ed9af4) giving 3 $ from node 2 to node 0
Validating Transaction
	 	 I am transaction (6b03130364cdbc9e6eb53eec293ac2168eae92e8) giving 3 $ from node 1 to node 3
127.0.0.1 - - [23/Mar/2020 20:57:38] "GET /Chain HTTP/1.1" 200 -
	 	 I am transaction (56446fd35cbd00ca5595ed583353bb1db2d24ae6) giving 5 $ from node 2 to node 3
127.0.0.1 - - [23/Mar/2020 20:57:38] "GET /Chain HTTP/1.1" 200 -
	 I am block with index 4
False
127.0.0.1 - - [23/Mar/2020 20:57:38] "GET /Chain HTTP/1.1" 200 -
	 My Transaction list contains:
True
Result True
127.0.0.1 - - [23/Mar/2020 20:57:38] "GET /Chain HTTP/1.1" 200 -
Transaction was already in chain or in block
	 	 I am transaction (f693990b4ba97ffa45974d842489e70d62b887e8) giving 4 $ from node 1 to node 0
	 	 I am transaction (52775aa21764f8c923c71c3aab103ac49444697c) giving 5 $ from node 1 to node 4
	 	 I am transaction (8c2bd3d8acb1610a994d972003f85122057739ff) giving 4 $ from node 2 to node 4
127.0.0.1 - - [23/Mar/2020 20:57:38] "POST /ValidateTransaction HTTP/1.1" 200 -
	 I am block with index 5
	 My Transaction list contains:
	 	 I am transaction (72f01b7c9ccea94888b00ed9ecaafe6d4ccb3eef) giving 6 $ from node 1 to node 3
	 	 I am transaction (1077a03e809bd5e682b27629a21afe6f8ade4df4) giving 7 $ from node 1 to node 2
127.0.0.1 - - [23/Mar/2020 20:57:39] "GET /Chain HTTP/1.1" 200 -
RESOLVE conflicts chain updated
	 I am block with index 6
	 My Transaction list contains:
Trani 56446fd35cbd00ca5595ed583353bb1db2d24ae6
Old chain
	 	 I am transaction (0ad25cbffd27da14df38a4ae2aaf87cea69eb18d) giving 8 $ from node 1 to node 2

	 	 I am transaction (9970a5c0a373b7858e01a02a59859ad880278031) giving 9 $ from node 1 to node 0

	 I am block with index 7
	 My Transaction list contains:
Blockchain:
	 I am block with index 8
	 I am block with index 0
	 My Transaction list contains:
	 My Transaction list contains:
	 	 I am transaction (22b1776df3cd11faed623a33f0143d0497ed9af4) giving 3 $ from node 2 to node 0
	 	 I am transaction (22638dedb224898aa6cae8cbd7cafb03ff303edc) giving 500 $ from node genesis to node 0
False
False
	 I am block with index 1
2 2
	 My Transaction list contains:
AAAA
	 	 I am transaction (f3f596d61dfa65e51ff1c749ed8d9e39f4227f3a) giving 100 $ from node 0 to node 1
	 	 I am transaction (4d4366153409aaf2ea130d97affea9bf6c91c2bb) giving 100 $ from node 0 to node 2
RESOLVE conflicts chain updated
	 	 I am transaction (1798cccfb048481cb904b2a0d7343f90941b9953) giving 1 $ from node 2 to node 4
	 	 I am transaction (4592016452dc7215913bea7029f2a6ff0c3cb2bb) giving 2 $ from node 2 to node 3
	 I am block with index 2
	 My Transaction list contains:
	 I am block with index 8
127.0.0.1 - - [23/Mar/2020 20:57:39] "POST /AddBlock HTTP/1.1" 200 -
	 My Transaction list contains:
	 	 I am transaction (01662993795fb5fd8093c5eb4414af9516606e8e) giving 100 $ from node 0 to node 3
	 	 I am transaction (c41568a85d921ed060a5f30a8ec96b7f255fec7e) giving 100 $ from node 0 to node 4
	 	 I am transaction (22b1776df3cd11faed623a33f0143d0497ed9af4) giving 3 $ from node 2 to node 0
	 I am block with index 3
127.0.0.1 - - [23/Mar/2020 20:57:39] "GET /Chain HTTP/1.1" 200 -
	 	 I am transaction (8c2bd3d8acb1610a994d972003f85122057739ff) giving 4 $ from node 2 to node 4
	 My Transaction list contains:


	 	 I am transaction (e3179905507f5ad52fc3922bfcfd435f3e8e4c53) giving 2 $ from node 1 to node 0
0 1 2 3 4 5 6 7 8

	 	 I am transaction (6b03130364cdbc9e6eb53eec293ac2168eae92e8) giving 3 $ from node 1 to node 3
	 I am block with index 4
	 My Transaction list contains:
127.0.0.1 - - [23/Mar/2020 20:57:39] "POST /AddBlock HTTP/1.1" 200 -
	 	 I am transaction (f693990b4ba97ffa45974d842489e70d62b887e8) giving 4 $ from node 1 to node 0
Old chain
	 	 I am transaction (52775aa21764f8c923c71c3aab103ac49444697c) giving 5 $ from node 1 to node 4


	 I am block with index 5
	 My Transaction list contains:
	 	 I am transaction (72f01b7c9ccea94888b00ed9ecaafe6d4ccb3eef) giving 6 $ from node 1 to node 3
	 	 I am transaction (1077a03e809bd5e682b27629a21afe6f8ade4df4) giving 7 $ from node 1 to node 2
Validate own block
	 I am block with index 6
127.0.0.1 - - [23/Mar/2020 20:57:39] "POST /AddBlock HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:39] "GET /Chain HTTP/1.1" 200 -
Blockchain:
	 I am block with index 0
	 My Transaction list contains:
127.0.0.1 - - [23/Mar/2020 20:57:39] "GET /Chain HTTP/1.1" 200 -
	 My Transaction list contains:
127.0.0.1 - - [23/Mar/2020 20:57:39] "GET /Chain HTTP/1.1" 200 -
	 	 I am transaction (0ad25cbffd27da14df38a4ae2aaf87cea69eb18d) giving 8 $ from node 1 to node 2
	 	 I am transaction (9970a5c0a373b7858e01a02a59859ad880278031) giving 9 $ from node 1 to node 0
	 	 I am transaction (22638dedb224898aa6cae8cbd7cafb03ff303edc) giving 500 $ from node genesis to node 0
127.0.0.1 - - [23/Mar/2020 20:57:39] "GET /Chain HTTP/1.1" 200 -
	 I am block with index 1
127.0.0.1 - - [23/Mar/2020 20:57:39] "POST /AddBlock HTTP/1.1" 200 -
	 I am block with index 7
	 My Transaction list contains:
	 My Transaction list contains:
Done
127.0.0.1 - - [23/Mar/2020 20:57:39] "POST /ValidateTransaction HTTP/1.1" 200 -
	 	 I am transaction (f3f596d61dfa65e51ff1c749ed8d9e39f4227f3a) giving 100 $ from node 0 to node 1
	 	 I am transaction (1798cccfb048481cb904b2a0d7343f90941b9953) giving 1 $ from node 2 to node 4
	 	 I am transaction (4d4366153409aaf2ea130d97affea9bf6c91c2bb) giving 100 $ from node 0 to node 2
	 	 I am transaction (4592016452dc7215913bea7029f2a6ff0c3cb2bb) giving 2 $ from node 2 to node 3
	 I am block with index 2
	 I am block with index 8
	 My Transaction list contains:
	 My Transaction list contains:
	 	 I am transaction (01662993795fb5fd8093c5eb4414af9516606e8e) giving 100 $ from node 0 to node 3
	 	 I am transaction (22b1776df3cd11faed623a33f0143d0497ed9af4) giving 3 $ from node 2 to node 0
	 	 I am transaction (c41568a85d921ed060a5f30a8ec96b7f255fec7e) giving 100 $ from node 0 to node 4
	 	 I am transaction (8c2bd3d8acb1610a994d972003f85122057739ff) giving 4 $ from node 2 to node 4
	 I am block with index 3

	 My Transaction list contains:

	 	 I am transaction (e3179905507f5ad52fc3922bfcfd435f3e8e4c53) giving 2 $ from node 1 to node 0
	 	 I am transaction (6b03130364cdbc9e6eb53eec293ac2168eae92e8) giving 3 $ from node 1 to node 3
	 I am block with index 4
	 My Transaction list contains:
	 	 I am transaction (f693990b4ba97ffa45974d842489e70d62b887e8) giving 4 $ from node 1 to node 0
	 	 I am transaction (52775aa21764f8c923c71c3aab103ac49444697c) giving 5 $ from node 1 to node 4
0 1 2 3 4 5 6 7 8
	 I am block with index 5

	 My Transaction list contains:
New Chain
	 	 I am transaction (72f01b7c9ccea94888b00ed9ecaafe6d4ccb3eef) giving 6 $ from node 1 to node 3

	 	 I am transaction (1077a03e809bd5e682b27629a21afe6f8ade4df4) giving 7 $ from node 1 to node 2

	 I am block with index 6
Blockchain:
	 My Transaction list contains:
	 I am block with index 0
	 	 I am transaction (0ad25cbffd27da14df38a4ae2aaf87cea69eb18d) giving 8 $ from node 1 to node 2
	 My Transaction list contains:
	 	 I am transaction (9970a5c0a373b7858e01a02a59859ad880278031) giving 9 $ from node 1 to node 0
	 	 I am transaction (22638dedb224898aa6cae8cbd7cafb03ff303edc) giving 500 $ from node genesis to node 0
	 I am block with index 7
	 I am block with index 1
	 My Transaction list contains:
	 My Transaction list contains:
	 	 I am transaction (1798cccfb048481cb904b2a0d7343f90941b9953) giving 1 $ from node 2 to node 4
	 	 I am transaction (4592016452dc7215913bea7029f2a6ff0c3cb2bb) giving 2 $ from node 2 to node 3
	 	 I am transaction (f3f596d61dfa65e51ff1c749ed8d9e39f4227f3a) giving 100 $ from node 0 to node 1
	 I am block with index 8
	 	 I am transaction (4d4366153409aaf2ea130d97affea9bf6c91c2bb) giving 100 $ from node 0 to node 2
	 My Transaction list contains:
	 I am block with index 2
	 	 I am transaction (22b1776df3cd11faed623a33f0143d0497ed9af4) giving 3 $ from node 2 to node 0
	 My Transaction list contains:
	 	 I am transaction (8c2bd3d8acb1610a994d972003f85122057739ff) giving 4 $ from node 2 to node 4
	 	 I am transaction (01662993795fb5fd8093c5eb4414af9516606e8e) giving 100 $ from node 0 to node 3

	 	 I am transaction (c41568a85d921ed060a5f30a8ec96b7f255fec7e) giving 100 $ from node 0 to node 4

	 I am block with index 3
0 1 2 3 4 5 6 7 8

New Chain
	 My Transaction list contains:

	 	 I am transaction (e3179905507f5ad52fc3922bfcfd435f3e8e4c53) giving 2 $ from node 1 to node 0
	 	 I am transaction (6b03130364cdbc9e6eb53eec293ac2168eae92e8) giving 3 $ from node 1 to node 3
	 I am block with index 4
	 My Transaction list contains:
	 	 I am transaction (f693990b4ba97ffa45974d842489e70d62b887e8) giving 4 $ from node 1 to node 0
	 	 I am transaction (52775aa21764f8c923c71c3aab103ac49444697c) giving 5 $ from node 1 to node 4

Blockchain:
	 I am block with index 5
127.0.0.1 - - [23/Mar/2020 20:57:39] "GET /Chain HTTP/1.1" 200 -
	 My Transaction list contains:
	 	 I am transaction (72f01b7c9ccea94888b00ed9ecaafe6d4ccb3eef) giving 6 $ from node 1 to node 3
	 I am block with index 0
	 	 I am transaction (1077a03e809bd5e682b27629a21afe6f8ade4df4) giving 7 $ from node 1 to node 2
	 I am block with index 6
	 My Transaction list contains:
	 	 I am transaction (0ad25cbffd27da14df38a4ae2aaf87cea69eb18d) giving 8 $ from node 1 to node 2
	 	 I am transaction (9970a5c0a373b7858e01a02a59859ad880278031) giving 9 $ from node 1 to node 0
	 I am block with index 7
	 My Transaction list contains:
	 My Transaction list contains:
	 	 I am transaction (22638dedb224898aa6cae8cbd7cafb03ff303edc) giving 500 $ from node genesis to node 0
	 I am block with index 1
	 	 I am transaction (1798cccfb048481cb904b2a0d7343f90941b9953) giving 1 $ from node 2 to node 4
	 My Transaction list contains:
	 	 I am transaction (4592016452dc7215913bea7029f2a6ff0c3cb2bb) giving 2 $ from node 2 to node 3
	 	 I am transaction (f3f596d61dfa65e51ff1c749ed8d9e39f4227f3a) giving 100 $ from node 0 to node 1
	 I am block with index 8
	 	 I am transaction (4d4366153409aaf2ea130d97affea9bf6c91c2bb) giving 100 $ from node 0 to node 2
	 My Transaction list contains:
	 I am block with index 2
	 	 I am transaction (22b1776df3cd11faed623a33f0143d0497ed9af4) giving 3 $ from node 2 to node 0
	 My Transaction list contains:
	 	 I am transaction (8c2bd3d8acb1610a994d972003f85122057739ff) giving 4 $ from node 2 to node 4
	 	 I am transaction (01662993795fb5fd8093c5eb4414af9516606e8e) giving 100 $ from node 0 to node 3


	 	 I am transaction (c41568a85d921ed060a5f30a8ec96b7f255fec7e) giving 100 $ from node 0 to node 4
	 I am block with index 3
0 1 2 3 4 5 6 7 8
	 My Transaction list contains:

	 	 I am transaction (e3179905507f5ad52fc3922bfcfd435f3e8e4c53) giving 2 $ from node 1 to node 0
old curr
	 	 I am transaction (6b03130364cdbc9e6eb53eec293ac2168eae92e8) giving 3 $ from node 1 to node 3
	 I am block with index 8
	 I am block with index 4
	 My Transaction list contains:
	 My Transaction list contains:
	 	 I am transaction (f693990b4ba97ffa45974d842489e70d62b887e8) giving 4 $ from node 1 to node 0
	 	 I am transaction (22b1776df3cd11faed623a33f0143d0497ed9af4) giving 3 $ from node 2 to node 0
	 	 I am transaction (52775aa21764f8c923c71c3aab103ac49444697c) giving 5 $ from node 1 to node 4
	 	 I am transaction (56446fd35cbd00ca5595ed583353bb1db2d24ae6) giving 5 $ from node 2 to node 3
new curr
	 I am block with index 5
	 I am block with index 8
	 My Transaction list contains:
	 My Transaction list contains:
	 	 I am transaction (72f01b7c9ccea94888b00ed9ecaafe6d4ccb3eef) giving 6 $ from node 1 to node 3
	 	 I am transaction (22b1776df3cd11faed623a33f0143d0497ed9af4) giving 3 $ from node 2 to node 0
	 	 I am transaction (1077a03e809bd5e682b27629a21afe6f8ade4df4) giving 7 $ from node 1 to node 2
	 I am block with index 6
	 My Transaction list contains:
	 	 I am transaction (0ad25cbffd27da14df38a4ae2aaf87cea69eb18d) giving 8 $ from node 1 to node 2
	 	 I am transaction (9970a5c0a373b7858e01a02a59859ad880278031) giving 9 $ from node 1 to node 0
	 I am block with index 7
	 My Transaction list contains:
	 	 I am transaction (1798cccfb048481cb904b2a0d7343f90941b9953) giving 1 $ from node 2 to node 4
	 	 I am transaction (4592016452dc7215913bea7029f2a6ff0c3cb2bb) giving 2 $ from node 2 to node 3
	 I am block with index 8
	 My Transaction list contains:
	 	 I am transaction (22b1776df3cd11faed623a33f0143d0497ed9af4) giving 3 $ from node 2 to node 0
	 	 I am transaction (8c2bd3d8acb1610a994d972003f85122057739ff) giving 4 $ from node 2 to node 4


0 1 2 3 4 5 6 7 8

old curr
	 I am block with index 8
	 My Transaction list contains:
	 	 I am transaction (22b1776df3cd11faed623a33f0143d0497ed9af4) giving 3 $ from node 2 to node 0
	 	 I am transaction (56446fd35cbd00ca5595ed583353bb1db2d24ae6) giving 5 $ from node 2 to node 3
new curr
	 I am block with index 8
	 My Transaction list contains:
	 	 I am transaction (22b1776df3cd11faed623a33f0143d0497ed9af4) giving 3 $ from node 2 to node 0
127.0.0.1 - - [23/Mar/2020 20:57:39] "GET /Chain HTTP/1.1" 200 -
Block added to blockchain!
	 I am block with index 9
	 My Transaction list contains:
	 	 I am transaction (56446fd35cbd00ca5595ed583353bb1db2d24ae6) giving 5 $ from node 2 to node 3
	 	 I am transaction (46a285e3651b33571ea19c5757fd31059d404849) giving 6 $ from node 2 to node 1


Blockchain:
	 I am block with index 0
	 My Transaction list contains:
	 	 I am transaction (22638dedb224898aa6cae8cbd7cafb03ff303edc) giving 500 $ from node genesis to node 0
	 I am block with index 1
	 My Transaction list contains:
	 	 I am transaction (f3f596d61dfa65e51ff1c749ed8d9e39f4227f3a) giving 100 $ from node 0 to node 1
	 	 I am transaction (4d4366153409aaf2ea130d97affea9bf6c91c2bb) giving 100 $ from node 0 to node 2
	 I am block with index 2
Validating Transaction
	 My Transaction list contains:
127.0.0.1 - - [23/Mar/2020 20:57:40] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:40] "GET /Chain HTTP/1.1" 200 -
	 	 I am transaction (01662993795fb5fd8093c5eb4414af9516606e8e) giving 100 $ from node 0 to node 3
	 	 I am transaction (c41568a85d921ed060a5f30a8ec96b7f255fec7e) giving 100 $ from node 0 to node 4
	 I am block with index 3
	 	 I am transaction (46a285e3651b33571ea19c5757fd31059d404849) giving 6 $ from node 2 to node 1
	 My Transaction list contains:
Result True
Trani 46a285e3651b33571ea19c5757fd31059d404849
	 I am block with index 8
	 My Transaction list contains:
	 	 I am transaction (22b1776df3cd11faed623a33f0143d0497ed9af4) giving 3 $ from node 2 to node 0
	 	 I am transaction (e3179905507f5ad52fc3922bfcfd435f3e8e4c53) giving 2 $ from node 1 to node 0
	 	 I am transaction (6b03130364cdbc9e6eb53eec293ac2168eae92e8) giving 3 $ from node 1 to node 3
	 I am block with index 4
	 My Transaction list contains:
	 	 I am transaction (f693990b4ba97ffa45974d842489e70d62b887e8) giving 4 $ from node 1 to node 0
	 	 I am transaction (52775aa21764f8c923c71c3aab103ac49444697c) giving 5 $ from node 1 to node 4
	 I am block with index 5
	 My Transaction list contains:
	 	 I am transaction (72f01b7c9ccea94888b00ed9ecaafe6d4ccb3eef) giving 6 $ from node 1 to node 3
	 	 I am transaction (1077a03e809bd5e682b27629a21afe6f8ade4df4) giving 7 $ from node 1 to node 2
	 I am block with index 6
	 My Transaction list contains:
	 	 I am transaction (0ad25cbffd27da14df38a4ae2aaf87cea69eb18d) giving 8 $ from node 1 to node 2
	 	 I am transaction (9970a5c0a373b7858e01a02a59859ad880278031) giving 9 $ from node 1 to node 0
	 I am block with index 7
	 My Transaction list contains:
	 	 I am transaction (1798cccfb048481cb904b2a0d7343f90941b9953) giving 1 $ from node 2 to node 4
	 	 I am transaction (4592016452dc7215913bea7029f2a6ff0c3cb2bb) giving 2 $ from node 2 to node 3
	 I am block with index 8
	 My Transaction list contains:
	 	 I am transaction (22b1776df3cd11faed623a33f0143d0497ed9af4) giving 3 $ from node 2 to node 0
	 	 I am transaction (8c2bd3d8acb1610a994d972003f85122057739ff) giving 4 $ from node 2 to node 4
	 I am block with index 9
	 My Transaction list contains:
	 	 I am transaction (56446fd35cbd00ca5595ed583353bb1db2d24ae6) giving 5 $ from node 2 to node 3
	 	 I am transaction (46a285e3651b33571ea19c5757fd31059d404849) giving 6 $ from node 2 to node 1


0 1 2 3 4 5 6 7 8 9

127.0.0.1 - - [23/Mar/2020 20:57:40] "POST /AddBlock HTTP/1.1" 200 -
False
True
Transaction was already in chain or in block
	 	 I am transaction (46a285e3651b33571ea19c5757fd31059d404849) giving 6 $ from node 2 to node 1
127.0.0.1 - - [23/Mar/2020 20:57:40] "POST /ValidateTransaction HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:40] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:40] "POST /AddBlock HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:40] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:40] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:40] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:40] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:40] "POST /AddBlock HTTP/1.1" 200 -
Validating Transaction
	 	 I am transaction (3074e7a3df830ddf77d6659604de340213315716) giving 7 $ from node 2 to node 1
Result True
Trani 3074e7a3df830ddf77d6659604de340213315716
127.0.0.1 - - [23/Mar/2020 20:57:40] "GET /Chain HTTP/1.1" 200 -
	 I am block with index 8
127.0.0.1 - - [23/Mar/2020 20:57:40] "GET /Chain HTTP/1.1" 200 -
	 My Transaction list contains:
	 	 I am transaction (22b1776df3cd11faed623a33f0143d0497ed9af4) giving 3 $ from node 2 to node 0
False
False
2 2
AAAA
127.0.0.1 - - [23/Mar/2020 20:57:40] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:40] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:40] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:41] "POST /AddBlock HTTP/1.1" 200 -
Validate own block
127.0.0.1 - - [23/Mar/2020 20:57:41] "GET /Chain HTTP/1.1" 200 -
Validating Transaction
	 	 I am transaction (3f089568d736d74daa8a39a7ff30ab3e5dc108f1) giving 8 $ from node 2 to node 1
Result True
Trani 3f089568d736d74daa8a39a7ff30ab3e5dc108f1
Validating Transaction
	 I am block with index 9
127.0.0.1 - - [23/Mar/2020 20:57:41] "POST /AddBlock HTTP/1.1" 200 -
	 My Transaction list contains:
	 	 I am transaction (81d6c88d9be8052927b806fa75aaf73d04ebf7b5) giving 9 $ from node 2 to node 0
False
Result True
False
Done
127.0.0.1 - - [23/Mar/2020 20:57:41] "POST /ValidateTransaction HTTP/1.1" 200 -
1 2
127.0.0.1 - - [23/Mar/2020 20:57:41] "POST /ValidateTransaction HTTP/1.1" 200 -
Trani 81d6c88d9be8052927b806fa75aaf73d04ebf7b5
	 I am block with index 9
	 My Transaction list contains:
	 	 I am transaction (3f089568d736d74daa8a39a7ff30ab3e5dc108f1) giving 8 $ from node 2 to node 1
False
False
2 2
AAAA
127.0.0.1 - - [23/Mar/2020 20:57:41] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:41] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:41] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:41] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:41] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:41] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:41] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:41] "POST /AddBlock HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:41] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:42] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:42] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:42] "POST /AddBlock HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:42] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:42] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:42] "POST /AddBlock HTTP/1.1" 200 -
Validating Transaction
127.0.0.1 - - [23/Mar/2020 20:57:42] "GET /Chain HTTP/1.1" 200 -
	 	 I am transaction (5a8ec7c0f99f6fbc4f20fc36ac69a92693da7eb9) giving 10 $ from node 2 to node 3
Result True
Trani 5a8ec7c0f99f6fbc4f20fc36ac69a92693da7eb9
	 I am block with index 10
	 My Transaction list contains:
False
False
1 2
127.0.0.1 - - [23/Mar/2020 20:57:42] "POST /ValidateTransaction HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:42] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:42] "GET /Chain HTTP/1.1" 200 -
Validate own block
127.0.0.1 - - [23/Mar/2020 20:57:42] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:42] "POST /AddBlock HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:42] "POST /AddBlock HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:42] "GET /Chain HTTP/1.1" 200 -
Done
127.0.0.1 - - [23/Mar/2020 20:57:42] "POST /ValidateTransaction HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:42] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:42] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:42] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:43] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:43] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:43] "POST /AddBlock HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:43] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:43] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:43] "POST /AddBlock HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:43] "GET /Chain HTTP/1.1" 200 -
Validating Transaction
	 	 I am transaction (2e8fea2a5a21fbe2154ea2614611acbfc6e2f5b4) giving 1 $ from node 3 to node 2
Result True
Trani 2e8fea2a5a21fbe2154ea2614611acbfc6e2f5b4
	 I am block with index 10
	 My Transaction list contains:
127.0.0.1 - - [23/Mar/2020 20:57:43] "GET /Chain HTTP/1.1" 200 -
	 	 I am transaction (5a8ec7c0f99f6fbc4f20fc36ac69a92693da7eb9) giving 10 $ from node 2 to node 3
False
False
2 2
AAAA
127.0.0.1 - - [23/Mar/2020 20:57:43] "POST /AddBlock HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:43] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:43] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:43] "GET /Chain HTTP/1.1" 200 -
Validating Transaction
	 	 I am transaction (3322428951970e1239ed073957e252e02a565759) giving 2 $ from node 3 to node 4
127.0.0.1 - - [23/Mar/2020 20:57:43] "GET /Chain HTTP/1.1" 200 -
Result True
Trani 3322428951970e1239ed073957e252e02a565759
	 I am block with index 11
	 My Transaction list contains:
False
False
1 2
127.0.0.1 - - [23/Mar/2020 20:57:43] "POST /ValidateTransaction HTTP/1.1" 200 -
Validate own block
Block added to blockchain!
	 I am block with index 10
	 My Transaction list contains:
	 	 I am transaction (5a8ec7c0f99f6fbc4f20fc36ac69a92693da7eb9) giving 10 $ from node 2 to node 3
	 	 I am transaction (2e8fea2a5a21fbe2154ea2614611acbfc6e2f5b4) giving 1 $ from node 3 to node 2


Blockchain:
	 I am block with index 0
	 My Transaction list contains:
	 	 I am transaction (22638dedb224898aa6cae8cbd7cafb03ff303edc) giving 500 $ from node genesis to node 0
	 I am block with index 1
	 My Transaction list contains:
	 	 I am transaction (f3f596d61dfa65e51ff1c749ed8d9e39f4227f3a) giving 100 $ from node 0 to node 1
	 	 I am transaction (4d4366153409aaf2ea130d97affea9bf6c91c2bb) giving 100 $ from node 0 to node 2
	 I am block with index 2
	 My Transaction list contains:
	 	 I am transaction (01662993795fb5fd8093c5eb4414af9516606e8e) giving 100 $ from node 0 to node 3
	 	 I am transaction (c41568a85d921ed060a5f30a8ec96b7f255fec7e) giving 100 $ from node 0 to node 4
	 I am block with index 3
	 My Transaction list contains:
	 	 I am transaction (e3179905507f5ad52fc3922bfcfd435f3e8e4c53) giving 2 $ from node 1 to node 0
	 	 I am transaction (6b03130364cdbc9e6eb53eec293ac2168eae92e8) giving 3 $ from node 1 to node 3
	 I am block with index 4
	 My Transaction list contains:
	 	 I am transaction (f693990b4ba97ffa45974d842489e70d62b887e8) giving 4 $ from node 1 to node 0
	 	 I am transaction (52775aa21764f8c923c71c3aab103ac49444697c) giving 5 $ from node 1 to node 4
	 I am block with index 5
	 My Transaction list contains:
	 	 I am transaction (72f01b7c9ccea94888b00ed9ecaafe6d4ccb3eef) giving 6 $ from node 1 to node 3
	 	 I am transaction (1077a03e809bd5e682b27629a21afe6f8ade4df4) giving 7 $ from node 1 to node 2
	 I am block with index 6
	 My Transaction list contains:
	 	 I am transaction (0ad25cbffd27da14df38a4ae2aaf87cea69eb18d) giving 8 $ from node 1 to node 2
	 	 I am transaction (9970a5c0a373b7858e01a02a59859ad880278031) giving 9 $ from node 1 to node 0
	 I am block with index 7
	 My Transaction list contains:
	 	 I am transaction (1798cccfb048481cb904b2a0d7343f90941b9953) giving 1 $ from node 2 to node 4
	 	 I am transaction (4592016452dc7215913bea7029f2a6ff0c3cb2bb) giving 2 $ from node 2 to node 3
	 I am block with index 8
	 My Transaction list contains:
	 	 I am transaction (22b1776df3cd11faed623a33f0143d0497ed9af4) giving 3 $ from node 2 to node 0
	 	 I am transaction (8c2bd3d8acb1610a994d972003f85122057739ff) giving 4 $ from node 2 to node 4
	 I am block with index 9
	 My Transaction list contains:
	 	 I am transaction (56446fd35cbd00ca5595ed583353bb1db2d24ae6) giving 5 $ from node 2 to node 3
	 	 I am transaction (46a285e3651b33571ea19c5757fd31059d404849) giving 6 $ from node 2 to node 1
	 I am block with index 10
	 My Transaction list contains:
	 	 I am transaction (5a8ec7c0f99f6fbc4f20fc36ac69a92693da7eb9) giving 10 $ from node 2 to node 3
	 	 I am transaction (2e8fea2a5a21fbe2154ea2614611acbfc6e2f5b4) giving 1 $ from node 3 to node 2


0 1 2 3 4 5 6 7 8 9 10

127.0.0.1 - - [23/Mar/2020 20:57:44] "POST /AddBlock HTTP/1.1" 200 -
Done
127.0.0.1 - - [23/Mar/2020 20:57:44] "POST /ValidateTransaction HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:44] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:44] "POST /AddBlock HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:44] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:45] "POST /AddBlock HTTP/1.1" 200 -
Block added to blockchain!
	 I am block with index 11
	 My Transaction list contains:
	 	 I am transaction (3322428951970e1239ed073957e252e02a565759) giving 2 $ from node 3 to node 4
	 	 I am transaction (133b7695dfbbbeebc068687462f272194c2c9db5) giving 3 $ from node 3 to node 0


Blockchain:
	 I am block with index 0
	 My Transaction list contains:
	 	 I am transaction (22638dedb224898aa6cae8cbd7cafb03ff303edc) giving 500 $ from node genesis to node 0
	 I am block with index 1
	 My Transaction list contains:
	 	 I am transaction (f3f596d61dfa65e51ff1c749ed8d9e39f4227f3a) giving 100 $ from node 0 to node 1
	 	 I am transaction (4d4366153409aaf2ea130d97affea9bf6c91c2bb) giving 100 $ from node 0 to node 2
	 I am block with index 2
	 My Transaction list contains:
	 	 I am transaction (01662993795fb5fd8093c5eb4414af9516606e8e) giving 100 $ from node 0 to node 3
	 	 I am transaction (c41568a85d921ed060a5f30a8ec96b7f255fec7e) giving 100 $ from node 0 to node 4
	 I am block with index 3
	 My Transaction list contains:
	 	 I am transaction (e3179905507f5ad52fc3922bfcfd435f3e8e4c53) giving 2 $ from node 1 to node 0
	 	 I am transaction (6b03130364cdbc9e6eb53eec293ac2168eae92e8) giving 3 $ from node 1 to node 3
	 I am block with index 4
	 My Transaction list contains:
	 	 I am transaction (f693990b4ba97ffa45974d842489e70d62b887e8) giving 4 $ from node 1 to node 0
	 	 I am transaction (52775aa21764f8c923c71c3aab103ac49444697c) giving 5 $ from node 1 to node 4
	 I am block with index 5
	 My Transaction list contains:
	 	 I am transaction (72f01b7c9ccea94888b00ed9ecaafe6d4ccb3eef) giving 6 $ from node 1 to node 3
	 	 I am transaction (1077a03e809bd5e682b27629a21afe6f8ade4df4) giving 7 $ from node 1 to node 2
	 I am block with index 6
	 My Transaction list contains:
	 	 I am transaction (0ad25cbffd27da14df38a4ae2aaf87cea69eb18d) giving 8 $ from node 1 to node 2
	 	 I am transaction (9970a5c0a373b7858e01a02a59859ad880278031) giving 9 $ from node 1 to node 0
	 I am block with index 7
	 My Transaction list contains:
	 	 I am transaction (1798cccfb048481cb904b2a0d7343f90941b9953) giving 1 $ from node 2 to node 4
	 	 I am transaction (4592016452dc7215913bea7029f2a6ff0c3cb2bb) giving 2 $ from node 2 to node 3
	 I am block with index 8
	 My Transaction list contains:
	 	 I am transaction (22b1776df3cd11faed623a33f0143d0497ed9af4) giving 3 $ from node 2 to node 0
	 	 I am transaction (8c2bd3d8acb1610a994d972003f85122057739ff) giving 4 $ from node 2 to node 4
	 I am block with index 9
	 My Transaction list contains:
	 	 I am transaction (56446fd35cbd00ca5595ed583353bb1db2d24ae6) giving 5 $ from node 2 to node 3
	 	 I am transaction (46a285e3651b33571ea19c5757fd31059d404849) giving 6 $ from node 2 to node 1
	 I am block with index 10
	 My Transaction list contains:
	 	 I am transaction (5a8ec7c0f99f6fbc4f20fc36ac69a92693da7eb9) giving 10 $ from node 2 to node 3
	 	 I am transaction (2e8fea2a5a21fbe2154ea2614611acbfc6e2f5b4) giving 1 $ from node 3 to node 2
	 I am block with index 11
	 My Transaction list contains:
	 	 I am transaction (3322428951970e1239ed073957e252e02a565759) giving 2 $ from node 3 to node 4
	 	 I am transaction (133b7695dfbbbeebc068687462f272194c2c9db5) giving 3 $ from node 3 to node 0


0 1 2 3 4 5 6 7 8 9 10 11

127.0.0.1 - - [23/Mar/2020 20:57:45] "POST /AddBlock HTTP/1.1" 200 -
Validating Transaction
	 	 I am transaction (133b7695dfbbbeebc068687462f272194c2c9db5) giving 3 $ from node 3 to node 0
Result True
Trani 133b7695dfbbbeebc068687462f272194c2c9db5
	 I am block with index 11
	 My Transaction list contains:
	 	 I am transaction (3322428951970e1239ed073957e252e02a565759) giving 2 $ from node 3 to node 4
False
True
Transaction was already in chain or in block
	 	 I am transaction (133b7695dfbbbeebc068687462f272194c2c9db5) giving 3 $ from node 3 to node 0
127.0.0.1 - - [23/Mar/2020 20:57:45] "GET /Chain HTTP/1.1" 200 -
Validating Transaction
	 	 I am transaction (843797a9e5d1b0854876dd99248dd83de25e2002) giving 4 $ from node 3 to node 2
Result True
Trani 843797a9e5d1b0854876dd99248dd83de25e2002
	 I am block with index 11
127.0.0.1 - - [23/Mar/2020 20:57:45] "POST /ValidateTransaction HTTP/1.1" 200 -
	 My Transaction list contains:
	 	 I am transaction (3322428951970e1239ed073957e252e02a565759) giving 2 $ from node 3 to node 4
False
False
2 2
AAAA
127.0.0.1 - - [23/Mar/2020 20:57:45] "GET /Chain HTTP/1.1" 200 -
Block added to blockchain!
	 I am block with index 12
	 My Transaction list contains:
	 	 I am transaction (843797a9e5d1b0854876dd99248dd83de25e2002) giving 4 $ from node 3 to node 2
127.0.0.1 - - [23/Mar/2020 20:57:45] "GET /Chain HTTP/1.1" 200 -
Validating Transaction
	 	 I am transaction (fb1236aa94f4e55fe778d32084c98905f28c9acc) giving 5 $ from node 3 to node 1
127.0.0.1 - - [23/Mar/2020 20:57:45] "POST /AddBlock HTTP/1.1" 200 -
	 	 I am transaction (fb1236aa94f4e55fe778d32084c98905f28c9acc) giving 5 $ from node 3 to node 1


Result True
Blockchain:
Trani fb1236aa94f4e55fe778d32084c98905f28c9acc
	 I am block with index 12
Validating Transaction
	 My Transaction list contains:
	 I am block with index 0
	 My Transaction list contains:
	 	 I am transaction (cb51a507ab01cae351eeb41cb71892ff97da9b52) giving 6 $ from node 3 to node 2
False
127.0.0.1 - - [23/Mar/2020 20:57:45] "GET /Chain HTTP/1.1" 200 -
	 	 I am transaction (22638dedb224898aa6cae8cbd7cafb03ff303edc) giving 500 $ from node genesis to node 0
	 I am block with index 1
True
	 My Transaction list contains:
Result True
	 	 I am transaction (f3f596d61dfa65e51ff1c749ed8d9e39f4227f3a) giving 100 $ from node 0 to node 1
Transaction was already in chain or in block
	 	 I am transaction (4d4366153409aaf2ea130d97affea9bf6c91c2bb) giving 100 $ from node 0 to node 2
	 I am block with index 2
	 	 I am transaction (fb1236aa94f4e55fe778d32084c98905f28c9acc) giving 5 $ from node 3 to node 1
127.0.0.1 - - [23/Mar/2020 20:57:45] "POST /ValidateTransaction HTTP/1.1" 200 -
	 My Transaction list contains:
Trani cb51a507ab01cae351eeb41cb71892ff97da9b52
	 I am block with index 12
	 	 I am transaction (01662993795fb5fd8093c5eb4414af9516606e8e) giving 100 $ from node 0 to node 3
	 	 I am transaction (c41568a85d921ed060a5f30a8ec96b7f255fec7e) giving 100 $ from node 0 to node 4
	 My Transaction list contains:
	 I am block with index 3
False
	 My Transaction list contains:
False
1 2
127.0.0.1 - - [23/Mar/2020 20:57:46] "POST /ValidateTransaction HTTP/1.1" 200 -
	 	 I am transaction (e3179905507f5ad52fc3922bfcfd435f3e8e4c53) giving 2 $ from node 1 to node 0
	 	 I am transaction (6b03130364cdbc9e6eb53eec293ac2168eae92e8) giving 3 $ from node 1 to node 3
	 I am block with index 4
	 My Transaction list contains:
	 	 I am transaction (f693990b4ba97ffa45974d842489e70d62b887e8) giving 4 $ from node 1 to node 0
	 	 I am transaction (52775aa21764f8c923c71c3aab103ac49444697c) giving 5 $ from node 1 to node 4
	 I am block with index 5
	 My Transaction list contains:
	 	 I am transaction (72f01b7c9ccea94888b00ed9ecaafe6d4ccb3eef) giving 6 $ from node 1 to node 3
	 	 I am transaction (1077a03e809bd5e682b27629a21afe6f8ade4df4) giving 7 $ from node 1 to node 2
	 I am block with index 6
	 My Transaction list contains:
	 	 I am transaction (0ad25cbffd27da14df38a4ae2aaf87cea69eb18d) giving 8 $ from node 1 to node 2
	 	 I am transaction (9970a5c0a373b7858e01a02a59859ad880278031) giving 9 $ from node 1 to node 0
	 I am block with index 7
	 My Transaction list contains:
	 	 I am transaction (1798cccfb048481cb904b2a0d7343f90941b9953) giving 1 $ from node 2 to node 4
	 	 I am transaction (4592016452dc7215913bea7029f2a6ff0c3cb2bb) giving 2 $ from node 2 to node 3
Validate own block
Block added to blockchain!
	 I am block with index 8
	 My Transaction list contains:
	 I am block with index 13
	 	 I am transaction (22b1776df3cd11faed623a33f0143d0497ed9af4) giving 3 $ from node 2 to node 0
	 My Transaction list contains:
	 	 I am transaction (8c2bd3d8acb1610a994d972003f85122057739ff) giving 4 $ from node 2 to node 4
127.0.0.1 - - [23/Mar/2020 20:57:46] "POST /AddBlock HTTP/1.1" 200 -
	 I am block with index 9
	 My Transaction list contains:
	 	 I am transaction (cb51a507ab01cae351eeb41cb71892ff97da9b52) giving 6 $ from node 3 to node 2
	 	 I am transaction (56446fd35cbd00ca5595ed583353bb1db2d24ae6) giving 5 $ from node 2 to node 3
	 	 I am transaction (f818497c1d6e70aa9ba133362cf3b6dff1ad3f27) giving 7 $ from node 3 to node 2
Validating Transaction
	 	 I am transaction (46a285e3651b33571ea19c5757fd31059d404849) giving 6 $ from node 2 to node 1

	 I am block with index 10

	 	 I am transaction (f818497c1d6e70aa9ba133362cf3b6dff1ad3f27) giving 7 $ from node 3 to node 2
Done
127.0.0.1 - - [23/Mar/2020 20:57:46] "POST /ValidateTransaction HTTP/1.1" 200 -
	 My Transaction list contains:
Blockchain:
	 I am block with index 0
	 My Transaction list contains:
	 	 I am transaction (22638dedb224898aa6cae8cbd7cafb03ff303edc) giving 500 $ from node genesis to node 0
	 I am block with index 1
	 My Transaction list contains:
	 	 I am transaction (f3f596d61dfa65e51ff1c749ed8d9e39f4227f3a) giving 100 $ from node 0 to node 1
	 	 I am transaction (4d4366153409aaf2ea130d97affea9bf6c91c2bb) giving 100 $ from node 0 to node 2
	 I am block with index 2
	 My Transaction list contains:
	 	 I am transaction (01662993795fb5fd8093c5eb4414af9516606e8e) giving 100 $ from node 0 to node 3
	 	 I am transaction (c41568a85d921ed060a5f30a8ec96b7f255fec7e) giving 100 $ from node 0 to node 4
	 I am block with index 3
	 My Transaction list contains:
	 	 I am transaction (e3179905507f5ad52fc3922bfcfd435f3e8e4c53) giving 2 $ from node 1 to node 0
	 	 I am transaction (6b03130364cdbc9e6eb53eec293ac2168eae92e8) giving 3 $ from node 1 to node 3
	 I am block with index 4
	 My Transaction list contains:
	 	 I am transaction (f693990b4ba97ffa45974d842489e70d62b887e8) giving 4 $ from node 1 to node 0
	 	 I am transaction (52775aa21764f8c923c71c3aab103ac49444697c) giving 5 $ from node 1 to node 4
	 I am block with index 5
	 My Transaction list contains:
	 	 I am transaction (72f01b7c9ccea94888b00ed9ecaafe6d4ccb3eef) giving 6 $ from node 1 to node 3
	 	 I am transaction (1077a03e809bd5e682b27629a21afe6f8ade4df4) giving 7 $ from node 1 to node 2
	 I am block with index 6
	 My Transaction list contains:
	 	 I am transaction (0ad25cbffd27da14df38a4ae2aaf87cea69eb18d) giving 8 $ from node 1 to node 2
	 	 I am transaction (9970a5c0a373b7858e01a02a59859ad880278031) giving 9 $ from node 1 to node 0
	 I am block with index 7
	 My Transaction list contains:
	 	 I am transaction (1798cccfb048481cb904b2a0d7343f90941b9953) giving 1 $ from node 2 to node 4
	 	 I am transaction (4592016452dc7215913bea7029f2a6ff0c3cb2bb) giving 2 $ from node 2 to node 3
	 I am block with index 8
	 My Transaction list contains:
	 	 I am transaction (22b1776df3cd11faed623a33f0143d0497ed9af4) giving 3 $ from node 2 to node 0
	 	 I am transaction (8c2bd3d8acb1610a994d972003f85122057739ff) giving 4 $ from node 2 to node 4
	 I am block with index 9
	 My Transaction list contains:
	 	 I am transaction (56446fd35cbd00ca5595ed583353bb1db2d24ae6) giving 5 $ from node 2 to node 3
	 	 I am transaction (46a285e3651b33571ea19c5757fd31059d404849) giving 6 $ from node 2 to node 1
	 I am block with index 10
	 My Transaction list contains:
	 	 I am transaction (5a8ec7c0f99f6fbc4f20fc36ac69a92693da7eb9) giving 10 $ from node 2 to node 3
Result True
Trani f818497c1d6e70aa9ba133362cf3b6dff1ad3f27
	 I am block with index 12
	 My Transaction list contains:
	 	 I am transaction (cb51a507ab01cae351eeb41cb71892ff97da9b52) giving 6 $ from node 3 to node 2
False
	 	 I am transaction (2e8fea2a5a21fbe2154ea2614611acbfc6e2f5b4) giving 1 $ from node 3 to node 2
Validating Transaction
	 I am block with index 11
	 	 I am transaction (40d8b89699b0df367495facd9331e7258d5af681) giving 8 $ from node 3 to node 4
True
	 	 I am transaction (5a8ec7c0f99f6fbc4f20fc36ac69a92693da7eb9) giving 10 $ from node 2 to node 3
	 My Transaction list contains:
Result True
Transaction was already in chain or in block
	 	 I am transaction (3322428951970e1239ed073957e252e02a565759) giving 2 $ from node 3 to node 4
	 	 I am transaction (f818497c1d6e70aa9ba133362cf3b6dff1ad3f27) giving 7 $ from node 3 to node 2
127.0.0.1 - - [23/Mar/2020 20:57:46] "POST /ValidateTransaction HTTP/1.1" 200 -
	 	 I am transaction (133b7695dfbbbeebc068687462f272194c2c9db5) giving 3 $ from node 3 to node 0
	 	 I am transaction (2e8fea2a5a21fbe2154ea2614611acbfc6e2f5b4) giving 1 $ from node 3 to node 2
	 I am block with index 12
	 I am block with index 11
	 My Transaction list contains:
	 My Transaction list contains:
	 	 I am transaction (843797a9e5d1b0854876dd99248dd83de25e2002) giving 4 $ from node 3 to node 2
Trani 40d8b89699b0df367495facd9331e7258d5af681
	 	 I am transaction (3322428951970e1239ed073957e252e02a565759) giving 2 $ from node 3 to node 4
	 	 I am transaction (133b7695dfbbbeebc068687462f272194c2c9db5) giving 3 $ from node 3 to node 0
	 	 I am transaction (fb1236aa94f4e55fe778d32084c98905f28c9acc) giving 5 $ from node 3 to node 1
	 I am block with index 12
	 My Transaction list contains:
	 	 I am transaction (cb51a507ab01cae351eeb41cb71892ff97da9b52) giving 6 $ from node 3 to node 2
False
	 I am block with index 12
	 I am block with index 13
False
	 My Transaction list contains:
2 2
	 	 I am transaction (843797a9e5d1b0854876dd99248dd83de25e2002) giving 4 $ from node 3 to node 2
AAAA
	 	 I am transaction (fb1236aa94f4e55fe778d32084c98905f28c9acc) giving 5 $ from node 3 to node 1
	 My Transaction list contains:
	 I am block with index 13
	 	 I am transaction (cb51a507ab01cae351eeb41cb71892ff97da9b52) giving 6 $ from node 3 to node 2
	 My Transaction list contains:
	 	 I am transaction (f818497c1d6e70aa9ba133362cf3b6dff1ad3f27) giving 7 $ from node 3 to node 2

	 	 I am transaction (cb51a507ab01cae351eeb41cb71892ff97da9b52) giving 6 $ from node 3 to node 2
	 	 I am transaction (f818497c1d6e70aa9ba133362cf3b6dff1ad3f27) giving 7 $ from node 3 to node 2



0 1 2 3 4 5 6 7 8 9 10 11 12 13

127.0.0.1 - - [23/Mar/2020 20:57:46] "POST /AddBlock HTTP/1.1" 200 -
0 1 2 3 4 5 6 7 8 9 10 11 12 13

Validate own block
127.0.0.1 - - [23/Mar/2020 20:57:46] "POST /AddBlock HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:46] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:46] "POST /AddBlock HTTP/1.1" 200 -
Done
127.0.0.1 - - [23/Mar/2020 20:57:46] "POST /ValidateTransaction HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:46] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:46] "GET /Chain HTTP/1.1" 200 -
Block added to blockchain!
	 I am block with index 14
	 My Transaction list contains:
	 	 I am transaction (40d8b89699b0df367495facd9331e7258d5af681) giving 8 $ from node 3 to node 4
	 	 I am transaction (2bf363cfe5bbcb5719055fcbc2c373cf540b75cb) giving 9 $ from node 3 to node 4


Blockchain:
	 I am block with index 0
	 My Transaction list contains:
	 	 I am transaction (22638dedb224898aa6cae8cbd7cafb03ff303edc) giving 500 $ from node genesis to node 0
	 I am block with index 1
	 My Transaction list contains:
	 	 I am transaction (f3f596d61dfa65e51ff1c749ed8d9e39f4227f3a) giving 100 $ from node 0 to node 1
	 	 I am transaction (4d4366153409aaf2ea130d97affea9bf6c91c2bb) giving 100 $ from node 0 to node 2
	 I am block with index 2
	 My Transaction list contains:
	 	 I am transaction (01662993795fb5fd8093c5eb4414af9516606e8e) giving 100 $ from node 0 to node 3
	 	 I am transaction (c41568a85d921ed060a5f30a8ec96b7f255fec7e) giving 100 $ from node 0 to node 4
	 I am block with index 3
	 My Transaction list contains:
	 	 I am transaction (e3179905507f5ad52fc3922bfcfd435f3e8e4c53) giving 2 $ from node 1 to node 0
	 	 I am transaction (6b03130364cdbc9e6eb53eec293ac2168eae92e8) giving 3 $ from node 1 to node 3
	 I am block with index 4
	 My Transaction list contains:
	 	 I am transaction (f693990b4ba97ffa45974d842489e70d62b887e8) giving 4 $ from node 1 to node 0
	 	 I am transaction (52775aa21764f8c923c71c3aab103ac49444697c) giving 5 $ from node 1 to node 4
	 I am block with index 5
	 My Transaction list contains:
	 	 I am transaction (72f01b7c9ccea94888b00ed9ecaafe6d4ccb3eef) giving 6 $ from node 1 to node 3
	 	 I am transaction (1077a03e809bd5e682b27629a21afe6f8ade4df4) giving 7 $ from node 1 to node 2
	 I am block with index 6
	 My Transaction list contains:
	 	 I am transaction (0ad25cbffd27da14df38a4ae2aaf87cea69eb18d) giving 8 $ from node 1 to node 2
	 	 I am transaction (9970a5c0a373b7858e01a02a59859ad880278031) giving 9 $ from node 1 to node 0
	 I am block with index 7
	 My Transaction list contains:
	 	 I am transaction (1798cccfb048481cb904b2a0d7343f90941b9953) giving 1 $ from node 2 to node 4
	 	 I am transaction (4592016452dc7215913bea7029f2a6ff0c3cb2bb) giving 2 $ from node 2 to node 3
	 I am block with index 8
	 My Transaction list contains:
	 	 I am transaction (22b1776df3cd11faed623a33f0143d0497ed9af4) giving 3 $ from node 2 to node 0
	 	 I am transaction (8c2bd3d8acb1610a994d972003f85122057739ff) giving 4 $ from node 2 to node 4
	 I am block with index 9
	 My Transaction list contains:
	 	 I am transaction (56446fd35cbd00ca5595ed583353bb1db2d24ae6) giving 5 $ from node 2 to node 3
	 	 I am transaction (46a285e3651b33571ea19c5757fd31059d404849) giving 6 $ from node 2 to node 1
	 I am block with index 10
	 My Transaction list contains:
	 	 I am transaction (5a8ec7c0f99f6fbc4f20fc36ac69a92693da7eb9) giving 10 $ from node 2 to node 3
	 	 I am transaction (2e8fea2a5a21fbe2154ea2614611acbfc6e2f5b4) giving 1 $ from node 3 to node 2
	 I am block with index 11
	 My Transaction list contains:
	 	 I am transaction (3322428951970e1239ed073957e252e02a565759) giving 2 $ from node 3 to node 4
	 	 I am transaction (133b7695dfbbbeebc068687462f272194c2c9db5) giving 3 $ from node 3 to node 0
	 I am block with index 12
	 My Transaction list contains:
	 	 I am transaction (843797a9e5d1b0854876dd99248dd83de25e2002) giving 4 $ from node 3 to node 2
	 	 I am transaction (fb1236aa94f4e55fe778d32084c98905f28c9acc) giving 5 $ from node 3 to node 1
	 I am block with index 13
	 My Transaction list contains:
	 	 I am transaction (cb51a507ab01cae351eeb41cb71892ff97da9b52) giving 6 $ from node 3 to node 2
	 	 I am transaction (f818497c1d6e70aa9ba133362cf3b6dff1ad3f27) giving 7 $ from node 3 to node 2
	 I am block with index 14
	 My Transaction list contains:
	 	 I am transaction (40d8b89699b0df367495facd9331e7258d5af681) giving 8 $ from node 3 to node 4
	 	 I am transaction (2bf363cfe5bbcb5719055fcbc2c373cf540b75cb) giving 9 $ from node 3 to node 4


0 1 2 3 4 5 6 7 8 9 10 11 12 13 14

127.0.0.1 - - [23/Mar/2020 20:57:47] "POST /AddBlock HTTP/1.1" 200 -
Validating Transaction
	 	 I am transaction (2bf363cfe5bbcb5719055fcbc2c373cf540b75cb) giving 9 $ from node 3 to node 4
Result True
Trani 2bf363cfe5bbcb5719055fcbc2c373cf540b75cb
	 I am block with index 13
	 My Transaction list contains:
False
True
Transaction was already in chain or in block
	 	 I am transaction (2bf363cfe5bbcb5719055fcbc2c373cf540b75cb) giving 9 $ from node 3 to node 4
127.0.0.1 - - [23/Mar/2020 20:57:47] "POST /ValidateTransaction HTTP/1.1" 200 -
Validating Transaction
	 	 I am transaction (2a4886fd71f36fce15eb0549944b297331a703a3) giving 10 $ from node 3 to node 0
Result True
Trani 2a4886fd71f36fce15eb0549944b297331a703a3
	 I am block with index 13
	 My Transaction list contains:
False
False
1 2
127.0.0.1 - - [23/Mar/2020 20:57:47] "POST /ValidateTransaction HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:47] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:47] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:47] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:47] "POST /AddBlock HTTP/1.1" 200 -
Validating Transaction
	 	 I am transaction (2790d441348fe56b4e5bf9dd13cededf4b2cfadb) giving 1 $ from node 4 to node 3
Result True
Trani 2790d441348fe56b4e5bf9dd13cededf4b2cfadb
127.0.0.1 - - [23/Mar/2020 20:57:47] "GET /Chain HTTP/1.1" 200 -
	 I am block with index 13
	 My Transaction list contains:
127.0.0.1 - - [23/Mar/2020 20:57:47] "GET /Chain HTTP/1.1" 200 -
	 	 I am transaction (2a4886fd71f36fce15eb0549944b297331a703a3) giving 10 $ from node 3 to node 0
False
127.0.0.1 - - [23/Mar/2020 20:57:47] "POST /AddBlock HTTP/1.1" 200 -
False
2 2
AAAA
127.0.0.1 - - [23/Mar/2020 20:57:47] "POST /AddBlock HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:47] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:47] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:47] "POST /AddBlock HTTP/1.1" 200 -
Validating Transaction
	 	 I am transaction (b7a2e5451c10c5bda77757fb3263ec1e126adad1) giving 2 $ from node 4 to node 0
Result True
127.0.0.1 - - [23/Mar/2020 20:57:47] "POST /AddBlock HTTP/1.1" 200 -
Trani b7a2e5451c10c5bda77757fb3263ec1e126adad1
127.0.0.1 - - [23/Mar/2020 20:57:47] "GET /Chain HTTP/1.1" 200 -
	 I am block with index 14
	 My Transaction list contains:
False
False
1 2
127.0.0.1 - - [23/Mar/2020 20:57:47] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:47] "POST /ValidateTransaction HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:48] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:48] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:48] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:48] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:48] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:48] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:48] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:48] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:48] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:48] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:48] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:49] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:49] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:49] "GET /Chain HTTP/1.1" 200 -
Validate own block
127.0.0.1 - - [23/Mar/2020 20:57:49] "POST /AddBlock HTTP/1.1" 200 -
Done
127.0.0.1 - - [23/Mar/2020 20:57:49] "POST /ValidateTransaction HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:50] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:50] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:50] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:50] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:50] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:50] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:50] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:50] "POST /AddBlock HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:50] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:50] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:50] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:51] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:51] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:51] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:51] "POST /AddBlock HTTP/1.1" 200 -
Validating Transaction
	 	 I am transaction (83cbee64c7ec2accff282f6a5b9a5a83974156e7) giving 3 $ from node 4 to node 1
Result True
Trani 83cbee64c7ec2accff282f6a5b9a5a83974156e7
Validating Transaction
	 	 I am transaction (0b528ce00b7afc9d14cc12b85668e4690211e446) giving 4 $ from node 4 to node 0
	 I am block with index 14
	 My Transaction list contains:
Result True
	 	 I am transaction (b7a2e5451c10c5bda77757fb3263ec1e126adad1) giving 2 $ from node 4 to node 0
False
False
2 2
AAAA
Trani 0b528ce00b7afc9d14cc12b85668e4690211e446
	 I am block with index 14
	 My Transaction list contains:
	 	 I am transaction (b7a2e5451c10c5bda77757fb3263ec1e126adad1) giving 2 $ from node 4 to node 0
	 	 I am transaction (83cbee64c7ec2accff282f6a5b9a5a83974156e7) giving 3 $ from node 4 to node 1
False
False
OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
127.0.0.1 - - [23/Mar/2020 20:57:51] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:51] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:51] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:51] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:51] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:51] "GET /Chain HTTP/1.1" 200 -
Validate own block
127.0.0.1 - - [23/Mar/2020 20:57:52] "POST /AddBlock HTTP/1.1" 200 -
Done
127.0.0.1 - - [23/Mar/2020 20:57:52] "POST /ValidateTransaction HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:52] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:52] "POST /AddBlock HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:52] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:52] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:52] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:53] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:53] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:53] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:53] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:53] "POST /AddBlock HTTP/1.1" 200 -
Validating Transaction
	 	 I am transaction (a969fe037758ae19eb784dd684e3360333cfcd63) giving 5 $ from node 4 to node 2
127.0.0.1 - - [23/Mar/2020 20:57:53] "GET /Chain HTTP/1.1" 200 -
Result True
Trani a969fe037758ae19eb784dd684e3360333cfcd63
	 I am block with index 15
	 My Transaction list contains:
False
False
1 2
127.0.0.1 - - [23/Mar/2020 20:57:53] "POST /ValidateTransaction HTTP/1.1" 200 -
Validating Transaction
	 	 I am transaction (cc3e263d25a3a9ad09bcc3980f600cbba3af1dc3) giving 6 $ from node 4 to node 1
Result True
Trani cc3e263d25a3a9ad09bcc3980f600cbba3af1dc3
	 I am block with index 15
	 My Transaction list contains:
	 	 I am transaction (a969fe037758ae19eb784dd684e3360333cfcd63) giving 5 $ from node 4 to node 2
False
False
2 2
AAAA
Validate own block
127.0.0.1 - - [23/Mar/2020 20:57:53] "POST /AddBlock HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:53] "POST /AddBlock HTTP/1.1" 200 -
Done
127.0.0.1 - - [23/Mar/2020 20:57:53] "POST /ValidateTransaction HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:53] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:53] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:54] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:54] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:54] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:54] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:54] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:54] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:54] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:54] "POST /AddBlock HTTP/1.1" 200 -
Block added to blockchain!
	 I am block with index 15
	 My Transaction list contains:
	 	 I am transaction (2a4886fd71f36fce15eb0549944b297331a703a3) giving 10 $ from node 3 to node 0
	 	 I am transaction (b7a2e5451c10c5bda77757fb3263ec1e126adad1) giving 2 $ from node 4 to node 0


Blockchain:
127.0.0.1 - - [23/Mar/2020 20:57:54] "GET /Chain HTTP/1.1" 200 -
	 I am block with index 0
	 My Transaction list contains:
	 	 I am transaction (22638dedb224898aa6cae8cbd7cafb03ff303edc) giving 500 $ from node genesis to node 0
	 I am block with index 1
	 My Transaction list contains:
	 	 I am transaction (f3f596d61dfa65e51ff1c749ed8d9e39f4227f3a) giving 100 $ from node 0 to node 1
	 	 I am transaction (4d4366153409aaf2ea130d97affea9bf6c91c2bb) giving 100 $ from node 0 to node 2
	 I am block with index 2
	 My Transaction list contains:
	 	 I am transaction (01662993795fb5fd8093c5eb4414af9516606e8e) giving 100 $ from node 0 to node 3
	 	 I am transaction (c41568a85d921ed060a5f30a8ec96b7f255fec7e) giving 100 $ from node 0 to node 4
	 I am block with index 3
	 My Transaction list contains:
	 	 I am transaction (e3179905507f5ad52fc3922bfcfd435f3e8e4c53) giving 2 $ from node 1 to node 0
	 	 I am transaction (6b03130364cdbc9e6eb53eec293ac2168eae92e8) giving 3 $ from node 1 to node 3
	 I am block with index 4
	 My Transaction list contains:
	 	 I am transaction (f693990b4ba97ffa45974d842489e70d62b887e8) giving 4 $ from node 1 to node 0
	 	 I am transaction (52775aa21764f8c923c71c3aab103ac49444697c) giving 5 $ from node 1 to node 4
	 I am block with index 5
	 My Transaction list contains:
	 	 I am transaction (72f01b7c9ccea94888b00ed9ecaafe6d4ccb3eef) giving 6 $ from node 1 to node 3
	 	 I am transaction (1077a03e809bd5e682b27629a21afe6f8ade4df4) giving 7 $ from node 1 to node 2
	 I am block with index 6
	 My Transaction list contains:
	 	 I am transaction (0ad25cbffd27da14df38a4ae2aaf87cea69eb18d) giving 8 $ from node 1 to node 2
	 	 I am transaction (9970a5c0a373b7858e01a02a59859ad880278031) giving 9 $ from node 1 to node 0
	 I am block with index 7
	 My Transaction list contains:
	 	 I am transaction (1798cccfb048481cb904b2a0d7343f90941b9953) giving 1 $ from node 2 to node 4
	 	 I am transaction (4592016452dc7215913bea7029f2a6ff0c3cb2bb) giving 2 $ from node 2 to node 3
	 I am block with index 8
	 My Transaction list contains:
	 	 I am transaction (22b1776df3cd11faed623a33f0143d0497ed9af4) giving 3 $ from node 2 to node 0
	 	 I am transaction (8c2bd3d8acb1610a994d972003f85122057739ff) giving 4 $ from node 2 to node 4
	 I am block with index 9
	 My Transaction list contains:
	 	 I am transaction (56446fd35cbd00ca5595ed583353bb1db2d24ae6) giving 5 $ from node 2 to node 3
	 	 I am transaction (46a285e3651b33571ea19c5757fd31059d404849) giving 6 $ from node 2 to node 1
	 I am block with index 10
	 My Transaction list contains:
	 	 I am transaction (5a8ec7c0f99f6fbc4f20fc36ac69a92693da7eb9) giving 10 $ from node 2 to node 3
	 	 I am transaction (2e8fea2a5a21fbe2154ea2614611acbfc6e2f5b4) giving 1 $ from node 3 to node 2
	 I am block with index 11
	 My Transaction list contains:
	 	 I am transaction (3322428951970e1239ed073957e252e02a565759) giving 2 $ from node 3 to node 4
	 	 I am transaction (133b7695dfbbbeebc068687462f272194c2c9db5) giving 3 $ from node 3 to node 0
	 I am block with index 12
	 My Transaction list contains:
	 	 I am transaction (843797a9e5d1b0854876dd99248dd83de25e2002) giving 4 $ from node 3 to node 2
	 	 I am transaction (fb1236aa94f4e55fe778d32084c98905f28c9acc) giving 5 $ from node 3 to node 1
	 I am block with index 13
	 My Transaction list contains:
	 	 I am transaction (cb51a507ab01cae351eeb41cb71892ff97da9b52) giving 6 $ from node 3 to node 2
	 	 I am transaction (f818497c1d6e70aa9ba133362cf3b6dff1ad3f27) giving 7 $ from node 3 to node 2
	 I am block with index 14
	 My Transaction list contains:
	 	 I am transaction (40d8b89699b0df367495facd9331e7258d5af681) giving 8 $ from node 3 to node 4
	 	 I am transaction (2bf363cfe5bbcb5719055fcbc2c373cf540b75cb) giving 9 $ from node 3 to node 4
	 I am block with index 15
	 My Transaction list contains:
	 	 I am transaction (2a4886fd71f36fce15eb0549944b297331a703a3) giving 10 $ from node 3 to node 0
	 	 I am transaction (b7a2e5451c10c5bda77757fb3263ec1e126adad1) giving 2 $ from node 4 to node 0


0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15

127.0.0.1 - - [23/Mar/2020 20:57:54] "POST /AddBlock HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:55] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:55] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:55] "GET /Chain HTTP/1.1" 200 -
RESOLVE conflicts chain updated
Old chain


Blockchain:
	 I am block with index 0
	 My Transaction list contains:
	 	 I am transaction (22638dedb224898aa6cae8cbd7cafb03ff303edc) giving 500 $ from node genesis to node 0
	 I am block with index 1
	 My Transaction list contains:
	 	 I am transaction (f3f596d61dfa65e51ff1c749ed8d9e39f4227f3a) giving 100 $ from node 0 to node 1
	 	 I am transaction (4d4366153409aaf2ea130d97affea9bf6c91c2bb) giving 100 $ from node 0 to node 2
	 I am block with index 2
	 My Transaction list contains:
	 	 I am transaction (01662993795fb5fd8093c5eb4414af9516606e8e) giving 100 $ from node 0 to node 3
	 	 I am transaction (c41568a85d921ed060a5f30a8ec96b7f255fec7e) giving 100 $ from node 0 to node 4
	 I am block with index 3
	 My Transaction list contains:
	 	 I am transaction (e3179905507f5ad52fc3922bfcfd435f3e8e4c53) giving 2 $ from node 1 to node 0
	 	 I am transaction (6b03130364cdbc9e6eb53eec293ac2168eae92e8) giving 3 $ from node 1 to node 3
	 I am block with index 4
	 My Transaction list contains:
	 	 I am transaction (f693990b4ba97ffa45974d842489e70d62b887e8) giving 4 $ from node 1 to node 0
	 	 I am transaction (52775aa21764f8c923c71c3aab103ac49444697c) giving 5 $ from node 1 to node 4
	 I am block with index 5
	 My Transaction list contains:
	 	 I am transaction (72f01b7c9ccea94888b00ed9ecaafe6d4ccb3eef) giving 6 $ from node 1 to node 3
	 	 I am transaction (1077a03e809bd5e682b27629a21afe6f8ade4df4) giving 7 $ from node 1 to node 2
	 I am block with index 6
	 My Transaction list contains:
	 	 I am transaction (0ad25cbffd27da14df38a4ae2aaf87cea69eb18d) giving 8 $ from node 1 to node 2
	 	 I am transaction (9970a5c0a373b7858e01a02a59859ad880278031) giving 9 $ from node 1 to node 0
	 I am block with index 7
	 My Transaction list contains:
	 	 I am transaction (1798cccfb048481cb904b2a0d7343f90941b9953) giving 1 $ from node 2 to node 4
	 	 I am transaction (4592016452dc7215913bea7029f2a6ff0c3cb2bb) giving 2 $ from node 2 to node 3
	 I am block with index 8
	 My Transaction list contains:
	 	 I am transaction (22b1776df3cd11faed623a33f0143d0497ed9af4) giving 3 $ from node 2 to node 0
	 	 I am transaction (8c2bd3d8acb1610a994d972003f85122057739ff) giving 4 $ from node 2 to node 4
	 I am block with index 9
	 My Transaction list contains:
	 	 I am transaction (56446fd35cbd00ca5595ed583353bb1db2d24ae6) giving 5 $ from node 2 to node 3
	 	 I am transaction (46a285e3651b33571ea19c5757fd31059d404849) giving 6 $ from node 2 to node 1
	 I am block with index 10
	 My Transaction list contains:
	 	 I am transaction (5a8ec7c0f99f6fbc4f20fc36ac69a92693da7eb9) giving 10 $ from node 2 to node 3
	 	 I am transaction (2e8fea2a5a21fbe2154ea2614611acbfc6e2f5b4) giving 1 $ from node 3 to node 2
	 I am block with index 11
	 My Transaction list contains:
	 	 I am transaction (3322428951970e1239ed073957e252e02a565759) giving 2 $ from node 3 to node 4
	 	 I am transaction (133b7695dfbbbeebc068687462f272194c2c9db5) giving 3 $ from node 3 to node 0
	 I am block with index 12
	 My Transaction list contains:
	 	 I am transaction (843797a9e5d1b0854876dd99248dd83de25e2002) giving 4 $ from node 3 to node 2
	 	 I am transaction (fb1236aa94f4e55fe778d32084c98905f28c9acc) giving 5 $ from node 3 to node 1
	 I am block with index 13
	 My Transaction list contains:
	 	 I am transaction (cb51a507ab01cae351eeb41cb71892ff97da9b52) giving 6 $ from node 3 to node 2
	 	 I am transaction (f818497c1d6e70aa9ba133362cf3b6dff1ad3f27) giving 7 $ from node 3 to node 2
	 I am block with index 14
	 My Transaction list contains:
	 	 I am transaction (40d8b89699b0df367495facd9331e7258d5af681) giving 8 $ from node 3 to node 4
	 	 I am transaction (2bf363cfe5bbcb5719055fcbc2c373cf540b75cb) giving 9 $ from node 3 to node 4
	 I am block with index 15
	 My Transaction list contains:
	 	 I am transaction (2a4886fd71f36fce15eb0549944b297331a703a3) giving 10 $ from node 3 to node 0
	 	 I am transaction (b7a2e5451c10c5bda77757fb3263ec1e126adad1) giving 2 $ from node 4 to node 0


0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15

New Chain


Blockchain:
	 I am block with index 0
	 My Transaction list contains:
	 	 I am transaction (22638dedb224898aa6cae8cbd7cafb03ff303edc) giving 500 $ from node genesis to node 0
	 I am block with index 1
	 My Transaction list contains:
	 	 I am transaction (f3f596d61dfa65e51ff1c749ed8d9e39f4227f3a) giving 100 $ from node 0 to node 1
	 	 I am transaction (4d4366153409aaf2ea130d97affea9bf6c91c2bb) giving 100 $ from node 0 to node 2
	 I am block with index 2
	 My Transaction list contains:
	 	 I am transaction (01662993795fb5fd8093c5eb4414af9516606e8e) giving 100 $ from node 0 to node 3
	 	 I am transaction (c41568a85d921ed060a5f30a8ec96b7f255fec7e) giving 100 $ from node 0 to node 4
	 I am block with index 3
	 My Transaction list contains:
	 	 I am transaction (e3179905507f5ad52fc3922bfcfd435f3e8e4c53) giving 2 $ from node 1 to node 0
	 	 I am transaction (6b03130364cdbc9e6eb53eec293ac2168eae92e8) giving 3 $ from node 1 to node 3
	 I am block with index 4
	 My Transaction list contains:
	 	 I am transaction (f693990b4ba97ffa45974d842489e70d62b887e8) giving 4 $ from node 1 to node 0
	 	 I am transaction (52775aa21764f8c923c71c3aab103ac49444697c) giving 5 $ from node 1 to node 4
	 I am block with index 5
	 My Transaction list contains:
	 	 I am transaction (72f01b7c9ccea94888b00ed9ecaafe6d4ccb3eef) giving 6 $ from node 1 to node 3
	 	 I am transaction (1077a03e809bd5e682b27629a21afe6f8ade4df4) giving 7 $ from node 1 to node 2
	 I am block with index 6
	 My Transaction list contains:
	 	 I am transaction (0ad25cbffd27da14df38a4ae2aaf87cea69eb18d) giving 8 $ from node 1 to node 2
	 	 I am transaction (9970a5c0a373b7858e01a02a59859ad880278031) giving 9 $ from node 1 to node 0
	 I am block with index 7
	 My Transaction list contains:
	 	 I am transaction (1798cccfb048481cb904b2a0d7343f90941b9953) giving 1 $ from node 2 to node 4
	 	 I am transaction (4592016452dc7215913bea7029f2a6ff0c3cb2bb) giving 2 $ from node 2 to node 3
	 I am block with index 8
	 My Transaction list contains:
	 	 I am transaction (22b1776df3cd11faed623a33f0143d0497ed9af4) giving 3 $ from node 2 to node 0
	 	 I am transaction (8c2bd3d8acb1610a994d972003f85122057739ff) giving 4 $ from node 2 to node 4
	 I am block with index 9
	 My Transaction list contains:
	 	 I am transaction (56446fd35cbd00ca5595ed583353bb1db2d24ae6) giving 5 $ from node 2 to node 3
	 	 I am transaction (46a285e3651b33571ea19c5757fd31059d404849) giving 6 $ from node 2 to node 1
	 I am block with index 10
	 My Transaction list contains:
	 	 I am transaction (5a8ec7c0f99f6fbc4f20fc36ac69a92693da7eb9) giving 10 $ from node 2 to node 3
	 	 I am transaction (2e8fea2a5a21fbe2154ea2614611acbfc6e2f5b4) giving 1 $ from node 3 to node 2
	 I am block with index 11
	 My Transaction list contains:
	 	 I am transaction (3322428951970e1239ed073957e252e02a565759) giving 2 $ from node 3 to node 4
	 	 I am transaction (133b7695dfbbbeebc068687462f272194c2c9db5) giving 3 $ from node 3 to node 0
	 I am block with index 12
	 My Transaction list contains:
	 	 I am transaction (843797a9e5d1b0854876dd99248dd83de25e2002) giving 4 $ from node 3 to node 2
	 	 I am transaction (fb1236aa94f4e55fe778d32084c98905f28c9acc) giving 5 $ from node 3 to node 1
	 I am block with index 13
	 My Transaction list contains:
	 	 I am transaction (cb51a507ab01cae351eeb41cb71892ff97da9b52) giving 6 $ from node 3 to node 2
	 	 I am transaction (f818497c1d6e70aa9ba133362cf3b6dff1ad3f27) giving 7 $ from node 3 to node 2
	 I am block with index 14
	 My Transaction list contains:
	 	 I am transaction (40d8b89699b0df367495facd9331e7258d5af681) giving 8 $ from node 3 to node 4
	 	 I am transaction (2bf363cfe5bbcb5719055fcbc2c373cf540b75cb) giving 9 $ from node 3 to node 4
	 I am block with index 15
	 My Transaction list contains:
	 	 I am transaction (2a4886fd71f36fce15eb0549944b297331a703a3) giving 10 $ from node 3 to node 0
	 	 I am transaction (b7a2e5451c10c5bda77757fb3263ec1e126adad1) giving 2 $ from node 4 to node 0


0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15

old curr
	 I am block with index 16
	 My Transaction list contains:
new curr
	 I am block with index 16
	 My Transaction list contains:
127.0.0.1 - - [23/Mar/2020 20:57:55] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:55] "POST /AddBlock HTTP/1.1" 200 -
RESOLVE conflicts chain updated
Old chain


Blockchain:
	 I am block with index 0
	 My Transaction list contains:
	 	 I am transaction (22638dedb224898aa6cae8cbd7cafb03ff303edc) giving 500 $ from node genesis to node 0
	 I am block with index 1
	 My Transaction list contains:
	 	 I am transaction (f3f596d61dfa65e51ff1c749ed8d9e39f4227f3a) giving 100 $ from node 0 to node 1
	 	 I am transaction (4d4366153409aaf2ea130d97affea9bf6c91c2bb) giving 100 $ from node 0 to node 2
	 I am block with index 2
	 My Transaction list contains:
	 	 I am transaction (01662993795fb5fd8093c5eb4414af9516606e8e) giving 100 $ from node 0 to node 3
	 	 I am transaction (c41568a85d921ed060a5f30a8ec96b7f255fec7e) giving 100 $ from node 0 to node 4
	 I am block with index 3
	 My Transaction list contains:
	 	 I am transaction (e3179905507f5ad52fc3922bfcfd435f3e8e4c53) giving 2 $ from node 1 to node 0
	 	 I am transaction (6b03130364cdbc9e6eb53eec293ac2168eae92e8) giving 3 $ from node 1 to node 3
	 I am block with index 4
	 My Transaction list contains:
	 	 I am transaction (f693990b4ba97ffa45974d842489e70d62b887e8) giving 4 $ from node 1 to node 0
	 	 I am transaction (52775aa21764f8c923c71c3aab103ac49444697c) giving 5 $ from node 1 to node 4
	 I am block with index 5
	 My Transaction list contains:
	 	 I am transaction (72f01b7c9ccea94888b00ed9ecaafe6d4ccb3eef) giving 6 $ from node 1 to node 3
	 	 I am transaction (1077a03e809bd5e682b27629a21afe6f8ade4df4) giving 7 $ from node 1 to node 2
	 I am block with index 6
	 My Transaction list contains:
	 	 I am transaction (0ad25cbffd27da14df38a4ae2aaf87cea69eb18d) giving 8 $ from node 1 to node 2
	 	 I am transaction (9970a5c0a373b7858e01a02a59859ad880278031) giving 9 $ from node 1 to node 0
	 I am block with index 7
	 My Transaction list contains:
	 	 I am transaction (1798cccfb048481cb904b2a0d7343f90941b9953) giving 1 $ from node 2 to node 4
	 	 I am transaction (4592016452dc7215913bea7029f2a6ff0c3cb2bb) giving 2 $ from node 2 to node 3
	 I am block with index 8
	 My Transaction list contains:
	 	 I am transaction (22b1776df3cd11faed623a33f0143d0497ed9af4) giving 3 $ from node 2 to node 0
RESOLVE conflicts chain updated
	 	 I am transaction (8c2bd3d8acb1610a994d972003f85122057739ff) giving 4 $ from node 2 to node 4
	 I am block with index 9
	 My Transaction list contains:
	 	 I am transaction (56446fd35cbd00ca5595ed583353bb1db2d24ae6) giving 5 $ from node 2 to node 3
	 	 I am transaction (46a285e3651b33571ea19c5757fd31059d404849) giving 6 $ from node 2 to node 1
	 I am block with index 10
	 My Transaction list contains:
	 	 I am transaction (5a8ec7c0f99f6fbc4f20fc36ac69a92693da7eb9) giving 10 $ from node 2 to node 3
	 	 I am transaction (2e8fea2a5a21fbe2154ea2614611acbfc6e2f5b4) giving 1 $ from node 3 to node 2
	 I am block with index 11
	 My Transaction list contains:
	 	 I am transaction (3322428951970e1239ed073957e252e02a565759) giving 2 $ from node 3 to node 4
	 	 I am transaction (133b7695dfbbbeebc068687462f272194c2c9db5) giving 3 $ from node 3 to node 0
	 I am block with index 12
	 My Transaction list contains:
	 	 I am transaction (843797a9e5d1b0854876dd99248dd83de25e2002) giving 4 $ from node 3 to node 2
	 	 I am transaction (fb1236aa94f4e55fe778d32084c98905f28c9acc) giving 5 $ from node 3 to node 1
	 I am block with index 13
	 My Transaction list contains:
127.0.0.1 - - [23/Mar/2020 20:57:56] "GET /Chain HTTP/1.1" 200 -
	 	 I am transaction (cb51a507ab01cae351eeb41cb71892ff97da9b52) giving 6 $ from node 3 to node 2
	 	 I am transaction (f818497c1d6e70aa9ba133362cf3b6dff1ad3f27) giving 7 $ from node 3 to node 2
	 I am block with index 14
	 My Transaction list contains:
	 	 I am transaction (40d8b89699b0df367495facd9331e7258d5af681) giving 8 $ from node 3 to node 4
127.0.0.1 - - [23/Mar/2020 20:57:56] "GET /Chain HTTP/1.1" 200 -
	 	 I am transaction (2bf363cfe5bbcb5719055fcbc2c373cf540b75cb) giving 9 $ from node 3 to node 4
	 I am block with index 15
	 My Transaction list contains:
	 	 I am transaction (2a4886fd71f36fce15eb0549944b297331a703a3) giving 10 $ from node 3 to node 0
	 	 I am transaction (b7a2e5451c10c5bda77757fb3263ec1e126adad1) giving 2 $ from node 4 to node 0


0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
127.0.0.1 - - [23/Mar/2020 20:57:56] "GET /Chain HTTP/1.1" 200 -

New Chain


Blockchain:
	 I am block with index 0
	 My Transaction list contains:
	 	 I am transaction (22638dedb224898aa6cae8cbd7cafb03ff303edc) giving 500 $ from node genesis to node 0
	 I am block with index 1
	 My Transaction list contains:
	 	 I am transaction (f3f596d61dfa65e51ff1c749ed8d9e39f4227f3a) giving 100 $ from node 0 to node 1
	 	 I am transaction (4d4366153409aaf2ea130d97affea9bf6c91c2bb) giving 100 $ from node 0 to node 2
	 I am block with index 2
	 My Transaction list contains:
	 	 I am transaction (01662993795fb5fd8093c5eb4414af9516606e8e) giving 100 $ from node 0 to node 3
	 	 I am transaction (c41568a85d921ed060a5f30a8ec96b7f255fec7e) giving 100 $ from node 0 to node 4
	 I am block with index 3
	 My Transaction list contains:
	 	 I am transaction (e3179905507f5ad52fc3922bfcfd435f3e8e4c53) giving 2 $ from node 1 to node 0
	 	 I am transaction (6b03130364cdbc9e6eb53eec293ac2168eae92e8) giving 3 $ from node 1 to node 3
	 I am block with index 4
	 My Transaction list contains:
	 	 I am transaction (f693990b4ba97ffa45974d842489e70d62b887e8) giving 4 $ from node 1 to node 0
	 	 I am transaction (52775aa21764f8c923c71c3aab103ac49444697c) giving 5 $ from node 1 to node 4
	 I am block with index 5
	 My Transaction list contains:
	 	 I am transaction (72f01b7c9ccea94888b00ed9ecaafe6d4ccb3eef) giving 6 $ from node 1 to node 3
	 	 I am transaction (1077a03e809bd5e682b27629a21afe6f8ade4df4) giving 7 $ from node 1 to node 2
	 I am block with index 6
	 My Transaction list contains:
	 	 I am transaction (0ad25cbffd27da14df38a4ae2aaf87cea69eb18d) giving 8 $ from node 1 to node 2
	 	 I am transaction (9970a5c0a373b7858e01a02a59859ad880278031) giving 9 $ from node 1 to node 0
	 I am block with index 7
	 My Transaction list contains:
	 	 I am transaction (1798cccfb048481cb904b2a0d7343f90941b9953) giving 1 $ from node 2 to node 4
	 	 I am transaction (4592016452dc7215913bea7029f2a6ff0c3cb2bb) giving 2 $ from node 2 to node 3
	 I am block with index 8
	 My Transaction list contains:
	 	 I am transaction (22b1776df3cd11faed623a33f0143d0497ed9af4) giving 3 $ from node 2 to node 0
	 	 I am transaction (8c2bd3d8acb1610a994d972003f85122057739ff) giving 4 $ from node 2 to node 4
	 I am block with index 9
	 My Transaction list contains:
	 	 I am transaction (56446fd35cbd00ca5595ed583353bb1db2d24ae6) giving 5 $ from node 2 to node 3
	 	 I am transaction (46a285e3651b33571ea19c5757fd31059d404849) giving 6 $ from node 2 to node 1
	 I am block with index 10
	 My Transaction list contains:
	 	 I am transaction (5a8ec7c0f99f6fbc4f20fc36ac69a92693da7eb9) giving 10 $ from node 2 to node 3
	 	 I am transaction (2e8fea2a5a21fbe2154ea2614611acbfc6e2f5b4) giving 1 $ from node 3 to node 2
	 I am block with index 11
	 My Transaction list contains:
	 	 I am transaction (3322428951970e1239ed073957e252e02a565759) giving 2 $ from node 3 to node 4
	 	 I am transaction (133b7695dfbbbeebc068687462f272194c2c9db5) giving 3 $ from node 3 to node 0
	 I am block with index 12
	 My Transaction list contains:
	 	 I am transaction (843797a9e5d1b0854876dd99248dd83de25e2002) giving 4 $ from node 3 to node 2
	 	 I am transaction (fb1236aa94f4e55fe778d32084c98905f28c9acc) giving 5 $ from node 3 to node 1
	 I am block with index 13
	 My Transaction list contains:
	 	 I am transaction (cb51a507ab01cae351eeb41cb71892ff97da9b52) giving 6 $ from node 3 to node 2
	 	 I am transaction (f818497c1d6e70aa9ba133362cf3b6dff1ad3f27) giving 7 $ from node 3 to node 2
	 I am block with index 14
	 My Transaction list contains:
	 	 I am transaction (40d8b89699b0df367495facd9331e7258d5af681) giving 8 $ from node 3 to node 4
	 	 I am transaction (2bf363cfe5bbcb5719055fcbc2c373cf540b75cb) giving 9 $ from node 3 to node 4
	 I am block with index 15
	 My Transaction list contains:
	 	 I am transaction (2a4886fd71f36fce15eb0549944b297331a703a3) giving 10 $ from node 3 to node 0
	 	 I am transaction (b7a2e5451c10c5bda77757fb3263ec1e126adad1) giving 2 $ from node 4 to node 0
	 I am block with index 16
	 My Transaction list contains:
	 	 I am transaction (2790d441348fe56b4e5bf9dd13cededf4b2cfadb) giving 1 $ from node 4 to node 3
	 	 I am transaction (83cbee64c7ec2accff282f6a5b9a5a83974156e7) giving 3 $ from node 4 to node 1


0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16

old curr
	 I am block with index 16
	 My Transaction list contains:
127.0.0.1 - - [23/Mar/2020 20:57:56] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:56] "GET /Chain HTTP/1.1" 200 -
Validate own block
new curr
	 I am block with index 16
	 My Transaction list contains:
127.0.0.1 - - [23/Mar/2020 20:57:56] "POST /AddBlock HTTP/1.1" 200 -
Validating Transaction
127.0.0.1 - - [23/Mar/2020 20:57:56] "GET /Chain HTTP/1.1" 200 -
	 	 I am transaction (c25ebfe18d25e4823bef98414663c8067c9bdb4d) giving 7 $ from node 4 to node 0
Result True
Trani c25ebfe18d25e4823bef98414663c8067c9bdb4d
Validating Transaction
127.0.0.1 - - [23/Mar/2020 20:57:56] "POST /AddBlock HTTP/1.1" 200 -
	 I am block with index 16
	 	 I am transaction (35a844537a4a84d6983fc3e834cd5f9391d0d8fa) giving 8 $ from node 4 to node 3
	 My Transaction list contains:
False
Result True
Done
127.0.0.1 - - [23/Mar/2020 20:57:56] "POST /ValidateTransaction HTTP/1.1" 200 -
False
1 2
127.0.0.1 - - [23/Mar/2020 20:57:56] "POST /AddBlock HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:56] "GET /Chain HTTP/1.1" 200 -
Trani 35a844537a4a84d6983fc3e834cd5f9391d0d8fa
	 I am block with index 16
127.0.0.1 - - [23/Mar/2020 20:57:56] "POST /ValidateTransaction HTTP/1.1" 200 -
	 My Transaction list contains:
	 	 I am transaction (c25ebfe18d25e4823bef98414663c8067c9bdb4d) giving 7 $ from node 4 to node 0
127.0.0.1 - - [23/Mar/2020 20:57:56] "GET /Chain HTTP/1.1" 200 -
False
False
2 2
AAAA
Old chain


Blockchain:
	 I am block with index 0
	 My Transaction list contains:
	 	 I am transaction (22638dedb224898aa6cae8cbd7cafb03ff303edc) giving 500 $ from node genesis to node 0
	 I am block with index 1
	 My Transaction list contains:
	 	 I am transaction (f3f596d61dfa65e51ff1c749ed8d9e39f4227f3a) giving 100 $ from node 0 to node 1
	 	 I am transaction (4d4366153409aaf2ea130d97affea9bf6c91c2bb) giving 100 $ from node 0 to node 2
	 I am block with index 2
	 My Transaction list contains:
127.0.0.1 - - [23/Mar/2020 20:57:57] "POST /AddBlock HTTP/1.1" 200 -
	 	 I am transaction (01662993795fb5fd8093c5eb4414af9516606e8e) giving 100 $ from node 0 to node 3
	 	 I am transaction (c41568a85d921ed060a5f30a8ec96b7f255fec7e) giving 100 $ from node 0 to node 4
	 I am block with index 3
	 My Transaction list contains:
	 	 I am transaction (e3179905507f5ad52fc3922bfcfd435f3e8e4c53) giving 2 $ from node 1 to node 0
	 	 I am transaction (6b03130364cdbc9e6eb53eec293ac2168eae92e8) giving 3 $ from node 1 to node 3
	 I am block with index 4
Validate own block
	 My Transaction list contains:
	 	 I am transaction (f693990b4ba97ffa45974d842489e70d62b887e8) giving 4 $ from node 1 to node 0
127.0.0.1 - - [23/Mar/2020 20:57:57] "GET /Chain HTTP/1.1" 200 -
Validating Transaction
	 	 I am transaction (52775aa21764f8c923c71c3aab103ac49444697c) giving 5 $ from node 1 to node 4
	 I am block with index 5
127.0.0.1 - - [23/Mar/2020 20:57:57] "GET /Chain HTTP/1.1" 200 -
	 My Transaction list contains:
	 	 I am transaction (f7fb9bb4fe17806ee1683103aeff7e2cd58c87ae) giving 9 $ from node 4 to node 3
Result True
127.0.0.1 - - [23/Mar/2020 20:57:57] "GET /Chain HTTP/1.1" 200 -
	 	 I am transaction (72f01b7c9ccea94888b00ed9ecaafe6d4ccb3eef) giving 6 $ from node 1 to node 3
127.0.0.1 - - [23/Mar/2020 20:57:57] "GET /Chain HTTP/1.1" 200 -
Trani f7fb9bb4fe17806ee1683103aeff7e2cd58c87ae
127.0.0.1 - - [23/Mar/2020 20:57:57] "POST /AddBlock HTTP/1.1" 200 -
Bootstrap Reading input transactions
	 I am block with index 17
127.0.0.1 - - [23/Mar/2020 20:57:57] "GET /Chain HTTP/1.1" 200 -
	 	 I am transaction (1077a03e809bd5e682b27629a21afe6f8ade4df4) giving 7 $ from node 1 to node 2
Done
	 My Transaction list contains:
127.0.0.1 - - [23/Mar/2020 20:57:57] "POST /ValidateTransaction HTTP/1.1" 200 -
	 I am block with index 6
127.0.0.1 - - [23/Mar/2020 20:57:57] "GET /Chain HTTP/1.1" 200 -
Validating Transaction
False
127.0.0.1 - - [23/Mar/2020 20:57:57] "GET /Chain HTTP/1.1" 200 -
	 	 I am transaction (253b81fd81576b0993973a2eeda532d90000f37a) giving 10 $ from node 4 to node 0
127.0.0.1 - - [23/Mar/2020 20:57:57] "GET /Chain HTTP/1.1" 200 -
False
	 My Transaction list contains:
127.0.0.1 - - [23/Mar/2020 20:57:57] "GET /Chain HTTP/1.1" 200 -
Result True
127.0.0.1 - - [23/Mar/2020 20:57:57] "GET /Chain HTTP/1.1" 200 -
1 2
127.0.0.1 - - [23/Mar/2020 20:57:57] "POST /ValidateTransaction HTTP/1.1" 200 -
	 	 I am transaction (0ad25cbffd27da14df38a4ae2aaf87cea69eb18d) giving 8 $ from node 1 to node 2
	 	 I am transaction (9970a5c0a373b7858e01a02a59859ad880278031) giving 9 $ from node 1 to node 0
	 I am block with index 7
	 My Transaction list contains:
	 	 I am transaction (1798cccfb048481cb904b2a0d7343f90941b9953) giving 1 $ from node 2 to node 4
	 	 I am transaction (4592016452dc7215913bea7029f2a6ff0c3cb2bb) giving 2 $ from node 2 to node 3
	 I am block with index 8
	 My Transaction list contains:
Validating Transaction
127.0.0.1 - - [23/Mar/2020 20:57:57] "GET /Chain HTTP/1.1" 200 -
Trani 253b81fd81576b0993973a2eeda532d90000f37a
	 I am block with index 17
127.0.0.1 - - [23/Mar/2020 20:57:57] "POST /AddBlock HTTP/1.1" 200 -
	 	 I am transaction (22b1776df3cd11faed623a33f0143d0497ed9af4) giving 3 $ from node 2 to node 0
	 	 I am transaction (8c2bd3d8acb1610a994d972003f85122057739ff) giving 4 $ from node 2 to node 4
127.0.0.1 - - [23/Mar/2020 20:57:58] "GET /Chain HTTP/1.1" 200 -
	 My Transaction list contains:
	 I am block with index 9
	 	 I am transaction (f7fb9bb4fe17806ee1683103aeff7e2cd58c87ae) giving 9 $ from node 4 to node 3
127.0.0.1 - - [23/Mar/2020 20:57:58] "GET /Chain HTTP/1.1" 200 -
	 My Transaction list contains:
127.0.0.1 - - [23/Mar/2020 20:57:58] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:58] "POST /AddBlock HTTP/1.1" 200 -
False
	 	 I am transaction (56446fd35cbd00ca5595ed583353bb1db2d24ae6) giving 5 $ from node 2 to node 3
False
127.0.0.1 - - [23/Mar/2020 20:57:58] "GET /Chain HTTP/1.1" 200 -
	 	 I am transaction (46a285e3651b33571ea19c5757fd31059d404849) giving 6 $ from node 2 to node 1
	 I am block with index 10
2 2
127.0.0.1 - - [23/Mar/2020 20:57:58] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:58] "GET /Chain HTTP/1.1" 200 -
	 	 I am transaction (19c9492d1e50dee759ed6be007407d261f92b668) giving 1 $ from node 0 to node 1
	 My Transaction list contains:
Result True
	 	 I am transaction (5a8ec7c0f99f6fbc4f20fc36ac69a92693da7eb9) giving 10 $ from node 2 to node 3
	 	 I am transaction (2e8fea2a5a21fbe2154ea2614611acbfc6e2f5b4) giving 1 $ from node 3 to node 2
AAAA
	 I am block with index 11
	 My Transaction list contains:
	 	 I am transaction (3322428951970e1239ed073957e252e02a565759) giving 2 $ from node 3 to node 4
	 	 I am transaction (133b7695dfbbbeebc068687462f272194c2c9db5) giving 3 $ from node 3 to node 0
	 I am block with index 12
	 My Transaction list contains:
Trani 19c9492d1e50dee759ed6be007407d261f92b668
	 	 I am transaction (843797a9e5d1b0854876dd99248dd83de25e2002) giving 4 $ from node 3 to node 2
	 	 I am transaction (fb1236aa94f4e55fe778d32084c98905f28c9acc) giving 5 $ from node 3 to node 1
	 I am block with index 13
	 My Transaction list contains:
	 	 I am transaction (cb51a507ab01cae351eeb41cb71892ff97da9b52) giving 6 $ from node 3 to node 2
	 	 I am transaction (f818497c1d6e70aa9ba133362cf3b6dff1ad3f27) giving 7 $ from node 3 to node 2
	 I am block with index 14
	 My Transaction list contains:
	 	 I am transaction (40d8b89699b0df367495facd9331e7258d5af681) giving 8 $ from node 3 to node 4
	 	 I am transaction (2bf363cfe5bbcb5719055fcbc2c373cf540b75cb) giving 9 $ from node 3 to node 4
	 I am block with index 15
	 My Transaction list contains:
	 	 I am transaction (2a4886fd71f36fce15eb0549944b297331a703a3) giving 10 $ from node 3 to node 0
	 I am block with index 17
	 	 I am transaction (b7a2e5451c10c5bda77757fb3263ec1e126adad1) giving 2 $ from node 4 to node 0


0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15

New Chain


Blockchain:
	 I am block with index 0
	 My Transaction list contains:
	 	 I am transaction (22638dedb224898aa6cae8cbd7cafb03ff303edc) giving 500 $ from node genesis to node 0
	 I am block with index 1
	 My Transaction list contains:
	 	 I am transaction (f3f596d61dfa65e51ff1c749ed8d9e39f4227f3a) giving 100 $ from node 0 to node 1
	 	 I am transaction (4d4366153409aaf2ea130d97affea9bf6c91c2bb) giving 100 $ from node 0 to node 2
	 My Transaction list contains:
	 I am block with index 2
	 	 I am transaction (f7fb9bb4fe17806ee1683103aeff7e2cd58c87ae) giving 9 $ from node 4 to node 3
	 	 I am transaction (253b81fd81576b0993973a2eeda532d90000f37a) giving 10 $ from node 4 to node 0
	 My Transaction list contains:
	 	 I am transaction (01662993795fb5fd8093c5eb4414af9516606e8e) giving 100 $ from node 0 to node 3
	 	 I am transaction (c41568a85d921ed060a5f30a8ec96b7f255fec7e) giving 100 $ from node 0 to node 4
	 I am block with index 3
	 My Transaction list contains:
	 	 I am transaction (e3179905507f5ad52fc3922bfcfd435f3e8e4c53) giving 2 $ from node 1 to node 0
	 	 I am transaction (6b03130364cdbc9e6eb53eec293ac2168eae92e8) giving 3 $ from node 1 to node 3
	 I am block with index 4
	 My Transaction list contains:
	 	 I am transaction (f693990b4ba97ffa45974d842489e70d62b887e8) giving 4 $ from node 1 to node 0
	 	 I am transaction (52775aa21764f8c923c71c3aab103ac49444697c) giving 5 $ from node 1 to node 4
	 I am block with index 5
	 My Transaction list contains:
	 	 I am transaction (72f01b7c9ccea94888b00ed9ecaafe6d4ccb3eef) giving 6 $ from node 1 to node 3
	 	 I am transaction (1077a03e809bd5e682b27629a21afe6f8ade4df4) giving 7 $ from node 1 to node 2
	 I am block with index 6
	 My Transaction list contains:
	 	 I am transaction (0ad25cbffd27da14df38a4ae2aaf87cea69eb18d) giving 8 $ from node 1 to node 2
	 	 I am transaction (9970a5c0a373b7858e01a02a59859ad880278031) giving 9 $ from node 1 to node 0
	 I am block with index 7
	 My Transaction list contains:
	 	 I am transaction (1798cccfb048481cb904b2a0d7343f90941b9953) giving 1 $ from node 2 to node 4
	 	 I am transaction (4592016452dc7215913bea7029f2a6ff0c3cb2bb) giving 2 $ from node 2 to node 3
	 I am block with index 8
	 My Transaction list contains:
	 	 I am transaction (22b1776df3cd11faed623a33f0143d0497ed9af4) giving 3 $ from node 2 to node 0
	 	 I am transaction (8c2bd3d8acb1610a994d972003f85122057739ff) giving 4 $ from node 2 to node 4
	 I am block with index 9
	 My Transaction list contains:
	 	 I am transaction (56446fd35cbd00ca5595ed583353bb1db2d24ae6) giving 5 $ from node 2 to node 3
	 	 I am transaction (46a285e3651b33571ea19c5757fd31059d404849) giving 6 $ from node 2 to node 1
	 I am block with index 10
	 My Transaction list contains:
	 	 I am transaction (5a8ec7c0f99f6fbc4f20fc36ac69a92693da7eb9) giving 10 $ from node 2 to node 3
	 	 I am transaction (2e8fea2a5a21fbe2154ea2614611acbfc6e2f5b4) giving 1 $ from node 3 to node 2
	 I am block with index 11
	 My Transaction list contains:
	 	 I am transaction (3322428951970e1239ed073957e252e02a565759) giving 2 $ from node 3 to node 4
	 	 I am transaction (133b7695dfbbbeebc068687462f272194c2c9db5) giving 3 $ from node 3 to node 0
	 I am block with index 12
	 My Transaction list contains:
	 	 I am transaction (843797a9e5d1b0854876dd99248dd83de25e2002) giving 4 $ from node 3 to node 2
	 	 I am transaction (fb1236aa94f4e55fe778d32084c98905f28c9acc) giving 5 $ from node 3 to node 1
	 I am block with index 13
	 My Transaction list contains:
	 	 I am transaction (cb51a507ab01cae351eeb41cb71892ff97da9b52) giving 6 $ from node 3 to node 2
	 	 I am transaction (f818497c1d6e70aa9ba133362cf3b6dff1ad3f27) giving 7 $ from node 3 to node 2
	 I am block with index 14
	 My Transaction list contains:
	 	 I am transaction (40d8b89699b0df367495facd9331e7258d5af681) giving 8 $ from node 3 to node 4
	 	 I am transaction (2bf363cfe5bbcb5719055fcbc2c373cf540b75cb) giving 9 $ from node 3 to node 4
	 I am block with index 15
	 My Transaction list contains:
	 	 I am transaction (2a4886fd71f36fce15eb0549944b297331a703a3) giving 10 $ from node 3 to node 0
	 	 I am transaction (b7a2e5451c10c5bda77757fb3263ec1e126adad1) giving 2 $ from node 4 to node 0
	 I am block with index 16
	 My Transaction list contains:
	 	 I am transaction (2790d441348fe56b4e5bf9dd13cededf4b2cfadb) giving 1 $ from node 4 to node 3
	 	 I am transaction (83cbee64c7ec2accff282f6a5b9a5a83974156e7) giving 3 $ from node 4 to node 1


0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16

old curr
	 I am block with index 16
	 My Transaction list contains:
new curr
	 I am block with index 18
	 My Transaction list contains:
False
False
OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
127.0.0.1 - - [23/Mar/2020 20:57:58] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:58] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:59] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:59] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:59] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:59] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:59] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:57:59] "GET /Chain HTTP/1.1" 200 -
Validate own block
Block added to blockchain!
	 I am block with index 17
	 My Transaction list contains:
	 	 I am transaction (35a844537a4a84d6983fc3e834cd5f9391d0d8fa) giving 8 $ from node 4 to node 3
	 	 I am transaction (f7fb9bb4fe17806ee1683103aeff7e2cd58c87ae) giving 9 $ from node 4 to node 3
127.0.0.1 - - [23/Mar/2020 20:58:00] "POST /AddBlock HTTP/1.1" 200 -


Done
127.0.0.1 - - [23/Mar/2020 20:58:00] "POST /ValidateTransaction HTTP/1.1" 200 -
Blockchain:
	 I am block with index 0
	 My Transaction list contains:
	 	 I am transaction (22638dedb224898aa6cae8cbd7cafb03ff303edc) giving 500 $ from node genesis to node 0
	 I am block with index 1
	 My Transaction list contains:
	 	 I am transaction (f3f596d61dfa65e51ff1c749ed8d9e39f4227f3a) giving 100 $ from node 0 to node 1
	 	 I am transaction (4d4366153409aaf2ea130d97affea9bf6c91c2bb) giving 100 $ from node 0 to node 2
	 I am block with index 2
	 My Transaction list contains:
	 	 I am transaction (01662993795fb5fd8093c5eb4414af9516606e8e) giving 100 $ from node 0 to node 3
	 	 I am transaction (c41568a85d921ed060a5f30a8ec96b7f255fec7e) giving 100 $ from node 0 to node 4
	 I am block with index 3
	 My Transaction list contains:
	 	 I am transaction (e3179905507f5ad52fc3922bfcfd435f3e8e4c53) giving 2 $ from node 1 to node 0
	 	 I am transaction (6b03130364cdbc9e6eb53eec293ac2168eae92e8) giving 3 $ from node 1 to node 3
	 I am block with index 4
	 My Transaction list contains:
	 	 I am transaction (f693990b4ba97ffa45974d842489e70d62b887e8) giving 4 $ from node 1 to node 0
	 	 I am transaction (52775aa21764f8c923c71c3aab103ac49444697c) giving 5 $ from node 1 to node 4
	 I am block with index 5
	 My Transaction list contains:
	 	 I am transaction (72f01b7c9ccea94888b00ed9ecaafe6d4ccb3eef) giving 6 $ from node 1 to node 3
	 	 I am transaction (1077a03e809bd5e682b27629a21afe6f8ade4df4) giving 7 $ from node 1 to node 2
	 I am block with index 6
	 My Transaction list contains:
	 	 I am transaction (0ad25cbffd27da14df38a4ae2aaf87cea69eb18d) giving 8 $ from node 1 to node 2
	 	 I am transaction (9970a5c0a373b7858e01a02a59859ad880278031) giving 9 $ from node 1 to node 0
	 I am block with index 7
	 My Transaction list contains:
	 	 I am transaction (1798cccfb048481cb904b2a0d7343f90941b9953) giving 1 $ from node 2 to node 4
	 	 I am transaction (4592016452dc7215913bea7029f2a6ff0c3cb2bb) giving 2 $ from node 2 to node 3
	 I am block with index 8
	 My Transaction list contains:
	 	 I am transaction (22b1776df3cd11faed623a33f0143d0497ed9af4) giving 3 $ from node 2 to node 0
	 	 I am transaction (8c2bd3d8acb1610a994d972003f85122057739ff) giving 4 $ from node 2 to node 4
	 I am block with index 9
	 My Transaction list contains:
	 	 I am transaction (56446fd35cbd00ca5595ed583353bb1db2d24ae6) giving 5 $ from node 2 to node 3
	 	 I am transaction (46a285e3651b33571ea19c5757fd31059d404849) giving 6 $ from node 2 to node 1
	 I am block with index 10
	 My Transaction list contains:
	 	 I am transaction (5a8ec7c0f99f6fbc4f20fc36ac69a92693da7eb9) giving 10 $ from node 2 to node 3
	 	 I am transaction (2e8fea2a5a21fbe2154ea2614611acbfc6e2f5b4) giving 1 $ from node 3 to node 2
	 I am block with index 11
	 My Transaction list contains:
	 	 I am transaction (3322428951970e1239ed073957e252e02a565759) giving 2 $ from node 3 to node 4
	 	 I am transaction (133b7695dfbbbeebc068687462f272194c2c9db5) giving 3 $ from node 3 to node 0
	 I am block with index 12
	 My Transaction list contains:
	 	 I am transaction (843797a9e5d1b0854876dd99248dd83de25e2002) giving 4 $ from node 3 to node 2
	 	 I am transaction (fb1236aa94f4e55fe778d32084c98905f28c9acc) giving 5 $ from node 3 to node 1
	 I am block with index 13
	 My Transaction list contains:
	 	 I am transaction (cb51a507ab01cae351eeb41cb71892ff97da9b52) giving 6 $ from node 3 to node 2
	 	 I am transaction (f818497c1d6e70aa9ba133362cf3b6dff1ad3f27) giving 7 $ from node 3 to node 2
	 I am block with index 14
	 My Transaction list contains:
	 	 I am transaction (40d8b89699b0df367495facd9331e7258d5af681) giving 8 $ from node 3 to node 4
	 	 I am transaction (2bf363cfe5bbcb5719055fcbc2c373cf540b75cb) giving 9 $ from node 3 to node 4
	 I am block with index 15
	 My Transaction list contains:
	 	 I am transaction (2a4886fd71f36fce15eb0549944b297331a703a3) giving 10 $ from node 3 to node 0
	 	 I am transaction (b7a2e5451c10c5bda77757fb3263ec1e126adad1) giving 2 $ from node 4 to node 0
	 I am block with index 16
	 My Transaction list contains:
	 	 I am transaction (2790d441348fe56b4e5bf9dd13cededf4b2cfadb) giving 1 $ from node 4 to node 3
	 	 I am transaction (83cbee64c7ec2accff282f6a5b9a5a83974156e7) giving 3 $ from node 4 to node 1
	 I am block with index 17
	 My Transaction list contains:
	 	 I am transaction (35a844537a4a84d6983fc3e834cd5f9391d0d8fa) giving 8 $ from node 4 to node 3
	 	 I am transaction (f7fb9bb4fe17806ee1683103aeff7e2cd58c87ae) giving 9 $ from node 4 to node 3


0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17

127.0.0.1 - - [23/Mar/2020 20:58:00] "POST /AddBlock HTTP/1.1" 200 -
Created transaction
	 	 I am transaction (19c9492d1e50dee759ed6be007407d261f92b668) giving 1 $ from node 0 to node 1
127.0.0.1 - - [23/Mar/2020 20:58:00] "GET /Chain HTTP/1.1" 200 -
Validating Transaction
	 	 I am transaction (7d0cbf9b3fd2966c3f5cfb1fd3c0e7667bb8b889) giving 2 $ from node 0 to node 2
Result True
Trani 7d0cbf9b3fd2966c3f5cfb1fd3c0e7667bb8b889
	 I am block with index 18
	 My Transaction list contains:
False
False
RESOLVE conflicts chain updated
127.0.0.1 - - [23/Mar/2020 20:58:00] "GET /Chain HTTP/1.1" 200 -
1 2
127.0.0.1 - - [23/Mar/2020 20:58:00] "POST /ValidateTransaction HTTP/1.1" 200 -
Created transaction
	 	 I am transaction (7d0cbf9b3fd2966c3f5cfb1fd3c0e7667bb8b889) giving 2 $ from node 0 to node 2
Validate own block
127.0.0.1 - - [23/Mar/2020 20:58:00] "GET /Chain HTTP/1.1" 200 -
Validating Transaction
	 	 I am transaction (e0f458077590b9a9fdd7e0739dff6916b2defd34) giving 3 $ from node 0 to node 2
Result True
Trani e0f458077590b9a9fdd7e0739dff6916b2defd34
	 I am block with index 18
	 My Transaction list contains:
False
False
1 2
127.0.0.1 - - [23/Mar/2020 20:58:01] "POST /ValidateTransaction HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:58:01] "POST /AddBlock HTTP/1.1" 200 -
Created transaction
	 	 I am transaction (e0f458077590b9a9fdd7e0739dff6916b2defd34) giving 3 $ from node 0 to node 2
127.0.0.1 - - [23/Mar/2020 20:58:01] "POST /AddBlock HTTP/1.1" 200 -
Done
127.0.0.1 - - [23/Mar/2020 20:58:01] "POST /ValidateTransaction HTTP/1.1" 200 -
Validating Transaction
	 	 I am transaction (d8f2751ca2aef896681a413809adc11f2c099d23) giving 4 $ from node 0 to node 2
Result True
Trani d8f2751ca2aef896681a413809adc11f2c099d23
	 I am block with index 18
	 My Transaction list contains:
	 	 I am transaction (e0f458077590b9a9fdd7e0739dff6916b2defd34) giving 3 $ from node 0 to node 2
False
False
2 2
AAAA
127.0.0.1 - - [23/Mar/2020 20:58:01] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:58:01] "POST /AddBlock HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:58:01] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:58:01] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:58:01] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:58:02] "GET /Chain HTTP/1.1" 200 -
Old chain
127.0.0.1 - - [23/Mar/2020 20:58:02] "GET /Chain HTTP/1.1" 200 -


Blockchain:
	 I am block with index 0
	 My Transaction list contains:
	 	 I am transaction (22638dedb224898aa6cae8cbd7cafb03ff303edc) giving 500 $ from node genesis to node 0
	 I am block with index 1
	 My Transaction list contains:
	 	 I am transaction (f3f596d61dfa65e51ff1c749ed8d9e39f4227f3a) giving 100 $ from node 0 to node 1
	 	 I am transaction (4d4366153409aaf2ea130d97affea9bf6c91c2bb) giving 100 $ from node 0 to node 2
	 I am block with index 2
	 My Transaction list contains:
	 	 I am transaction (01662993795fb5fd8093c5eb4414af9516606e8e) giving 100 $ from node 0 to node 3
	 	 I am transaction (c41568a85d921ed060a5f30a8ec96b7f255fec7e) giving 100 $ from node 0 to node 4
	 I am block with index 3
	 My Transaction list contains:
	 	 I am transaction (e3179905507f5ad52fc3922bfcfd435f3e8e4c53) giving 2 $ from node 1 to node 0
	 	 I am transaction (6b03130364cdbc9e6eb53eec293ac2168eae92e8) giving 3 $ from node 1 to node 3
	 I am block with index 4
	 My Transaction list contains:
127.0.0.1 - - [23/Mar/2020 20:58:02] "GET /Chain HTTP/1.1" 200 -
	 	 I am transaction (f693990b4ba97ffa45974d842489e70d62b887e8) giving 4 $ from node 1 to node 0
	 	 I am transaction (52775aa21764f8c923c71c3aab103ac49444697c) giving 5 $ from node 1 to node 4
	 I am block with index 5
	 My Transaction list contains:
	 	 I am transaction (72f01b7c9ccea94888b00ed9ecaafe6d4ccb3eef) giving 6 $ from node 1 to node 3
	 	 I am transaction (1077a03e809bd5e682b27629a21afe6f8ade4df4) giving 7 $ from node 1 to node 2
127.0.0.1 - - [23/Mar/2020 20:58:02] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:58:02] "GET /Chain HTTP/1.1" 200 -
	 I am block with index 6
	 My Transaction list contains:
	 	 I am transaction (0ad25cbffd27da14df38a4ae2aaf87cea69eb18d) giving 8 $ from node 1 to node 2
	 	 I am transaction (9970a5c0a373b7858e01a02a59859ad880278031) giving 9 $ from node 1 to node 0
	 I am block with index 7
	 My Transaction list contains:
	 	 I am transaction (1798cccfb048481cb904b2a0d7343f90941b9953) giving 1 $ from node 2 to node 4
	 	 I am transaction (4592016452dc7215913bea7029f2a6ff0c3cb2bb) giving 2 $ from node 2 to node 3
	 I am block with index 8
	 My Transaction list contains:
	 	 I am transaction (22b1776df3cd11faed623a33f0143d0497ed9af4) giving 3 $ from node 2 to node 0
	 	 I am transaction (8c2bd3d8acb1610a994d972003f85122057739ff) giving 4 $ from node 2 to node 4
	 I am block with index 9
	 My Transaction list contains:
	 	 I am transaction (56446fd35cbd00ca5595ed583353bb1db2d24ae6) giving 5 $ from node 2 to node 3
	 	 I am transaction (46a285e3651b33571ea19c5757fd31059d404849) giving 6 $ from node 2 to node 1
	 I am block with index 10
127.0.0.1 - - [23/Mar/2020 20:58:02] "GET /Chain HTTP/1.1" 200 -
	 My Transaction list contains:
	 	 I am transaction (5a8ec7c0f99f6fbc4f20fc36ac69a92693da7eb9) giving 10 $ from node 2 to node 3
127.0.0.1 - - [23/Mar/2020 20:58:02] "GET /Chain HTTP/1.1" 200 -
	 	 I am transaction (2e8fea2a5a21fbe2154ea2614611acbfc6e2f5b4) giving 1 $ from node 3 to node 2
	 I am block with index 11
	 My Transaction list contains:
127.0.0.1 - - [23/Mar/2020 20:58:02] "GET /Chain HTTP/1.1" 200 -
	 	 I am transaction (3322428951970e1239ed073957e252e02a565759) giving 2 $ from node 3 to node 4
	 	 I am transaction (133b7695dfbbbeebc068687462f272194c2c9db5) giving 3 $ from node 3 to node 0
	 I am block with index 12
	 My Transaction list contains:
	 	 I am transaction (843797a9e5d1b0854876dd99248dd83de25e2002) giving 4 $ from node 3 to node 2
	 	 I am transaction (fb1236aa94f4e55fe778d32084c98905f28c9acc) giving 5 $ from node 3 to node 1
	 I am block with index 13
	 My Transaction list contains:
	 	 I am transaction (cb51a507ab01cae351eeb41cb71892ff97da9b52) giving 6 $ from node 3 to node 2
	 	 I am transaction (f818497c1d6e70aa9ba133362cf3b6dff1ad3f27) giving 7 $ from node 3 to node 2
	 I am block with index 14
127.0.0.1 - - [23/Mar/2020 20:58:02] "GET /Chain HTTP/1.1" 200 -
	 My Transaction list contains:
	 	 I am transaction (40d8b89699b0df367495facd9331e7258d5af681) giving 8 $ from node 3 to node 4
	 	 I am transaction (2bf363cfe5bbcb5719055fcbc2c373cf540b75cb) giving 9 $ from node 3 to node 4
	 I am block with index 15
	 My Transaction list contains:
	 	 I am transaction (2a4886fd71f36fce15eb0549944b297331a703a3) giving 10 $ from node 3 to node 0
	 	 I am transaction (b7a2e5451c10c5bda77757fb3263ec1e126adad1) giving 2 $ from node 4 to node 0
	 I am block with index 16
	 My Transaction list contains:
	 	 I am transaction (2790d441348fe56b4e5bf9dd13cededf4b2cfadb) giving 1 $ from node 4 to node 3
	 	 I am transaction (83cbee64c7ec2accff282f6a5b9a5a83974156e7) giving 3 $ from node 4 to node 1
	 I am block with index 17
	 My Transaction list contains:
	 	 I am transaction (35a844537a4a84d6983fc3e834cd5f9391d0d8fa) giving 8 $ from node 4 to node 3
	 	 I am transaction (f7fb9bb4fe17806ee1683103aeff7e2cd58c87ae) giving 9 $ from node 4 to node 3


0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17

New Chain


Blockchain:
	 I am block with index 0
	 My Transaction list contains:
	 	 I am transaction (22638dedb224898aa6cae8cbd7cafb03ff303edc) giving 500 $ from node genesis to node 0
	 I am block with index 1
	 My Transaction list contains:
	 	 I am transaction (f3f596d61dfa65e51ff1c749ed8d9e39f4227f3a) giving 100 $ from node 0 to node 1
	 	 I am transaction (4d4366153409aaf2ea130d97affea9bf6c91c2bb) giving 100 $ from node 0 to node 2
	 I am block with index 2
	 My Transaction list contains:
	 	 I am transaction (01662993795fb5fd8093c5eb4414af9516606e8e) giving 100 $ from node 0 to node 3
	 	 I am transaction (c41568a85d921ed060a5f30a8ec96b7f255fec7e) giving 100 $ from node 0 to node 4
	 I am block with index 3
	 My Transaction list contains:
	 	 I am transaction (e3179905507f5ad52fc3922bfcfd435f3e8e4c53) giving 2 $ from node 1 to node 0
	 	 I am transaction (6b03130364cdbc9e6eb53eec293ac2168eae92e8) giving 3 $ from node 1 to node 3
	 I am block with index 4
	 My Transaction list contains:
	 	 I am transaction (f693990b4ba97ffa45974d842489e70d62b887e8) giving 4 $ from node 1 to node 0
	 	 I am transaction (52775aa21764f8c923c71c3aab103ac49444697c) giving 5 $ from node 1 to node 4
	 I am block with index 5
	 My Transaction list contains:
	 	 I am transaction (72f01b7c9ccea94888b00ed9ecaafe6d4ccb3eef) giving 6 $ from node 1 to node 3
	 	 I am transaction (1077a03e809bd5e682b27629a21afe6f8ade4df4) giving 7 $ from node 1 to node 2
	 I am block with index 6
	 My Transaction list contains:
	 	 I am transaction (0ad25cbffd27da14df38a4ae2aaf87cea69eb18d) giving 8 $ from node 1 to node 2
	 	 I am transaction (9970a5c0a373b7858e01a02a59859ad880278031) giving 9 $ from node 1 to node 0
	 I am block with index 7
	 My Transaction list contains:
	 	 I am transaction (1798cccfb048481cb904b2a0d7343f90941b9953) giving 1 $ from node 2 to node 4
	 	 I am transaction (4592016452dc7215913bea7029f2a6ff0c3cb2bb) giving 2 $ from node 2 to node 3
	 I am block with index 8
	 My Transaction list contains:
	 	 I am transaction (22b1776df3cd11faed623a33f0143d0497ed9af4) giving 3 $ from node 2 to node 0
	 	 I am transaction (8c2bd3d8acb1610a994d972003f85122057739ff) giving 4 $ from node 2 to node 4
	 I am block with index 9
	 My Transaction list contains:
	 	 I am transaction (56446fd35cbd00ca5595ed583353bb1db2d24ae6) giving 5 $ from node 2 to node 3
	 	 I am transaction (46a285e3651b33571ea19c5757fd31059d404849) giving 6 $ from node 2 to node 1
	 I am block with index 10
	 My Transaction list contains:
	 	 I am transaction (5a8ec7c0f99f6fbc4f20fc36ac69a92693da7eb9) giving 10 $ from node 2 to node 3
	 	 I am transaction (2e8fea2a5a21fbe2154ea2614611acbfc6e2f5b4) giving 1 $ from node 3 to node 2
	 I am block with index 11
	 My Transaction list contains:
	 	 I am transaction (3322428951970e1239ed073957e252e02a565759) giving 2 $ from node 3 to node 4
	 	 I am transaction (133b7695dfbbbeebc068687462f272194c2c9db5) giving 3 $ from node 3 to node 0
	 I am block with index 12
	 My Transaction list contains:
	 	 I am transaction (843797a9e5d1b0854876dd99248dd83de25e2002) giving 4 $ from node 3 to node 2
	 	 I am transaction (fb1236aa94f4e55fe778d32084c98905f28c9acc) giving 5 $ from node 3 to node 1
	 I am block with index 13
	 My Transaction list contains:
	 	 I am transaction (cb51a507ab01cae351eeb41cb71892ff97da9b52) giving 6 $ from node 3 to node 2
	 	 I am transaction (f818497c1d6e70aa9ba133362cf3b6dff1ad3f27) giving 7 $ from node 3 to node 2
	 I am block with index 14
	 My Transaction list contains:
	 	 I am transaction (40d8b89699b0df367495facd9331e7258d5af681) giving 8 $ from node 3 to node 4
	 	 I am transaction (2bf363cfe5bbcb5719055fcbc2c373cf540b75cb) giving 9 $ from node 3 to node 4
	 I am block with index 15
	 My Transaction list contains:
	 	 I am transaction (2a4886fd71f36fce15eb0549944b297331a703a3) giving 10 $ from node 3 to node 0
	 	 I am transaction (b7a2e5451c10c5bda77757fb3263ec1e126adad1) giving 2 $ from node 4 to node 0
	 I am block with index 16
	 My Transaction list contains:
	 	 I am transaction (2790d441348fe56b4e5bf9dd13cededf4b2cfadb) giving 1 $ from node 4 to node 3
	 	 I am transaction (83cbee64c7ec2accff282f6a5b9a5a83974156e7) giving 3 $ from node 4 to node 1
	 I am block with index 17
	 My Transaction list contains:
	 	 I am transaction (35a844537a4a84d6983fc3e834cd5f9391d0d8fa) giving 8 $ from node 4 to node 3
	 	 I am transaction (f7fb9bb4fe17806ee1683103aeff7e2cd58c87ae) giving 9 $ from node 4 to node 3


0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17

old curr
	 I am block with index 18
	 My Transaction list contains:
	 	 I am transaction (7d0cbf9b3fd2966c3f5cfb1fd3c0e7667bb8b889) giving 2 $ from node 0 to node 2
new curr
	 I am block with index 19
	 My Transaction list contains:
127.0.0.1 - - [23/Mar/2020 20:58:03] "POST /AddBlock HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:58:03] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:58:04] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:58:04] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:58:05] "GET /Chain HTTP/1.1" 200 -
Block added to blockchain!
	 I am block with index 18
	 My Transaction list contains:
	 	 I am transaction (f7fb9bb4fe17806ee1683103aeff7e2cd58c87ae) giving 9 $ from node 4 to node 3
	 	 I am transaction (19c9492d1e50dee759ed6be007407d261f92b668) giving 1 $ from node 0 to node 1


Blockchain:
	 I am block with index 0
	 My Transaction list contains:
	 	 I am transaction (22638dedb224898aa6cae8cbd7cafb03ff303edc) giving 500 $ from node genesis to node 0
	 I am block with index 1
	 My Transaction list contains:
	 	 I am transaction (f3f596d61dfa65e51ff1c749ed8d9e39f4227f3a) giving 100 $ from node 0 to node 1
	 	 I am transaction (4d4366153409aaf2ea130d97affea9bf6c91c2bb) giving 100 $ from node 0 to node 2
	 I am block with index 2
	 My Transaction list contains:
	 	 I am transaction (01662993795fb5fd8093c5eb4414af9516606e8e) giving 100 $ from node 0 to node 3
	 	 I am transaction (c41568a85d921ed060a5f30a8ec96b7f255fec7e) giving 100 $ from node 0 to node 4
	 I am block with index 3
	 My Transaction list contains:
	 	 I am transaction (e3179905507f5ad52fc3922bfcfd435f3e8e4c53) giving 2 $ from node 1 to node 0
	 	 I am transaction (6b03130364cdbc9e6eb53eec293ac2168eae92e8) giving 3 $ from node 1 to node 3
	 I am block with index 4
	 My Transaction list contains:
	 	 I am transaction (f693990b4ba97ffa45974d842489e70d62b887e8) giving 4 $ from node 1 to node 0
	 	 I am transaction (52775aa21764f8c923c71c3aab103ac49444697c) giving 5 $ from node 1 to node 4
	 I am block with index 5
	 My Transaction list contains:
	 	 I am transaction (72f01b7c9ccea94888b00ed9ecaafe6d4ccb3eef) giving 6 $ from node 1 to node 3
	 	 I am transaction (1077a03e809bd5e682b27629a21afe6f8ade4df4) giving 7 $ from node 1 to node 2
Validate own block
	 I am block with index 6
	 My Transaction list contains:
	 	 I am transaction (0ad25cbffd27da14df38a4ae2aaf87cea69eb18d) giving 8 $ from node 1 to node 2
	 	 I am transaction (9970a5c0a373b7858e01a02a59859ad880278031) giving 9 $ from node 1 to node 0
	 I am block with index 7
	 My Transaction list contains:
	 	 I am transaction (1798cccfb048481cb904b2a0d7343f90941b9953) giving 1 $ from node 2 to node 4
	 	 I am transaction (4592016452dc7215913bea7029f2a6ff0c3cb2bb) giving 2 $ from node 2 to node 3
	 I am block with index 8
	 My Transaction list contains:
	 	 I am transaction (22b1776df3cd11faed623a33f0143d0497ed9af4) giving 3 $ from node 2 to node 0
	 	 I am transaction (8c2bd3d8acb1610a994d972003f85122057739ff) giving 4 $ from node 2 to node 4
	 I am block with index 9
	 My Transaction list contains:
127.0.0.1 - - [23/Mar/2020 20:58:05] "POST /AddBlock HTTP/1.1" 200 -
	 	 I am transaction (56446fd35cbd00ca5595ed583353bb1db2d24ae6) giving 5 $ from node 2 to node 3
	 	 I am transaction (46a285e3651b33571ea19c5757fd31059d404849) giving 6 $ from node 2 to node 1
	 I am block with index 10
	 My Transaction list contains:
	 	 I am transaction (5a8ec7c0f99f6fbc4f20fc36ac69a92693da7eb9) giving 10 $ from node 2 to node 3
	 	 I am transaction (2e8fea2a5a21fbe2154ea2614611acbfc6e2f5b4) giving 1 $ from node 3 to node 2
	 I am block with index 11
	 My Transaction list contains:
	 	 I am transaction (3322428951970e1239ed073957e252e02a565759) giving 2 $ from node 3 to node 4
	 	 I am transaction (133b7695dfbbbeebc068687462f272194c2c9db5) giving 3 $ from node 3 to node 0
	 I am block with index 12
	 My Transaction list contains:
	 	 I am transaction (843797a9e5d1b0854876dd99248dd83de25e2002) giving 4 $ from node 3 to node 2
	 	 I am transaction (fb1236aa94f4e55fe778d32084c98905f28c9acc) giving 5 $ from node 3 to node 1
Done
127.0.0.1 - - [23/Mar/2020 20:58:05] "POST /ValidateTransaction HTTP/1.1" 200 -
	 I am block with index 13
	 My Transaction list contains:
	 	 I am transaction (cb51a507ab01cae351eeb41cb71892ff97da9b52) giving 6 $ from node 3 to node 2
	 	 I am transaction (f818497c1d6e70aa9ba133362cf3b6dff1ad3f27) giving 7 $ from node 3 to node 2
	 I am block with index 14
	 My Transaction list contains:
	 	 I am transaction (40d8b89699b0df367495facd9331e7258d5af681) giving 8 $ from node 3 to node 4
Created transaction
	 	 I am transaction (2bf363cfe5bbcb5719055fcbc2c373cf540b75cb) giving 9 $ from node 3 to node 4
	 	 I am transaction (d8f2751ca2aef896681a413809adc11f2c099d23) giving 4 $ from node 0 to node 2
	 I am block with index 15
	 My Transaction list contains:
	 	 I am transaction (2a4886fd71f36fce15eb0549944b297331a703a3) giving 10 $ from node 3 to node 0
	 	 I am transaction (b7a2e5451c10c5bda77757fb3263ec1e126adad1) giving 2 $ from node 4 to node 0
	 I am block with index 16
	 My Transaction list contains:
	 	 I am transaction (2790d441348fe56b4e5bf9dd13cededf4b2cfadb) giving 1 $ from node 4 to node 3
	 	 I am transaction (83cbee64c7ec2accff282f6a5b9a5a83974156e7) giving 3 $ from node 4 to node 1
	 I am block with index 17
	 My Transaction list contains:
	 	 I am transaction (35a844537a4a84d6983fc3e834cd5f9391d0d8fa) giving 8 $ from node 4 to node 3
	 	 I am transaction (f7fb9bb4fe17806ee1683103aeff7e2cd58c87ae) giving 9 $ from node 4 to node 3
	 I am block with index 18
	 My Transaction list contains:
	 	 I am transaction (f7fb9bb4fe17806ee1683103aeff7e2cd58c87ae) giving 9 $ from node 4 to node 3
	 	 I am transaction (19c9492d1e50dee759ed6be007407d261f92b668) giving 1 $ from node 0 to node 1

Validating Transaction

	 	 I am transaction (29431c36112e958a44f81e43975495259277222e) giving 5 $ from node 0 to node 1
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
Result True

127.0.0.1 - - [23/Mar/2020 20:58:05] "POST /AddBlock HTTP/1.1" 200 -
Trani 29431c36112e958a44f81e43975495259277222e
	 I am block with index 19
	 My Transaction list contains:
False
False
1 2
127.0.0.1 - - [23/Mar/2020 20:58:05] "POST /ValidateTransaction HTTP/1.1" 200 -
Created transaction
	 	 I am transaction (29431c36112e958a44f81e43975495259277222e) giving 5 $ from node 0 to node 1
Validating Transaction
	 	 I am transaction (e11ae10e699decb5332d38c68dc084705d692124) giving 6 $ from node 0 to node 3
Result True
Trani e11ae10e699decb5332d38c68dc084705d692124
	 I am block with index 19
	 My Transaction list contains:
	 	 I am transaction (29431c36112e958a44f81e43975495259277222e) giving 5 $ from node 0 to node 1
False
False
2 2
AAAA
127.0.0.1 - - [23/Mar/2020 20:58:07] "POST /AddBlock HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:58:07] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:58:07] "POST /AddBlock HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:58:08] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:58:08] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:58:08] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:58:09] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:58:09] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:58:09] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:58:09] "POST /AddBlock HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:58:10] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:58:10] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:58:10] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:58:11] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:58:11] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:58:11] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:58:11] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:58:11] "GET /Chain HTTP/1.1" 200 -
Block added to blockchain!
	 I am block with index 19
	 My Transaction list contains:
	 	 I am transaction (f7fb9bb4fe17806ee1683103aeff7e2cd58c87ae) giving 9 $ from node 4 to node 3
	 	 I am transaction (35a844537a4a84d6983fc3e834cd5f9391d0d8fa) giving 8 $ from node 4 to node 3


Blockchain:
	 I am block with index 0
	 My Transaction list contains:
	 	 I am transaction (22638dedb224898aa6cae8cbd7cafb03ff303edc) giving 500 $ from node genesis to node 0
	 I am block with index 1
	 My Transaction list contains:
	 	 I am transaction (f3f596d61dfa65e51ff1c749ed8d9e39f4227f3a) giving 100 $ from node 0 to node 1
	 	 I am transaction (4d4366153409aaf2ea130d97affea9bf6c91c2bb) giving 100 $ from node 0 to node 2
	 I am block with index 2
	 My Transaction list contains:
	 	 I am transaction (01662993795fb5fd8093c5eb4414af9516606e8e) giving 100 $ from node 0 to node 3
	 	 I am transaction (c41568a85d921ed060a5f30a8ec96b7f255fec7e) giving 100 $ from node 0 to node 4
	 I am block with index 3
	 My Transaction list contains:
	 	 I am transaction (e3179905507f5ad52fc3922bfcfd435f3e8e4c53) giving 2 $ from node 1 to node 0
	 	 I am transaction (6b03130364cdbc9e6eb53eec293ac2168eae92e8) giving 3 $ from node 1 to node 3
	 I am block with index 4
	 My Transaction list contains:
	 	 I am transaction (f693990b4ba97ffa45974d842489e70d62b887e8) giving 4 $ from node 1 to node 0
	 	 I am transaction (52775aa21764f8c923c71c3aab103ac49444697c) giving 5 $ from node 1 to node 4
	 I am block with index 5
	 My Transaction list contains:
	 	 I am transaction (72f01b7c9ccea94888b00ed9ecaafe6d4ccb3eef) giving 6 $ from node 1 to node 3
	 	 I am transaction (1077a03e809bd5e682b27629a21afe6f8ade4df4) giving 7 $ from node 1 to node 2
	 I am block with index 6
	 My Transaction list contains:
	 	 I am transaction (0ad25cbffd27da14df38a4ae2aaf87cea69eb18d) giving 8 $ from node 1 to node 2
	 	 I am transaction (9970a5c0a373b7858e01a02a59859ad880278031) giving 9 $ from node 1 to node 0
	 I am block with index 7
	 My Transaction list contains:
	 	 I am transaction (1798cccfb048481cb904b2a0d7343f90941b9953) giving 1 $ from node 2 to node 4
	 	 I am transaction (4592016452dc7215913bea7029f2a6ff0c3cb2bb) giving 2 $ from node 2 to node 3
	 I am block with index 8
	 My Transaction list contains:
	 	 I am transaction (22b1776df3cd11faed623a33f0143d0497ed9af4) giving 3 $ from node 2 to node 0
	 	 I am transaction (8c2bd3d8acb1610a994d972003f85122057739ff) giving 4 $ from node 2 to node 4
	 I am block with index 9
	 My Transaction list contains:
	 	 I am transaction (56446fd35cbd00ca5595ed583353bb1db2d24ae6) giving 5 $ from node 2 to node 3
	 	 I am transaction (46a285e3651b33571ea19c5757fd31059d404849) giving 6 $ from node 2 to node 1
	 I am block with index 10
	 My Transaction list contains:
	 	 I am transaction (5a8ec7c0f99f6fbc4f20fc36ac69a92693da7eb9) giving 10 $ from node 2 to node 3
	 	 I am transaction (2e8fea2a5a21fbe2154ea2614611acbfc6e2f5b4) giving 1 $ from node 3 to node 2
	 I am block with index 11
	 My Transaction list contains:
	 	 I am transaction (3322428951970e1239ed073957e252e02a565759) giving 2 $ from node 3 to node 4
	 	 I am transaction (133b7695dfbbbeebc068687462f272194c2c9db5) giving 3 $ from node 3 to node 0
	 I am block with index 12
	 My Transaction list contains:
	 	 I am transaction (843797a9e5d1b0854876dd99248dd83de25e2002) giving 4 $ from node 3 to node 2
	 	 I am transaction (fb1236aa94f4e55fe778d32084c98905f28c9acc) giving 5 $ from node 3 to node 1
	 I am block with index 13
	 My Transaction list contains:
	 	 I am transaction (cb51a507ab01cae351eeb41cb71892ff97da9b52) giving 6 $ from node 3 to node 2
	 	 I am transaction (f818497c1d6e70aa9ba133362cf3b6dff1ad3f27) giving 7 $ from node 3 to node 2
	 I am block with index 14
	 My Transaction list contains:
	 	 I am transaction (40d8b89699b0df367495facd9331e7258d5af681) giving 8 $ from node 3 to node 4
	 	 I am transaction (2bf363cfe5bbcb5719055fcbc2c373cf540b75cb) giving 9 $ from node 3 to node 4
	 I am block with index 15
	 My Transaction list contains:
	 	 I am transaction (2a4886fd71f36fce15eb0549944b297331a703a3) giving 10 $ from node 3 to node 0
	 	 I am transaction (b7a2e5451c10c5bda77757fb3263ec1e126adad1) giving 2 $ from node 4 to node 0
	 I am block with index 16
	 My Transaction list contains:
	 	 I am transaction (2790d441348fe56b4e5bf9dd13cededf4b2cfadb) giving 1 $ from node 4 to node 3
	 	 I am transaction (83cbee64c7ec2accff282f6a5b9a5a83974156e7) giving 3 $ from node 4 to node 1
	 I am block with index 17
	 My Transaction list contains:
	 	 I am transaction (35a844537a4a84d6983fc3e834cd5f9391d0d8fa) giving 8 $ from node 4 to node 3
	 	 I am transaction (f7fb9bb4fe17806ee1683103aeff7e2cd58c87ae) giving 9 $ from node 4 to node 3
	 I am block with index 18
	 My Transaction list contains:
	 	 I am transaction (f7fb9bb4fe17806ee1683103aeff7e2cd58c87ae) giving 9 $ from node 4 to node 3
	 	 I am transaction (19c9492d1e50dee759ed6be007407d261f92b668) giving 1 $ from node 0 to node 1
	 I am block with index 19
	 My Transaction list contains:
	 	 I am transaction (f7fb9bb4fe17806ee1683103aeff7e2cd58c87ae) giving 9 $ from node 4 to node 3
	 	 I am transaction (35a844537a4a84d6983fc3e834cd5f9391d0d8fa) giving 8 $ from node 4 to node 3


0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19

127.0.0.1 - - [23/Mar/2020 20:58:12] "POST /AddBlock HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:58:12] "POST /AddBlock HTTP/1.1" 200 -
Validate own block
127.0.0.1 - - [23/Mar/2020 20:58:13] "POST /AddBlock HTTP/1.1" 200 -
Done
127.0.0.1 - - [23/Mar/2020 20:58:13] "POST /ValidateTransaction HTTP/1.1" 200 -
Created transaction
	 	 I am transaction (e11ae10e699decb5332d38c68dc084705d692124) giving 6 $ from node 0 to node 3
Validating Transaction
	 	 I am transaction (c9f584c3960d9f95d01da1d666121f3a9df04ec2) giving 7 $ from node 0 to node 1
Result True
Trani c9f584c3960d9f95d01da1d666121f3a9df04ec2
	 I am block with index 20
	 My Transaction list contains:
False
False
1 2
127.0.0.1 - - [23/Mar/2020 20:58:13] "POST /ValidateTransaction HTTP/1.1" 200 -
Created transaction
	 	 I am transaction (c9f584c3960d9f95d01da1d666121f3a9df04ec2) giving 7 $ from node 0 to node 1
Validating Transaction
	 	 I am transaction (3deca67678c32472b4441e264fa2619a343ffe70) giving 8 $ from node 0 to node 4
Result True
Trani 3deca67678c32472b4441e264fa2619a343ffe70
	 I am block with index 20
	 My Transaction list contains:
	 	 I am transaction (c9f584c3960d9f95d01da1d666121f3a9df04ec2) giving 7 $ from node 0 to node 1
False
False
2 2
AAAA
127.0.0.1 - - [23/Mar/2020 20:58:14] "GET /Chain HTTP/1.1" 200 -
Block added to blockchain!
	 I am block with index 20
	 My Transaction list contains:
	 	 I am transaction (29431c36112e958a44f81e43975495259277222e) giving 5 $ from node 0 to node 1
	 	 I am transaction (e11ae10e699decb5332d38c68dc084705d692124) giving 6 $ from node 0 to node 3


Blockchain:
	 I am block with index 0
	 My Transaction list contains:
	 	 I am transaction (22638dedb224898aa6cae8cbd7cafb03ff303edc) giving 500 $ from node genesis to node 0
	 I am block with index 1
	 My Transaction list contains:
	 	 I am transaction (f3f596d61dfa65e51ff1c749ed8d9e39f4227f3a) giving 100 $ from node 0 to node 1
	 	 I am transaction (4d4366153409aaf2ea130d97affea9bf6c91c2bb) giving 100 $ from node 0 to node 2
	 I am block with index 2
	 My Transaction list contains:
	 	 I am transaction (01662993795fb5fd8093c5eb4414af9516606e8e) giving 100 $ from node 0 to node 3
	 	 I am transaction (c41568a85d921ed060a5f30a8ec96b7f255fec7e) giving 100 $ from node 0 to node 4
	 I am block with index 3
	 My Transaction list contains:
	 	 I am transaction (e3179905507f5ad52fc3922bfcfd435f3e8e4c53) giving 2 $ from node 1 to node 0
	 	 I am transaction (6b03130364cdbc9e6eb53eec293ac2168eae92e8) giving 3 $ from node 1 to node 3
	 I am block with index 4
	 My Transaction list contains:
	 	 I am transaction (f693990b4ba97ffa45974d842489e70d62b887e8) giving 4 $ from node 1 to node 0
	 	 I am transaction (52775aa21764f8c923c71c3aab103ac49444697c) giving 5 $ from node 1 to node 4
	 I am block with index 5
	 My Transaction list contains:
	 	 I am transaction (72f01b7c9ccea94888b00ed9ecaafe6d4ccb3eef) giving 6 $ from node 1 to node 3
	 	 I am transaction (1077a03e809bd5e682b27629a21afe6f8ade4df4) giving 7 $ from node 1 to node 2
	 I am block with index 6
	 My Transaction list contains:
	 	 I am transaction (0ad25cbffd27da14df38a4ae2aaf87cea69eb18d) giving 8 $ from node 1 to node 2
	 	 I am transaction (9970a5c0a373b7858e01a02a59859ad880278031) giving 9 $ from node 1 to node 0
	 I am block with index 7
	 My Transaction list contains:
	 	 I am transaction (1798cccfb048481cb904b2a0d7343f90941b9953) giving 1 $ from node 2 to node 4
	 	 I am transaction (4592016452dc7215913bea7029f2a6ff0c3cb2bb) giving 2 $ from node 2 to node 3
	 I am block with index 8
	 My Transaction list contains:
	 	 I am transaction (22b1776df3cd11faed623a33f0143d0497ed9af4) giving 3 $ from node 2 to node 0
	 	 I am transaction (8c2bd3d8acb1610a994d972003f85122057739ff) giving 4 $ from node 2 to node 4
	 I am block with index 9
	 My Transaction list contains:
	 	 I am transaction (56446fd35cbd00ca5595ed583353bb1db2d24ae6) giving 5 $ from node 2 to node 3
	 	 I am transaction (46a285e3651b33571ea19c5757fd31059d404849) giving 6 $ from node 2 to node 1
	 I am block with index 10
	 My Transaction list contains:
	 	 I am transaction (5a8ec7c0f99f6fbc4f20fc36ac69a92693da7eb9) giving 10 $ from node 2 to node 3
	 	 I am transaction (2e8fea2a5a21fbe2154ea2614611acbfc6e2f5b4) giving 1 $ from node 3 to node 2
	 I am block with index 11
	 My Transaction list contains:
	 	 I am transaction (3322428951970e1239ed073957e252e02a565759) giving 2 $ from node 3 to node 4
	 	 I am transaction (133b7695dfbbbeebc068687462f272194c2c9db5) giving 3 $ from node 3 to node 0
	 I am block with index 12
	 My Transaction list contains:
	 	 I am transaction (843797a9e5d1b0854876dd99248dd83de25e2002) giving 4 $ from node 3 to node 2
	 	 I am transaction (fb1236aa94f4e55fe778d32084c98905f28c9acc) giving 5 $ from node 3 to node 1
	 I am block with index 13
	 My Transaction list contains:
	 	 I am transaction (cb51a507ab01cae351eeb41cb71892ff97da9b52) giving 6 $ from node 3 to node 2
	 	 I am transaction (f818497c1d6e70aa9ba133362cf3b6dff1ad3f27) giving 7 $ from node 3 to node 2
	 I am block with index 14
	 My Transaction list contains:
	 	 I am transaction (40d8b89699b0df367495facd9331e7258d5af681) giving 8 $ from node 3 to node 4
	 	 I am transaction (2bf363cfe5bbcb5719055fcbc2c373cf540b75cb) giving 9 $ from node 3 to node 4
	 I am block with index 15
	 My Transaction list contains:
	 	 I am transaction (2a4886fd71f36fce15eb0549944b297331a703a3) giving 10 $ from node 3 to node 0
	 	 I am transaction (b7a2e5451c10c5bda77757fb3263ec1e126adad1) giving 2 $ from node 4 to node 0
	 I am block with index 16
	 My Transaction list contains:
	 	 I am transaction (2790d441348fe56b4e5bf9dd13cededf4b2cfadb) giving 1 $ from node 4 to node 3
	 	 I am transaction (83cbee64c7ec2accff282f6a5b9a5a83974156e7) giving 3 $ from node 4 to node 1
	 I am block with index 17
	 My Transaction list contains:
	 	 I am transaction (35a844537a4a84d6983fc3e834cd5f9391d0d8fa) giving 8 $ from node 4 to node 3
	 	 I am transaction (f7fb9bb4fe17806ee1683103aeff7e2cd58c87ae) giving 9 $ from node 4 to node 3
	 I am block with index 18
	 My Transaction list contains:
	 	 I am transaction (f7fb9bb4fe17806ee1683103aeff7e2cd58c87ae) giving 9 $ from node 4 to node 3
	 	 I am transaction (19c9492d1e50dee759ed6be007407d261f92b668) giving 1 $ from node 0 to node 1
	 I am block with index 19
	 My Transaction list contains:
Validate own block
	 	 I am transaction (f7fb9bb4fe17806ee1683103aeff7e2cd58c87ae) giving 9 $ from node 4 to node 3
	 	 I am transaction (35a844537a4a84d6983fc3e834cd5f9391d0d8fa) giving 8 $ from node 4 to node 3
	 I am block with index 20
	 My Transaction list contains:
	 	 I am transaction (29431c36112e958a44f81e43975495259277222e) giving 5 $ from node 0 to node 1
	 	 I am transaction (e11ae10e699decb5332d38c68dc084705d692124) giving 6 $ from node 0 to node 3


127.0.0.1 - - [23/Mar/2020 20:58:14] "POST /AddBlock HTTP/1.1" 200 -
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20

127.0.0.1 - - [23/Mar/2020 20:58:14] "POST /AddBlock HTTP/1.1" 200 -
Done
127.0.0.1 - - [23/Mar/2020 20:58:14] "POST /ValidateTransaction HTTP/1.1" 200 -
Created transaction
	 	 I am transaction (3deca67678c32472b4441e264fa2619a343ffe70) giving 8 $ from node 0 to node 4
Validating Transaction
	 	 I am transaction (4d4eedc6e5da0f63f0a94d3d6ba2d3bd3c245b51) giving 9 $ from node 0 to node 4
Result True
Trani 4d4eedc6e5da0f63f0a94d3d6ba2d3bd3c245b51
	 I am block with index 21
	 My Transaction list contains:
False
False
1 2
127.0.0.1 - - [23/Mar/2020 20:58:14] "POST /ValidateTransaction HTTP/1.1" 200 -
Created transaction
	 	 I am transaction (4d4eedc6e5da0f63f0a94d3d6ba2d3bd3c245b51) giving 9 $ from node 0 to node 4
Validating Transaction
	 	 I am transaction (0bf0c2494d1eb53d4bdfdbe9e50ca2aab4b038f9) giving 10 $ from node 0 to node 4
Result True
Trani 0bf0c2494d1eb53d4bdfdbe9e50ca2aab4b038f9
	 I am block with index 21
	 My Transaction list contains:
	 	 I am transaction (4d4eedc6e5da0f63f0a94d3d6ba2d3bd3c245b51) giving 9 $ from node 0 to node 4
False
False
2 2
AAAA
127.0.0.1 - - [23/Mar/2020 20:58:15] "GET /Chain HTTP/1.1" 200 -
Block added to blockchain!
	 I am block with index 21
	 My Transaction list contains:
	 	 I am transaction (29431c36112e958a44f81e43975495259277222e) giving 5 $ from node 0 to node 1
	 	 I am transaction (253b81fd81576b0993973a2eeda532d90000f37a) giving 10 $ from node 4 to node 0


Blockchain:
	 I am block with index 0
	 My Transaction list contains:
	 	 I am transaction (22638dedb224898aa6cae8cbd7cafb03ff303edc) giving 500 $ from node genesis to node 0
	 I am block with index 1
	 My Transaction list contains:
	 	 I am transaction (f3f596d61dfa65e51ff1c749ed8d9e39f4227f3a) giving 100 $ from node 0 to node 1
	 	 I am transaction (4d4366153409aaf2ea130d97affea9bf6c91c2bb) giving 100 $ from node 0 to node 2
	 I am block with index 2
	 My Transaction list contains:
	 	 I am transaction (01662993795fb5fd8093c5eb4414af9516606e8e) giving 100 $ from node 0 to node 3
	 	 I am transaction (c41568a85d921ed060a5f30a8ec96b7f255fec7e) giving 100 $ from node 0 to node 4
	 I am block with index 3
	 My Transaction list contains:
	 	 I am transaction (e3179905507f5ad52fc3922bfcfd435f3e8e4c53) giving 2 $ from node 1 to node 0
	 	 I am transaction (6b03130364cdbc9e6eb53eec293ac2168eae92e8) giving 3 $ from node 1 to node 3
	 I am block with index 4
	 My Transaction list contains:
	 	 I am transaction (f693990b4ba97ffa45974d842489e70d62b887e8) giving 4 $ from node 1 to node 0
	 	 I am transaction (52775aa21764f8c923c71c3aab103ac49444697c) giving 5 $ from node 1 to node 4
	 I am block with index 5
	 My Transaction list contains:
	 	 I am transaction (72f01b7c9ccea94888b00ed9ecaafe6d4ccb3eef) giving 6 $ from node 1 to node 3
	 	 I am transaction (1077a03e809bd5e682b27629a21afe6f8ade4df4) giving 7 $ from node 1 to node 2
	 I am block with index 6
	 My Transaction list contains:
	 	 I am transaction (0ad25cbffd27da14df38a4ae2aaf87cea69eb18d) giving 8 $ from node 1 to node 2
	 	 I am transaction (9970a5c0a373b7858e01a02a59859ad880278031) giving 9 $ from node 1 to node 0
	 I am block with index 7
	 My Transaction list contains:
	 	 I am transaction (1798cccfb048481cb904b2a0d7343f90941b9953) giving 1 $ from node 2 to node 4
	 	 I am transaction (4592016452dc7215913bea7029f2a6ff0c3cb2bb) giving 2 $ from node 2 to node 3
	 I am block with index 8
	 My Transaction list contains:
	 	 I am transaction (22b1776df3cd11faed623a33f0143d0497ed9af4) giving 3 $ from node 2 to node 0
	 	 I am transaction (8c2bd3d8acb1610a994d972003f85122057739ff) giving 4 $ from node 2 to node 4
	 I am block with index 9
	 My Transaction list contains:
127.0.0.1 - - [23/Mar/2020 20:58:16] "POST /AddBlock HTTP/1.1" 200 -
	 	 I am transaction (56446fd35cbd00ca5595ed583353bb1db2d24ae6) giving 5 $ from node 2 to node 3
	 	 I am transaction (46a285e3651b33571ea19c5757fd31059d404849) giving 6 $ from node 2 to node 1
127.0.0.1 - - [23/Mar/2020 20:58:16] "GET /Chain HTTP/1.1" 200 -
	 I am block with index 10
	 My Transaction list contains:
	 	 I am transaction (5a8ec7c0f99f6fbc4f20fc36ac69a92693da7eb9) giving 10 $ from node 2 to node 3
	 	 I am transaction (2e8fea2a5a21fbe2154ea2614611acbfc6e2f5b4) giving 1 $ from node 3 to node 2
	 I am block with index 11
	 My Transaction list contains:
	 	 I am transaction (3322428951970e1239ed073957e252e02a565759) giving 2 $ from node 3 to node 4
	 	 I am transaction (133b7695dfbbbeebc068687462f272194c2c9db5) giving 3 $ from node 3 to node 0
	 I am block with index 12
	 My Transaction list contains:
127.0.0.1 - - [23/Mar/2020 20:58:16] "GET /Chain HTTP/1.1" 200 -
	 	 I am transaction (843797a9e5d1b0854876dd99248dd83de25e2002) giving 4 $ from node 3 to node 2
127.0.0.1 - - [23/Mar/2020 20:58:16] "GET /Chain HTTP/1.1" 200 -
	 	 I am transaction (fb1236aa94f4e55fe778d32084c98905f28c9acc) giving 5 $ from node 3 to node 1
	 I am block with index 13
	 My Transaction list contains:
	 	 I am transaction (cb51a507ab01cae351eeb41cb71892ff97da9b52) giving 6 $ from node 3 to node 2
	 	 I am transaction (f818497c1d6e70aa9ba133362cf3b6dff1ad3f27) giving 7 $ from node 3 to node 2
	 I am block with index 14
	 My Transaction list contains:
	 	 I am transaction (40d8b89699b0df367495facd9331e7258d5af681) giving 8 $ from node 3 to node 4
	 	 I am transaction (2bf363cfe5bbcb5719055fcbc2c373cf540b75cb) giving 9 $ from node 3 to node 4
	 I am block with index 15
	 My Transaction list contains:
	 	 I am transaction (2a4886fd71f36fce15eb0549944b297331a703a3) giving 10 $ from node 3 to node 0
	 	 I am transaction (b7a2e5451c10c5bda77757fb3263ec1e126adad1) giving 2 $ from node 4 to node 0
	 I am block with index 16
	 My Transaction list contains:
	 	 I am transaction (2790d441348fe56b4e5bf9dd13cededf4b2cfadb) giving 1 $ from node 4 to node 3
	 	 I am transaction (83cbee64c7ec2accff282f6a5b9a5a83974156e7) giving 3 $ from node 4 to node 1
	 I am block with index 17
	 My Transaction list contains:
	 	 I am transaction (35a844537a4a84d6983fc3e834cd5f9391d0d8fa) giving 8 $ from node 4 to node 3
	 	 I am transaction (f7fb9bb4fe17806ee1683103aeff7e2cd58c87ae) giving 9 $ from node 4 to node 3
	 I am block with index 18
	 My Transaction list contains:
	 	 I am transaction (f7fb9bb4fe17806ee1683103aeff7e2cd58c87ae) giving 9 $ from node 4 to node 3
	 	 I am transaction (19c9492d1e50dee759ed6be007407d261f92b668) giving 1 $ from node 0 to node 1
	 I am block with index 19
	 My Transaction list contains:
	 	 I am transaction (f7fb9bb4fe17806ee1683103aeff7e2cd58c87ae) giving 9 $ from node 4 to node 3
	 	 I am transaction (35a844537a4a84d6983fc3e834cd5f9391d0d8fa) giving 8 $ from node 4 to node 3
	 I am block with index 20
	 My Transaction list contains:
	 	 I am transaction (29431c36112e958a44f81e43975495259277222e) giving 5 $ from node 0 to node 1
	 	 I am transaction (e11ae10e699decb5332d38c68dc084705d692124) giving 6 $ from node 0 to node 3
	 I am block with index 21
	 My Transaction list contains:
	 	 I am transaction (29431c36112e958a44f81e43975495259277222e) giving 5 $ from node 0 to node 1
	 	 I am transaction (253b81fd81576b0993973a2eeda532d90000f37a) giving 10 $ from node 4 to node 0


0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21

127.0.0.1 - - [23/Mar/2020 20:58:17] "POST /AddBlock HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:58:17] "GET /Chain HTTP/1.1" 200 -
Validate own block
127.0.0.1 - - [23/Mar/2020 20:58:18] "POST /AddBlock HTTP/1.1" 200 -
Done
127.0.0.1 - - [23/Mar/2020 20:58:18] "POST /ValidateTransaction HTTP/1.1" 200 -
Created transaction
	 	 I am transaction (0bf0c2494d1eb53d4bdfdbe9e50ca2aab4b038f9) giving 10 $ from node 0 to node 4
127.0.0.1 - - [23/Mar/2020 20:58:19] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:58:19] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:58:19] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:58:19] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:58:20] "POST /AddBlock HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:58:20] "POST /AddBlock HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:58:20] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:58:20] "GET /Chain HTTP/1.1" 200 -
Block added to blockchain!
	 I am block with index 22
	 My Transaction list contains:
	 	 I am transaction (4d4eedc6e5da0f63f0a94d3d6ba2d3bd3c245b51) giving 9 $ from node 0 to node 4
	 	 I am transaction (3deca67678c32472b4441e264fa2619a343ffe70) giving 8 $ from node 0 to node 4

127.0.0.1 - - [23/Mar/2020 20:58:21] "GET /Chain HTTP/1.1" 200 -

Blockchain:
	 I am block with index 0
	 My Transaction list contains:
	 	 I am transaction (22638dedb224898aa6cae8cbd7cafb03ff303edc) giving 500 $ from node genesis to node 0
	 I am block with index 1
	 My Transaction list contains:
	 	 I am transaction (f3f596d61dfa65e51ff1c749ed8d9e39f4227f3a) giving 100 $ from node 0 to node 1
	 	 I am transaction (4d4366153409aaf2ea130d97affea9bf6c91c2bb) giving 100 $ from node 0 to node 2
	 I am block with index 2
	 My Transaction list contains:
	 	 I am transaction (01662993795fb5fd8093c5eb4414af9516606e8e) giving 100 $ from node 0 to node 3
	 	 I am transaction (c41568a85d921ed060a5f30a8ec96b7f255fec7e) giving 100 $ from node 0 to node 4
	 I am block with index 3
	 My Transaction list contains:
	 	 I am transaction (e3179905507f5ad52fc3922bfcfd435f3e8e4c53) giving 2 $ from node 1 to node 0
	 	 I am transaction (6b03130364cdbc9e6eb53eec293ac2168eae92e8) giving 3 $ from node 1 to node 3
	 I am block with index 4
	 My Transaction list contains:
	 	 I am transaction (f693990b4ba97ffa45974d842489e70d62b887e8) giving 4 $ from node 1 to node 0
	 	 I am transaction (52775aa21764f8c923c71c3aab103ac49444697c) giving 5 $ from node 1 to node 4
	 I am block with index 5
	 My Transaction list contains:
	 	 I am transaction (72f01b7c9ccea94888b00ed9ecaafe6d4ccb3eef) giving 6 $ from node 1 to node 3
	 	 I am transaction (1077a03e809bd5e682b27629a21afe6f8ade4df4) giving 7 $ from node 1 to node 2
	 I am block with index 6
	 My Transaction list contains:
	 	 I am transaction (0ad25cbffd27da14df38a4ae2aaf87cea69eb18d) giving 8 $ from node 1 to node 2
	 	 I am transaction (9970a5c0a373b7858e01a02a59859ad880278031) giving 9 $ from node 1 to node 0
	 I am block with index 7
	 My Transaction list contains:
	 	 I am transaction (1798cccfb048481cb904b2a0d7343f90941b9953) giving 1 $ from node 2 to node 4
	 	 I am transaction (4592016452dc7215913bea7029f2a6ff0c3cb2bb) giving 2 $ from node 2 to node 3
	 I am block with index 8
	 My Transaction list contains:
	 	 I am transaction (22b1776df3cd11faed623a33f0143d0497ed9af4) giving 3 $ from node 2 to node 0
	 	 I am transaction (8c2bd3d8acb1610a994d972003f85122057739ff) giving 4 $ from node 2 to node 4
	 I am block with index 9
	 My Transaction list contains:
	 	 I am transaction (56446fd35cbd00ca5595ed583353bb1db2d24ae6) giving 5 $ from node 2 to node 3
	 	 I am transaction (46a285e3651b33571ea19c5757fd31059d404849) giving 6 $ from node 2 to node 1
	 I am block with index 10
	 My Transaction list contains:
	 	 I am transaction (5a8ec7c0f99f6fbc4f20fc36ac69a92693da7eb9) giving 10 $ from node 2 to node 3
	 	 I am transaction (2e8fea2a5a21fbe2154ea2614611acbfc6e2f5b4) giving 1 $ from node 3 to node 2
	 I am block with index 11
	 My Transaction list contains:
	 	 I am transaction (3322428951970e1239ed073957e252e02a565759) giving 2 $ from node 3 to node 4
	 	 I am transaction (133b7695dfbbbeebc068687462f272194c2c9db5) giving 3 $ from node 3 to node 0
	 I am block with index 12
	 My Transaction list contains:
	 	 I am transaction (843797a9e5d1b0854876dd99248dd83de25e2002) giving 4 $ from node 3 to node 2
	 	 I am transaction (fb1236aa94f4e55fe778d32084c98905f28c9acc) giving 5 $ from node 3 to node 1
	 I am block with index 13
	 My Transaction list contains:
	 	 I am transaction (cb51a507ab01cae351eeb41cb71892ff97da9b52) giving 6 $ from node 3 to node 2
	 	 I am transaction (f818497c1d6e70aa9ba133362cf3b6dff1ad3f27) giving 7 $ from node 3 to node 2
	 I am block with index 14
	 My Transaction list contains:
	 	 I am transaction (40d8b89699b0df367495facd9331e7258d5af681) giving 8 $ from node 3 to node 4
	 	 I am transaction (2bf363cfe5bbcb5719055fcbc2c373cf540b75cb) giving 9 $ from node 3 to node 4
	 I am block with index 15
	 My Transaction list contains:
	 	 I am transaction (2a4886fd71f36fce15eb0549944b297331a703a3) giving 10 $ from node 3 to node 0
	 	 I am transaction (b7a2e5451c10c5bda77757fb3263ec1e126adad1) giving 2 $ from node 4 to node 0
	 I am block with index 16
	 My Transaction list contains:
	 	 I am transaction (2790d441348fe56b4e5bf9dd13cededf4b2cfadb) giving 1 $ from node 4 to node 3
	 	 I am transaction (83cbee64c7ec2accff282f6a5b9a5a83974156e7) giving 3 $ from node 4 to node 1
	 I am block with index 17
	 My Transaction list contains:
	 	 I am transaction (35a844537a4a84d6983fc3e834cd5f9391d0d8fa) giving 8 $ from node 4 to node 3
	 	 I am transaction (f7fb9bb4fe17806ee1683103aeff7e2cd58c87ae) giving 9 $ from node 4 to node 3
	 I am block with index 18
	 My Transaction list contains:
	 	 I am transaction (f7fb9bb4fe17806ee1683103aeff7e2cd58c87ae) giving 9 $ from node 4 to node 3
	 	 I am transaction (19c9492d1e50dee759ed6be007407d261f92b668) giving 1 $ from node 0 to node 1
	 I am block with index 19
	 My Transaction list contains:
	 	 I am transaction (f7fb9bb4fe17806ee1683103aeff7e2cd58c87ae) giving 9 $ from node 4 to node 3
	 	 I am transaction (35a844537a4a84d6983fc3e834cd5f9391d0d8fa) giving 8 $ from node 4 to node 3
	 I am block with index 20
	 My Transaction list contains:
	 	 I am transaction (29431c36112e958a44f81e43975495259277222e) giving 5 $ from node 0 to node 1
	 	 I am transaction (e11ae10e699decb5332d38c68dc084705d692124) giving 6 $ from node 0 to node 3
	 I am block with index 21
	 My Transaction list contains:
	 	 I am transaction (29431c36112e958a44f81e43975495259277222e) giving 5 $ from node 0 to node 1
	 	 I am transaction (253b81fd81576b0993973a2eeda532d90000f37a) giving 10 $ from node 4 to node 0
	 I am block with index 22
	 My Transaction list contains:
	 	 I am transaction (4d4eedc6e5da0f63f0a94d3d6ba2d3bd3c245b51) giving 9 $ from node 0 to node 4
	 	 I am transaction (3deca67678c32472b4441e264fa2619a343ffe70) giving 8 $ from node 0 to node 4


0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22

127.0.0.1 - - [23/Mar/2020 20:58:21] "POST /AddBlock HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:58:21] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:58:22] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:58:22] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:58:22] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:58:22] "POST /AddBlock HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:58:23] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:58:23] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:58:23] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:58:23] "GET /Chain HTTP/1.1" 200 -
RESOLVE conflicts chain updated
127.0.0.1 - - [23/Mar/2020 20:58:24] "GET /Chain HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2020 20:58:24] "POST /AddBlock HTTP/1.1" 200 -
RESOLVE conflicts chain updated
127.0.0.1 - - [23/Mar/2020 20:58:24] "GET /Chain HTTP/1.1" 200 -
Old chain


Blockchain:
	 I am block with index 0
	 My Transaction list contains:
	 	 I am transaction (22638dedb224898aa6cae8cbd7cafb03ff303edc) giving 500 $ from node genesis to node 0
	 I am block with index 1
	 My Transaction list contains:
	 	 I am transaction (f3f596d61dfa65e51ff1c749ed8d9e39f4227f3a) giving 100 $ from node 0 to node 1
	 	 I am transaction (4d4366153409aaf2ea130d97affea9bf6c91c2bb) giving 100 $ from node 0 to node 2
	 I am block with index 2
	 My Transaction list contains:
	 	 I am transaction (01662993795fb5fd8093c5eb4414af9516606e8e) giving 100 $ from node 0 to node 3
	 	 I am transaction (c41568a85d921ed060a5f30a8ec96b7f255fec7e) giving 100 $ from node 0 to node 4
	 I am block with index 3
	 My Transaction list contains:
	 	 I am transaction (e3179905507f5ad52fc3922bfcfd435f3e8e4c53) giving 2 $ from node 1 to node 0
	 	 I am transaction (6b03130364cdbc9e6eb53eec293ac2168eae92e8) giving 3 $ from node 1 to node 3
	 I am block with index 4
	 My Transaction list contains:
	 	 I am transaction (f693990b4ba97ffa45974d842489e70d62b887e8) giving 4 $ from node 1 to node 0
	 	 I am transaction (52775aa21764f8c923c71c3aab103ac49444697c) giving 5 $ from node 1 to node 4
	 I am block with index 5
	 My Transaction list contains:
	 	 I am transaction (72f01b7c9ccea94888b00ed9ecaafe6d4ccb3eef) giving 6 $ from node 1 to node 3
	 	 I am transaction (1077a03e809bd5e682b27629a21afe6f8ade4df4) giving 7 $ from node 1 to node 2
	 I am block with index 6
	 My Transaction list contains:
	 	 I am transaction (0ad25cbffd27da14df38a4ae2aaf87cea69eb18d) giving 8 $ from node 1 to node 2
	 	 I am transaction (9970a5c0a373b7858e01a02a59859ad880278031) giving 9 $ from node 1 to node 0
	 I am block with index 7
	 My Transaction list contains:
	 	 I am transaction (1798cccfb048481cb904b2a0d7343f90941b9953) giving 1 $ from node 2 to node 4
	 	 I am transaction (4592016452dc7215913bea7029f2a6ff0c3cb2bb) giving 2 $ from node 2 to node 3
	 I am block with index 8
	 My Transaction list contains:
	 	 I am transaction (22b1776df3cd11faed623a33f0143d0497ed9af4) giving 3 $ from node 2 to node 0
	 	 I am transaction (8c2bd3d8acb1610a994d972003f85122057739ff) giving 4 $ from node 2 to node 4
	 I am block with index 9
	 My Transaction list contains:
	 	 I am transaction (56446fd35cbd00ca5595ed583353bb1db2d24ae6) giving 5 $ from node 2 to node 3
	 	 I am transaction (46a285e3651b33571ea19c5757fd31059d404849) giving 6 $ from node 2 to node 1
	 I am block with index 10
	 My Transaction list contains:
	 	 I am transaction (5a8ec7c0f99f6fbc4f20fc36ac69a92693da7eb9) giving 10 $ from node 2 to node 3
	 	 I am transaction (2e8fea2a5a21fbe2154ea2614611acbfc6e2f5b4) giving 1 $ from node 3 to node 2
	 I am block with index 11
	 My Transaction list contains:
	 	 I am transaction (3322428951970e1239ed073957e252e02a565759) giving 2 $ from node 3 to node 4
	 	 I am transaction (133b7695dfbbbeebc068687462f272194c2c9db5) giving 3 $ from node 3 to node 0
	 I am block with index 12
	 My Transaction list contains:
	 	 I am transaction (843797a9e5d1b0854876dd99248dd83de25e2002) giving 4 $ from node 3 to node 2
	 	 I am transaction (fb1236aa94f4e55fe778d32084c98905f28c9acc) giving 5 $ from node 3 to node 1
	 I am block with index 13
	 My Transaction list contains:
	 	 I am transaction (cb51a507ab01cae351eeb41cb71892ff97da9b52) giving 6 $ from node 3 to node 2
	 	 I am transaction (f818497c1d6e70aa9ba133362cf3b6dff1ad3f27) giving 7 $ from node 3 to node 2
	 I am block with index 14
	 My Transaction list contains:
	 	 I am transaction (40d8b89699b0df367495facd9331e7258d5af681) giving 8 $ from node 3 to node 4
	 	 I am transaction (2bf363cfe5bbcb5719055fcbc2c373cf540b75cb) giving 9 $ from node 3 to node 4
	 I am block with index 15
	 My Transaction list contains:
	 	 I am transaction (2a4886fd71f36fce15eb0549944b297331a703a3) giving 10 $ from node 3 to node 0
	 	 I am transaction (b7a2e5451c10c5bda77757fb3263ec1e126adad1) giving 2 $ from node 4 to node 0
	 I am block with index 16
	 My Transaction list contains:
	 	 I am transaction (2790d441348fe56b4e5bf9dd13cededf4b2cfadb) giving 1 $ from node 4 to node 3
	 	 I am transaction (83cbee64c7ec2accff282f6a5b9a5a83974156e7) giving 3 $ from node 4 to node 1
	 I am block with index 17
	 My Transaction list contains:
	 	 I am transaction (35a844537a4a84d6983fc3e834cd5f9391d0d8fa) giving 8 $ from node 4 to node 3
	 	 I am transaction (f7fb9bb4fe17806ee1683103aeff7e2cd58c87ae) giving 9 $ from node 4 to node 3
	 I am block with index 18
	 My Transaction list contains:
	 	 I am transaction (f7fb9bb4fe17806ee1683103aeff7e2cd58c87ae) giving 9 $ from node 4 to node 3
	 	 I am transaction (19c9492d1e50dee759ed6be007407d261f92b668) giving 1 $ from node 0 to node 1
	 I am block with index 19
	 My Transaction list contains:
	 	 I am transaction (f7fb9bb4fe17806ee1683103aeff7e2cd58c87ae) giving 9 $ from node 4 to node 3
	 	 I am transaction (35a844537a4a84d6983fc3e834cd5f9391d0d8fa) giving 8 $ from node 4 to node 3
	 I am block with index 20
	 My Transaction list contains:
	 	 I am transaction (29431c36112e958a44f81e43975495259277222e) giving 5 $ from node 0 to node 1
	 	 I am transaction (e11ae10e699decb5332d38c68dc084705d692124) giving 6 $ from node 0 to node 3
	 I am block with index 21
	 My Transaction list contains:
	 	 I am transaction (29431c36112e958a44f81e43975495259277222e) giving 5 $ from node 0 to node 1
	 	 I am transaction (253b81fd81576b0993973a2eeda532d90000f37a) giving 10 $ from node 4 to node 0
	 I am block with index 22
	 My Transaction list contains:
	 	 I am transaction (4d4eedc6e5da0f63f0a94d3d6ba2d3bd3c245b51) giving 9 $ from node 0 to node 4
	 	 I am transaction (3deca67678c32472b4441e264fa2619a343ffe70) giving 8 $ from node 0 to node 4


0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22

New Chain


Blockchain:
	 I am block with index 0
	 My Transaction list contains:
	 	 I am transaction (22638dedb224898aa6cae8cbd7cafb03ff303edc) giving 500 $ from node genesis to node 0
	 I am block with index 1
	 My Transaction list contains:
	 	 I am transaction (f3f596d61dfa65e51ff1c749ed8d9e39f4227f3a) giving 100 $ from node 0 to node 1
	 	 I am transaction (4d4366153409aaf2ea130d97affea9bf6c91c2bb) giving 100 $ from node 0 to node 2
	 I am block with index 2
	 My Transaction list contains:
	 	 I am transaction (01662993795fb5fd8093c5eb4414af9516606e8e) giving 100 $ from node 0 to node 3
	 	 I am transaction (c41568a85d921ed060a5f30a8ec96b7f255fec7e) giving 100 $ from node 0 to node 4
	 I am block with index 3
	 My Transaction list contains:
	 	 I am transaction (e3179905507f5ad52fc3922bfcfd435f3e8e4c53) giving 2 $ from node 1 to node 0
	 	 I am transaction (6b03130364cdbc9e6eb53eec293ac2168eae92e8) giving 3 $ from node 1 to node 3
	 I am block with index 4
	 My Transaction list contains:
	 	 I am transaction (f693990b4ba97ffa45974d842489e70d62b887e8) giving 4 $ from node 1 to node 0
	 	 I am transaction (52775aa21764f8c923c71c3aab103ac49444697c) giving 5 $ from node 1 to node 4
	 I am block with index 5
	 My Transaction list contains:
	 	 I am transaction (72f01b7c9ccea94888b00ed9ecaafe6d4ccb3eef) giving 6 $ from node 1 to node 3
	 	 I am transaction (1077a03e809bd5e682b27629a21afe6f8ade4df4) giving 7 $ from node 1 to node 2
	 I am block with index 6
	 My Transaction list contains:
	 	 I am transaction (0ad25cbffd27da14df38a4ae2aaf87cea69eb18d) giving 8 $ from node 1 to node 2
	 	 I am transaction (9970a5c0a373b7858e01a02a59859ad880278031) giving 9 $ from node 1 to node 0
	 I am block with index 7
	 My Transaction list contains:
	 	 I am transaction (1798cccfb048481cb904b2a0d7343f90941b9953) giving 1 $ from node 2 to node 4
	 	 I am transaction (4592016452dc7215913bea7029f2a6ff0c3cb2bb) giving 2 $ from node 2 to node 3
	 I am block with index 8
	 My Transaction list contains:
	 	 I am transaction (22b1776df3cd11faed623a33f0143d0497ed9af4) giving 3 $ from node 2 to node 0
	 	 I am transaction (8c2bd3d8acb1610a994d972003f85122057739ff) giving 4 $ from node 2 to node 4
	 I am block with index 9
	 My Transaction list contains:
	 	 I am transaction (56446fd35cbd00ca5595ed583353bb1db2d24ae6) giving 5 $ from node 2 to node 3
	 	 I am transaction (46a285e3651b33571ea19c5757fd31059d404849) giving 6 $ from node 2 to node 1
	 I am block with index 10
	 My Transaction list contains:
	 	 I am transaction (5a8ec7c0f99f6fbc4f20fc36ac69a92693da7eb9) giving 10 $ from node 2 to node 3
	 	 I am transaction (2e8fea2a5a21fbe2154ea2614611acbfc6e2f5b4) giving 1 $ from node 3 to node 2
	 I am block with index 11
	 My Transaction list contains:
	 	 I am transaction (3322428951970e1239ed073957e252e02a565759) giving 2 $ from node 3 to node 4
	 	 I am transaction (133b7695dfbbbeebc068687462f272194c2c9db5) giving 3 $ from node 3 to node 0
	 I am block with index 12
	 My Transaction list contains:
	 	 I am transaction (843797a9e5d1b0854876dd99248dd83de25e2002) giving 4 $ from node 3 to node 2
	 	 I am transaction (fb1236aa94f4e55fe778d32084c98905f28c9acc) giving 5 $ from node 3 to node 1
	 I am block with index 13
	 My Transaction list contains:
	 	 I am transaction (cb51a507ab01cae351eeb41cb71892ff97da9b52) giving 6 $ from node 3 to node 2
	 	 I am transaction (f818497c1d6e70aa9ba133362cf3b6dff1ad3f27) giving 7 $ from node 3 to node 2
	 I am block with index 14
	 My Transaction list contains:
	 	 I am transaction (40d8b89699b0df367495facd9331e7258d5af681) giving 8 $ from node 3 to node 4
	 	 I am transaction (2bf363cfe5bbcb5719055fcbc2c373cf540b75cb) giving 9 $ from node 3 to node 4
	 I am block with index 15
	 My Transaction list contains:
	 	 I am transaction (2a4886fd71f36fce15eb0549944b297331a703a3) giving 10 $ from node 3 to node 0
	 	 I am transaction (b7a2e5451c10c5bda77757fb3263ec1e126adad1) giving 2 $ from node 4 to node 0
	 I am block with index 16
	 My Transaction list contains:
	 	 I am transaction (2790d441348fe56b4e5bf9dd13cededf4b2cfadb) giving 1 $ from node 4 to node 3
	 	 I am transaction (83cbee64c7ec2accff282f6a5b9a5a83974156e7) giving 3 $ from node 4 to node 1
	 I am block with index 17
	 My Transaction list contains:
	 	 I am transaction (35a844537a4a84d6983fc3e834cd5f9391d0d8fa) giving 8 $ from node 4 to node 3
	 	 I am transaction (f7fb9bb4fe17806ee1683103aeff7e2cd58c87ae) giving 9 $ from node 4 to node 3
	 I am block with index 18
	 My Transaction list contains:
	 	 I am transaction (f7fb9bb4fe17806ee1683103aeff7e2cd58c87ae) giving 9 $ from node 4 to node 3
	 	 I am transaction (19c9492d1e50dee759ed6be007407d261f92b668) giving 1 $ from node 0 to node 1
	 I am block with index 19
	 My Transaction list contains:
	 	 I am transaction (f7fb9bb4fe17806ee1683103aeff7e2cd58c87ae) giving 9 $ from node 4 to node 3
	 	 I am transaction (35a844537a4a84d6983fc3e834cd5f9391d0d8fa) giving 8 $ from node 4 to node 3
	 I am block with index 20
	 My Transaction list contains:
	 	 I am transaction (29431c36112e958a44f81e43975495259277222e) giving 5 $ from node 0 to node 1
	 	 I am transaction (e11ae10e699decb5332d38c68dc084705d692124) giving 6 $ from node 0 to node 3
	 I am block with index 21
	 My Transaction list contains:
	 	 I am transaction (29431c36112e958a44f81e43975495259277222e) giving 5 $ from node 0 to node 1
	 	 I am transaction (253b81fd81576b0993973a2eeda532d90000f37a) giving 10 $ from node 4 to node 0
	 I am block with index 22
	 My Transaction list contains:
	 	 I am transaction (4d4eedc6e5da0f63f0a94d3d6ba2d3bd3c245b51) giving 9 $ from node 0 to node 4
	 	 I am transaction (3deca67678c32472b4441e264fa2619a343ffe70) giving 8 $ from node 0 to node 4


0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22

old curr
	 I am block with index 22
	 My Transaction list contains:
new curr
	 I am block with index 22
	 My Transaction list contains:
Old chain


Blockchain:
	 I am block with index 0
	 My Transaction list contains:
	 	 I am transaction (22638dedb224898aa6cae8cbd7cafb03ff303edc) giving 500 $ from node genesis to node 0
	 I am block with index 1
	 My Transaction list contains:
	 	 I am transaction (f3f596d61dfa65e51ff1c749ed8d9e39f4227f3a) giving 100 $ from node 0 to node 1
	 	 I am transaction (4d4366153409aaf2ea130d97affea9bf6c91c2bb) giving 100 $ from node 0 to node 2
	 I am block with index 2
	 My Transaction list contains:
	 	 I am transaction (01662993795fb5fd8093c5eb4414af9516606e8e) giving 100 $ from node 0 to node 3
	 	 I am transaction (c41568a85d921ed060a5f30a8ec96b7f255fec7e) giving 100 $ from node 0 to node 4
	 I am block with index 3
	 My Transaction list contains:
	 	 I am transaction (e3179905507f5ad52fc3922bfcfd435f3e8e4c53) giving 2 $ from node 1 to node 0
	 	 I am transaction (6b03130364cdbc9e6eb53eec293ac2168eae92e8) giving 3 $ from node 1 to node 3
	 I am block with index 4
	 My Transaction list contains:
	 	 I am transaction (f693990b4ba97ffa45974d842489e70d62b887e8) giving 4 $ from node 1 to node 0
	 	 I am transaction (52775aa21764f8c923c71c3aab103ac49444697c) giving 5 $ from node 1 to node 4
	 I am block with index 5
	 My Transaction list contains:
	 	 I am transaction (72f01b7c9ccea94888b00ed9ecaafe6d4ccb3eef) giving 6 $ from node 1 to node 3
	 	 I am transaction (1077a03e809bd5e682b27629a21afe6f8ade4df4) giving 7 $ from node 1 to node 2
	 I am block with index 6
	 My Transaction list contains:
	 	 I am transaction (0ad25cbffd27da14df38a4ae2aaf87cea69eb18d) giving 8 $ from node 1 to node 2
	 	 I am transaction (9970a5c0a373b7858e01a02a59859ad880278031) giving 9 $ from node 1 to node 0
	 I am block with index 7
	 My Transaction list contains:
	 	 I am transaction (1798cccfb048481cb904b2a0d7343f90941b9953) giving 1 $ from node 2 to node 4
	 	 I am transaction (4592016452dc7215913bea7029f2a6ff0c3cb2bb) giving 2 $ from node 2 to node 3
	 I am block with index 8
	 My Transaction list contains:
	 	 I am transaction (22b1776df3cd11faed623a33f0143d0497ed9af4) giving 3 $ from node 2 to node 0
	 	 I am transaction (8c2bd3d8acb1610a994d972003f85122057739ff) giving 4 $ from node 2 to node 4
	 I am block with index 9
	 My Transaction list contains:
	 	 I am transaction (56446fd35cbd00ca5595ed583353bb1db2d24ae6) giving 5 $ from node 2 to node 3
	 	 I am transaction (46a285e3651b33571ea19c5757fd31059d404849) giving 6 $ from node 2 to node 1
	 I am block with index 10
	 My Transaction list contains:
	 	 I am transaction (5a8ec7c0f99f6fbc4f20fc36ac69a92693da7eb9) giving 10 $ from node 2 to node 3
	 	 I am transaction (2e8fea2a5a21fbe2154ea2614611acbfc6e2f5b4) giving 1 $ from node 3 to node 2
	 I am block with index 11
	 My Transaction list contains:
	 	 I am transaction (3322428951970e1239ed073957e252e02a565759) giving 2 $ from node 3 to node 4
	 	 I am transaction (133b7695dfbbbeebc068687462f272194c2c9db5) giving 3 $ from node 3 to node 0
	 I am block with index 12
	 My Transaction list contains:
	 	 I am transaction (843797a9e5d1b0854876dd99248dd83de25e2002) giving 4 $ from node 3 to node 2
	 	 I am transaction (fb1236aa94f4e55fe778d32084c98905f28c9acc) giving 5 $ from node 3 to node 1
	 I am block with index 13
	 My Transaction list contains:
	 	 I am transaction (cb51a507ab01cae351eeb41cb71892ff97da9b52) giving 6 $ from node 3 to node 2
	 	 I am transaction (f818497c1d6e70aa9ba133362cf3b6dff1ad3f27) giving 7 $ from node 3 to node 2
	 I am block with index 14
	 My Transaction list contains:
	 	 I am transaction (40d8b89699b0df367495facd9331e7258d5af681) giving 8 $ from node 3 to node 4
	 	 I am transaction (2bf363cfe5bbcb5719055fcbc2c373cf540b75cb) giving 9 $ from node 3 to node 4
	 I am block with index 15
	 My Transaction list contains:
	 	 I am transaction (2a4886fd71f36fce15eb0549944b297331a703a3) giving 10 $ from node 3 to node 0
	 	 I am transaction (b7a2e5451c10c5bda77757fb3263ec1e126adad1) giving 2 $ from node 4 to node 0
	 I am block with index 16
	 My Transaction list contains:
	 	 I am transaction (2790d441348fe56b4e5bf9dd13cededf4b2cfadb) giving 1 $ from node 4 to node 3
	 	 I am transaction (83cbee64c7ec2accff282f6a5b9a5a83974156e7) giving 3 $ from node 4 to node 1
	 I am block with index 17
	 My Transaction list contains:
	 	 I am transaction (35a844537a4a84d6983fc3e834cd5f9391d0d8fa) giving 8 $ from node 4 to node 3
	 	 I am transaction (f7fb9bb4fe17806ee1683103aeff7e2cd58c87ae) giving 9 $ from node 4 to node 3
	 I am block with index 18
	 My Transaction list contains:
	 	 I am transaction (f7fb9bb4fe17806ee1683103aeff7e2cd58c87ae) giving 9 $ from node 4 to node 3
	 	 I am transaction (19c9492d1e50dee759ed6be007407d261f92b668) giving 1 $ from node 0 to node 1
	 I am block with index 19
	 My Transaction list contains:
	 	 I am transaction (f7fb9bb4fe17806ee1683103aeff7e2cd58c87ae) giving 9 $ from node 4 to node 3
	 	 I am transaction (35a844537a4a84d6983fc3e834cd5f9391d0d8fa) giving 8 $ from node 4 to node 3
	 I am block with index 20
	 My Transaction list contains:
	 	 I am transaction (29431c36112e958a44f81e43975495259277222e) giving 5 $ from node 0 to node 1
	 	 I am transaction (e11ae10e699decb5332d38c68dc084705d692124) giving 6 $ from node 0 to node 3
	 I am block with index 21
	 My Transaction list contains:
	 	 I am transaction (29431c36112e958a44f81e43975495259277222e) giving 5 $ from node 0 to node 1
	 	 I am transaction (253b81fd81576b0993973a2eeda532d90000f37a) giving 10 $ from node 4 to node 0
	 I am block with index 22
	 My Transaction list contains:
	 	 I am transaction (4d4eedc6e5da0f63f0a94d3d6ba2d3bd3c245b51) giving 9 $ from node 0 to node 4
	 	 I am transaction (3deca67678c32472b4441e264fa2619a343ffe70) giving 8 $ from node 0 to node 4


0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22

New Chain
