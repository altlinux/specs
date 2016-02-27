%def_with python
%def_with python3

Name: libcap-ng
Version: 0.7.4
Release: alt1.3

Summary: An alternate posix capabilities library
License: LGPLv2+
Group: System/Libraries

Url: http://people.redhat.com/sgrubb/libcap-ng
Source: http://people.redhat.com/sgrubb/libcap-ng/%name-%version.tar.gz

BuildRequires: kernel-headers >= 2.6.11
BuildRequires: libattr-devel

%if_with python3
# not BR(pre) as we don't need those macros to rpm -bs
# (only used within setup/build/install/files sections);
# see also https://bugzilla.altlinux.org/8579
BuildPreReq: rpm-build-python3
BuildPreReq: python3-devel
%endif

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

%if_with python
%package -n python-module-%name
Summary: Python bindings for libcap-ng library
License: LGPLv2+
Group: Development/Python
BuildRequires: python-devel swig
Requires: %name = %version-%release

%description -n python-module-%name
The libcap-ng-python package contains the bindings so that libcap-ng
and can be used by python applications.
%endif

%if_with python3
%package -n python3-module-%name
Summary: Python bindings for libcap-ng library
License: LGPLv2+
Group: Development/Python3
BuildRequires: swig
Requires: %name = %version-%release

%description -n python3-module-%name
The libcap-ng-python package contains the bindings so that libcap-ng
and can be used by python applications.
%endif

%package utils
Summary: Utilities for analysing and setting file capabilities
License: GPLv2+
Group: Development/C

%description utils
The libcap-ng-utils package contains applications to analyse the
posix capabilities of all the program running on a system. It also
lets you set the file system based capabilities.

%prep
%setup

%if_with python3
cp -fR . ../python3
sed -i "/LIBS/s/libcap-ng.la/libcap-ng.la -lpython%_python3_version%_python3_abiflags/g" \
	../python3/bindings/python/Makefile.am
sed -i 's|swig -o|swig -py3 -o|' \
	../python3/bindings/python/Makefile.am
sed -i 's|\(\/Python.h\)|%_python3_abiflags\1|' \
	../python3/configure.ac
%endif

sed -i "/LIBS/s/libcap-ng.la/libcap-ng.la -lpython%_python_version/g" \
	bindings/python/Makefile.am

%build
%autoreconf
%configure --libdir=/%_lib
%make_build

%if_with python3
pushd ../python3
export PYTHON=python3
%autoreconf
#add_optflags -I%python3_includedir%_python3_abiflags
%configure --libdir=/%_lib
%make_build PYLIBVER=python%_python3_version%_python3_abiflags
popd
%endif

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

%if_with python3
pushd ../python3
%make install DESTDIR=$PWD/buildroot
install -d %buildroot%python3_sitelibdir
mv buildroot%python3_sitelibdir/* %buildroot%python3_sitelibdir/
rm -f %buildroot%python3_sitelibdir/*.{a,la}
popd
%endif

%files
%doc COPYING.LIB
/%_lib/libcap-ng.so.*

%files devel
%_man3dir/*
%_includedir/cap-ng.h
%_libdir/libcap-ng.so
%_datadir/aclocal/cap-ng.m4
%_pkgconfigdir/libcap-ng.pc

%if_with python
%files -n python-module-%name
%python_sitelibdir/*
%endif

%files utils
%doc COPYING
%_bindir/*
%_man8dir/*

%if_with python3
%files -n python3-module-%name
%python3_sitelibdir/*
%endif

%changelog
* Wed Feb 24 2016 Michael Shigorin <mike@altlinux.org> 0.7.4-alt1.3
- fix BR(pre): rpm-build-python3 towards a simple BR
  (makes --without python3 work again with hasher >= 1.3.28)

* Sun Feb 07 2016 Michael Shigorin <mike@altlinux.org> 0.7.4-alt1.2
- fix knobs so that both python modules get built by default
  (thx ldv@ for spotting the breakage)

* Mon Jan 18 2016 Michael Shigorin <mike@altlinux.org> 0.7.4-alt1.1
- BOOTSTRAP: disable python, python3, don't ask for swig either

* Tue Sep 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.4-alt1
- Version 0.7.4
- Added module for Python 3

* Thu Feb 07 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 0.7.3-alt1
- New version

* Wed Sep 12 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 0.7-alt1
- New version

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
