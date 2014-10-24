gulp = require "gulp"

simpleCopyTask = require "../utils/simpleCopyTask"

simpleCopyTask "html"
simpleCopyTask "bower"
# simpleCopyTask "requirejs"

gulp.task "copy", ["copy-html", "copy-bower", ]
