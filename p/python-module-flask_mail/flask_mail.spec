%define oname flask_mail

%def_with python3

Name: python-module-%oname
Version: 0.9.1
Release: alt1.git20141015.1.1
Summary: Flask extension for sending email
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/Flask-Mail/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/mattupstate/flask-mail.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-nose
BuildPreReq: python-module-flask
BuildPreReq: python-module-blinker
BuildPreReq: python-module-speaklater
BuildPreReq: python-module-mock
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-nose
BuildPreReq: python3-module-flask
BuildPreReq: python3-module-blinker
BuildPreReq: python3-module-speaklater
BuildPreReq: python3-module-mock
%endif

%py_provides %oname

%description
Flask-Mail is a Flask extension providing simple email sending
capabilities.

Documentation: http://packages.python.org/Flask-Mail

%package -n python3-module-%oname
Summary: Flask extension for sending email
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Flask-Mail is a Flask extension providing simple email sending
capabilities.

Documentation: http://packages.python.org/Flask-Mail

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
%doc CHANGES *.rst docs/*.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc CHANGES *.rst docs/*.rst
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.9.1-alt1.git20141015.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9.1-alt1.git20141015.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Oct 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.1-alt1.git20141015
- Initial build for Sisyphus

