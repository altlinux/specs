Name: 	  osync
Version:  1.01
Release:  alt1

Summary:  A robust two way (bidirectional) file sync script based on rsync with fault tolerance
License:  BSD
Group:    Other
Url: 	  http://www.netpower.fr/osync
# VCS:	  https://github.com/deajan/osync

Packager: Andrey Cherepanov <cas@altlinux.org>

Source:   %name-%version.tar

BuildArch: noarch

%description
A two way filesync script with fault tolerance, resuming, deletion
backup and conflict backups running on linux and virtually any system
supporting bash. File synchronization is bidirectional, based on rsync,
and can be run manually, by cron, or triggered via inotifytools
(whenever a file changes on master, a file sync is triggered).

%prep
%setup

%install
install -Dm 0644 sync.conf %buildroot%_sysconfdir/osync/sync.conf.example
install -Dm 0644 exclude.list.example %buildroot%_sysconfdir/osync/exclude.list.example
install -Dm 0755 osync.sh %buildroot%_bindir/osync.sh
install -Dm 0755 osync-batch.sh %buildroot%_bindir/osync-batch.sh
install -Dm 0644 osync-srv %buildroot%_initdir/osync-srv

%post
%post_service osync-srv

%preun
%preun_service osync-srv

%files
%doc *.md *.txt *.lyx
%_bindir/*
%_sysconfdir/osync/
%_initdir/osync-srv

%changelog
* Mon Sep 14 2015 Andrey Cherepanov <cas@altlinux.org> 1.01-alt1
- New version

* Thu Jun 25 2015 Andrey Cherepanov <cas@altlinux.org> 1.0-alt0.1.pre.gitd765bef
- Initial build for ALT Linux
