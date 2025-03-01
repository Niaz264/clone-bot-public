from bot import CMD_INDEX

class _BotCommands:
    def __init__(self) -> None:
        self.StartCommand = f'start{CMD_INDEX}'
        self.MirrorCommand = f'm1{CMD_INDEX}'
        self.UnzipMirrorCommand = f'unzipx{CMD_INDEX}'
        self.ZipMirrorCommand = f'zipx{CMD_INDEX}'
        self.CancelMirror = f'cancelx{CMD_INDEX}'
        self.CancelAllCommand = f'cancelallx{CMD_INDEX}'
        self.ListCommand = f'd{CMD_INDEX}'
        self.SearchCommand = f'sea{CMD_INDEX}'
        self.StatusCommand = f'statusx{CMD_INDEX}'
        self.AuthorizedUsersCommand = f'users{CMD_INDEX}'
        self.AuthorizeCommand = f'authorize{CMD_INDEX}'
        self.UnAuthorizeCommand = f'unauthorize{CMD_INDEX}'
        self.AddSudoCommand = f'addsudo{CMD_INDEX}'
        self.RmSudoCommand = f'rmsudo{CMD_INDEX}'
        self.PingCommand = f'p{CMD_INDEX}'
        self.RestartCommand = f'restart{CMD_INDEX}'
        self.StatsCommand = f'statsx{CMD_INDEX}'
        self.HelpCommand = f'htp{CMD_INDEX}'
        self.LogCommand = f'logx{CMD_INDEX}'
        self.CloneCommand = f'clonex{CMD_INDEX}'
        self.CountCommand = f'countx{CMD_INDEX}'
        self.WatchCommand = f'watchx{CMD_INDEX}'
        self.ZipWatchCommand = f'zipwatchx{CMD_INDEX}'
        self.DeleteCommand = f'delx{CMD_INDEX}'
        self.ShellCommand = f'shellx{CMD_INDEX}'
        self.ExecHelpCommand = f'exechelp{CMD_INDEX}'
        self.LeechSetCommand = f'leechsetx{CMD_INDEX}'
        self.SetThumbCommand = f'setthumbx{CMD_INDEX}'
        self.LeechCommand = f'leechx{CMD_INDEX}'
        self.UnzipLeechCommand = f'unzipleechx{CMD_INDEX}'
        self.ZipLeechCommand = f'zipleechx{CMD_INDEX}'
        self.LeechWatchCommand = f'leechwatchx{CMD_INDEX}'
        self.LeechZipWatchCommand = f'leechzipwatchx{CMD_INDEX}'
        
BotCommands = _BotCommands()
