Name: 	  osync
Version:  1.1.5
Release:  alt1

Summary:  A robust two way (bidirectional) file sync script based on rsync with fault tolerance
License:  BSD
Group:    Other
Url: 	  http://www.netpower.fr/osync
# VCS:	  https://github.com/deajan/osync

Packager: Andrey Cherepanov <cas@altlinux.org>

Source:   %name-%version.tar
Patch:    %name-%version-%release.patch

BuildArch: noarch
%filter_from_requires /^\/usr\/local\/bin\/mail.php$/d

%description
A two way filesync script with fault tolerance, resuming, deletion
backup and conflict backups running on linux and virtually any system
supporting bash. File synchronization is bidirectional, based on rsync,
and can be run manually, by cron, or triggered via inotifytools
(whenever a file changes on master, a file sync is triggered).

%prep
%setup
%patch -p1

%install
export DESTDIR=%buildroot
mkdir -p $DESTDIR
./install.sh --no-stats
install -Dp -m 0644 sync.conf %buildroot%_sysconfdir/osync/sync.conf

%post
%post_service osync-srv

%preun
%preun_service osync-srv

%files
%doc *.md *.lyx tests
%_bindir/*
%dir %_sysconfdir/osync/
%config(noreplace) %_sysconfdir/osync/sync.conf
%_initdir/osync-srv
%_unitdir/*.service
%_sysconfdir/systemd/user/*.service.user

%changelog
* Sat Jan 28 2017 Andrey Cherepanov <cas@altlinux.org> 1.1.5-alt1
- new version 1.1.5

* Tue Jun 14 2016 Andrey Cherepanov <cas@altlinux.org> 1.1-alt2.rc1.1.git99d923f
- New version from upstream Git
- Package systemd services and tests

* Mon Sep 14 2015 Andrey Cherepanov <cas@altlinux.org> 1.01-alt1
- New version

* Thu Jun 25 2015 Andrey Cherepanov <cas@altlinux.org> 1.0-alt0.1.pre.gitd765bef
- Initial build for ALT Linux
