%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict
%define soname 9
%def_without python

Name: log4cplus
Version: 2.1.2
Release: alt2
Summary: Logging library to C++
License: Apache-2.0 or BSD-2-Clause
Group: Development/C++
Url: https://sourceforge.net/projects/log4cplus/
VCS: https://github.com/log4cplus/log4cplus.git
Source: %name-%version.tar

# submodules
Source1: %name-%version-catch.tar
Source2: %name-%version-threadpool.tar

Patch1: %name-%version-alt.patch

%if_with python
BuildRequires(pre): rpm-build-python3
BuildRequires: swit
BuildRequires: python3-devel
%endif
BuildRequires: gcc-c++ doxygen graphviz

%description
log4cplus is a simple to use C++ logging API providing thread-safe,
flexible, and arbitrarily granular control over log management and
configuration.  It is modeled after the Java log4j API.

%package -n lib%name%soname
Summary: Shared libraries of logging library to C++
Group: System/Libraries

%description -n lib%name%soname
log4cplus is a simple to use C++ logging API providing thread-safe,
flexible, and arbitrarily granular control over log management and
configuration.  It is modeled after the Java log4j API.

This package contains shared libraries of log4cplus.

%package -n lib%name-devel
Summary: Development files of logging library to C++
Group: Development/C++
Requires: lib%name%soname = %EVR

%description -n lib%name-devel
log4cplus is a simple to use C++ logging API providing thread-safe,
flexible, and arbitrarily granular control over log management and
configuration.  It is modeled after the Java log4j API.

This package contains development files of log4cplus.

%if_with python

%package -n python3-module-%name
Summary: Python bindings of logging library to C++
Group: Development/Python3
Requires: lib%name%soname = %EVR
%py3_provides %name

%description -n python3-module-%name
log4cplus is a simple to use C++ logging API providing thread-safe,
flexible, and arbitrarily granular control over log management and
configuration.  It is modeled after the Java log4j API.

This package contains Python bindings of log4cplus.
%endif

%prep
%setup -a1 -a2
%patch1 -p1
%ifarch %e2k
# INTEL COMPILER is based on the EDG frontend, so the workarounds
# for it work for any compiler based on the EDG frontend.
sed -i "s/__INTEL_COMPILER/__EDG__/" include/log4cplus/config.hxx
%endif

%build
%add_optflags -D_FILE_OFFSET_BITS=64

export PYTHON=python3
export CPPFLAGS="-D_FILE_OFFSET_BITS=64"
%autoreconf
%configure \
	--enable-static=no \
	--enable-threads=yes \
	--with-working-c-locale \
	%if_with python
	--with-python \
	%endif
	%nil

sed -i 's|^\(SWIG =.*\)|\1 -py3|' $(find ./ -name Makefile)

%make_build

%install
%makeinstall_std

%check
%make check

%files -n lib%name%soname
%doc LICENSE
%doc AUTHORS ChangeLog NEWS README* TODO
%_libdir/*.so.%soname
%_libdir/*.so.%soname.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*

%if_with python
%files -n python3-module-%name
%python3_sitelibdir/%name
%endif

%changelog
* Thu Aug 07 2025 Anton Farygin <rider@altlinux.com> 2.1.2-alt2
- fix FTBFS: built without python

* Tue May 13 2025 Anton Farygin <rider@altlinux.com> 2.1.2-alt1
- 2.0.7 -> 2.1.2

* Tue Jun 06 2023 Grigory Ustinov <grenka@altlinux.org> 2.0.7-alt1.2
- Make docs arch dependent.

* Tue Feb 15 2022 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 2.0.7-alt1.1
- Fixed build for Elbrus.

* Mon Jan 10 2022 Aleksei Nikiforov <darktemplar@altlinux.org> 2.0.7-alt1
- Updated to upstream version 2.0.7.

* Fri Jun 18 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 2.0.6-alt1
- Updated to upstream version 2.0.6.

* Mon Oct 26 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 2.0.5-alt1
- Updated to upstream version 2.0.5.

* Thu Mar 12 2020 Andrey Bychkov <mrdrew@altlinux.org> 2.0.0-alt3.rc2.1
- Build fot python2 disabled.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.0.0-alt2.rc2.1
- (NMU) Rebuilt with python-3.6.4.

* Wed Nov 15 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.0.0-alt2.rc2
- Updated to upstream version 2.0.0-rc2.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0.0-alt1.git20150807.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Fri Aug 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1.git20150807
- New snapshot (ALT #31238)

* Sat Jun 13 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.0.0-alt1.git20150412.1
- Rebuilt for gcc5 C++11 ABI.

* Thu May 07 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1.git20150412
- Version 2.0.0
- Added module for Python

* Mon Jul 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt1.rc2
- Version 1.2.0-rc2

* Thu Jun 05 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt1.rc1
- Version 1.2.0-rc1

* Thu Nov 14 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.2-alt1
- Version 1.1.2

* Wed Feb 06 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt1.rc3
- Version 1.1.1-rc3

* Fri Nov 30 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1
- Initial build for Sisyphus

