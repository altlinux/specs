%define oname ipyroute

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.0.16
Release: alt1.git20150210
Summary: Yet another interface for iproute2
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/ipyroute/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/jta/ipyroute.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-sh python-module-netaddr
BuildPreReq: python-module-six python-module-nose
BuildPreReq: python-module-mock
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-sh python3-module-netaddr
BuildPreReq: python3-module-six python3-module-nose
BuildPreReq: python3-module-mock
%endif

%py_provides %oname
Requires: iproute2
%py_requires sh netaddr six

%description
Yet another interface for iproute2.

%package -n python3-module-%oname
Summary: Yet another interface for iproute2
Group: Development/Python3
%py3_provides %oname
Requires: iproute2
%py3_requires sh netaddr six

%description -n python3-module-%oname
Yet another interface for iproute2.

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
python setup.py test
nosetests -v
%if_with python3
pushd ../python3
python3 setup.py test
nosetests3 -v
popd
%endif

%files
%doc *.md
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/*
%endif

%changelog
* Wed Feb 11 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.16-alt1.git20150210
- Version 0.0.16

* Tue Feb 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.13-alt1.git20150202
- Initial build for Sisyphus

