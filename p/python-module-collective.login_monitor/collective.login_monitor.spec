%define mname collective
%define oname %mname.login_monitor
Name: python-module-%oname
Version: 0.3.1
Release: alt1.dev0.git20141031
Summary: Store and monitor login access to your Plone site
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.login_monitor/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/RedTurtle/collective.login_monitor.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-z3c.saconfig python-module-SQLAlchemy
BuildPreReq: python-module-collective.js.jqueryui
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-zope.i18nmessageid

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname z3c.saconfig collective.js.jqueryui zope.component
%py_requires Products.CMFPlone Products.CMFCore zope.i18nmessageid
%py_requires zope.interface

%description
Save any login operation done in your Plone site to an external database
and provide a Plone interface for query the database.

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

%changelog
* Fri Oct 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.1-alt1.dev0.git20141031
- Initial build for Sisyphus

