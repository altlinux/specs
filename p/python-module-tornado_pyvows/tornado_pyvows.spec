%define oname tornado_pyvows

%def_disable check

Name: python-module-%oname
Version: 0.5.3
Release: alt1.git20141008
Summary: tornado_pyvows are pyvows extensions to tornado web framework
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/tornado_pyvows/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/rafaelcaricio/tornado_pyvows.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests python-module-mock
BuildPreReq: python-module-pyvows-tests python-module-tornado
BuildPreReq: python-module-pycurl python-module-urllib3
BuildPreReq: python-module-gevent python-module-unidecode

%py_provides %oname

%description
This project contains extensions to test Tornado apps under pyvows.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%check
python setup.py test
%make test

%files
%doc *.mkd
%python_sitelibdir/*

%changelog
* Fri Nov 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.3-alt1.git20141008
- Initial build for Sisyphus

