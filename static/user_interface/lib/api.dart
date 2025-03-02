import 'dart:convert';

import 'package:http/http.dart' as http;

Future<String> transferImage(base64Image) async {
  final url = Uri.parse('http://127.0.0.1:5000/image');
  final response = await http.post(url,headers: {'Content-Type': 'application/json'}, body: jsonEncode({'image': base64Image}));

  if (response.statusCode == 200) {
    return 'Sent';
  } else {
    return response.reasonPhrase.toString();
  }
}

Future<Map<String, List<String>>> getHomePageData() async {
  final url = Uri.parse('http://10.97.186.194:8000/get');
  final response = await http.get(url);
  if (response.statusCode == 200) {
    final result = jsonDecode(response.body);
    return result;
  } else {
    print(response.reasonPhrase);
    return {};
  }
}
