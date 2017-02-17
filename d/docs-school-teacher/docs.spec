%define variant school-teacher
%define Variant School Teacher

%define _documentationdir %_defaultdocdir/documentation
%define _docsinstalldir %_defaultdocdir/%variant

%define variants docs-office-server docs-backup-server docs-desktop docs-school-master docs-school-junior docs-school-lite docs-school-server docs-kdesktop docs-school-terminal docs-school-newlite docs-centaurus docs-simply-linux docs-lxdesktop docs-lxdesktop-lite docs-school-teacher docs-alt-education docs-alt-kworkstation docs-alt-server docs-alt-workstation

Name: docs-%variant
Version: 7.0.5
Release: alt3

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
* Fri Feb 17 2017 Elena Mishina <lepata@altlinux.org> 7.0.5-alt3
- update Conflicts list

* Sat Mar 5 2016 Artem Zolochevskiy <azol@altlinux.org> 7.0.5-alt2
- rebuild with publclian4

* Sun Jan 24 2016 Artem Zolochevskiy <azol@altlinux.org> 7.0.5-alt1
- update to 7.0.5

* Fri Dec 27 2013 Andrey Cherepanov <cas@altlinux.org> 7.0-alt3
- Update screenshot with slideshow

* Wed Dec 25 2013 Andrey Cherepanov <cas@altlinux.org> 7.0-alt2
- Update screenshots from release

* Sun Dec 15 2013 Artem Zolochevskiy <azol@altlinux.ru> 7.0-alt1
- initial build for Sisyphus

