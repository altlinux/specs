Summary:	Mouse and keyboard sharing utility
Name:		synergy
Version:	1.6.3
Release:	alt1
License:	GPL
Group:		Accessibility
URL:		http://synergy-project.org/
Source0:	%name-%version.tar
Patch0:		%name-%version-%release.patch

Packager:	Evgeny Sinelnikov <sin@altlinux.ru>

# Automatically added by buildreq on Fri Sep 28 2007
BuildRequires: gcc-c++ libXtst-devel
BuildRequires: libcurl-devel
BuildRequires: libcryptopp-devel
BuildRequires: rpm-macros-cmake
BuildRequires: cmake

%def_without test

%description
Synergy lets you easily share a single mouse and keyboard between
multiple computers with different operating systems, each with its own
display, without special hardware. It's intended for users with
multiple computers on their desk since each system uses its own
display.

%prep
%setup -q
%patch0 -p1

%if_with test
unzip ext/gtest-1.6.0.zip -d ext/gtest-1.6.0
unzip ext/gmock-1.6.0.zip -d ext/gmock-1.6.0
%endif

%build
./configure \
%if_with test
    -DWITH_TEST=1
%endif
    #

%make_build -j1 VERBOSE=1

%install
install -D bin/synergyc %buildroot%_bindir/synergyc
install -D bin/synergys %buildroot%_bindir/synergys
install -D -m0644 doc/synergy.conf.example %buildroot%_sysconfdir/synergy.conf
install -D -m0644 doc/synergys.man %buildroot/%_man1dir/synergys.1
install -D -m0644 doc/synergyc.man %buildroot/%_man1dir/synergyc.1

#%if_with test
#install -D bin/synergyd %buildroot%_bindir/synergyd
#install -D bin/usynergy %buildroot%_bindir/usynergy
#install -D bin/syntool %buildroot%_bindir/syntool
#install -D bin/integtests %buildroot%_bindir/integtests
#install -D bin/unittests %buildroot%_bindir/unittests
#%endif

%files
%doc ChangeLog COPYING README
%doc doc/synergy.conf*
%_bindir/synergyc
%_bindir/synergys
%config(noreplace) %_sysconfdir/synergy.conf
%_man1dir/synergys*
%_man1dir/synergyc*

%changelog
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

