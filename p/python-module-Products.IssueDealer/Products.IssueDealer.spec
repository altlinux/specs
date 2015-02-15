%define oname Products.IssueDealer
Name: python-module-%oname
Version: 0.9.140
Release: alt1
Summary: The Issue Dealer is an application for managing information
License: GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.IssueDealer/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-docutils python-module-pytz
BuildPreReq: python-module-zope.structuredtext
BuildPreReq: python-module-Products.ZCatalog
BuildPreReq: python-module-Products.ZCTextIndex
BuildPreReq: python-module-Products.BTreeFolder2
BuildPreReq: python-module-zope.component-tests
BuildPreReq: python-module-zope.testing

%py_provides %oname
Requires: python-module-Zope2
%py_requires zope.structuredtext docutils pytz Products.ZCatalog
%py_requires Products.ZCTextIndex
%py_requires Products.BTreeFolder2

%description
The Issue Dealer is a tool for managing issues, currently
it focuses on the information in, and structuring of, issues.

It can be used as a generic issue tracker, a knowledge management
tool, a weblog or an outliner.

It also contains an experimental framework for creating content
classes through the web.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.component.testing zope.testing

%description tests
The Issue Dealer is a tool for managing issues, currently
it focuses on the information in, and structuring of, issues.

It can be used as a generic issue tracker, a knowledge management
tool, a weblog or an outliner.

It also contains an experimental framework for creating content
classes through the web.

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
%doc *.txt
%python_sitelibdir/Products/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/Products/*/*test*

%files tests
 %python_sitelibdir/Products/*/*test*

%changelog
* Sun Feb 15 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.140-alt1
- Initial build for Sisyphus

