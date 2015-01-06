%define mname xmldirector
%define oname %mname.plonecore
Name: python-module-%oname
Version: 0.3.3.1
Release: alt1.git20150105
Summary: Technical foundation of the XML-Director project
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/xmldirector.plonecore/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/xml-director/xmldirector.plonecore.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-humanize python-module-requests
BuildPreReq: python-module-progressbar python-module-dateutil
BuildPreReq: python-module-fs python-module-dexml
BuildPreReq: python-module-grampg python-module-openid
BuildPreReq: python-module-plone.app.dexterity
BuildPreReq: python-module-plone.directives.form
BuildPreReq: python-module-hurry.filesize
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-plone.browserlayer
BuildPreReq: python-module-plone.api
BuildPreReq: python-module-zope.testing
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-plone.supermodel
BuildPreReq: python-module-plone.namedfile
BuildPreReq: python-module-plone.schemaeditor
BuildPreReq: python-module-plone.behavior
BuildPreReq: python-module-plone.dexterity
BuildPreReq: python-module-plone.registry
BuildPreReq: python-module-plone.indexer
BuildPreReq: python-module-plone.app.layout
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-zope.annotation
BuildPreReq: python-module-z3c.form
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-zope.configuration
BuildPreReq: python-module-sphinx-devel

%py_provides %oname
Requires: python-module-%mname = %EVR
Requires: python-module-Zope2
%py_requires plone.app.dexterity plone.directives.form hurry.filesize
%py_requires humanize zope.i18nmessageid plone.browserlayer plone.api
%py_requires requests progressbar dateutil fs dexml grampg zope.schema
%py_requires Products.CMFCore plone.supermodel plone.namedfile z3c.form
%py_requires plone.schemaeditor plone.behavior plone.dexterity
%py_requires plone.registry plone.indexer plone.app.layout
%py_requires zope.component zope.interface zope.publisher
%py_requires zope.annotation

%description
xmldirector.plonecore is the technical foundation of the XML-Director
project (www.xml-director.info). The goal of the XML-Director project is
building an enterprise-level XML content management system on top of the
CMS Plone (www.plone.org) with support for XML databases like eXis-db or
Base-X. However the underlaying implementation can also be used to mount
arbitrary backend through WebDAV into Plone.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.testing plone.app.testing zope.configuration

%description tests
xmldirector.plonecore is the technical foundation of the XML-Director
project (www.xml-director.info). The goal of the XML-Director project is
building an enterprise-level XML content management system on top of the
CMS Plone (www.plone.org) with support for XML databases like eXis-db or
Base-X. However the underlaying implementation can also be used to mount
arbitrary backend through WebDAV into Plone.

This package contains tests for %oname.

%package -n python-module-%mname
Summary: Core files of %mname
Group: Development/Python
%py_provides %mname

%description -n python-module-%mname
Core files of %mname.

%prep
%setup

%prepare_sphinx docs
ln -s ../objects.inv docs/source/

%build
%python_build_debug

%install
%python_install

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

install -p -m644 %mname/__init__.py \
	%buildroot%python_sitelibdir/%mname/

%make -C docs html

%check
python setup.py test

%files
%doc *.rst docs/build/html
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/tests
%exclude %python_sitelibdir/%mname/*/*/tests
%exclude %python_sitelibdir/%mname/__init__.py*

%files tests
%python_sitelibdir/%mname/*/tests
%python_sitelibdir/%mname/*/*/tests

%files -n python-module-%mname
%dir %python_sitelibdir/%mname
%python_sitelibdir/%mname/__init__.py*

%changelog
* Tue Jan 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.3.1-alt1.git20150105
- Version 0.3.3.1

* Tue Dec 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2-alt1.git20141230
- Initial build for Sisyphus

