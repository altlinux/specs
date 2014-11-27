%define mname collective.dms
%define oname %mname.batchimport
Name: python-module-%oname
Epoch: 1
Version: 1.2.2
Release: alt1.dev0.git20141127
Summary: Batch import of files into the Documents Management System
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.dms.batchimport/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.dms.batchimport.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-collective.dms.basecontent
BuildPreReq: python-module-collective.dms.mailcontent
BuildPreReq: python-module-collective.z3cform.datagridfield
BuildPreReq: python-module-five.grok python-module-openid
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-ecreall.helpers.testing

%py_provides %oname
%py_requires %mname collective.dms.basecontent five.grok
%py_requires collective.dms.mailcontent collective.z3cform.datagridfield

%description
Batch import of files into the Documents Management System.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing ecreall.helpers.testing

%description tests
Batch import of files into the Documents Management System.

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
%doc *.rst docs/*
%python_sitelibdir/collective/dms/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/collective/dms/*/test*

%files tests
%python_sitelibdir/collective/dms/*/test*

%changelog
* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.2.2-alt1.dev0.git20141127
- Version 1.2.2.dev0

* Sat Oct 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt1.dev0.git20141024
- Initial build for Sisyphus

