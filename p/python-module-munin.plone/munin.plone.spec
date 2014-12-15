%define mname munin
%define oname %mname.plone
Name: python-module-%oname
Version: 1.2.1
Release: alt1.git20130308
Summary: Munin plugins for Plone
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/munin.plone/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/munin.plone.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2
BuildPreReq: python-module-gocept.munin

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname gocept.munin

%description
This package provides munin plugins for monitoring various aspects of a
Plone instance.

It uses gocept.munin for plugin registration. Please refer to its
documentation if you want to write new plugins.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

install -p -m644 src/munin/plone/*.zcml \
	%buildroot%python_sitelibdir/munin/plone/
mv %buildroot%_bindir/%mname %buildroot%_bindir/%mname.plone

%check
python setup.py test

%files
%doc *.txt docs/*
%_bindir/*
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info

%changelog
* Mon Dec 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.1-alt1.git20130308
- Initial build for Sisyphus

