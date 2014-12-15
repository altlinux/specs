%define mname munin
%define oname %mname.zope
Name: python-module-%oname
Version: 2.2
Release: alt2.dev0.git20140917
Summary: Munin plugins for Zope/Plone
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/munin.zope/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/RedTurtle/munin.zope.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-gocept.munin
BuildPreReq: python-module-Products.ZServerViews
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-zope.configuration

%py_provides %oname
Requires: python-module-%mname = %EVR
Requires: python-module-Zope2
%py_requires gocept.munin Products.ZServerViews

%description
This package provides munin plugins for monitoring various aspects of a
Zope instance.

It uses gocept.munin for plugin registration. Please refer to its
documentation if you want to write new plugins.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing zope.configuration

%description tests
This package provides munin plugins for monitoring various aspects of a
Zope instance.

It uses gocept.munin for plugin registration. Please refer to its
documentation if you want to write new plugins.

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

install -p -m644 src/%mname/__init__.py \
	%buildroot%python_sitelibdir/%mname/
install -p -m644 src/%mname/zope/*.txt \
	%buildroot%python_sitelibdir/%mname/zope/
mv %buildroot%_bindir/%mname %buildroot%_bindir/%mname.zope

%check
python setup.py test
py.test src/munin/zope/tests.py

%files
%doc *.txt *.rst docs/*
%_bindir/*
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/tests*
%exclude %python_sitelibdir/%mname/__init__.py*

%files tests
%python_sitelibdir/%mname/*/tests*

%files -n python-module-%mname
%dir %python_sitelibdir/%mname
%python_sitelibdir/%mname/__init__.py*

%changelog
* Mon Dec 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2-alt2.dev0.git20140917
- Renamed %_bindir/%mname -> %_bindir/%mname.zope

* Mon Dec 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2-alt1.dev0.git20140917
- Initial build for Sisyphus

