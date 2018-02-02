%define oname click-plugins

%def_with python3

Name: python-module-%oname
Version: 1.0.2
Release: alt1.1
Summary: Register CLI commands via setuptools entry-points
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/click-plugins

# https://github.com/click-contrib/click-plugins.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-click-tests python-module-pytest-cov
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-click-tests python3-module-pytest-cov
%endif

%py_provides click_plugins
%py_requires click

%description
An extension module for click to enable registering CLI commands via
setuptools entry-points.

%if_with python3
%package -n python3-module-%oname
Summary: Register CLI commands via setuptools entry-points
Group: Development/Python3
%py3_provides click_plugins
%py3_requires click

%description -n python3-module-%oname
An extension module for click to enable registering CLI commands via
setuptools entry-points.
%endif

%package examples
Summary: Examples for %oname
Group: Development/Documentation
BuildArch: noarch

%description examples
An extension module for click to enable registering CLI commands via
setuptools entry-points.

This package contains examples for %oname.

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
python setup.py test -v
py.test -vv tests --cov click_plugins --cov-report term-missing
%if_with python3
pushd ../python3
python3 setup.py test -v
py.test3 -vv tests --cov click_plugins --cov-report term-missing
popd
%endif

%files
%doc *.txt *.rst
%python_sitelibdir/*

%files examples
%doc example/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0.2-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Aug 16 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.2-alt1
- Updated to upstream version 1.0.2.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0-alt1.git20150720.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Aug 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.git20150720
- Initial build for Sisyphus

