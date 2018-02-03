%define _unpackaged_files_terminate_build 1
%define oname cligj

%def_with python3

Name: python-module-%oname
Version: 0.4.0
Release: alt2.1
Summary: Click params for GeoJSON CLI
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/cligj/

# https://github.com/mapbox/cligj.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-click-tests
BuildRequires: python-module-pytest
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildRequires: python3-module-pytest
BuildPreReq: python3-module-click-tests
%endif

%py_provides %oname
%py_requires click

%description
Common arguments and options for GeoJSON processing commands, using
Click.

%package -n python3-module-%oname
Summary: Click params for GeoJSON CLI
Group: Development/Python3
%py3_provides %oname
%py3_requires click

%description -n python3-module-%oname
Common arguments and options for GeoJSON processing commands, using
Click.

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
py.test -vv
%if_with python3
pushd ../python3
export PYTHONPATH=$PWD
py.test3 -vv
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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.4.0-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Aug 16 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.4.0-alt2
- Fixed build.

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.4.0-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.0-alt1.git20150528.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Aug 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt1.git20150528
- Version 0.2.0

* Wed Jan 21 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt1.git20141227
- Initial build for Sisyphus

