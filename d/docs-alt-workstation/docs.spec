%define variant alt-workstation
%define Variant ALT Workstation

%define _documentationdir %_defaultdocdir/documentation
%define _docsinstalldir %_defaultdocdir/%variant

%define variants docs-office-server docs-backup-server docs-desktop docs-school-master docs-school-junior docs-school-lite docs-school-server docs-kdesktop docs-school-terminal docs-school-newlite docs-centaurus docs-simply-linux docs-lxdesktop docs-lxdesktop-lite docs-school-teacher docs-alt-education docs-alt-kworkstation docs-alt-server docs-alt-workstation docs-alt-spworkstation docs-alt-server-v

Name: docs-%variant
Version: 10.1
Release: alt7

Summary: %Variant documentation
License: %fdl
Group: Documentation

Packager: ALT Docs Team <docs@packages.altlinux.org>
BuildArch: noarch

Source: %name-%version-%release.tar

Conflicts: %(for n in %variants ; do [ "$n" = %name ] || echo -n "$n "; done)

BuildRequires(pre):rpm-build-licenses
BuildRequires: publican
BuildRequires: perl-podlators
BuildRequires: libwebp-tools

%description
%Variant documentation.

%prep
%setup -n %name-%version-%release

%build
%make_build

%install
%make_install DESTDIR=%buildroot docdir=%_docsinstalldir install
ln -s $(relative %_docsinstalldir %_documentationdir) %buildroot%_documentationdir
sed -i 's/src="images\/\(.*\).png"/src="images\/\1.webp"/g' %buildroot%_docsinstalldir/ru-RU/index.html
for file in %buildroot%_docsinstalldir/ru-RU/images/*.png; do cwebp $file -o %buildroot%_docsinstalldir/ru-RU/images/$(basename $file .png).webp -quiet && rm $file; done

%files
%_docsinstalldir
%_documentationdir

%changelog
* Sun Dec 18 2022 Elena Mishina <lepata@altlinux.org> 10.1-alt7
- fix some typos (ALT #44664, #44665)

* Fri Dec 02 2022 Elena Mishina <lepata@altlinux.org> 10.1-alt6
- update documentation

* Fri Oct 28 2022 Elena Mishina <lepata@altlinux.org> 10.1-alt5
- update to ALT Workstation 10.1

* Mon Oct 24 2022 Elena Mishina <lepata@altlinux.org> 10.1-alt4
- fix some typos (ALT #43731)
- update documentation

* Mon Sep 05 2022 Elena Mishina <lepata@altlinux.org> 10.1-alt3
- update to ALT Workstation 10.1rc

* Wed Aug 03 2022 Elena Mishina <lepata@altlinux.org> 10.1-alt2
- fix some typos (ALT 43358, 43369, 43398, 43400, 43394)
- update documentation

* Wed Jul 20 2022 Elena Mishina <lepata@altlinux.org> 10.1-alt1
- update to beta version of ALT Workstation 10.1

* Wed Apr 06 2022 Elena Mishina <lepata@altlinux.org> 10.0-alt4
- fix some typos
- update documentation

* Tue Dec 07 2021 Elena Mishina <lepata@altlinux.org> 10.0-alt3
- update to ALT Workstation 10.0

* Tue Nov 30 2021 Elena Mishina <lepata@altlinux.org> 10.0-alt2
- update to ALT Workstation 10.0rc
- reduce package size

* Tue Nov 09 2021 Elena Mishina <lepata@altlinux.org> 10.0-alt1
- update to beta version of ALT Workstation 10.0

* Wed Jul 07 2021 Elena Mishina <lepata@altlinux.org> 9.2-alt1
- update to ALT Workstation 9.2

* Tue Apr 06 2021 Elena Mishina <lepata@altlinux.org> 9.1-alt4
- fix some typos
- update screenshots
- update info: network-configuration

* Mon Mar 15 2021 Elena Mishina <lepata@altlinux.org> 9.1-alt3
- system-management: add group policy
- functional: add alt-csp-cryptopro, luks password
- install-packages-advanced: add epm
- fix typo

* Mon Nov 16 2020 Elena Mishina <lepata@altlinux.org> 9.1-alt2
- update thunderbird
- add recoll settings
- add ALT Media Writer

* Tue Jul 14 2020 Elena Mishina <lepata@altlinux.org> 9.1-alt1
- update to latest public distr of ALT Workstation 9.1

* Fri Oct 04 2019 Elena Mishina <lepata@altlinux.org> 9.0-alt1
- update to latest public distr of ALT Workstation 9.0

* Mon Jul 29 2019 Elena Mishina <lepata@altlinux.org> 8.90-alt2
- update to beta verson of ALT Workstation 9.0
- fix pam_mount options (ALT #37031)

* Mon Jul 01 2019 Elena Mishina <lepata@altlinux.org> 8.90-alt1
- update to alpha verson of ALT Workstation 9.0

* Wed Oct 17 2018 Elena Mishina <lepata@altlinux.org> 8.2-alt3
- fix typo
- update documentation

* Fri Mar 16 2018 Elena Mishina <lepata@altlinux.org> 8.2-alt2
- update documentation

* Mon Nov 27 2017 Elena Mishina <lepata@altlinux.org> 8.2-alt1
- fix typo
- update doc

* Wed May 24 2017 Elena Mishina <lepata@altlinux.org> 8.1-alt4
- fix typo
- update doc

* Fri Feb 10 2017 Elena Mishina <lepata@altlinux.org> 8.1-alt3
- update Conflicts list

* Thu Jan 19 2017 Artem Zolochevskiy <azol@altlinux.ru> 8.1-alt2
- updated to latest public distr

* Tue Nov 15 2016 Michael Shigorin <mike@altlinux.org> 8.1-alt1
- update for 8.1 release

* Tue Jun 21 2016 Michael Shigorin <mike@altlinux.org> 8.0-alt3
- renamed to docs-alt-workstation

* Tue Apr 19 2016 Artem Zolochevskiy <azol@altlinux.org> 8.0-alt2
- update to alpha verson (18/04/2016)

* Mon Apr 4 2016 Artem Zolochevskiy <azol@altlinux.org> 8.0-alt1
- initial build
