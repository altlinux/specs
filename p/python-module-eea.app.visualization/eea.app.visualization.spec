%define mname eea
%define oname %mname.app.visualization
Name: python-module-%oname
Version: 9.1
Release: alt1.dev.git20141212
Summary: The core API for Data Visualization in Plone
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/eea.app.visualization/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/eea/eea.app.visualization.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-dateutil
BuildPreReq: python-module-plone.i18n
BuildPreReq: python-module-z3c.autoinclude
BuildPreReq: python-module-eea.jquery
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-Products.EEAContentTypes
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.ResourceRegistries
BuildPreReq: python-module-Products.statusmessages
BuildPreReq: python-module-Products.ATContentTypes
BuildPreReq: python-module-plone.app.blob
BuildPreReq: python-module-plone.app.form
BuildPreReq: python-module-zope.formlib
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.lifecycleevent
BuildPreReq: python-module-zope.event
BuildPreReq: python-module-zope.security
BuildPreReq: python-module-zope.annotation
BuildPreReq: python-module-zope.app.pagetemplate
BuildPreReq: python-module-zope.browserpage
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.configuration

%py_provides %oname
Requires: python-module-%mname.app = %EVR
Requires: python-module-Zope2
%py_requires plone.i18n z3c.autoinclude eea.jquery Products.CMFCore
%py_requires Products.EEAContentTypes Products.ResourceRegistries
%py_requires Products.statusmessages Products.ATContentTypes zope.schema
%py_requires plone.app.blob plone.app.form zope.component zope.formlib
%py_requires zope.publisher zope.interface zope.lifecycleevent
%py_requires zope.event zope.security zope.annotation zope.browserpage
%py_requires zope.app.pagetemplate zope.i18nmessageid

%description
EEA App Visualization is the Core API for EEA Daviz. This package was
added in order to be able to use EEA Google Charts without EEA Exhibit
and viceversa or any other visualization library as a standalone
visualization or as part of a bundle package (eea.daviz).

This package as standalone is just an API, you have to either install
eea.daviz bundle, either install one of the available visualization
libraries (eea.exhibit, eea.googlecharts, etc) in order to have a
working Visualization Tool for your files.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing zope.configuration

%description tests
EEA App Visualization is the Core API for EEA Daviz. This package was
added in order to be able to use EEA Google Charts without EEA Exhibit
and viceversa or any other visualization library as a standalone
visualization or as part of a bundle package (eea.daviz).

This package as standalone is just an API, you have to either install
eea.daviz bundle, either install one of the available visualization
libraries (eea.exhibit, eea.googlecharts, etc) in order to have a
working Visualization Tool for your files.

This package contains tests for %oname.

%package -n python-module-%mname.app
Summary: Core files of %mname.app
Group: Development/Python
%py_provides %mname.app
%py_requires %mname

%description -n python-module-%mname.app
Core files of %mname.app.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

install -p -m644 %mname/app/__init__.py \
	%buildroot%python_sitelibdir/%mname/app/
pushd %mname/app/visualization
cp -fR *.txt *.zcml docs documentation locales profiles \
	%buildroot%python_sitelibdir/%mname/app/visualization/
cp -fR tests/data \
	%buildroot%python_sitelibdir/%mname/app/visualization/tests/
pushd browser
cp -fR *.zcml css img js zpt \
	%buildroot%python_sitelibdir/%mname/app/visualization/browser/
popd
pushd views/data
install -p -m644 *.zcml *.png *.pt \
	%buildroot%python_sitelibdir/%mname/app/visualization/views/data/
popd
install -p -m644 controlpanel/*.zcml controlpanel/*.pt \
	%buildroot%python_sitelibdir/%mname/app/visualization/controlpanel/
install -p -m644 zopera/*.zcml zopera/*.pt \
	%buildroot%python_sitelibdir/%mname/app/visualization/zopera/
for i in browser/res cache converter converter/types data facets \
	facets/list storage subtypes upgrades views
do
	install -p -m644 $i/*.zcml \
		%buildroot%python_sitelibdir/%mname/app/visualization/$i/
done
popd

%check
python setup.py test

%files
%doc *.md *.txt docs/*
%python_sitelibdir/%mname/app/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/app/*/tests
%exclude %python_sitelibdir/%mname/app/__init__.py*

%files tests
%python_sitelibdir/%mname/app/*/tests

%files -n python-module-%mname.app
%dir %python_sitelibdir/%mname/app
%python_sitelibdir/%mname/app/__init__.py*

%changelog
* Wed Dec 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 9.1-alt1.dev.git20141212
- Initial build for Sisyphus

