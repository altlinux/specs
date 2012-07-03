# $Id: duma.spec 6105 2008-01-21 09:55:51Z dries $
# Authority: dries
# Upstream:  Hayati Ayguen <h_ayguen$web,de>

%define real_version 2_5_15

Summary: Detect Unintended Memory Access
Name: duma
Version: 2.5.15
Release: alt2
License: GPL
Group: Development/Other
Url: http://duma.sourceforge.net/

Source: http://dl.sf.net/duma/duma_%real_version.tar.gz
Patch: duma-LEAKDETECTION.patch

BuildRequires: gcc-c++

%description
DUMA (Detect Unintended Memory Access) stops your program on the exact
instruction that overruns (or underruns) a malloc() memory buffer. GDB
will then display the source-code line that causes the bug. It works by
using the virtual-memory hardware to create a red-zone at the border of
each buffer: touch that, and your program stops. It can catch formerly
impossible-to-catch overrun bugs.

DUMA is a fork of Bruce Perens' Electric Fence library.

%package devel
Summary: Header files, libraries and development documentation for %name
Group: Development/Other
Requires: %name = %version-%release

%description devel
This package contains the header files, static libraries and development
documentation for %name. If you like to develop programs using %name,
you will need to install %name-devel.

%prep
%setup -n duma_%real_version
%patch -p0
find . -depth -name CVS -exec rm -rf {} \;
sed -i 's@[.]/libduma@%_libdir/libduma@g' duma.sh
sed -i 's@%_lib/@%_libdir@g' gdbinit.rc

%build
# duma doesn't build with _smp_mflags
%make all

%install
%makeinstall

%check
%make test

%files
%doc INSTALL README.txt TODO gdbinit.rc
%_man3dir/duma.3*
%_bindir/duma
%_libdir/libduma.so.*

%files devel
%doc comparisons
%_libdir/libduma.a
%_libdir/libduma.so
%_includedir/*

%changelog
* Wed Apr 14 2010 Fr. Br. George <george@altlinux.ru> 2.5.15-alt2
- Loader script real library path fix
- Some documentation added

* Mon Apr 13 2009 Fr. Br. George <george@altlinux.ru> 2.5.15-alt1
- Version up

* Thu Sep 25 2008 Fr. Br. George <george@altlinux.ru> 2.5.14-alt1
- Version up

* Mon Feb 25 2008 Fr. Br. George <george@altlinux.ru> 2.5.11-alt1
- Initial build from RF

* Mon Jan 21 2008 Dries Verachtert <dries@ulyssis.org> - 2.5.11-1 - 6105/dries
- Updated to release 2.5.11.

* Tue Jan 15 2008 Dries Verachtert <dries@ulyssis.org> - 2.5.10-1
- Updated to release 2.5.10.

* Wed Sep  5 2007 Dries Verachtert <dries@ulyssis.org> - 2.5.8-2
- Fix build on systems with multiple processors, thanks to Brian Watt.

* Mon Aug 20 2007 Dries Verachtert <dries@ulyssis.org> - 2.5.8-1
- Updated to release 2.5.8.

* Fri Aug 17 2007 Dries Verachtert <dries@ulyssis.org> - 2.5.7-1
- Updated to release 2.5.7.

* Fri Aug 17 2007 Dries Verachtert <dries@ulyssis.org> - 2.5.6-1
- Updated to release 2.5.6.

* Sun Aug 12 2007 Dries Verachtert <dries@ulyssis.org> - 2.5.5-1
- Updated to release 2.5.5.

* Wed Aug 01 2007 Dries Verachtert <dries@ulyssis.org> - 2.5.4-1
- Updated to release 2.5.4.

* Mon Jul 16 2007 Dries Verachtert <dries@ulyssis.org> - 2.5.3-1
- Updated to release 2.5.3.

* Tue Jul 10 2007 Dries Verachtert <dries@ulyssis.org> - 2.5.1-1
- Updated to release 2.5.1.

* Thu Apr 27 2006 Dries Verachtert <dries@ulyssis.org> - 2.4.27-1
- Updated to release 2.4.27.

* Thu Nov 10 2005 Dries Verachtert <dries@ulyssis.org> - 2.4.26-2
- Fixed the project url and source url.

* Fri Oct 28 2005 Dries Verachtert <dries@ulyssis.org> - 2.4.26-1

- Updated to release 2.4.26.

* Sat Oct 08 2005 Dries Verachtert <dries@ulyssis.org> - 2.4.23-1
- Updated to release 2.4.23.

* Fri Oct 07 2005 Dries Verachtert <dries@ulyssis.org> - 2.4.22-1
- Updated to release 2.4.22.

* Tue Sep 20 2005 Dries Verachtert <dries@ulyssis.org> - 2.4.19-1
- Initial package.
