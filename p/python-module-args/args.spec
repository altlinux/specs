%define oname args

%def_with python3

Name: python-module-%oname
Version: 0.1.0
Release: alt1.git20121115
Summary: Command Arguments for Humans
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/args/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/kennethreitz/args.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-nose
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-nose
%endif

%py_provides %oname

%description
This simple module gives you an elegant interface for your command line
argumemnts.

%package -n python3-module-%oname
Summary: Command Arguments for Humans
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
This simple module gives you an elegant interface for your command line
argumemnts.

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
%doc *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Wed Feb 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt1.git20121115
- Initial build for Sisyphus

