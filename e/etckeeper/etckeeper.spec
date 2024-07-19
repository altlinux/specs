%define _unpackaged_files_terminate_build 1

Name: etckeeper
Version: 1.18.21
Release: alt3
Summary: Etckeeper help to keep your /etc directory in VCS repository
License: GPL-2.0-or-later
Group: System/Configuration/Other
Url: https://etckeeper.branchable.com/
Vcs: https://git.joeyh.name/index.cgi/etckeeper.git
BuildArch: noarch
AutoReq: yes,noshell
Requires: coreutils diffutils findutils grep sh
Requires: git-core >= 1.6.0
Requires: perl-base
Obsoletes: %name-origin < %version-%release

Source: %name-%version.tar

%description
etckeeper is a collection of tools to let /etc be stored in a VCS
repository. It hooks into apt/yum/packman/etc to automatically commit
changes made to /etc during package upgrades. It's quite modular and
configurable, while also being simple to use if you understand the
basics of working with VCS.

%prep
%setup
sed -i '/^LOWLEVEL_PACKAGE_MANAGER=/s/=.*/=rpm/' etckeeper.conf
# No DPkg support, no empty lines.
sed -i '/^RPM::/!d' apt.conf
sed -i '/apt.apt.conf.d/s/05etckeeper/%name.conf/' Makefile
# We dont want bzr now:
sed -i '/etckeeper-bzr/d' Makefile
# There is no cruft package for ALT:
sed -i '/cruft/d' Makefile

%install
make install DESTDIR=%buildroot PYTHON=%__python3 systemddir=%_unitdir
install -Dp .gear/cron.daily %buildroot%_sysconfdir/cron.daily/%name

%check
grep -x LOWLEVEL_PACKAGE_MANAGER=rpm %buildroot%_sysconfdir/%name/etckeeper.conf
grep -x HIGHLEVEL_PACKAGE_MANAGER=apt %buildroot%_sysconfdir/%name/etckeeper.conf
find %buildroot -type f | xargs file | grep 'shell script' | cut -d: -f1 | xargs -n1 -t bash -n

%triggerin -- %name < 1.18.16
pl="/var/cache/etckeeper/packagelist.pre-install"
[ ! -e $pl ] || LC_COLLATE=C LC_ALL= sort -o $pl{,}

%files
%define _customdocdir %_docdir/%name
%doc README.md GPL CHANGELOG COPYRIGHT
%_bindir/%name
%_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/%name.conf
%_sysconfdir/apt/apt.conf.d/%name.conf
%_man8dir/%{name}.8*
/usr/share/bash-completion/completions/%name
/usr/share/zsh/vendor-completions/_etckeeper
%_cachedir/%name
%_sysconfdir/cron.daily/%name
%_unitdir/%{name}.*

%changelog
* Thu Jul 11 2024 Vitaly Chikunov <vt@altlinux.org> 1.18.21-alt3
- Fix FTBFS after usrmerge related systemd update.

* Thu Mar 21 2024 Vitaly Chikunov <vt@altlinux.org> 1.18.21-alt2
- pre-install.d/10packagelist: Fix hook run under non-root users.

* Tue Jan 09 2024 Vitaly Chikunov <vt@altlinux.org> 1.18.21-alt1
- Update to 1.18.21 (2023-11-28).

* Tue Jun 28 2022 Vitaly Chikunov <vt@altlinux.org> 1.18.8-alt2
- Fixed annoying 'egrep is obsolescent' warning.
- Updated License, Group, and Url tags.

* Sun Sep 30 2018 Terechkov Evgenii <evg@altlinux.org> 1.18.8-alt1
- 1.18.8

* Sat Aug 26 2017 Terechkov Evgenii <evg@altlinux.org> 1.18.7-alt1
- 1.18.7

* Sat Jun 25 2016 Terechkov Evgenii <evg@altlinux.org> 1.18.4-alt1
- 1.18.4

* Sat Apr  4 2015 Terechkov Evgenii <evg@altlinux.org> 1.18.1-alt1
- 1.18.1

* Sun Mar  1 2015 Terechkov Evgenii <evg@altlinux.org> 1.17-alt1
- 1.17

* Tue Oct 28 2014 Terechkov Evgenii <evg@altlinux.org> 1.15-alt1
- 1.15

* Sat Jun 28 2014 Terechkov Evgenii <evg@altlinux.org> 1.12-alt1
- 1.12

* Sat Sep 28 2013 Terechkov Evgenii <evg@altlinux.org> 1.9-alt1
- 1.9

* Mon Jun 24 2013 Terechkov Evgenii <evg@altlinux.org> 1.4-alt1
- 1.4

* Sun Dec 23 2012 Terechkov Evgenii <evg@altlinux.org> 0.64-alt1
- 0.64

* Sat Feb 18 2012 Terechkov Evgenii <evg@altlinux.org> 0.61-alt1
- 0.61
- Require perl again
- Require fresh git-core

* Wed Nov  9 2011 Terechkov Evgenii <evg@altlinux.org> 0.57-alt1
- 0.57

* Fri Sep 30 2011 Terechkov Evgenii <evg@altlinux.org> 0.56-alt1
- 0.56-87-ge3eadd8

* Sat Mar 19 2011 Terechkov Evgenii <evg@altlinux.org> 0.53-alt1
- 0.53
- Drop useless and dangerous etckeeper-origin

* Fri Jan 14 2011 Terechkov Evgenii <evg@altlinux.org> 0.51-alt2
- Update from upstream (ALT#24903)

* Mon Dec 27 2010 Terechkov Evgenii <evg@altlinux.org> 0.51-alt1
- 0.51

* Tue Dec  7 2010 Terechkov Evgenii <evg@altlinux.org> 0.50-alt6
- Workaround for #24678

* Wed Dec  1 2010 Terechkov Evgenii <evg@altlinux.org> 0.50-alt5.1
- Fixup postin script

* Wed Dec  1 2010 Terechkov Evgenii <evg@altlinux.org> 0.50-alt5
- git-20101201 (workaround for #24479)

* Thu Nov 11 2010 Terechkov Evgenii <evg@altlinux.org> 0.50-alt4
- etckeeper-origin

* Sun Nov  7 2010 Terechkov Evgenii <evg@altlinux.org> 0.50-alt3
- Futher filter out alt-specific hardlinked files complains

* Mon Oct 25 2010 Terechkov Evgenii <evg@altlinux.org> 0.50-alt2
- Drop useless /etc/skel* complains

* Sun Oct 24 2010 Terechkov Evgenii <evg@altlinux.org> 0.50-alt1
- 0.50

* Tue Sep 14 2010 Terechkov Evgenii <evg@altlinux.org> 0.49-alt1
- 0.49

* Sat Jul 17 2010 Terechkov Evgenii <evg@altlinux.ru> 0.48-alt1
- 0.48

* Mon May 31 2010 Terechkov Evgenii <evg@altlinux.ru> 0.47-alt1
- 0.47

* Mon May 17 2010 Terechkov Evgenii <evg@altlinux.ru> 0.46-alt1
- 0.46

* Fri Apr 16 2010 Terechkov Evgenii <evg@altlinux.ru> 0.45-alt1
- 0.45

* Thu Apr 15 2010 Terechkov Evgenii <evg@altlinux.ru> 0.44-alt1
- 0.44

* Fri Feb 19 2010 Terechkov Evgenii <evg@altlinux.ru> 0.43-alt1
- 0.43

* Fri Oct  2 2009 Terechkov Evgenii <evg@altlinux.ru> 0.41-alt2
- Package list generation fixed

* Sun Sep 27 2009 Terechkov Evgenii <evg@altlinux.ru> 0.41-alt1
- 0.41

* Thu Aug 27 2009 Terechkov Evgenii <evg@altlinux.ru> 0.40-alt1
- 0.40

* Thu Jul  9 2009 Terechkov Evgenii <evg@altlinux.ru> 0.38-alt1
- 0.38

* Sat Jul  4 2009 Terechkov Evgenii <evg@altlinux.ru> 0.37-alt2
- Document ETCKEEPER_CONF_DIR in man page (ALT #20587)
- Description updated

* Tue Jun  9 2009 Terechkov Evgenii <evg@altlinux.ru> 0.37-alt1
- 0.37

* Sun May 17 2009 Terechkov Evgenii <evg@altlinux.ru> 0.36-alt1
- 0.36

* Thu May 14 2009 Terechkov Evgenii <evg@altlinux.ru> 0.35-alt2
- Typo fixed (ALT #20038)
- Dont require perl anymore
- Dont build bzr plugin (requires python)

* Thu May  7 2009 Terechkov Evgenii <evg@altlinux.ru> 0.35-alt1
- 0.35

* Thu Apr 16 2009 Terechkov Evgenii <evg@altlinux.ru> 0.34-alt4
- Upgrade from etckeeper < 0.34-alt2 fixed (ALT #19638)

* Thu Apr  2 2009 Terechkov Evgenii <evg@altlinux.ru> 0.34-alt3
- Paths in precommit hook fixed

* Wed Apr  1 2009 Terechkov Evgenii <evg@altlinux.ru> 0.34-alt2
- Cron paths fixed

* Sat Mar 21 2009 Terechkov Evgenii <evg@altlinux.ru> 0.34-alt1
- 0.34

* Sun Feb  8 2009 Terechkov Evgenii <evg@altlinux.ru> 0.27-alt1.1
- Stupid typo in apt conf fixed

* Sun Feb  8 2009 Terechkov Evgenii <evg@altlinux.ru> 0.27-alt1
- 0.27

* Sat Sep 20 2008 Terechkov Evgenii <evg@altlinux.ru> 0.21-alt1
- 0.21

* Sat Jul 19 2008 Terechkov Evgenii <evg@altlinux.ru> 0.20-alt1
- 0.20
- Patch updated (obsoleted code removed, package list support for RPM added)
- Obsoleted fix removed from spec

* Sat Mar 22 2008 Terechkov Evgenii <evg@altlinux.ru> 0.12-alt1
- 0.12

* Sun Feb 10 2008 Terechkov Evgenii <evg@altlinux.ru> 0.10-alt2
- Unneeded patches removed

* Sat Feb  9 2008 Terechkov Evgenii <evg@altlinux.ru> 0.10-alt1
- 0.10

* Wed Jan  2 2008 Terechkov Evgenii <evg@altlinux.ru> 0.6-alt0
- Initial build for ALT Linux Sisyphus
