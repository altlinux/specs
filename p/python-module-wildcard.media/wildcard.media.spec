%define mname wildcard
%define oname %mname.media
Name: python-module-%oname
Version: 1.2
Release: alt1.b5.git20141007
Summary: HTML5 audio and video integration with plone
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/wildcard.media/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/wildcard.media.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-plone.transformchain
BuildPreReq: python-module-plone.app.dexterity
BuildPreReq: python-module-plone.autoform
BuildPreReq: python-module-plone.app.textfield
BuildPreReq: python-module-plone.app.blob
BuildPreReq: python-module-plone.rfc822
BuildPreReq: python-module-plone.supermodel
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-collective.cover
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-zope.cachedescriptors
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.annotation
BuildPreReq: python-module-zope.app.component
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zc.async
BuildPreReq: python-module-z3c.form
BuildPreReq: python-module-zope.configuration

%py_provides %oname
Requires: python-module-%mname = %EVR
Requires: python-module-Zope2
%py_requires plone.transformchain plone.app.dexterity plone.autoform
%py_requires plone.app.textfield plone.app.blob plone.rfc822 zope.schema
%py_requires plone.supermodel collective.cover Products.CMFCore zc.async
%py_requires Products.CMFPlone zope.cachedescriptors zope.component
%py_requires zope.interface zope.annotation zope.app.component z3c.form
%py_requires zope.publisher zope.i18nmessageid

%description
This package provides Audio and Video Dexterity content types and
behaviors, conversions and players/views.

It integrates the HTML5 media player mediaelementjs and uses Async if
installed to convert videos to common formats.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing zope.configuration

%description tests
This package provides Audio and Video Dexterity content types and
behaviors, conversions and players/views.

It integrates the HTML5 media player mediaelementjs and uses Async if
installed to convert videos to common formats.

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
pushd %mname/media
cp -fR *.zcml Extensions locales profiles static templates \
	%buildroot%python_sitelibdir/%mname/media/
cp schema/*.xml %buildroot%python_sitelibdir/%mname/media/schema/
cp -fR tests/files %buildroot%python_sitelibdir/%mname/media/tests/
cp -fR tiles/*.zcml tiles/templates \
	%buildroot%python_sitelibdir/%mname/media/tiles/
popd

%check
python setup.py test

%files
%doc *.txt docs/*
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/test*
%exclude %python_sitelibdir/%mname/__init__.py*

%files tests
%python_sitelibdir/%mname/*/test*

%files -n python-module-%mname
%dir %python_sitelibdir/%mname
%python_sitelibdir/%mname/__init__.py*

%changelog
* Fri Dec 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1.b5.git20141007
- Initial build for Sisyphus

