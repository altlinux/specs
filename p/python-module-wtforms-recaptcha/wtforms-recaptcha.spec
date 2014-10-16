%define oname wtforms-recaptcha

%def_with python3

Name: python-module-%oname
Version: 0.3.2
Release: alt1
Summary: Custom WTForms field that handles reCaptcha display and validation
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/wtforms-recaptcha/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-wtforms python-module-nose
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-wtforms python3-module-nose
%endif

%py_provides %oname

%description
WTForms-reCaptcha is a convenient field for WTForms that transparently
handles reCaptcha display and validation via corresponding widget and
validator classes.

%package -n python3-module-%oname
Summary: Custom WTForms field that handles reCaptcha display and validation
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
WTForms-reCaptcha is a convenient field for WTForms that transparently
handles reCaptcha display and validation via corresponding widget and
validator classes.

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
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc AUTHORS *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS *.rst
%python3_sitelibdir/*
%endif

%changelog
* Thu Oct 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2-alt1
- Initial build for Sisyphus

