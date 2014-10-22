%define oname trytond_nereid_auth_facebook

%def_disable check

Name: python-module-%oname
Version: 3.0.2.1
Release: alt1
Summary: Nereid User Authentication using Facebook
License: GPLv3
Group: Development/Python
Url: https://pypi.python.org/pypi/trytond_nereid_auth_facebook/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-flask_oauth python-module-coverage
BuildPreReq: python-module-trytond-tests python-module-trytond_nereid-tests
BuildPreReq: python-module-openlabs_email_queue python-module-blinker
BuildPreReq: python-module-trytond_company python-module-flask-login
BuildPreReq: python-module-trytond_party python-module-trytond_currency
BuildPreReq: python-module-trytond_country python-module-unittest2
#BuildPreReq: python-module-unittest-xml-reporting

%py_provides %oname

%description
Nereid User Authentication using Facebook.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%check
python setup.py test

%files
%python_sitelibdir/*

%changelog
* Wed Oct 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.2.1-alt1
- Initial build for Sisyphus

