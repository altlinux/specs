%define mname souper
%define oname %mname.plone
Name: python-module-%oname
Version: 1.2
Release: alt1.git20140427
Summary: Plone Souper Integration: Container for many lightweight queryable Records
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/souper.plone/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/bluedynamics/souper.plone.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-openid
BuildPreReq: python-module-%mname python-module-interlude
BuildPreReq: python-module-Plone
BuildPreReq: python-module-zopyx.txng3.core
BuildPreReq: python-module-zope.annotation
BuildPreReq: python-module-plone.app.testing

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname Plone zope.component zope.interface zope.annotation

%description
souper.plone helps developers who need to store many small data records,
where heavy-weight Archetypes or Dexterity content types are too much
effort and are too slow. E.g. if you need a queryable container for
non-CMSish content, like votes, data from a poll, orders in a webshop,
measuring data, or the like.

A Soup-container can be moved to an own ZODB mount-point and may be
shared across multiple independent Plone instances!

A control-panel provides actions to rebuild, reindex and move Soups
around.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires zopyx.txng3.core plone.app.testing

%description tests
souper.plone helps developers who need to store many small data records,
where heavy-weight Archetypes or Dexterity content types are too much
effort and are too slow. E.g. if you need a queryable container for
non-CMSish content, like votes, data from a poll, orders in a webshop,
measuring data, or the like.

A Soup-container can be moved to an own ZODB mount-point and may be
shared across multiple independent Plone instances!

A control-panel provides actions to rebuild, reindex and move Soups
around.

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
%doc *.rst
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/test*

%files tests
%python_sitelibdir/%mname/*/test*

%changelog
* Fri Dec 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1.git20140427
- Initial build for Sisyphus

