%def_disable static

Name: libsynce
Version: 0.15.1
Release: alt1
Summary: Core libraries needed to use SynCE
Packager: Mobile Development Team <mobile@packages.altlinux.org>
License: MIT
Group: System/Libraries
Url: http://synce.sourceforge.net
Source: %name-%version.tar
Source1: %name.map
Patch1: %name-alt-symver.patch

BuildPreReq: libdbus-devel >= 0.60
BuildPreReq: libdbus-glib-devel >= 0.60
BuildRequires: gcc-c++

%description
Core libraries needed to use SynCE

%package devel
Summary: Libraries and headers needed for developing with SynCE
Group: Development/C
Requires: %name = %version-%release

%description devel
Libraries and headers needed for developing with SynCE

%if_enabled static
%package devel-static
Summary: Static library for developing with SynCE
Group: Development/C
Requires: %name = %version-%release

%description devel-static
Static Libraries needed for developing with SynCE
See http://synce.sourceforge.net for more information.
%endif


%prep
%setup -q
#%patch1 -p1
#install -p -m644 %SOURCE1 lib/%name.map

%build
%autoreconf
%configure \
	%{subst_enable static} \
	--enable-dccm-file-support \
	--enable-odccm-support \
	--enable-udev-support \
	--disable-hal-support

%make

%install
%make install DESTDIR=%buildroot

%files
%_libdir/*.so.*
%doc README TODO

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*
%_man3dir/*
%_man7dir/*

%if_enabled static
%files devel-static
%_libdir/*.a
%endif

%changelog
* Wed Feb 16 2011 Alexey Shabalin <shaba@altlinux.ru> 0.15.1-alt1
- 0.15.1
- build withouth hal support
- disable versioning

* Tue Nov 23 2010 Denis Smirnov <mithraen@altlinux.ru> 0.15-alt1.1
- rebuild (with the help of girar-nmu utility)

* Mon May 17 2010 Alexey Shabalin <shaba@altlinux.ru> 0.15-alt1
- 0.15

* Fri Aug 21 2009 Alexey Shabalin <shaba@altlinux.ru> 0.14-alt1
- 0.14
- add versioning

* Sun Mar 01 2009 Alexey Shabalin <shaba@altlinux.ru> 0.13-alt1
- 0.13
- removed pre/post scripts

* Sat Oct 04 2008 Alexey Shabalin <shaba@altlinux.ru> 0.12-alt1
- 0.12

* Mon Jun 30 2008 Grigory Milev <week@altlinux.ru> 0.11.1-alt2
- add devel static package
- fix Sisyphus requires

* Thu Apr 17 2008 Eugene V. Horohorin <genix@altlinux.ru> 0.11.1-alt1
- 0.11.1
- update buildreq

* Thu Jan 31 2008 Eugene V. Horohorin <genix@altlinux.ru> 0.11-alt2
- add %%post and %%postun spec sections

* Wed Jan 09 2008 Eugene V. Horohorin <genix@altlinux.ru> 0.11-alt1
- 0.11

* Thu Jan 03 2008 Eugene V. Horohorin <genix@altlinux.ru> 0.10.0-alt3
- update to SVN 20080102 version

* Fri Dec 07 2007 Eugene V. Horohorin <genix@altlinux.ru> 0.10.0-alt2
- update to SVN 20071207 version

* Mon May 14 2007 Eugene V. Horohorin <genix@altlinux.ru> 0.10.0-alt1
- 0.10.0

* Fri Jan 12 2007 Eugene V. Horohorin <genix@altlinux.ru> 0.9.3-alt1
- 0.9.3

* Sun Jul 24 2005 Eugene V. Horohorin <genix@altlinux.ru> 0.9.1-alt1
- 0.9.1
- spec clean-up (gcc3.2 dependency removed)

* Wed Sep 01 2004 Michael Shigorin <mike@altlinux.ru> 0.9.0-alt1
- 0.9.0

* Sun Apr 25 2004 Michael Shigorin <mike@altlinux.ru> 0.8.9-alt1
- 0.8.9
- using gcc3.2 for now (can't patch "type punning" in trivial way)

* Fri Nov 28 2003 Michael Shigorin <mike@altlinux.ru> 0.8.1-alt2
- removed *.la and devel-static subpackage

* Fri Nov 07 2003 Michael Shigorin <mike@altlinux.ru> 0.8.1-alt1
- built for ALT Linux

