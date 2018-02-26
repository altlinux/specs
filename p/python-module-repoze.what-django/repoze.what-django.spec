%define oname repoze.what-django
Name: python-module-%oname
Version: 1.0a1
Release: alt1.git20100310.1.1
Summary: Django plugin for repoze.what authorization framework
License: BSD
Group: Development/Python
Url: https://github.com/repoze/repoze.what-django
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/repoze/repoze.what-django.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute
BuildPreReq: python-module-sphinx-devel python-module-django

Requires: python-module-django
%py_requires repoze.what.plugins repoze.what twod.wsgi decorator

%description
This is an extras plugin for repoze.what which provides optional and
handy utilities for Django applications using this authorization
framework.

%package pickles
Summary: Pickles for repoze.what-django
Group: Development/Python

%description pickles
This is an extras plugin for repoze.what which provides optional and
handy utilities for Django applications using this authorization
framework.

This package contains pickles for repoze.what-django.

%package docs
Summary: Documentation for repoze.what-django
Group: Development/Documentation
BuildArch: noarch

%description docs
This is an extras plugin for repoze.what which provides optional and
handy utilities for Django applications using this authorization
framework.

This package contains documentation for repoze.what-django.

%prep
%setup

%prepare_sphinx docs
ln -s ../objects.inv docs/source/

%build
%python_build

export PYTHONPATH=$PWD
pushd docs
%make pickle
%make html
popd

%install
%python_install

%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/build/pickle %buildroot%python_sitelibdir/%oname/

%files
%doc README.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/tests
%exclude %python_sitelibdir/%oname/pickle

%files pickles
%python_sitelibdir/%oname/pickle

%files docs
%doc docs/build/html/*

%changelog
* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0a1-alt1.git20100310.1.1
- Rebuild with Python-2.7

* Thu Jun 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0a1-alt1.git20100310.1
- Added necessary requirements
- Excluded *.pth

* Fri Jun 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0a1-alt1.git20100310
- Initial build for Sisyphus

