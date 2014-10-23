browserify = require "gulp-browserify"
gulp = require "gulp"
paths = require "../paths"
rename = require "gulp-rename"

opts =
  extensions: [".coffee", ]
  transform: ['coffeeify', ]

gulp.task "scripts", ["coffee"], ->
  gulp.src("#{paths.coffee.src}", { read: false })
    .pipe browserify opts
    .pipe rename paths.coffee.dest_filename
    .pipe gulp.dest paths.coffee.dest_path
