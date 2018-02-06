%define oname webplot

%def_with python3

Name: python-module-%oname
Version: 0.8
Release: alt1.git20150320.1.1
Summary: Expose matplotlib figures over http
License: GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/webplot/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/huyng/webplot.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-matplotlib python-module-flask
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-matplotlib python3-module-flask
%endif

%py_provides %oname
%py_requires matplotlib flask

%description
Expose your matplotlib figures over http with 1 line of code.

%if_with python3
%package -n python3-module-%oname
Summary: Expose matplotlib figures over http
Group: Development/Python3
%py3_provides %oname
%py3_requires matplotlib flask

%description -n python3-module-%oname
Expose your matplotlib figures over http with 1 line of code.
%endif

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
%doc *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.8-alt1.git20150320.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.8-alt1.git20150320.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Mar 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8-alt1.git20150320
- Initial build for Sisyphus

