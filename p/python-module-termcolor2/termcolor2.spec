%define oname termcolor2

%def_with python3

Name: python-module-%oname
Version: 0.0.3
Release: alt1.git20150309
Summary: Simple termcolor wrapper
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/termcolor2
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/v2e4lisp/termcolor2.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-termcolor
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-termcolor
%endif

%py_provides %oname
%py_requires termcolor

%description
Simple wrapper for termcolor (cli colored string).

%if_with python3
%package -n python3-module-%oname
Summary: Simple termcolor wrapper
Group: Development/Python3
%py3_provides %oname
%py3_requires termcolor

%description -n python3-module-%oname
Simple wrapper for termcolor (cli colored string).
%endif

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
python setup.py test -v
python -c 'from termcolor2 import c, colored; \
print (c("hello").red.on_white.blink.underline.dark); \
print (colored("hello", "red", "on_white", ["blink", "underline", "dark"]))'
%if_with python3
pushd ../python3
python3 setup.py test -v
python3 -c 'from termcolor2 import c, colored;
print (c("hello").red.on_white.blink.underline.dark);
print (colored("hello", "red", "on_white", ["blink", "underline", "dark"]))'
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
* Sun Aug 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.3-alt1.git20150309
- Initial build for Sisyphus

