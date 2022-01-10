%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: log4cplus
Version: 2.0.7
Release: alt1
Summary: Logging library to C++
License: Apache-2.0 or BSD-2-Clause
Group: Development/C++
Url: http://log4cplus.sourceforge.net/

# https://github.com/log4cplus/log4cplus.git
Source: %name-%version.tar

# submodules
Source1: %name-%version-catch.tar
Source2: %name-%version-threadpool.tar

Patch1: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: gcc-c++ doxygen graphviz swig
BuildRequires: python3-devel

%description
log4cplus is a simple to use C++ logging API providing thread-safe,
flexible, and arbitrarily granular control over log management and
configuration.  It is modeled after the Java log4j API.

%package -n lib%name
Summary: Shared libraries of logging library to C++
Group: System/Libraries

%description -n lib%name
log4cplus is a simple to use C++ logging API providing thread-safe,
flexible, and arbitrarily granular control over log management and
configuration.  It is modeled after the Java log4j API.

This package contains shared libraries of log4cplus.

%package -n lib%name-devel
Summary: Development files of logging library to C++
Group: Development/C++
Requires: lib%name = %EVR

%description -n lib%name-devel
log4cplus is a simple to use C++ logging API providing thread-safe,
flexible, and arbitrarily granular control over log management and
configuration.  It is modeled after the Java log4j API.

This package contains development files of log4cplus.

%package -n lib%name-devel-docs
Summary: Development documentation for logging library to C++
Group: Development/Documentation
BuildArch: noarch

%description -n lib%name-devel-docs
log4cplus is a simple to use C++ logging API providing thread-safe,
flexible, and arbitrarily granular control over log management and
configuration.  It is modeled after the Java log4j API.

This package contains development documentation and manpages for
log4cplus.

%package -n python3-module-%name
Summary: Python bindings of logging library to C++
Group: Development/Python3
Requires: lib%name = %EVR
%py3_provides %name

%description -n python3-module-%name
log4cplus is a simple to use C++ logging API providing thread-safe,
flexible, and arbitrarily granular control over log management and
configuration.  It is modeled after the Java log4j API.

This package contains Python bindings of log4cplus.

%prep
%setup -a1 -a2
%patch1 -p1

%build
%add_optflags -D_FILE_OFFSET_BITS=64

export PYTHON=python3
%autoreconf
%configure \
	--enable-static=no \
	--enable-threads=yes \
	--with-working-c-locale \
	--with-python \
	%nil

sed -i 's|^\(SWIG =.*\)|\1 -py3|' $(find ./ -name Makefile)

%make_build

pushd docs
doxygen doxygen.config
popd

%install
%makeinstall_std

%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
mkdir -p %buildroot%python3_sitelibdir/%name
mv %buildroot%python3_sitelibdir_noarch/%name/* %buildroot%python3_sitelibdir/%name/
%endif

install -d %buildroot%_man3dir
install -m644 docs/man/man3/* %buildroot%_man3dir

%check
%make check

%files -n lib%name
%doc LICENSE
%doc AUTHORS ChangeLog NEWS README* TODO
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*

%files -n lib%name-devel-docs
%doc docs/html/*
%_man3dir/*

%files -n python3-module-%name
%python3_sitelibdir/%name

%changelog
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

