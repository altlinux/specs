%define oname martian
Name: python-module-%oname
Version: 0.14
Release: alt2.1
Summary: A library to grok configuration from Python code
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/martian/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-distribute

%py_requires zope.interface

%description
Martian is a library that allows the embedding of configuration
information in Python code. Martian can then grok the system and do the
appropriate configuration registrations. One example of a system that
uses Martian is the system where it originated: Grok
(http://grok.zope.org)

%package tests
Summary: Tests for martian
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing

%description tests
Martian is a library that allows the embedding of configuration
information in Python code. Martian can then grok the system and do the
appropriate configuration registrations. One example of a system that
uses Martian is the system where it originated: Grok
(http://grok.zope.org)

This package contains tests for martian.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test*

%files tests
%python_sitelibdir/*/test*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.14-alt2.1
- Rebuild with Python-2.7

* Thu Jun 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.14-alt2
- Added necessary requirements

* Tue May 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.14-alt1
- Initial build for Sisyphus

