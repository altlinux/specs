%define mname collective
%define oname %mname.cachepurger
Name: python-module-%oname
Version: 1.2
Release: alt1.dev0.git20141027
Summary: Purges RAM caches and refreshes resource registry
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.cachepurger/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/headnet/collective.cachepurger.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-Products.CMFCore

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname Products.CMFCore

%description
Cachepurger scraches a small itch. We've experienced that when we deploy
a new version of a Plone package, it does not behave as expected even
though it did at the test server. One reason is that the resource
registries or caches contains old data.

Cachepurge simply empties the different Zope RAM caches and rebuilds CSS
and Javascript from the registries.

Just call http://mysite/@@purge-caches

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
* Tue Oct 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1.dev0.git20141027
- Initial build for Sisyphus

