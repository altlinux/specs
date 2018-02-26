Name: librtfcomp
Version: 1.1
Release: alt2.1.1
Packager: Mobile Development Team <mobile@packages.altlinux.org>
Summary: Library to read and write compressed RTF files
License: LGPLv2+
Group: System/Libraries
Url: http://synce.sourceforge.net/
Source: %name-%version.tar.gz
Patch: %name-%version-link.patch

# Automatically added by buildreq on Thu Jan 31 2008
BuildRequires: python-module-Pyrex python-modules-compiler time

%description
Can decompress and recompress compressed RTF and convert from
UTF8 to RTF for use in things like the AirSync protocols

%package -n	%name-devel
Summary: Headers for developing programs that will use %name
Group: Development/C
Requires: %name = %version

%description -n	%name-devel
This package contains the headers that programmers will need to develop
applications which will use %name.

%prep
%setup -q
%patch -p0
sed -i -e 's,^\(pyrtfcomp_la_LIBADD = \$(top_builddir)/src/librtfcomp.la\),\1 -lpython%__python_version,g' python/Makefile.am
sed -i -e 's,^\(librtfcomp_la_LIBADD = -lpython2.4\),librtfcomp_la_LIBADD = -lpython%__python_version,g' src/Makefile.am

%build
%__autoreconf
%configure --disable-static
%make

%install
%makeinstall

%files
%exclude %_bindir/test
%_bindir/*
%_libdir/*.so.*
%_libdir/python*/site-packages/*.so

%files -n %name-devel
%_includedir/*
%_libdir/*.so

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1-alt2.1.1
- Rebuild with Python-2.7

* Tue Dec 01 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt2.1
- Rebuilt with python 2.6

* Sun Mar 02 2008 Alexey Shabalin <shaba@altlinux.ru> 1.1-alt2
- Link with current python.
- fix license tag
- cleanup spec

* Thu Jan 31 2008 Eugene V. Horohorin <genix@altlinux.ru> 1.1-alt1
- fix python linking
- exclude %_bindir/test
- initial build for ALT Linux

