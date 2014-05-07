%define oname libguess

Name: libguess1
Version: 1.2
Release: alt1

Summary: High-speed character set detection library

Group: System/Libraries
License: BSD
Url: http://www.atheme.org/project/libguess

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %name-%version.tar

BuildRequires: pkgconfig
BuildRequires: libmowgli2-devel >= 2.0.0
BuildRequires: autoconf libtool

%description
libguess employs discrete-finite automata to deduce the character set of
the input buffer. The advantage of this is that all character sets can be
checked in parallel, and quickly. Right now, libguess passes a byte to
each DFA on the same pass, meaning that the winning character set can be
deduced as efficiently as possible.

libguess is fully reentrant, using only local stack memory for DFA
operations.

%package devel
Summary: Files needed for developing with %name
Group: Development/Other
Requires: %name = %version-%release

%description devel
This package contains the files that are needed when building
software that uses %name.

%prep
%setup
%__subst '\,^.SILENT:,d' buildsys.mk.in

%build
# https://github.com/atheme/buildsys
touch src/libguess/autoconf.h.in
aclocal -I m4
autoconf
%configure
%make_build

%install
%makeinstall_std

%check
cd src/tests/testbench
LD_LIBRARY_PATH=%buildroot%_libdir make

%files
%doc README
%_libdir/%oname.so.1
%_libdir/%oname.so.1.*

%files devel
%_libdir/%oname.so
%dir %_includedir/%oname/
%_includedir/%oname/%oname.h
%_pkgconfigdir/%oname.pc

%changelog
* Wed May 07 2014 Vitaly Lipatov <lav@altlinux.ru> 1.2-alt1
- initial build for ALT Linux Sisyphus

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Apr 21 2013 Michael Schwendt <mschwendt@fedoraproject.org> - 1.1-5
- Patch configure.ac to define m4 macro dir.
- BR autoconf libtool and run autoreconf -f for aarch64 updates (#925758).

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan  5 2012 Michael Schwendt <mschwendt@fedoraproject.org> - 1.1-2
- rebuild for GCC 4.7 as requested

* Sat Dec  3 2011 Michael Schwendt <mschwendt@fedoraproject.org> - 1.1-1
- Upgrade to 1.1 with added %%check section.

* Fri Sep 16 2011 Michael Schwendt <mschwendt@fedoraproject.org> - 1.0-3
- Use %%_isa in -devel package dependency.
- Drop %%defattr lines.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jul 14 2010 Michael Schwendt <mschwendt@fedoraproject.org> - 1.0-1
- Use fresh 1.0 release tarball, which only adds the makerelease.sh script.
- Drop unneeded BuildRoot stuff.

* Tue Jul 13 2010 Michael Schwendt <mschwendt@fedoraproject.org> - 1.0-0.1.20100713
- Initial RPM packaging.
