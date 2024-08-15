%define variant alt-server
%define Variant ALT Server

%define _documentationdir %_defaultdocdir/documentation
%define _docsinstalldir %_defaultdocdir/%variant

%define variants docs-office-server docs-backup-server docs-desktop docs-school-master docs-school-junior docs-school-lite docs-school-server docs-kdesktop docs-school-terminal docs-school-newlite docs-centaurus docs-simply-linux docs-lxdesktop docs-lxdesktop-lite docs-school-teacher docs-alt-education docs-alt-kworkstation docs-alt-server docs-alt-workstation docs-alt-kworkstation docs-alt-spworkstation docs-alt-server-v

Name: docs-%variant
Version: 10.2
Release: alt10

Summary: %Variant documentation
License: %fdl
Group: Documentation

Packager: ALT Docs Team <docs@packages.altlinux.org>
BuildArch: noarch

Source: %name-%version-%release.tar

Obsoletes: docs-basealt-desktop <= 8.0-alt2
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
* Thu Aug 15 2024 Elena Mishina <lepata@altlinux.org> 10.2-alt10
- PBS: added tape-backup
- OpenUDS: added UDSActorRegister
- small improvements

* Fri Mar 1 2024 Elena Mishina <lepata@altlinux.org> 10.2-alt9
- update to latest public distr of ALT Server 10.2
- small improvements

* Tue Feb 20 2024 Elena Mishina <lepata@altlinux.org> 10.2-alt8
- bug fixes (closes: #49441)

* Mon Feb 12 2024 Elena Mishina <lepata@altlinux.org> 10.2-alt7
- update to ALT Server 10.2

* Wed Jan 03 2024 Elena Mishina <lepata@altlinux.org> 10.2-alt6
- bug fixes (closes: #48990, #48988, #48993, #48995, #48997)

* Thu Dec 28 2023 Elena Mishina <lepata@altlinux.org> 10.2-alt5
- update to ALT Server 10.2rc
- add FS, cryptsetup, audit

* Tue Oct 31 2023 Elena Mishina <lepata@altlinux.org> 10.2-alt4
- small improvements

* Thu Oct 19 2023 Elena Mishina <lepata@altlinux.org> 10.2-alt3
- install-distro: add autoinstall

* Wed Oct 11 2023 Elena Mishina <lepata@altlinux.org> 10.2-alt2
- bug fixes
- update support

* Wed Sep 27 2023 Elena Mishina <lepata@altlinux.org> 10.2-alt1
- update to ALT Server 10.2Beta1

* Wed Sep 13 2023 Elena Mishina <lepata@altlinux.org> 10.1-alt18
- fix install Zabbix
- small improvements

* Tue Aug 15 2023 Elena Mishina <lepata@altlinux.org> 10.1-alt17
- fix some typos (ALT 47183)
- small improvements

* Mon Jul 31 2023 Elena Mishina <lepata@altlinux.org> 10.1-alt16
- update OpenUDS
- add Dovecot sieve

* Mon Feb 20 2023 Elena Mishina <lepata@altlinux.org> 10.1-alt15
- update to latest public distr of ALT Server 10.1
- add Nextcloud
- add SPICE to OpenUDS

* Mon Feb 13 2023 Elena Mishina <lepata@altlinux.org> 10.1-alt14
- install-system: delete Nexcloud

* Fri Feb 10 2023 Elena Mishina <lepata@altlinux.org> 10.1-alt13
- update to latest public distr of ALT Server 10.1

* Tue Feb 07 2023 Elena Mishina <lepata@altlinux.org> 10.1-alt12
- update FreeIPA

* Sat Jan 21 2023 Elena Mishina <lepata@altlinux.org> 10.1-alt11
- update OpenUDS, PBS, group policy

* Wed Dec 21 2022 Elena Mishina <lepata@altlinux.org> 10.1-alt10
- update to latest public distr of ALT Server 10.1

* Tue Dec 13 2022 Elena Mishina <lepata@altlinux.org> 10.1-alt9
- update Samba DC
- fix gpoup policy (closes: #44651, #44650)

* Tue Dec 13 2022 Elena Mishina <lepata@altlinux.org> 10.1-alt8
- delete OpenLDAP domain

* Fri Dec 2 2022 Elena Mishina <lepata@altlinux.org> 10.1-alt7
- update documentation

* Tue Nov 15 2022 Elena Mishina <lepata@altlinux.org> 10.1-alt6
- update to ALT Server 10.1
- fix OpenUDS HA (closes: #43979, #43977)

* Fri Sep 16 2022 Elena Mishina <lepata@altlinux.org> 10.1-alt5
- update to ALT Server 10.1rc
- fix typo (closes: #43710)

* Fri Aug 19 2022 Elena Mishina <lepata@altlinux.org> 10.1-alt4
- add OpenUDS HA
- add OpenUDS tunnel

* Mon Jul 18 2022 Elena Mishina <lepata@altlinux.org> 10.1-alt3
- update to ALT Server 10.1Beta4

* Tue Jul 12 2022 Elena Mishina <lepata@altlinux.org> 10.1-alt2
- fix typo (closes: #43146, #43079, #43073)
- fix pbs (closes: #43131, #43132, #43133)

* Mon Jun 20 2022 Elena Mishina <lepata@altlinux.org> 10.1-alt1
- update to ALT Server 10.1Beta
- add proxmox backup server

* Wed Apr 06 2022 Elena Mishina <lepata@altlinux.org> 10.0-alt3
- fix some typos
- add UrBackup, delete bacula
- update documentation

* Tue Nov 30 2021 Elena Mishina <lepata@altlinux.org> 10.0-alt2
- update to ALT Server 10.0rc
- reduce package size

* Tue Nov 09 2021 Elena Mishina <lepata@altlinux.org> 10.0-alt1
- update to ALT Server 10.0Beta

* Wed Jul 09 2021 Elena Mishina <lepata@altlinux.org> 9.2-alt1
- update to ALT Server 9.2
- add OpenUDS

* Mon Mar 15 2021 Elena Mishina <lepata@altlinux.org> 9.1-alt5
- install-packages-advanced: add epm
- admin: pacemaker, group policy
- fix typo

* Mon Nov 30 2020 Elena Mishina <lepata@altlinux.org> 9.1-alt4
- update Zabbix documentation for 5.0

* Mon Nov 16 2020 Elena Mishina <lepata@altlinux.org> 9.1-alt3
- add ALT Media Writer
- add configured new hosts in Zabbix
- update documentation

* Tue Jul 14 2020 Elena Mishina <lepata@altlinux.org> 9.1-alt1
- update to latest public distr of ALT Server 9.1

* Fri Oct 04 2019 Elena Mishina <lepata@altlinux.org> 9.0-alt1
- update to latest public distr

* Mon Jul 29 2019 Elena Mishina <lepata@altlinux.org> 8.90-alt1
- update to beta verson of ALT Server 9.0

* Wed Oct 17 2018 Elena Mishina <lepata@altlinux.org> 8.2-alt4
- fix typo
- update documentation

* Fri Mar 16 2018 Elena Mishina <lepata@altlinux.org> 8.2-alt3
- update documentation

* Thu Dec 11 2017 Elena Mishina <lepata@altlinux.org> 8.2-alt2
- fix conflict package

* Thu Nov 30 2017 Elena Mishina <lepata@altlinux.org> 8.2-alt1
- updated to latest public distr
- fix typo

* Wed May 24 2017 Elena Mishina <lepata@altlinux.org> 8.0-alt6
- update documentation
- fix typo

* Thu Mar 20 2017 Elena Mishina <lepata@altlinux.org> 8.0-alt5
- update documentation
- fix typo

* Thu Feb 09 2017 Elena Mishina <lepata@altlinux.org> 8.0-alt4
- update Conflicts list
- update documentation

* Thu Jan 19 2017 Artem Zolochevskiy <azol@altlinux.ru> 8.0-alt3
- updated to latest public distr

* Fri Jan 13 2017 Artem Zolochevskiy <azol@altlinux.org> 8.0-alt2
- update doc

* Fri Jan 13 2017 Artem Zolochevskiy <azol@altlinux.org> 8.0-alt1
- initial build
