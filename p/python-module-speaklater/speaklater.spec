%define oname speaklater

%def_with python3

Name: python-module-%oname
Version: 1.3
Release: alt1.git20120701.1.1
Summary: Implements a lazy string for python useful for use with gettext
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/speaklater/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/mitsuhiko/speaklater.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_provides %oname

%description
A module that provides lazy strings for translations. Basically you get
an object that appears to be a string but changes the value every time
the value is evaluated based on a callable you provide.

For example you can have a global lazy_gettext function that returns a
lazy string with the value of the current set language.

%package -n python3-module-%oname
Summary: Implements a lazy string for python useful for use with gettext
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
A module that provides lazy strings for translations. Basically you get
an object that appears to be a string but changes the value every time
the value is evaluated based on a callable you provide.

For example you can have a global lazy_gettext function that returns a
lazy string with the value of the current set language.

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
%doc README
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc README
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.3-alt1.git20120701.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.3-alt1.git20120701.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Oct 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt1.git20120701
- Initial build for Sisyphus

