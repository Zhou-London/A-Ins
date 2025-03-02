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

Future<Map<String, List<String>>> getHomePageData(likeList) async {
  final url = Uri.parse('http://127.0.0.1:5000/require');
  final response = await http.post(url, headers: {'Content-Type': 'application/json'}, body: jsonEncode({'likeList': jsonEncode(likeList)}));
  if (response.statusCode == 200) {
    final result = jsonDecode(response.body);
    return result;
  } else {
    print(response.reasonPhrase);
    return {};
  }
}
