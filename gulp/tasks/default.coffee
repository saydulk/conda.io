gulp = require "gulp"
paths = require "../paths"

gulp.task "default", ["build"], ->
  gulp.watch "source/coffee/**/*.*", ["scripts", ]
  gulp.watch paths.sass.src, ["sass", ]
