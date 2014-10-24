%define oname plone.app.discussion

Name: python-module-%oname
Version: 2.3.4
Release: alt1.dev0.git20141023
Summary: Enhanced discussion support for Plone
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.app.discussion/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.app.discussion.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-sphinx-devel
BuildPreReq: python-module-repoze.sphinx.autointerface
BuildPreReq: python-module-collective.monkeypatcher
BuildPreReq: python-module-plone.app.layout
BuildPreReq: python-module-plone.app.registry
BuildPreReq: python-module-plone.app.uuid
BuildPreReq: python-module-plone.app.z3cform
BuildPreReq: python-module-plone.indexer
BuildPreReq: python-module-plone.registry
BuildPreReq: python-module-plone.z3cform
BuildPreReq: python-module-zope.annotation
BuildPreReq: python-module-zope.event
BuildPreReq: python-module-zope.container
BuildPreReq: python-module-zope.lifecycleevent
BuildPreReq: python-module-zope.site
BuildPreReq: python-module-z3c.form
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-plone.stringinterp
BuildPreReq: python-module-plone.contentrules
BuildPreReq: python-module-plone.app.contentrules
BuildPreReq: python-module-plone.app.contenttypes-tests
BuildPreReq: python-module-plone.app.robotframework
BuildPreReq: python-module-Products.CMFPlone

%py_provides %oname
%py_requires plone.app collective.monkeypatcher plone.app.layout
%py_requires plone.app.registry plone.app.uuid plone.app.z3cform
%py_requires plone.indexer plone.registry ZODB3 zope.interface
%py_requires zope.component zope.annotation zope.event zope.container
%py_requires zope.lifecycleevent zope.site z3c.form
%py_requires Products.CMFPlone

%description
plone.app.discussion replaces the old commenting system in Plone 4.1 and
is also available as an add-on product for Plone 3 and 4. It was
initially developed as part of the Google Summer of Code 2009 by Timo
Stollenwerk (student) and Martin Aspeli (mentor).

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing plone.stringinterp plone.contentrules
%py_requires plone.app.contentrules plone.app.contenttypes.testing
%py_requires plone.app.robotframework

%description tests
plone.app.discussion replaces the old commenting system in Plone 4.1 and
is also available as an add-on product for Plone 3 and 4. It was
initially developed as part of the Google Summer of Code 2009 by Timo
Stollenwerk (student) and Martin Aspeli (mentor).

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
plone.app.discussion replaces the old commenting system in Plone 4.1 and
is also available as an add-on product for Plone 3 and 4. It was
initially developed as part of the Google Summer of Code 2009 by Timo
Stollenwerk (student) and Martin Aspeli (mentor).

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
plone.app.discussion replaces the old commenting system in Plone 4.1 and
is also available as an add-on product for Plone 3 and 4. It was
initially developed as part of the Google Summer of Code 2009 by Timo
Stollenwerk (student) and Martin Aspeli (mentor).

This package contains documentation for %oname.

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

export PYTHONPATH=$PWD
pushd docs
sphinx-build -b pickle -d build/doctrees source build/pickle
sphinx-build -b html -d build/doctrees source build/html
popd

install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test

%files
%doc *.rst docs/*.*
%dir %python_sitelibdir/%oname
%python_sitelibdir/plone/app/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/plone/app/*/test*

%files tests
%python_sitelibdir/plone/app/*/test*

%files pickles
%python_sitelibdir/%oname/pickle

%files docs
%doc docs/build/html/*

%changelog
* Fri Oct 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.4-alt1.dev0.git20141023
- Version 2.3.4.dev0

* Thu Oct 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.3-alt2.dev0.git20141009
- Added necessary requirements
- Enabled testing

* Wed Oct 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.3-alt1.dev0.git20141009
- Initial build for Sisyphus

