%define oname jdcal

%def_with python3

Name: python-module-%oname
Version: 1.0
Release: alt2.git20111008
Summary: Julian dates from proleptic Gregorian and Julian calendars
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/jdcal/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/phn/jdcal.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires: python-devel python-module-setuptools-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools-tests
%endif

%py_provides %oname

%description
This module contains functions for converting between Julian dates and
calendar dates.

%package -n python3-module-%oname
Summary: Julian dates from proleptic Gregorian and Julian calendars
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
This module contains functions for converting between Julian dates and
calendar dates.

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

%files
%doc *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Mon Feb 08 2016 Sergey Alembekov <rt@altlinux.ru> 1.0-alt2.git20111008
- Disabled unnecessary dependents

* Wed Feb 11 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.git20111008
- Initial build for Sisyphus

