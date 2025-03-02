import 'package:flutter/material.dart';
import 'package:flutter_staggered_grid_view/flutter_staggered_grid_view.dart';
import 'dart:convert';
import 'dart:io';
import 'dart:typed_data';
// import 'api.dart';
// import 'package:image/image.dart' as img;

List<bool> likeList = [false, false, false, false, false, false];

void main() {
  WidgetsFlutterBinding.ensureInitialized();

  runApp(
    MaterialApp(
      theme: ThemeData(
          colorScheme: ColorScheme.fromSeed(seedColor: Colors.lightBlueAccent),
          useMaterial3: true,
      ),
      home: HomePage(),
    ),
  );
}

class DisplayCard extends StatelessWidget {
  const DisplayCard({super.key, required this.displayImagePath, required this.text, required this.content, required this.id});

  final String displayImagePath;
  final String text;
  final String content;
  final int id;

  @override
  Widget build(BuildContext context) {
    Image imageFile = Image.asset(displayImagePath);
    // final fileName = displayImagePath.split('.');
    // Image imageFile;
    // if (fileName[1] == 'jpg'){
    //   imageFile = await img.decodeJpgFile(displayImagePath);
    // } else if(fileName[1] == 'png') {
    //   imageFile = img.decodePngFile(displayImagePath);
    // }
  
    return GestureDetector(
      onTap: () {
        Navigator.push(
          context, 
          MaterialPageRoute(
            builder: (context) => InformationPage(displayImagePath: displayImagePath, text: text, content: content, id: id)));
      },
      child: Container(
        decoration: BoxDecoration(
          color: Colors.white,
          borderRadius: BorderRadius.circular(12),
          boxShadow: [
            BoxShadow(
              color: Colors.grey,
              blurRadius: 2,
            ),
          ],
        ),
        child: ClipRRect(
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            mainAxisSize: MainAxisSize.min,
            children: [
              imageFile,
              const SizedBox(height: 10),
              Text(overflow: TextOverflow.ellipsis, style: TextStyle(fontWeight: FontWeight.bold), maxLines: 2, text)
            ],
          ),
        )
      ),
    );
  }
}

class HomePage extends StatefulWidget {
  const HomePage({super.key});

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  List<String> imagePathList = [
    'assets/images/out_blender.png',
    'assets/images/out_sakiko.png',
    'assets/images/out_table.png',
    'assets/images/out_ue.png',
    'assets/images/out_uika.png',
    'assets/images/out_flower.png'
  ];
  List<String> textList = [
    'This is an image about blender.',
    'This is an image about theree images.',
    'This is an image about a table with one computer and three drinks and a bag of tissue.',
    'This is an image about unreal engine.',
    'This is an image about a drawing of Uika.',
    'This is an image about a flower.'
  ];
  List<String> contentList = [
    'I am working on blender...',
    'This is crazy',
    'I am attending HackLondon',
    'I am working with Unreal Engine',
    'What a beautful drawing of Uika',
    'This flower is genreated by AI'
  ];
  List<List<String>> tagList = [
    ['technology', 'art'],
    ['amusement', 'art'],
    ['technology'],
    ['technology', 'art'],
    ['art'],
    ['art']
  ];

  void empty() {
    print('An empty void');
  }

  Future<void> deleteImage(imagePath) async {
    final file = File(imagePath);
    if (await file.exists()) {
      await file.delete();
    }
  }

  Future<void> processImage(img, id) async {
    Uint8List bytes = base64Decode(img);

    String filePath = 'assets/images/$id.png';

    File file = File(filePath);
    await file.writeAsBytes(bytes);
  }

  Future<void> refresh() async {
    empty();
    // final result = await getHomePageData();
    // setState(() {
    //   for (int i = 0; i < imagePathList.length; i++) {
    //     deleteImage(imagePathList[i]);
    //   }
    //   imagePathList = [];
    //   likeList = [];
    //   for (int i = 0; i < result['imagePathList']!.length; i++) {
    //     processImage(result['imagePathList']![i], i);
    //     imagePathList.add('assets/images/$i.png');
    //     likeList.add(false);
    //   }
    //   textList = result['textList']!;
    //   contentList = result['contentList']!;
    // });
    return Future<void>.delayed(Duration(seconds: 3));
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        actions: [
          IconButton(onPressed: empty, icon: Icon(Icons.menu))
        ],
      ),
      body: RefreshIndicator(
        onRefresh: () async {
          refresh();
        },
        child: MasonryGridView.count(
          crossAxisCount: 2, 
          crossAxisSpacing: 5,
          mainAxisSpacing: 5,
          itemCount: 6,
          itemBuilder: (content, index) {
            return DisplayCard(displayImagePath: imagePathList[index], text: textList[index],content: contentList[index], id: index);
          }
      ),
      )
    );
  }
}

class InformationPage extends StatefulWidget {
  const InformationPage({super.key, required this.displayImagePath, required this.text, required this.content, required this.id});

  final String displayImagePath;
  final String text;
  final String content;
  final int id;

  @override
  State<InformationPage> createState() => _InformationPageState();
}

class _InformationPageState extends State<InformationPage> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        actions: [
          if (likeList[widget.id])
          Icon(Icons.favorite, color: Colors.pink)
      ],),
      body: GestureDetector(
        onDoubleTap: () {
          setState(() {
            likeList[widget.id] = !likeList[widget.id];
          });
        },
        child: SingleChildScrollView(
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Image.asset(widget.displayImagePath),
              Text(
                widget.text, 
                style: TextStyle(fontSize: 20),
                textAlign: TextAlign.left,
              ),
              SizedBox(height: 5),
              Text(
                widget.content,
                textAlign: TextAlign.left
              ),
              SizedBox(height: 50)
            ],
          ),
        ),
      ),
    );
  }
}