%define _unpackaged_files_terminate_build 1
%define oname space.shad.alt-mirror-switcher

Name: alt-mirror-switcher
Version: 1.1.0
Release: alt1

Summary: Simple local mirror switcher for ALT

License: GPLv2+
Group: Other

Url: https://altlinux.space/shad/alt-mirror-switcher

BuildArch: noarch

Source: %name-%version.tar

%add_python3_path %_datadir/%name

BuildRequires(pre): rpm-build-python3

%description
%summary.

%package lists-sisyphus
Summary: Additional mirrors for %name
Group: Other
BuildArch: noarch
Requires: %name = %EVR
Conflicts: %name-lists-branch
%description lists-sisyphus
Additional mirrors for %name.

%package lists-branch
Summary: Additional mirrors for %name
Group: Other
BuildArch: noarch
Requires: %name = %EVR
Conflicts: %name-lists-sisyphus
%description lists-branch
Additional mirrors for %name.

%package cli
Summary: A terminal simple local mirror switcher for ALT
Group: Other
BuildArch: noarch
BuildRequires: perl-String-Util perl-Date-Calc perl-Config-Tiny
%description cli
A terminal simple local mirror switcher for ALT.

%prep
%setup
rm -v mirrors/ams.sh

%build
%install
install -d %buildroot
%make_install \
    SHAREDIR=%buildroot%_datadir \
    PREFIXBIN=%buildroot%_bindir

install -d %buildroot%_sysconfdir/apt/sources.list.d
mv %buildroot%_datadir/%name/mirrors/*.list \
  %buildroot%_sysconfdir/apt/sources.list.d/
rm -r %buildroot%_datadir/%name/mirrors

%find_lang %name --all-name

%post
if [ "$1" -eq 2 ]; then
   python3 %_datadir/%name/ams_check.py
fi

%files -f %name.lang
%_bindir/%name
%_datadir/%name
%_datadir/metainfo/%oname.metainfo.xml
%_desktopdir/%oname.desktop
%doc README.md

%files lists-sisyphus
%_sysconfdir/apt/sources.list.d/ams_*_sisyphus.list

%files lists-branch
%_sysconfdir/apt/sources.list.d/ams_*_branch.list

%files cli
%_bindir/ams

%changelog
* Tue Jul 07 2026 Aleksandr Shamaraev <shad@altlinux.org> 1.1.0-alt1
- added metainfo file
- cli: added automatic switch http -> https if http exists and choosed
- cli: fixed showing active mirror and enabled protocol when used ams.list
- added autofix if enabled >1 system repo list

* Wed Jun 24 2026 Aleksandr Shamaraev <shad@altlinux.org> 1.0.0-alt1
- cli: added command for enable sources.list and disable or not disable all system lists
- cli: added show command as an alternative active command
- cli: added list command as an alternative mirror command
- cli: added command for do not write config file
- cli: automatic write config file if GUI ams and conf exist for sync
- cli: added command for showing active mirror and enabled protocol
- cli: added command for not do automatic restore active list if GUI ams and conf exist
- cli: added command for not disable sources.list and not do automatic restore active list if GUI ams and conf exist
- cli: added command for ignoring sources.list and not disable it
- cli: fixed: some errors
- cli: automatic restored mirror from GUI utility config file if exists

* Fri May 29 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.10.1-alt1
- excluded: update.altsp.ru mirror
- cli: fixed: Use of uninitialized value

* Thu May 14 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.10.0-alt1
- cli: added set Sisyphus archive date
- cli: added show version number
- cli: splitted into several execution commands (use: ams --help)

* Tue May 05 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.9.5-alt1
- 0.9.4 -> 0.9.5

* Mon May 04 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.9.4-alt1
- gui: shortened time: mirror speed tests

* Fri Apr 17 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.9.3-alt1
- gui: fixed: work with locale
- gui: fixed: lock autocheck

* Thu Apr 16 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.9.2-alt1
- 0.9.0 -> 0.9.2

* Tue Apr 14 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.9.0-alt1
- 0.8.0 -> 0.9.0

* Wed Apr 08 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.8.0-alt1
- cli: added FTPS support
- gui: added FTPS support
- gui: added automatic mirror selection for HTTP|HTTPS|FTP|FTPS protocols:
    - for HTTP|HTTPS protocols, channel speed measurement is performed using
    the standard method via the requests library
    - for FTP|FTPS protocols, file download time is measured and the shortest
    time is determined, using the standard method via the urllib.request library

* Thu Mar 26 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.7.2-alt2
- updated URL (issue#26)

* Thu Mar 12 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.7.2-alt1
- 0.7.1 -> 0.7.2

* Mon Feb 16 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.7.1-alt1
- 0.7.0 -> 0.7.1

* Mon Feb 09 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.7.0-alt1
- gui: added: switching to the Sisyphus archive

* Sat Jan 24 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.6.6-alt1
- cli: fixed: check branch (ALT #57565)
- cli: fixed: check ams lists

* Sat Jan 17 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.6.5-alt1
- excluded: ftp.heanet.ie (HEAnet, Ireland)

* Tue Jan 13 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.6.4-alt1
- GUI: fix: don't closing the application if there is no architecture.
- CLI: fix: some errors.
- CLI: add: architecture check.
- CLI: add: ams list check.

* Mon Jan 05 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.6.3-alt1
- GUI: fix: some errors
- GUI: add: architecture check
- CLI: fix: switch with no active mirror
- CLI: add: check branch

* Mon Dec 29 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.6.2-alt1
- GUI: added: https protocol support.
- GUI: added: convert http -> https.
- GUI: fix: minor flaws.

* Mon Dec 22 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.6.1-alt1
- ams: added: "file" protocol
- fix: some errors

* Fri Dec 12 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.6.0-alt1
- added: alt-mirror-switcher-cli sub package:
  + ams mirror: show local mirrors
  + ams mirror switch <mirror> <http|https|ftp|rsync>: switching local mirror with need protocol

* Wed Dec 10 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.5.1-alt1
- 0.4.4.3 -> 0.5.1

* Sat Dec 06 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.4.4.3-alt1
- 0.4.4.2 -> 0.4.4.3

* Thu Nov 27 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.4.4.2-alt1
- added mirror: mirror.truenetwork.ru

* Sat Nov 22 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.4.4.1-alt1
- Splitting additional mirrors into sub-packages.
- Added mirrors:
  + download.etersoft.ru
  + mirror.datacenter.by (p11)
  + mirror.mephi.ru

* Wed Nov 19 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.4.4-alt1
- added mirror: download.basealt.ru

* Tue Nov 18 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.4.3-alt1
- 0.4.2 -> 0.4.3 (ALT #56880)

* Mon Nov 17 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.4.2-alt1
- 0.4.1 -> 0.4.2:
  + added: localization
  + disable system *.list and enable /etc/apt/sources.list

* Sat Nov 15 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.4.1-alt1
- 0.4.0 -> 0.4.1 (ALT #56850)

* Fri Nov 14 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.4.0-alt1
- 0.3.1 -> 0.4.0 (ALT #56850)

* Sat Nov 01 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.3.1-alt1
- 0.3.0 -> 0.3.1

* Wed Oct 29 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.3.0-alt1
- 0.2.1 -> 0.3.0:
  + add: labels and protocols
  + change for branch [p1*

* Wed Oct 22 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.2.1-alt1
- 0.2 -> 0.2.1

* Mon Oct 20 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.2-alt1
- 0.1 -> 0.2

* Sun Oct 19 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.1-alt1
- Initial build for ALT Linux.
