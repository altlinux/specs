%define variant backup-server
%define Variant Backup Server

%define _documentationdir %_defaultdocdir/documentation
%define _docsinstalldir %_defaultdocdir/%variant

%define variants docs-office-server docs-backup-server docs-desktop docs-school-master docs-school-junior docs-school-lite docs-school-server docs-kdesktop docs-school-terminal docs-school-newlite docs-centaurus

Name: docs-%variant
Version: 5.0
Release: alt5

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
* Mon Mar 07 2011 Artem Zolochevskiy <azol@altlinux.ru> 5.0-alt5
- update Conflicts list

* Wed Nov 04 2009 Artem Zolochevskiy <azol@altlinux.ru> 5.0-alt4
- install-guide: fix typo (thx Rinat Bikov)
- add authorship and revision information

* Mon Oct 26 2009 Artem Zolochevskiy <azol@altlinux.ru> 5.0-alt3
- update install guide

* Mon Oct 26 2009 Artem Zolochevskiy <azol@altlinux.ru> 5.0-alt2
- fix build with new asciidoc

* Wed Jun 24 2009 Artem Zolochevskiy <azol@altlinux.ru> 5.0-alt1
- initial build for Sisyphus
