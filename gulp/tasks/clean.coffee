gulp = require "gulp"
del = require "del"
vinylPaths = require "vinyl-paths"

gulp.task "clean", ->
  dirs = [
    "build",
  ]
  for dir in dirs
    gulp.src dir
      .pipe vinylPaths del
