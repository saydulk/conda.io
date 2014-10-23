coffee = require "gulp-coffee"
gulp = require "gulp"

paths = require "../paths"

gulp.task "coffee", ->
  gulp.src paths.coffee.src
    .pipe coffee
      sourceMap: true
    .pipe gulp.dest(paths.coffee.dest)
