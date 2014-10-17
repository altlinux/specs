%define oname exam

%def_with python3

Name: python-module-%oname
Version: 0.10.5
Release: alt1.git20141006
Summary: Helpers for better testing
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/exam/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/Fluxx/exam.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-mock python-tools-pep8 pyflakes
BuildPreReq: python-module-mock python-module-nose
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-mock python3-tools-pep8 pyflakes
BuildPreReq: python3-module-mock python3-module-nose
%endif

%py_provides %oname

%description
Exam is a Python toolkit for writing better tests. It aims to remove a
lot of the boiler plate testing code one often writes, while still
following Python conventions and adhering to the unit testing interface.

%package -n python3-module-%oname
Summary: Helpers for better testing
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Exam is a Python toolkit for writing better tests. It aims to remove a
lot of the boiler plate testing code one often writes, while still
following Python conventions and adhering to the unit testing interface.

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
python setup.py nosetests
%if_with python3
pushd ../python3
python3 setup.py test
python3 setup.py nosetests
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
* Fri Oct 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.5-alt1.git20141006
- Initial build for Sisyphus

