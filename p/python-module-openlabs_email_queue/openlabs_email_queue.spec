%define oname openlabs_email_queue

%def_without python3
%def_disable check

Name: python-module-%oname
Version: 3.2.0.1
Release: alt1.git20140902
Summary: Trytond Email Queue Module
License: GPLv3
Group: Development/Python
Url: https://pypi.python.org/pypi/openlabs_email_queue/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/openlabs/email-queue.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-flake8 python-module-psycopg2
BuildPreReq: python-module-mock python-module-fake-factory
BuildPreReq: python-module-pretend python-module-coveralls
BuildPreReq: python-module-trytond-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-flake8 python3-module-psycopg2
BuildPreReq: python3-module-mock python3-module-fake-factory
BuildPreReq: python3-module-pretend python3-module-coveralls
BuildPreReq: python-tools-2to3 python3-module-trytond-tests
%endif

%py_provides email_queue

%description
This module implements an email queue which acts as a transaction safe
buffer for tryton modules to send emails.

%package -n python3-module-%oname
Summary: Trytond Email Queue Module
Group: Development/Python3
%py3_provides email_queue

%description -n python3-module-%oname
This module implements an email queue which acts as a transaction safe
buffer for tryton modules to send emails.

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
%doc CHANGELOG *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc CHANGELOG *.rst
%python3_sitelibdir/*
%endif

%changelog
* Tue Oct 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.0.1-alt1.git20140902
- Initial build for Sisyphus

