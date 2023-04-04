%def_disable bootstrap

Name: libcap-ng
Version: 0.8.3
Release: alt2

Summary: An alternate posix capabilities library
License: LGPLv2+
Group: System/Libraries

Url: http://people.redhat.com/sgrubb/libcap-ng
Source: %name-%version.tar

BuildRequires: kernel-headers
BuildRequires: libattr-devel

# not BR(pre) as we don't need those macros to rpm -bs
# (only used within setup/build/install/files sections);
# see also https://bugzilla.altlinux.org/8579
%if_disabled bootstrap
BuildPreReq: rpm-build-python3
BuildPreReq: python3-devel
BuildRequires: swig
%endif

%description
Libcap-ng is a library that makes using posix capabilities easier

%package devel
Summary: Header files for libcap-ng library
License: LGPLv2+
Group: Development/C
Requires: kernel-headers >= 2.6.11
Requires: %name = %EVR

%description devel
The libcap-ng-devel package contains the files needed for developing
applications that need to use the libcap-ng library.

%if_disabled bootstrap

%package -n python3-module-%name
Summary: Python bindings for libcap-ng library
License: LGPLv2+
Group: Development/Python3
Requires: %name = %EVR

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

%build
%autoreconf
%if_disabled bootstrap

export PYTHON=python3
%configure --libdir=/%_lib
%make_build PYLIBVER=python%_python3_version%_python3_abiflags

%else

%configure --libdir=/%_lib \
	--with-python=no \
	--with-python3=no \
	%nil
%make_build

%endif

%install
%makeinstall_std

# Move the symlink
rm -f %buildroot/%_lib/%name.so
rm -f %buildroot/%_lib/libdrop_ambient.so
mkdir -p %buildroot%_libdir
VLIBNAME=$(ls %buildroot/%_lib/%name.so.*.*.*)
VLIBNAME_DROP=$(ls %buildroot/%_lib/libdrop_ambient.so.*.*.*)
LIBNAME=$(basename $VLIBNAME)
LIBDROP_NAME=$(basename $VLIBNAME_DROP)
ln -s ../../%_lib/$LIBNAME %buildroot%_libdir/%name.so
ln -s ../../%_lib/$LIBDROP_NAME %buildroot%_libdir/libdrop_ambient.so

# Move the pkgconfig file
mv %buildroot/%_lib/pkgconfig %buildroot%_libdir

# Remove a couple things so they don't get picked up
rm -f %buildroot/%_lib/*.{a,la}
rm -f %buildroot%python3_sitelibdir/*.{a,la}

%files
%doc COPYING.LIB
/%_lib/libcap-ng.so.*
/%_lib/libdrop_ambient.so.*

%files devel
%_man3dir/*
%_includedir/cap-ng.h
%_libdir/libcap-ng.so
%_libdir/libdrop_ambient.so
%_datadir/aclocal/cap-ng.m4
%_pkgconfigdir/libcap-ng.pc

%files utils
%doc COPYING
%_bindir/*
%_man8dir/*
%_man7dir/*

%if_disabled bootstrap

%files -n python3-module-%name
%python3_sitelibdir/*

%endif

%changelog
* Mon Apr 03 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 0.8.3-alt2
- Simplified the bootstrap sequence (closes: #45741)

* Wed Apr 06 2022 Anton Farygin <rider@altlinux.ru> 0.8.3-alt1
- 0.8.3

* Tue Dec 22 2020 Anton Farygin <rider@altlinux.ru> 0.8.2-alt1
- 0.8.2

* Mon Nov 23 2020 Anton Farygin <rider@altlinux.ru> 0.8.1-alt1
- 0.8.1

* Thu Oct 08 2020 Anton Farygin <rider@altlinux.ru> 0.8-alt1
- 0.8

* Tue Sep 15 2020 Anton Farygin <rider@altlinux.ru> 0.7.11-alt1
- 0.7.11

* Thu Oct 03 2019 Anton Farygin <rider@altlinux.ru> 0.7.10-alt1
- new version
- removed python-2 support

* Tue May 08 2018 Anton Farygin <rider@altlinux.ru> 0.7.9-alt1
- new version

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.7.8-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Mon Oct 09 2017 Anton Farygin <rider@altlinux.ru> 0.7.8-alt1
- new version

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.7.4-alt1.3.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

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
