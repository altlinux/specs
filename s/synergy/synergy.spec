Summary:	Mouse and keyboard sharing utility
Name:		synergy
Version:	2.0.12
Release:	alt1.beta.1
License:	GPLv2
Group:		Accessibility
URL:		http://synergy-project.org/
Source0:	%name-%version.tar
Patch0:		%name-%version-%release.patch

%define githash 59572061

Packager:	Evgeny Sinelnikov <sin@altlinux.org>

# Automatically added by buildreq on Fri Sep 28 2007
BuildRequires: cmake gcc-c++
BuildRequires: libcurl-devel libssl-devel libXtst-devel
#BuildRequires: qt5-base-devel
#BuildRequires: qt5-tools-devel
#BuildRequires: libavahi-devel
BuildRequires: cmake

Conflicts: synergy1

%description
Synergy lets you easily share a single mouse and keyboard between
multiple computers with different operating systems, each with its own
display, without special hardware. It's intended for users with
multiple computers on their desk since each system uses its own
display.

%prep
%setup
%patch0 -p1

%build
%cmake -DSYNERGY_REVISION=%githash
%cmake_build

%install
pushd %_cmake__builddir
install -D bin/synergyc %buildroot%_bindir/synergyc
install -D bin/synergys %buildroot%_bindir/synergys
install -D bin/synergy-core %buildroot%_bindir/synergy-core
popd
install -D -m0644 doc/synergy.conf.alt %buildroot%_sysconfdir/synergy.conf
install -D -m0644 doc/synergys.man %buildroot/%_man1dir/synergys.1
install -D -m0644 doc/synergyc.man %buildroot/%_man1dir/synergyc.1

%files
%doc ChangeLog LICENSE
%doc doc/synergy.conf*
%_bindir/synergy-core
%_bindir/synergyc
%_bindir/synergys
%config(noreplace) %_sysconfdir/synergy.conf
%_man1dir/synergys*
%_man1dir/synergyc*

%changelog
* Wed Apr 28 2021 Arseny Maslennikov <arseny@altlinux.org> 2.0.12-alt1.beta.1
- NMU: spec: adapted to new cmake macros.

* Sun Aug 02 2020 Evgeny Sinelnikov <sin@altlinux.org> 2.0.12-alt1.beta
- Update to latest beta of development branch v2
- Stable release build as conflicts package synergy1

* Wed Aug 29 2018 Grigory Ustinov <grenka@altlinux.org> 2.0.0-alt1.1
- NMU: Rebuild with new openssl 1.1.0.

* Thu Jan 18 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.0-alt1
- 2.0.0 released

* Mon Mar 28 2016 Anton Farygin <rider@altlinux.ru> 1.7.6-alt1
- new version

* Mon Dec 07 2015 Anton Farygin <rider@altlinux.ru> 1.7.4-alt1
- new version

* Sat Jul 11 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.3-alt1.1
- Rebuilt with gcc5

* Sat Jan 17 2015 Evgeny Sinelnikov <sin@altlinux.ru> 1.6.3-alt1
- Update to new stable release for happy hacking

* Sun May 11 2014 Evgeny Sinelnikov <sin@altlinux.ru> 1.4.17-alt1
- Update to new stable release
- Build without tests

* Mon Jan 13 2014 Evgeny Sinelnikov <sin@altlinux.ru> 1.4.15-alt1
- Update to new stable release

* Wed Jul 17 2013 Evgeny Sinelnikov <sin@altlinux.ru> 1.4.12-alt1
- Update to last release with encryption support

* Wed Jan 02 2013 Evgeny Sinelnikov <sin@altlinux.ru> 1.4.10-alt1
- Update to last release

* Sun Sep 11 2011 Evgeny Sinelnikov <sin@altlinux.ru> 1.3.7-alt1
- Build new version with bew scheme

* Fri Sep 28 2007 Eugene V. Horohorin <genix@altlinux.ru> 1.3.1-alt1
- initial build
