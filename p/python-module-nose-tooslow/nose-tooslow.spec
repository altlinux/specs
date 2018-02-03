%define oname nose-tooslow

%def_with python3

Name: python-module-%oname
Version: 0.1
Release: alt1.git20141104.1.1
Summary: Treat tests that execute too slowly as failed
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/nose-tooslow/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/mpirnat/nose-tooslow.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-nose
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-nose python-tools-2to3
%endif

%py_provides tooslow

%description
Plugin for the Nose test framework that treats tests that take too long
to execute as errors.

The maximum allowable time defaults to 1.0 seconds or may be configured
as desired.

%package -n python3-module-%oname
Summary: Treat tests that execute too slowly as failed
Group: Development/Python3
%py3_provides tooslow

%description -n python3-module-%oname
Plugin for the Nose test framework that treats tests that take too long
to execute as errors.

The maximum allowable time defaults to 1.0 seconds or may be configured
as desired.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
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
%doc *.md
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1-alt1.git20141104.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1-alt1.git20141104.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Nov 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.git20141104
- Initial build for Sisyphus

