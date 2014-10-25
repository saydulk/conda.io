gulp = require "gulp"
gutil = require "gulp-util"
paths = require "../paths"
{spawn} = require "child_process"

createServer = ->
  prefix = gutil.colors.cyan "flask:"
  serverOutput = (data) ->
    data.replace /\s*$/, ""
      .split("\n")
      .forEach (line) ->
        gutil.log "#{prefix} #{gutil.colors.grey line}"

  server = spawn "python", ["server.py", ]
  server.stdout.setEncoding "utf8"
  server.stdout.on "data", serverOutput

  server.stderr.setEncoding "utf8"
  server.stderr.on "data", serverOutput

  server

gulp.task "default", ["build"], ->
  createServer()

  gulp.watch "source/coffee/**/*.*", ["scripts", ]
  gulp.watch paths.sass.src, ["sass", ]
