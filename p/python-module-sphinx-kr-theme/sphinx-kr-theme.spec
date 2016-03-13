%define oname sphinx-kr-theme

%def_with python3

Name: python-module-%oname
Version: 0.1.0
Release: alt1.git20140613.1
Summary: The third-part package of kennethreitz/kr-sphinx-themes
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/sphinx-kr-theme/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/tonyseek/sphinx-kr-theme.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
%endif

%py_provides sphinx_kr_theme

%description
This is the third-part package of Kenneth Reitz's krTheme. You will not
have to copy the theme files into VCS or register it as submodule
anymore.

%package -n python3-module-%oname
Summary: The third-part package of kennethreitz/kr-sphinx-themes
Group: Development/Python3
%py3_provides sphinx_kr_theme

%description -n python3-module-%oname
This is the third-part package of Kenneth Reitz's krTheme. You will not
have to copy the theme files into VCS or register it as submodule
anymore.

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
%doc *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.0-alt1.git20140613.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Jan 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt1.git20140613
- Initial build for Sisyphus

