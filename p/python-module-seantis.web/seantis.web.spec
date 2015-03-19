%define mname seantis
%define oname %mname.web
Name: python-module-%oname
Version: 1.2
Release: alt1.git20150319
Summary: The seantis website
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/seantis.web/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/seantis/seantis.web.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-robotsuite
BuildPreReq: python-module-plone.app.theming
BuildPreReq: python-module-plone.app.themingplugins
BuildPreReq: python-module-Products.ContentWellPortlets
BuildPreReq: python-module-collective.portlet.embed
BuildPreReq: python-module-plone.app.testing

%py_provides %oname
Requires: python-module-%mname = %EVR
%py_requires plone.app.theming plone.app.themingplugins
%py_requires Products.ContentWellPortlets collective.portlet.embed

%description
Foundation-based Plone theme for the seantis website.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing robotsuite

%description tests
Foundation-based Plone theme for the seantis website.

This package contains tests for %oname.

%package -n python-module-%mname
Summary: Core files of %mname
Group: Development/Python
%py_provides %mname

%description -n python-module-%mname
Core files of %mname.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

install -p -m644 %mname/__init__.py \
	%buildroot%python_sitelibdir/%mname/

%check
python setup.py test

%files
%doc *.rst
%python_sitelibdir/%mname/web
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/web/test*

%files tests
%python_sitelibdir/%mname/web/test*

%files -n python-module-%mname
%dir %python_sitelibdir/%mname
%python_sitelibdir/%mname/__init__.py*

%changelog
* Thu Mar 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1.git20150319
- Initial build for Sisyphus

