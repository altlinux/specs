%define oname webenv
Name: python-module-%oname
Version: 0.6.3
Release: alt1.1
Summary: Abstraction layer on top of wsgi providing request, response and application abstractions
License: MPL 1.1/GPL 2.0/LGPL 2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/webenv/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools python-module-functest
BuildPreReq: python-module-cherrypy python-modules-json
BuildPreReq: python-module-httplib2

%py_provides %oname

%description
A thin abstraction layer on top of wsgi providing request, response and
application abstractions.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%check
python setup.py test

%files
%doc README doc/_build/html
%_bindir/*
%python_sitelibdir/*

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.6.3-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Dec 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.3-alt1
- Initial build for Sisyphus

