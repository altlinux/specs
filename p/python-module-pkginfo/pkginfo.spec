%define oname pkginfo

%def_with python3
%def_with check

Name: python-module-%oname
Version: 1.9.6
Release: alt1
Summary: Query metadatdata from sdists / bdists / installed packages
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pkginfo/

Source: %name-%version.tar
BuildArch: noarch

BuildRequires: python-modules-wsgiref
%if_with python3
BuildRequires(pre): rpm-build-python3
%endif
%if_with check
BuildRequires: python3-module-pytest-cov
%endif

%add_python_req_skip configparser

%description
This package provides an API for querying the distutils metadata written
in the PKG-INFO file inside a source distriubtion (an sdist) or a binary
distribution (e.g., created by running bdist_egg). It can also query the
EGG-INFO directory of an installed distribution, and the *.egg-info
stored in a "development checkout" (e.g, created by running setup.py
develop).

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This package provides an API for querying the distutils metadata written
in the PKG-INFO file inside a source distriubtion (an sdist) or a binary
distribution (e.g., created by running bdist_egg). It can also query the
EGG-INFO directory of an installed distribution, and the *.egg-info
stored in a "development checkout" (e.g, created by running setup.py
develop).

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Query metadatdata from sdists / bdists / installed packages
Group: Development/Python3

%description -n python3-module-%oname
This package provides an API for querying the distutils metadata written
in the PKG-INFO file inside a source distriubtion (an sdist) or a binary
distribution (e.g., created by running bdist_egg). It can also query the
EGG-INFO directory of an installed distribution, and the *.egg-info
stored in a "development checkout" (e.g, created by running setup.py
develop).

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
This package provides an API for querying the distutils metadata written
in the PKG-INFO file inside a source distriubtion (an sdist) or a binary
distribution (e.g., created by running bdist_egg). It can also query the
EGG-INFO directory of an installed distribution, and the *.egg-info
stored in a "development checkout" (e.g, created by running setup.py
develop).

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
This package provides an API for querying the distutils metadata written
in the PKG-INFO file inside a source distriubtion (an sdist) or a binary
distribution (e.g., created by running bdist_egg). It can also query the
EGG-INFO directory of an installed distribution, and the *.egg-info
stored in a "development checkout" (e.g, created by running setup.py
develop).

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
This package provides an API for querying the distutils metadata written
in the PKG-INFO file inside a source distriubtion (an sdist) or a binary
distribution (e.g., created by running bdist_egg). It can also query the
EGG-INFO directory of an installed distribution, and the *.egg-info
stored in a "development checkout" (e.g, created by running setup.py
develop).

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install

%check
%tox_check

%files
%doc *.txt
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%_bindir/*.py3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Thu Mar 02 2023 Anton Vyatkin <toni@altlinux.org> 1.9.6-alt1
- (NMU) New version 1.9.6
- Fix BuildRequires
- Enable check

* Tue Aug 10 2021 Grigory Ustinov <grenka@altlinux.org> 1.2-alt3
- Build without docs.

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.2-alt2.b1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.2-alt2.b1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Feb 03 2016 Sergey Alembekov <rt@altlinux.ru> 1.2-alt2.b1
- cleanup buildreq

* Sat Oct 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1.b1
- Initial build for Sisyphus

