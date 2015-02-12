%define oname derive

%def_with python3

Name: python-module-%oname
Version: 0.0.3
Release: alt1.git20150208
Summary: Python base classes
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/Derive/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/geowurster/Derive.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-coverage python-module-nose
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-coverage python3-module-nose
%endif

%py_provides %oname

%description
Common Python base classes.

%package -n python3-module-%oname
Summary: Python base classes
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Common Python base classes.

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
nosetests
%if_with python3
pushd ../python3
python3 setup.py test
nosetests3
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
* Thu Feb 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.3-alt1.git20150208
- Initial build for Sisyphus

