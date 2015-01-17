%define oname delfick_error

%def_with python3

Name: python-module-%oname
Version: 1.6.1
Release: alt1.git20141115
Summary: Customized Exception class
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/delfick_error/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/delfick/delfick_error.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-six
BuildPreReq: python-module-noseOfYeti python-module-nose
BuildPreReq: python-module-mock
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-six
BuildPreReq: python3-module-noseOfYeti python3-module-nose
BuildPreReq: python3-module-mock
%endif

%py_provides %oname
%py_requires functools six

%description
This is an error class that I keep remaking in projects.

%package -n python3-module-%oname
Summary: Customized Exception class
Group: Development/Python3
%py3_provides %oname
%py3_requires functools six

%description -n python3-module-%oname
This is an error class that I keep remaking in projects.

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
./test.sh -v
%if_with python3
pushd ../python3
python3 setup.py test
sed -i 's|nosetests|nosetests3|' test.sh
./test.sh -v
popd
%endif

%files
%doc *.rst docs/docs/*.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst docs/docs/*.rst
%python3_sitelibdir/*
%endif

%changelog
* Sat Jan 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.1-alt1.git20141115
- Initial build for Sisyphus

