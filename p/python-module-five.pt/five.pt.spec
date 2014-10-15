%define oname five.pt
Name: python-module-%oname
Version: 2.2.2
Release: alt1.git20140415
Summary: Five bridges and patches to use Chameleon with Zope 2
License: ZPL
Group: Development/Python
Url: https://pypi.python.org/pypi/five.pt/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/zopefoundation/five.pt.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-sourcecodegen
BuildPreReq: python-module-z3c.pt
BuildPreReq: python-module-zope.pagetemplate

%py_provides %oname
%py_requires five z3c.pt zope.pagetemplate

%description
This package brings the Chameleon template engine to the Zope
application server.

It works using monkey-patching onto the existing API (specifically, the
TALInterpreter and PageTemplate classes). In simple terms, what the
patching does is to replace the TAL interpreter class and make sure that
the so-called "cooking" routine uses the Chameleon parser and compiler
instead of the zope.* reference implementation.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This package brings the Chameleon template engine to the Zope
application server.

It works using monkey-patching onto the existing API (specifically, the
TALInterpreter and PageTemplate classes). In simple terms, what the
patching does is to replace the TAL interpreter class and make sure that
the so-called "cooking" routine uses the Chameleon parser and compiler
instead of the zope.* reference implementation.

This package contains tests for %oname.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
python setup.py test

%files
%doc *.rst
%python_sitelibdir/five/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/five/*/tests

%files tests
%python_sitelibdir/five/*/tests

%changelog
* Wed Oct 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.2-alt1.git20140415
- Initial build for Sisyphus

