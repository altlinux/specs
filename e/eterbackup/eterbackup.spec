Name: eterbackup
Version: 0.3
Release: alt1

Summary: Etersoft backup tools for journaling backup

License: AGPLv3
Group: System/Configuration/Packaging
Url: https://github.com/vitlav/eterbackup

Packager: Vitaly Lipatov <lav@altlinux.ru>

# git-clone http://git.etersoft.ru/projects/korinf/eterbackup.git
Source: ftp://updates.etersoft.ru/pub/Etersoft/Sisyphus/sources/tarball/%name-%version.tar

BuildArchitectures: noarch

Requires: zpaq >= 705

%description
Etersoft Backup Tools intended for resolve typical backup tasks.
- eterpack is a tool for condensing files from a directory tree to one archive file.
- etertimemachine is a tool for backup and/or rotate file tree every time.

See detailed russian description here: http://wiki.etersoft.ru/Eterbackup

%prep
%setup

%install
# install to datadir and so on
%makeinstall version=%version-%release

#mkdir -p %buildroot%_sysconfdir/bash_completion.d/
#install -m 0644 bash_completion/erc %buildroot%_sysconfdir/bash_completion.d/erc

# shebang.req.files
#chmod a+x %buildroot%_datadir/%name/{erc-}*

%files
%doc README.md LICENSE TODO
%_bindir/eterpack
%_bindir/etertimemachine
#%_datadir/%name/
%_man1dir/*
#%_sysconfdir/bash_completion.d/erc

%changelog
* Sun Jul 19 2015 Vitaly Lipatov <lav@altlinux.ru> 0.3-alt1
- eterpack: add --execute option
- eterpack: backup root files too
- eterpack: fix DESTDIR heuristic
- eterpack: write dirs.list and files.list

* Sat Jul 18 2015 Vitaly Lipatov <lav@altlinux.ru> 0.2-alt1
- initial build for ALT Linux Sisyphus
