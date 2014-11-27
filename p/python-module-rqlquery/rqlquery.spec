%define oname rqlquery
Name: python-module-%oname
Version: 0.2.0
Release: alt1
Summary: Experimental ORM Query object
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/rqlquery/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests cubicweb
BuildPreReq: python-module-iso8601

Requires: cubicweb
%py_requires iso8601

%description
Experimental ORM Query object

The idea is to make RQL requests building simpler, and all with pythonic
syntax.

It borrows a lot from the SQLAlchemy ORM.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%check
python setup.py test

%files
%doc README
%python_sitelibdir/*

%changelog
* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt1
- Initial build for Sisyphus

