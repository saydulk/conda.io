gulp = require "gulp"
gutil = require "gulp-util"
paths = require "../paths"
{spawn} = require "child_process"
psTree = require "ps-tree"

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

  server.on "error", ->
    gutil.log "huh?"
  server.onUnexpectedExit = (code, signal) ->
    gutil.log gutil.colors.red "flask server has stopped with: #{code}"
    process.exit 1

  server.on "exit", server.onUnexpectedExit

  server.shutdown = (cb) ->
    gutil.log gutil.colors.red "flask shutdown initiated"
    @removeListener "exit", @onUnexpectedExit
    psTree server.pid, (err, children) ->
      kill = spawn('kill', ['-9'].concat(children.map (p) -> p.PID))
      kill.on "exit", ->
        server.kill "SIGTERM"
        cb() if cb?
  server

gulp.task "default", ["build"], ->
  server = createServer()

  gulp.watch "source/coffee/**/*.*", ["scripts", ]
  gulp.watch paths.sass.watch, ["sass", ]

  process.handleExit = ->
    gutil.log "calling server.shutodwn"
    server.shutdown

  process.once "exit", process.handleExit
  process.once "SIGTERM", process.exit
  process.once "SIGINT", process.exit

  process.once "uncaughtException", (e) ->
    if process.listeners("uncaughtException").length is 0
      process.removeListener "exit", process.handleExit
      server.shutdown ->
        throw e
