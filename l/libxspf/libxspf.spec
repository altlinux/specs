Name: libxspf
Version: 1.2.0
Release: alt1.1

Summary: XSPF playlist reading and writing support

License: BSD
Group: System/Libraries
Url: http://libspiff.sourceforge.net/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://prdownloads.sourceforge.net/libspiff/%name-%version.tar.bz2

# Automatically added by buildreq on Sat Mar 07 2009
BuildRequires: gcc-c++ libexpat-devel liburiparser-devel libcpptest-devel

Provides: libspiff
Obsoletes: libspiff

%description
libxspf brings XSPF playlist reading and writing support to your C++
application.

%package devel
Summary: Header files for %name
Group: Development/Other
Requires: %name = %version-%release
Provides: libspiff-devel
Obsoletes: libspiff-devel

%description devel
Header files for libspiff.

%prep
%setup -q

%build
%configure --disable-static
sed -ri 's/^(hardcode_libdir_flag_spec|runpath_var)=.*/\1=/' libtool
%make_build

%install
%makeinstall_std

%files
%doc AUTHORS ChangeLog NEWS README THANKS
%_bindir/*
%_libdir/lib*.so.*

%files devel
%_libdir/lib*.so
%_includedir/xspf/
%_pkgconfigdir/*
%doc examples/

%changelog
* Sat Feb 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt1.1
- Removed bad RPATH

* Sat Mar 07 2009 Vitaly Lipatov <lav@altlinux.ru> 1.2.0-alt1
- new version (1.2.0)
- rename package

* Mon Sep 22 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt1
- new version 1.0.0 (with rpmrb script)

* Sat Mar 08 2008 Vitaly Lipatov <lav@altlinux.ru> 0.8.3-alt1
- new version 0.8.3 (with rpmrb script)

* Mon Dec 24 2007 Vitaly Lipatov <lav@altlinux.ru> 0.8.2-alt2
- rebuld with new liburiparser 0.6.2 (change soname)

* Sat Nov 03 2007 Vitaly Lipatov <lav@altlinux.ru> 0.8.2-alt1
- new version 0.8.2 (with rpmrb script)

* Sun Oct 07 2007 Vitaly Lipatov <lav@altlinux.ru> 0.8.1-alt1
- new version 0.8.1 (with rpmrb script)

* Tue Sep 18 2007 Vitaly Lipatov <lav@altlinux.ru> 0.8.0-alt1
- new version 0.8.0 (with rpmrb script)

* Sun Aug 05 2007 Vitaly Lipatov <lav@altlinux.ru> 0.7.1-alt1
- initial build for ALT Linux Sisyphus (spec from PLD)

