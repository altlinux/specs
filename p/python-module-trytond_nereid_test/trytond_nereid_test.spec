%define oname trytond_nereid_test
Name: python-module-%oname
Version: 3.2.1.0
Release: alt1
Summary: Tryton - Web Framework Test Supplement
License: GPLv3
Group: Development/Python
Url: https://pypi.python.org/pypi/trytond_nereid_test/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests python-module-trytond
BuildPreReq: python-module-trytond_nereid python-module-sql
BuildPreReq: python-module-polib python-module-dateutil
BuildPreReq: python-module-genshi python-module-relatorio
BuildPreReq: python-module-lxml python-module-openlabs_email_queue
BuildPreReq: python-module-trytond_company python-module-flask-login
BuildPreReq: python-module-blink python-module-blinker
BuildPreReq: python-module-trytond_party python-module-trytond_currency
BuildPreReq: python-module-trytond_country

%description
This module is an optional tryton module which helps in testing nereid
features. This module is not required for the regular functioning of
nereid but if you are developing on nereid, you could use this module to
write tests.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%check
python setup.py test

%files
%doc *.rst
%python_sitelibdir/*

%changelog
* Tue Oct 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.1.0-alt1
- Initial build for Sisyphus

