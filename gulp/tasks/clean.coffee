gulp = require "gulp"
clean = require "gulp-clean"

gulp.task "clean", ->
  dirs = [
    "build",
  ]
  for dir in dirs
    gulp.src dir
      .pipe clean()
