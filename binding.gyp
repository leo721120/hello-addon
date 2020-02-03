{
  "targets": [
    {
      "target_name": "hello",
      "sources": [
        "src/main.cpp"
      ],
      "include_dirs": [
        "<!(node -e \"require('nan')\")",
      ],
    },
    {
      "target_name": "copy",
      "type":"none",
      "dependencies" : [
        "hello",
      ],
      "copies":
      [
        {
            'destination': '<(module_root_dir)/out',
            'files': ['<(module_root_dir)/build/Release/hello.node']
        },
      ],
    },
  ]
}