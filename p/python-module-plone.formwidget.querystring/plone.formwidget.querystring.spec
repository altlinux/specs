%define mname plone.formwidget
%define oname %mname.querystring
Name: python-module-%oname
Version: 1.1.4
Release: alt1.dev0.git20141101
Summary: A widget for composing a Query string/search
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.formwidget.querystring/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.formwidget.querystring.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-zLOG
BuildPreReq: python-module-initgroups python-module-unittest2
BuildPreReq: python-module-argparse
BuildPreReq: python-module-plone.app.querystring
BuildPreReq: python-module-plone.registry
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.interface
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.browserpage
BuildPreReq: python-module-zope.component
BuildPreReq: python-module-zope.site
BuildPreReq: python-module-z3c.form

%py_provides %oname
%py_requires %mname plone.app.querystring plone.registry zope.interface
%py_requires zope.i18nmessageid zope.schema zope.browserpage zope.site
%py_requires zope.component z3c.form

%description
A z3c.form-based widget for composing a Query string/search.

This widget is used by the contentlisting tile and the dexterity-based
version of plone.app.collection (>2.0), to make selections, and 'build'
your query. It stores a list of dictionaries containing the query you've
build. This query is being parsed by using plone.app.collection and that
used plone.app.contentlisting to display the results in the tile.

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
%python_sitelibdir/plone/formwidget/*
%python_sitelibdir/*.egg-info

%changelog
* Tue Nov 04 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.4-alt1.dev0.git20141101
- Initial build for Sisyphus

