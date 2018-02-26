
Summary: An alternate posix capabilities library
Name: libcap-ng
Version: 0.6.6
Release: alt1.1
License: LGPLv2+
Group: System/Libraries
Url: http://people.redhat.com/sgrubb/libcap-ng

Source: http://people.redhat.com/sgrubb/libcap-ng/%name-%version.tar.gz

BuildRequires: kernel-headers >= 2.6.11 libattr-devel python-devel swig

%description
Libcap-ng is a library that makes using posix capabilities easier

%package devel
Summary: Header files for libcap-ng library
License: LGPLv2+
Group: Development/C
Requires: kernel-headers >= 2.6.11
Requires: %name = %version-%release

%description devel
The libcap-ng-devel package contains the files needed for developing
applications that need to use the libcap-ng library.

%package -n python-module-%name
Summary: Python bindings for libcap-ng library
License: LGPLv2+
Group: Development/Python
Requires: %name = %version-%release

%description -n python-module-%name
The libcap-ng-python package contains the bindings so that libcap-ng
and can be used by python applications.

%package utils
Summary: Utilities for analysing and setting file capabilities
License: GPLv2+
Group: Development/C

%description utils
The libcap-ng-utils package contains applications to analyse the
posix capabilities of all the program running on a system. It also
lets you set the file system based capabilities.

%prep
%setup -q
sed -i "/LIBS/s/libcap-ng.la/libcap-ng.la -lpython%__python_version/g" bindings/python/Makefile.am

%build
%autoreconf
%configure --libdir=/%_lib
%make_build

%install
%makeinstall_std

# Move the symlink
rm -f %buildroot/%_lib/%name.so
mkdir -p %buildroot%_libdir
VLIBNAME=$(ls %buildroot/%_lib/%name.so.*.*.*)
LIBNAME=$(basename $VLIBNAME)
ln -s ../../%_lib/$LIBNAME %buildroot%_libdir/%name.so

# Move the pkgconfig file
mv %buildroot/%_lib/pkgconfig %buildroot%_libdir

# Remove a couple things so they don't get picked up
rm -f %buildroot/%_lib/*.{a,la}
rm -f %buildroot%python_sitelibdir/*.{a,la}

%files
%doc COPYING.LIB
/%_lib/libcap-ng.so.*

%files devel
%_man3dir/*
%_includedir/cap-ng.h
%_libdir/libcap-ng.so
%_datadir/aclocal/cap-ng.m4
%_pkgconfigdir/libcap-ng.pc

%files -n python-module-%name
%python_sitelibdir/*

%files utils
%doc COPYING
%_bindir/*
%_man8dir/*

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.6-alt1.1
- Rebuild with Python-2.7

* Sun Jul 17 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 0.6.6-alt1
- New version

* Fri Apr 15 2011 Alexey Shabalin <shaba@altlinux.ru> 0.6.5-alt1.1
- cleanup spec
- rebuild for debuginfo

* Thu Nov 04 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 0.6.5-alt1
- New version

* Thu Jul 22 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 0.6.4-alt1
- Build for ALT
