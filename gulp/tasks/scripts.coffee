browserify = require "browserify"
source = require "vinyl-source-stream"
gulp = require "gulp"
paths = require "../paths"

gulp.task "scripts", ->
  browserify paths.coffee.src
    .bundle()
    .pipe source paths.coffee.dest_filename
    .pipe gulp.dest paths.coffee.dest_path
