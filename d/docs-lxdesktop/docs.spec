%define variant lxdesktop
%define Variant ALTLinux LXDEsktop Standart

%define _documentationdir %_defaultdocdir/documentation
%define _docsinstalldir %_defaultdocdir/%variant

%define variants docs-office-server docs-backup-server docs-desktop docs-school-master docs-school-junior docs-school-lite docs-school-server docs-kdesktop docs-school-terminal docs-school-newlite docs-centaurus docs-simply-linux docs-lxdesktop docs-lxdesktop-lite

Name: docs-%variant
Version: 6.0
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
* Wed Mar 21 2012 Artem Zolochevskiy <azol@altlinux.ru> 6.0-alt3
- some tiny fixes

* Fri Mar 09 2012 Artem Zolochevskiy <azol@altlinux.ru> 6.0-alt2
- fix some typos

* Tue Mar 06 2012 Artem Zolochevskiy <azol@altlinux.ru> 6.0-alt1
- initial build
