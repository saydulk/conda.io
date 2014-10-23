gulp = require "gulp"
clean = require "gulp-clean"

gulp.task "clean", ->
  dirs = [
    "release/vendor"
    "release/coffee"
    "release/sass"
    "release/build.txt"
  ]
  for dir in dirs
    gulp.src dir
      .pipe clean()
