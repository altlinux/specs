%define oname WTForms-Test

%def_with python3

Name: python-module-%oname
Version: 0.1.1
Release: alt1.git20130208
Summary: Various unit test helpers for WTForms based forms
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/WTForms-Test/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/kvesteri/wtforms-test.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-wtforms
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-wtforms python3-module-six
%endif

%py_provides wtforms_test

%description
Various unit test helpers for WTForms based forms.

%package -n python3-module-%oname
Summary: Various unit test helpers for WTForms based forms
Group: Development/Python3
%py3_provides wtforms_test

%description -n python3-module-%oname
Various unit test helpers for WTForms based forms.

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
py.test tests.py
%if_with python3
pushd ../python3
python3 setup.py test
py.test-%_python3_version tests.py
popd
%endif

%files
%doc *.rst docs/*.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst docs/*.rst
%python3_sitelibdir/*
%endif

%changelog
* Tue Dec 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.1-alt1.git20130208
- Initial build for Sisyphus

