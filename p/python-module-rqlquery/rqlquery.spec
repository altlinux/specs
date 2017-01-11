%define _unpackaged_files_terminate_build 1
%define oname rqlquery
Name: python-module-%oname
Version: 0.4.0
Release: alt1
Summary: Experimental ORM Query object
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/rqlquery/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/10/e3/973737d1b582bc6816041bb4c3e00f29e60f834f4efc8cfc193c0d3fd0a8/%{oname}-%{version}.tar.gz
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
%setup -q -n %{oname}-%{version}

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
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.4.0-alt1
- automated PyPI update

* Wed Dec 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt1
- Version 0.2.1

* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt1
- Initial build for Sisyphus

