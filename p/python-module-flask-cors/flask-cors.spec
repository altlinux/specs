%define _unpackaged_files_terminate_build 1
%define oname flask-cors

%def_with python3

Name: python-module-%oname
Version: 3.0.2
Release: alt1.1
Summary: Cross Origin Resource Sharing ( CORS ) support for Flask
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/Flask-Cors/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/wcdolphin/flask-cors.git
Source0: https://pypi.python.org/packages/1d/ea/86765a4ae667b4517dc16ef0fc8dd632ca3ea56ef419c4a6de31e715324e/Flask-Cors-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-flask python-module-six
BuildPreReq: python-module-nose
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-flask python3-module-six
BuildPreReq: python3-module-nose
%endif

%py_provides flask_cors

%description
A Flask extension for handling Cross Origin Resource Sharing (CORS),
making cross-origin AJAX possible.

%package -n python3-module-%oname
Summary: Cross Origin Resource Sharing ( CORS ) support for Flask
Group: Development/Python3
%py3_provides flask_cors

%description -n python3-module-%oname
A Flask extension for handling Cross Origin Resource Sharing (CORS),
making cross-origin AJAX possible.

%prep
%setup -q -n Flask-Cors-%{version}

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
%doc *.rst docs/*.rst examples
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst docs/*.rst examples
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 3.0.2-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 3.0.2-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.9.0-alt1.git20141028.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Nov 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.0-alt1.git20141028
- Initial build for Sisyphus

