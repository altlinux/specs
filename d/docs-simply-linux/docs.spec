%define variant simply-linux
%define Variant Simply Linux

%define _documentationdir %_defaultdocdir/documentation
%define _docsinstalldir %_defaultdocdir/%variant

%define variants docs-office-server docs-backup-server docs-desktop docs-school-master docs-school-junior docs-school-lite docs-school-server docs-kdesktop docs-school-terminal docs-school-newlite docs-centaurus docs-simply-linux docs-lxdesktop docs-lxdesktop-lite

Name: docs-%variant
Version: 6.0.1
Release: alt3

Summary: %Variant documentation
License: %fdl
Group: Documentation

Packager: ALT Docs Team <docs@packages.altlinux.org>
BuildArch: noarch

Source: %name-%version-%release.tar

Conflicts: %(for n in %variants ; do [ "$n" = %name ] || echo -n "$n "; done)

BuildRequires(pre):rpm-build-licenses
BuildRequires: asciidoc-a2x

%description
%Variant documentation.

%prep
%setup -n %name-%version-%release

%build
%make_build

%install
%make_install DESTDIR=%buildroot docdir=%_docsinstalldir install
ln -s $(relative %_docsinstalldir %_documentationdir) %buildroot%_documentationdir

%files
%_docsinstalldir
%_documentationdir

%changelog
* Fri Mar 09 2012 Artem Zolochevskiy <azol@altlinux.ru> 6.0.1-alt3
- fix some typos

* Tue Mar 06 2012 Artem Zolochevskiy <azol@altlinux.ru> 6.0.1-alt2
- improve sumode section
- add docs-lxdesktop, docs-lxdesktop-lite to conflicts list

* Tue Feb 21 2012 Artem Zolochevskiy <azol@altlinux.ru> 6.0.1-alt1
- initial 6.0.1 adaptation

* Fri Oct 21 2011 Artem Zolochevskiy <azol@altlinux.ru> 6.0-alt9
- update documentation
- closes bug: #26457

* Mon Aug 29 2011 Artem Zolochevskiy <azol@altlinux.ru> 6.0-alt8
- fix some typos

* Fri Aug 26 2011 Artem Zolochevskiy <azol@altlinux.ru> 6.0-alt7
- update

* Fri Aug 19 2011 Alexandr Boltris <alex@altlinux.org> 6.0-alt6
- update

* Thu Aug 18 2011 Alexandr Boltris <alex@altlinux.org> 6.0-alt5
- update

* Thu Jun 30 2011 Alexandr Boltris <alex@altlinux.org> 6.0-alt4
- add initial livecd section
- add system-start section
- desktop-software: add initial brasero description
- packages: remove apt-get section
- system-management: remove nm-applet section
- system-start: add initial system-login-gdm
- some rephrasings / typo and formatting fixes

* Fri Jun 10 2011 Alexandr Boltris <alex@altlinux.ru> 6.0-alt3
- system-management: add initial network section
- desktop-software: add initial audacity description
- desktop-software: update thunderbird description
- desktop-xfce: initial xfce-setting-manager description
- install-guide: add missing first step
- some rephrasings / typo fixes
- update screenschots

* Mon Jun 06 2011 Alexandr Boltris <alex@altlinux.ru> 6.0-alt2
- add initial Thunar description

* Mon Jun 06 2011 Artem Zolochevskiy <azol@altlinux.ru> 6.0-alt1
- initial build
