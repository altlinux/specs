%define oname pretend

%def_with python3

Name: python-module-%oname
Version: 1.0.8
Release: alt1.git20140630
Summary: A library for stubbing in Python
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/pretend/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/alex/pretend.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-py
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-py
%endif

%py_provides %oname

%description
Pretend is a library to make stubbing with Python easier.

%package -n python3-module-%oname
Summary: A library for stubbing in Python
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Pretend is a library to make stubbing with Python easier.

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
py.test
%if_with python3
pushd ../python3
python3 setup.py test
py.test-%_python3_version
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
* Fri Oct 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.8-alt1.git20140630
- Initial build for Sisyphus

