%define variant centaurus
%define Variant Centaurus

%define _documentationdir %_defaultdocdir/documentation
%define _docsinstalldir %_defaultdocdir/%variant

%define variants docs-office-server docs-backup-server docs-desktop docs-school-master docs-school-junior docs-school-lite docs-school-server docs-kdesktop docs-school-terminal docs-school-newlite docs-centaurus docs-simply-linux docs-lxdesktop docs-lxdesktop-lite docs-school-teacher docs-alt-education docs-alt-kworkstation docs-alt-server docs-alt-workstation

Name: docs-%variant
Version: 7.0.5
Release: alt4

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
* Fri Feb 17 2017 Elena Mishina <lepata@altlinux.org> 7.0.5-alt4
- update Conflicts list

* Sat Mar 5 2016 Artem Zolochevskiy <azol@altlinux.org> 7.0.5-alt3
- fix changelog

* Sat Jan 23 2016 Artem Zolochevskiy <azol@altlinux.org> 7.0.5-alt2
- rebuild with publclian4

* Sat Jan 23 2016 Artem Zolochevskiy <azol@altlinux.org> 7.0.5-alt1
- update to 7.0.5

* Tue Jun 25 2013 Artem Zolochevskiy <azol@altlinux.ru> 7.0-alt3
- update dvd- usb-burn section

* Wed Jun 19 2013 Artem Zolochevskiy <azol@altlinux.ru> 7.0-alt2
- update doc

* Fri Apr 26 2013 Artem Zolochevskiy <azol@altlinux.ru> 7.0-alt1
- initial 7.0 version

* Wed Nov 9 2011 Artem Zolochevskiy <azol@altlinux.ru> 6.0-alt6
- update

* Fri Aug 19 2011 Alexandr Boltris <alex@altlinux.org> 6.0-alt4
- update

* Thu Aug 18 2011 Alexandr Boltris <alex@altlinux.org> 6.0-alt3
- update

* Thu Jun 30 2011 Alexandr Boltris <alex@altlinux.org> 6.0-alt2
- add initial admin-basics section
- add initial backup-before-install subsection to install guide
- add system-start part
- admin-basics: add initial sumode section
- alternative-install: rewrite create flash section
- backup-before-install: add Windows 7 to resize warning
- desktop-software: add initial Audacious description
- desktop-software: add initial Evolution description based on KMail
- desktop-software: add initial Kino description
- desktop-software: add initial LibreOffice description
- desktop-software: add initial Pidgin description
- desktop-software: add initial brasero description
- desktop-software: firefox actualisation
- desktop-software: improve Pidgin description
- install-guide: add package selection to pkg step
- packages: add forgotten apt-get section
- packages: apt-get adaptation
- packages: fix using of application/package term
- system-management: add initial network section
- system-start: add initial system-login-gdm
- some rephrasing / typo and formatting fixes
- update screenshots

* Thu Feb 17 2011 Artem Zolochevskiy <azol@altlinux.ru> 6.0-alt1
- initial build
