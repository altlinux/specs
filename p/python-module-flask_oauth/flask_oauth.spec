%define oname flask_oauth

%def_with python3

Name: python-module-%oname
Version: 0.13
Release: alt1.git20121006.1.1
Summary: Adds OAuth support to Flask
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/Flask-OAuth/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/mitsuhiko/flask-oauth.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-flask python-module-oauth2
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-flask python3-module-oauth2
BuildPreReq: python-tools-2to3
%endif

%py_provides %oname

%description
Implements basic OAuth support for Flask.  Currently it can only
be used to hook up with external OAuth services.  It does not yet
support implementing providers.

%package -n python3-module-%oname
Summary: Adds OAuth support to Flask
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Implements basic OAuth support for Flask.  Currently it can only
be used to hook up with external OAuth services.  It does not yet
support implementing providers.

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
%doc README example docs/*.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc README example docs/*.rst
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.13-alt1.git20121006.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.13-alt1.git20121006.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Oct 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.13-alt1.git20121006
- Initial build for Sisyphus

