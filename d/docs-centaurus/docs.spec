%define variant centaurus
%define Variant Centaurus

%define _documentationdir %_defaultdocdir/documentation
%define _docsinstalldir %_defaultdocdir/%variant

%define variants docs-office-server docs-backup-server docs-desktop docs-school-master docs-school-junior docs-school-lite docs-school-server docs-kdesktop docs-school-terminal docs-school-newlite docs-centaurus docs-simply-linux

Name: docs-%variant
Version: 6.0
Release: alt6

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
