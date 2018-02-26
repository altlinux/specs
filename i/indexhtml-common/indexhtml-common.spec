%define _indexhtmldir %_defaultdocdir/indexhtml

Name: indexhtml-common
Version: 0.6.1
Release: alt1

Summary: indexhtml-common
License: %gpl3plus
Group: System/Base
Buildarch: noarch
Packager: ALT Docs Team <docs@packages.altlinux.org>

Source: %name-%version.tar

BuildRequires(pre): rpm-build-licenses
BuildRequires: cmake

%description
This package contains files required to integrate indexhtml packages.

%prep
%setup

%build
cmake -DCMAKE_INSTALL_PREFIX=%prefix -DDEFAULTINDEXHTMLDIR=%_indexhtmldir .
%make_build

%install
%makeinstall_std
mkdir -p %buildroot{%_indexhtmldir,%_sysconfdir/firsttime.d}
ln -s $(relative %_sbindir/indexhtml-update %_sysconfdir/firsttime.d/indexhtml) \
  %buildroot%_sysconfdir/firsttime.d/indexhtml

%files
%_sbindir/*
%_defaultdocdir/HTML/*
%_indexhtmldir/
%_sysconfdir/firsttime.d/*

%changelog
* Thu Oct 29 2009 Artem Zolochevskiy <azol@altlinux.ru> 0.6.1-alt1
- indexhtml-update: better diagnostics, minor cleanup (thx Michael Shigorin)

* Mon Oct 26 2009 Artem Zolochevskiy <azol@altlinux.ru> 0.6-alt1
- indexhtml-update: treat first parameter as indexhtml dir
- add initial CMake build system

* Thu Oct 22 2009 Artem Zolochevskiy <azol@altlinux.ru> 0.5-alt1
- new indexhtmldir
- remove no more needed conflicts list

* Fri Mar 27 2009 Artem Zolochevskiy <azol@altlinux.ru> 0.4-alt1
- updated Conflicts list

* Fri Jan 23 2009 Artem Zolochevskiy <azol@altlinux.ru> 0.3-alt1
- fix quote use
- use stderr for debug output

* Wed Nov 26 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.2-alt2
- updated Conflicts list

* Wed Sep 24 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.2-alt1
- added firsttime.d sript (as symlink)

* Fri May 23 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt2
- updated Conflicts list

* Tue May 20 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1
- initial build for Sisyphus

