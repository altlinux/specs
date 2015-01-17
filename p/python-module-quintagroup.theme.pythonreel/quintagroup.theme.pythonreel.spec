%define mname quintagroup
%define oname %mname.theme.pythonreel
Name: python-module-%oname
Version: 1.5
Release: alt1.git20141229
Summary: Free Diazo theme for Plone
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/quintagroup.theme.pythonreel/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/quintagroup/quintagroup.theme.pythonreel.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-initgroups
BuildPreReq: python-module-unittest2
BuildPreReq: python-module-plone.app.theming
BuildPreReq: python-module-plone.app.themingplugins

%py_provides %oname
%py_requires %mname.theme plone.app.theming plone.app.themingplugins

%description
Python Reel Theme is a free fully responsive diazo theme for Plone.

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
%doc *.rst docs/*.rst
%python_sitelibdir/%mname/theme/*
%python_sitelibdir/*.egg-info

%changelog
* Sat Jan 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5-alt1.git20141229
- Initial build for Sisyphus

