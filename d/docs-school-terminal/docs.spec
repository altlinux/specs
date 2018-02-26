%define variant school-terminal
%define Variant School Terminal

%define _documentationdir %_defaultdocdir/documentation
%define _docsinstalldir %_defaultdocdir/%variant

%define variants docs-office-server docs-backup-server docs-desktop docs-school-master docs-school-junior docs-school-lite docs-school-server docs-kdesktop docs-school-terminal docs-school-newlite docs-centaurus docs-simply-linux

Name: docs-%variant
Version: 5.0
Release: alt8

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
* Fri Jun 10 2011 Artem Zolochevskiy <azol@altlinux.ru> 5.0-alt8
- add docs-simply-linux to Conflicts list

* Mon Mar 07 2011 Artem Zolochevskiy <azol@altlinux.ru> 5.0-alt7
- update Conflicts list

* Mon Mar 08 2010 Artem Zolochevskiy <azol@altlinux.ru> 5.0-alt6
- add initial 'whatis' section
- add initial 'deploy' section

* Fri Feb 26 2010 Artem Zolochevskiy <azol@altlinux.ru> 5.0-alt5
- install-guide: fix info on RAID creation during install

* Thu Feb 25 2010 Andrey Cherepanov <cas@altlinux.org> 5.0-alt4
- initial build for Sisyphus

