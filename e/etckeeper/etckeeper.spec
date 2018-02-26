%define _unpackaged_files_terminate_build 1

Name: etckeeper
Version: 0.61
Release: alt1

Summary: Etckeeper help to keep your /etc directory in VCS repository
License: GPL2+
Group: Development/Other
Url: http://kitenet.net/~joey/code/etckeeper/
Source: %name-%version.tar
Patch: %name-%version-%release.patch
BuildArch: noarch
AutoReq: yes,noshell
Requires: coreutils diffutils findutils grep sh
Requires: git-core >= 1.6.0
Requires: perl-base
Obsoletes: %name-origin < %version-%release

Packager: Evgenii Terechkov <evg@altlinux.org>

%description
etckeeper is a collection of tools to let /etc be stored in a VCS
repository. It hooks into apt/yum/packman/etc to automatically commit
changes made to /etc during package upgrades. It's quite modular and
configurable, while also being simple to use if you understand the
basics of working with VCS.

%prep
%setup
%patch -p1

%build
%install
make install DESTDIR=%buildroot
install -D debian/cron.daily %buildroot%_sysconfdir/cron.daily/%name

# We dont want bzr now:
rm -rf %buildroot%_libdir/python*
# There is no cruft package for ALT:
rm -rf %buildroot%_sysconfdir/cruft

%post
if [ -e %_sysconfdir/.git/hooks/pre-commit ] && egrep '^(/us[rb]/s?bin/)?%name' %_sysconfdir/.git/hooks/pre-commit >/dev/null 2>&1; then
 echo "Replacing path to etckeeper in %_sysconfdir/.git/hooks/pre-commit"
 sed -i 's!^/usr/sbin/etckeeper!etckeeper!;s!^/usr/bin/etckeeper!etckeeper!;s!^/usb/sbin/etckeeper!etckeeper!' %_sysconfdir/.git/hooks/pre-commit
fi

%files
%_bindir/%name
%_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/%name.conf
%_sysconfdir/apt/apt.conf.d/%name.conf
%_man8dir/%{name}.*
%_sysconfdir/bash_completion.d/%name
%_cachedir/%name
%_sysconfdir/cron.daily/%name
%doc README TODO

%changelog
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
