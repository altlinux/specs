%define oname wcwidth

%def_with python3

Name: python-module-%oname
Version: 0.1.7
Release: alt2.1
Summary: Measures number of Terminal column cells of wide-character codes
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/wcwidth/

# https://github.com/jquast/wcwidth.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-coverage python-module-pytest-pep8
BuildPreReq: python-module-pytest-flakes python-module-pytest-cov
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-coverage python3-module-pytest-pep8
BuildPreReq: python3-module-pytest-flakes python3-module-pytest-cov
%endif

%py_provides %oname

%description
This API is mainly for Terminal Emulator implementors - any python
program that attempts to determine the printable width of a string on a
Terminal. It is implemented in python (no C library calls) and has no
3rd-party dependencies.

%package tests
Summary: tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This API is mainly for Terminal Emulator implementors - any python
program that attempts to determine the printable width of a string on a
Terminal. It is implemented in python (no C library calls) and has no
3rd-party dependencies.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Measures number of Terminal column cells of wide-character codes
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
This API is mainly for Terminal Emulator implementors - any python
program that attempts to determine the printable width of a string on a
Terminal. It is implemented in python (no C library calls) and has no
3rd-party dependencies.

%package -n python3-module-%oname-tests
Summary: tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
This API is mainly for Terminal Emulator implementors - any python
program that attempts to determine the printable width of a string on a
Terminal. It is implemented in python (no C library calls) and has no
3rd-party dependencies.

This package contains tests for %oname.

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
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
export LC_ALL=en_US.UTF-8
export PYTHONPATH=$PWD
rm -fR build
py.test -vv \
	-rs -W error --flakes \
	wcwidth/tests
%if_with python3
pushd ../python3
export PYTHONPATH=$PWD
rm -fR build
py.test3 -vv \
	-x -W error --flakes \
	--cov wcwidth
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1.7-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Aug 21 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.7-alt2
- Fixed tests.

* Fri Aug 11 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.7-alt1
- Updated to upstream version 0.1.7.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.4-alt1.git20150413.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Aug 08 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.4-alt1.git20150413
- New snapshot

* Fri Feb 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.4-alt1.git20150125
- Initial build for Sisyphus

