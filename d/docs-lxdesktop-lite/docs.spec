%define variant lxdesktop-lite
%define Variant ALTLinux LXDEesktop Lite

%define _documentationdir %_defaultdocdir/documentation
%define _docsinstalldir %_defaultdocdir/%variant

%define variants docs-office-server docs-backup-server docs-desktop docs-school-master docs-school-junior docs-school-lite docs-school-server docs-kdesktop docs-school-terminal docs-school-newlite docs-centaurus docs-simply-linux docs-lxdesktop docs-lxdesktop-lite docs-school-teacher docs-alt-education docs-alt-kworkstation docs-alt-server docs-alt-workstation

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
* Fri Feb 17 2017 Elena Mishina <lepata@altlinux.org> 6.0-alt6
- update Conflicts list

* Fri Mar 04 2016 Artem Zolochevskiy <azol@altlinux.org> 6.0-alt5
- rebuild with publclian4

* Thu Feb 25 2016 Artem Zolochevskiy <azol@altlinux.org> 6.0-alt4
- switch to publican

* Wed Mar 21 2012 Artem Zolochevskiy <azol@altlinux.ru> 6.0-alt3
- some tiny fixes

* Fri Mar 09 2012 Artem Zolochevskiy <azol@altlinux.ru> 6.0-alt2
- fix some typos
- add gnumeric description
- add pkg-groups step to install guide

* Thu Mar 08 2012 Artem Zolochevskiy <azol@altlinux.ru> 6.0-alt1
- initial build
