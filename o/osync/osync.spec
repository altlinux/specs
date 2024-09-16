Name: 	  osync
Version:  1.3
Release:  alt1

Summary:  A robust two way (bidirectional) file sync script based on rsync with fault tolerance
License:  BSD
Group:    Other
Url: 	  http://www.netpower.fr/osync
# VCS:	  https://github.com/deajan/osync

Packager: Andrey Cherepanov <cas@altlinux.org>

Source:   %name-%version.tar
Patch:    %name-services.patch

BuildArch: noarch
%filter_from_requires /^\/usr\/bin\/mail.php$/d

%description
A two way filesync script with fault tolerance, resuming, deletion
backup and conflict backups running on linux and virtually any system
supporting bash. File synchronization is bidirectional, based on rsync,
and can be run manually, by cron, or triggered via inotifytools
(whenever a file changes on master, a file sync is triggered).

%prep
%setup
%patch -p1
# Replace all /usr/local/bin by /usr/bin
subst 's,/usr/local/bin,%_bindir,g' *.lyx *.sh osync*srv* *.md *.service*

%install
export BUILDROOT=%buildroot
./install.sh --no-stats
install -Dp -m 0644 sync.conf.example %buildroot%_sysconfdir/osync/sync.conf
# Fix command interpreter for executables
subst '1,1 s,^.*,#!/bin/bash,' %buildroot%_bindir/*.sh

%post
%post_service osync-srv

%preun
%preun_service osync-srv

%files
%doc *.md *.lyx
%_bindir/*
%dir %_sysconfdir/osync/
%config(noreplace) %_sysconfdir/osync/sync.conf
%_sysconfdir/osync/*.example
%_initdir/osync-srv
%_initdir/osync-target-helper-srv
%_unitdir/*.service
%_userunitdir/*.service.user

%changelog
* Mon Sep 16 2024 Andrey Cherepanov <cas@altlinux.org> 1.3-alt1
- New version.

* Sun Mar 26 2017 Andrey Cherepanov <cas@altlinux.org> 1.2-alt1
- New version

* Sat Jan 28 2017 Andrey Cherepanov <cas@altlinux.org> 1.1.5-alt1
- new version 1.1.5

* Tue Jun 14 2016 Andrey Cherepanov <cas@altlinux.org> 1.1-alt2.rc1.1.git99d923f
- New version from upstream Git
- Package systemd services and tests

* Mon Sep 14 2015 Andrey Cherepanov <cas@altlinux.org> 1.01-alt1
- New version

* Thu Jun 25 2015 Andrey Cherepanov <cas@altlinux.org> 1.0-alt0.1.pre.gitd765bef
- Initial build for ALT Linux
