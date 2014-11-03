coffee = require "gulp-coffee"
gulp = require "gulp"
livereload = require "gulp-livereload"

paths = require "../paths"

gulp.task "coffee", ->
  gulp.src paths.coffee.src
    .pipe coffee sourceMap: true
    .pipe gulp.dest(paths.coffee.dest_path)
    .pipe livereload auto: false
