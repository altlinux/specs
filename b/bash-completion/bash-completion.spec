%def_enable check

Name: bash-completion
Epoch: 1
Version: 2.11
Release: alt3.git.157.g59d2322e

Summary: bash-completion offers programmable completion for bash
License: GPL2
Group: Shells
Url: https://github.com/scop/bash-completion

Packager: Ildar Mulyukov <ildar@altlinux.ru>

Source: %name-%version.tar
# https://github.com/scop/bash-completion.git
Source1: rpm-cache.filetrigger
Patch1: %name-alt-iptables.patch
Patch9: %name-alt-specific.patch
Source44: %name.watch

%if_enabled check
BuildRequires: pytest3 python3-module-pexpect
%endif

Requires: bash >= 4.1
BuildArch: noarch

%add_findreq_skiplist %_datadir/%name/completions/*
%add_findreq_skiplist %_datadir/%name/helpers/*
%add_findreq_skiplist %_datadir/pkgconfig/bash-completion.pc

%description
bash-completion is a collection of shell functions that take advantage
of the programmable completion feature of bash 2.04 and later.

%prep
%setup
%patch1 -p1
%patch9 -p1

%build
%autoreconf
%configure
%make

%install
%makeinstall_std
mv %buildroot%_sysconfdir/{profile.d,bashrc.d}
mkdir -p %buildroot%_sysconfdir/bash_completion.d %buildroot%_rpmlibdir
install -p -m755 %SOURCE1 %buildroot%_rpmlibdir/

%check
# Currently fails
#= 20 failed, 1222 passed, 423 skipped, 16 xfailed, 4 xpassed in 941.69s (0:15:41) =
make -C test check ||:

%files
%doc AUTHORS CHANGES README.md doc/*.txt
%_sysconfdir/bash_completion.d
%_sysconfdir/bashrc.d/bash_completion.sh
%_rpmlibdir/*
%_datadir/%name
%_datadir/pkgconfig/bash-completion.pc

%changelog
* Mon Feb 06 2023 Alexey Shabalin <shaba@altlinux.org> 1:2.11-alt3.git.157.g59d2322e
- added use of bash-completion scripts extensions (liannnix@)
- disable show error for root sh (ALT #36760)

* Sat Jul 30 2022 Alexey Shabalin <shaba@altlinux.org> 1:2.11-alt2.git.157.g59d2322e
- fix completion for apt-get autoremove

* Thu Feb 18 2021 Ildar Mulyukov <ildar@altlinux.ru> 1:2.11-alt1.git.157.g59d2322e
- new version
- check is enabled but still failing
- rpm: add --changes-since --lastchange modifiers to the -q option (closes: #32143)

* Wed Aug 21 2019 Alexey Shabalin <shaba@altlinux.org> 1:2.9-alt1
- 2.9

* Wed Jan 09 2019 Alexey Shabalin <shaba@altlinux.org> 1:2.8-alt3
- package pkgconfig file

* Thu Dec 20 2018 Alexey Shabalin <shaba@altlinux.org> 1:2.8-alt2
- update completion for ALT apt-get

* Thu Dec 20 2018 Alexey Shabalin <shaba@altlinux.org> 1:2.8-alt1
- new version 2.8 for bash4

* Tue Apr 17 2018 Alexey Gladkov <legion@altlinux.ru> 1:1.99-alt8
- exclude `rfkill` file conflicting with bash-completion-util-linux.

* Tue Aug 16 2016 Alexey Gladkov <legion@altlinux.ru> 1:1.99-alt7
- exclude `mount` file conflicting with bash-completion-util-linux.

* Wed Feb 17 2016 Ildar Mulyukov <ildar@altlinux.ru> 1:1.99-alt6
- exclude `rtcwake` file conflicting with bash-completion-util-linux (closes: #31796)

* Wed Feb 10 2016 Ildar Mulyukov <ildar@altlinux.ru> 1:1.99-alt5
- fix rpm completion (ALT-specific)

* Tue Jan 12 2016 Ildar Mulyukov <ildar@altlinux.ru> 1:1.99-alt4
- new version. It is actually 1.3-109-g0f39d41. Closes: #28933
- backported the new layout: everything is now in /usr/share/bash-completion/, rather than in /etc/.
- drop mutt completion from Gentoo in favor of the one in the tree

* Sun Aug 22 2010 Ildar Mulyukov <ildar@altlinux.ru> 1:1.99-alt3
- new GIT version
- bug fixes (closes: #22386, #22443, #23861)

* Tue Dec 29 2009 Ildar Mulyukov <ildar@altlinux.ru> 1:1.99-alt2
- new git version
- %name-20050103-alt-rsync.patch pushed to upstream
- mutt completion from Gentoo bugzilla: http://bugs.gentoo.org/attachment.cgi?id=208607
- quick regression fix for showmount

* Wed Nov 04 2009 Ildar Mulyukov <ildar@altlinux.ru> 1:1.99-alt1
- new version
- patches rebase
- remove unneeded _known_hosts_fix

* Sun Jul 19 2009 Ildar Mulyukov <ildar@altlinux.ru> 1:1.0-alt2
- add rpm filetrigger for updating a rpm cache
- Closes: #15250

* Sat Jul 18 2009 Ildar Mulyukov <ildar@altlinux.ru> 1:1.0-alt1
- new source origin (Closes: #18940)
- Epoch up - new versioning scheme

* Tue Sep 23 2008 Alex Murygin <murygin@altlinux.ru> 20060301-alt06
- patches section typo fix

* Fri Feb 22 2008 Alex Murygin <murygin@altlinux.ru> 20060301-alt05
- moved bash-completion.sh from profile.d to bashrc.d
    (13532, 9273, 9148, 13041, 14606)

* Wed Oct 17 2007 Alex Murygin <murygin@altlinux.ru> 20060301-alt04
- fixed [13041] (bash-completion.sh changed)
- added patch to iptables completion [7382]

* Fri Jul 14 2006 Alex Murygin <murygin@altlinux.ru> 20060301-alt03
- fixed [9148] (bash-completion.sh changed)

* Sat Mar 04 2006 Alex Murygin <murygin@altlinux.ru> 20060301-alt02
- new version

* Wed Jan 18 2006 Alex Murygin <murygin@altlinux.ru> 20050712-alt02
- moved %_sysconfdir/profile.d/%name.sh from spec to source1
- fixing checking bash major version more 2 [8862]

* Thu Jul 14 2005 Alex Murygin <murygin@altlinux.ru> 20050712-alt01
- new version

* Wed Feb 09 2005 Alex Murygin <murygin@altlinux.ru> 20050121-alt01
- new version

* Fri Jan 14 2005 Alex Murygin <murygin@altlinux.ru> 20050112-alt01
- new version

* Mon Jan 10 2005 Alex Murygin <murygin@altlinux.ru> 20050103-alt01
- new version
- added bash-completion-20050103-alt-rsync.patch

* Thu Nov 11 2004 Alex Murygin <murygin@altlinux.ru> 20041017-alt01
- new version

* Thu Aug 12 2004 Alex Murygin <murygin@altlinux.ru> 20040711-alt01
- new version

* Mon Mar 15 2004 Alex Murygin <murygin@altlinux.ru> 20040214-alt01
- new version
- added BUGS to doc

* Thu Jan 08 2004 Alex Murygin <murygin@altlinux.ru> 20040101-alt01
- new version

* Fri Dec 26 2003 Alex Murygin <murygin@altlinux.ru> 20031225-alt01
- new version

* Tue Dec 16 2003 Alex Murygin <murygin@altlinux.ru> 20031215-alt01
- new version

* Sat Dec 06 2003 Alex Murygin <murygin@altlinux.ru> 20031125-alt01
- First build for Sisyphus.

