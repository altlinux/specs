%define mname collective
%define oname %mname.tablepage
Name: python-module-%oname
Version: 0.10.2
Release: alt1.dev0.git20141127
Summary: A Plone page with an editable table as main content
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.tablepage/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/RedTurtle/collective.tablepage.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-pyquery
BuildPreReq: python-module-Products.ATContentTypes
BuildPreReq: python-module-collective.datagridcolumns
BuildPreReq: python-module-collective.autopermission
BuildPreReq: python-module-Products.ATReferenceBrowserWidget
BuildPreReq: python-module-Products.TinyMCE
BuildPreReq: python-module-Products.AdvancedQuery
BuildPreReq: python-module-Products.DataGridField
BuildPreReq: python-module-plone.app.testing

%py_provides %oname
%py_requires %mname Products.ATContentTypes collective.datagridcolumns
%py_requires collective.autopermission Products.ATReferenceBrowserWidget
%py_requires Products.TinyMCE Products.AdvancedQuery
%py_requires Products.DataGridField

%description
A new Plone content type similar to the standard Page but with a table
as main content.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing

%description tests
A new Plone content type similar to the standard Page but with a table
as main content.

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
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/test*

%files tests
%python_sitelibdir/%mname/*/test*

%changelog
* Fri Nov 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.2-alt1.dev0.git20141127
- Initial build for Sisyphus

