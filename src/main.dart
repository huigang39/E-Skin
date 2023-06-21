import 'package:flutter/material.dart';
import 'dart:io';
import 'dart:convert';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'E-Skin',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: MyHomePage(title: '电子皮肤手势信号分类'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  MyHomePage({Key? key, required this.title}) : super(key: key);

  final String title;

  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  TextEditingController _controller = TextEditingController();
  String _serverResponse = '';

  Future<void> _sendData() async {
    String ip = '10.67.104.154';

    Socket socket = await Socket.connect(ip, 12345);
    socket.writeln(_controller.text);
    await socket.flush();

    socket.listen((List<int> event) {
      setState(() {
        _serverResponse = utf8.decode(event);
      });
    });

    _controller.text = '';
    socket.close();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(widget.title),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Padding(
              padding: const EdgeInsets.all(30.0),
              child: TextField(
                controller: _controller,
                decoration: InputDecoration(
                  border: OutlineInputBorder(),
                  labelText: '输出采集的特征数据',
                ),
              ),
            ),
            ElevatedButton(
              onPressed: _sendData,
              child: Text('发送数据'),
            ),
            Padding(
              padding: const EdgeInsets.all(30.0),
              child: Text(
                '识别手势为: $_serverResponse',
                style: Theme.of(context).textTheme.titleLarge,
              ),
            ),
          ],
        ),
      ),
    );
  }
}