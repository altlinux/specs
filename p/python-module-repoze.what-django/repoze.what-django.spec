%define oname repoze.what-django

%def_with python3

Name: python-module-%oname
Version: 1.0a1
Release: alt2.git20100310.1.1
Summary: Django plugin for repoze.what authorization framework
License: BSD
Group: Development/Python
Url: https://github.com/repoze/repoze.what-django
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/repoze/repoze.what-django.git
Source: %name-%version.tar

#BuildPreReq: python-devel python-module-setuptools
#BuildPreReq: python-module-sphinx-devel python-module-django
#BuildPreReq: python-module-repoze.what
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
#BuildPreReq: python-tools-2to3
%endif

Requires: python-module-django
%py_requires repoze.what.plugins repoze.what twod.wsgi decorator

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-PasteDeploy python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-paste python-module-psycopg2 python-module-pytz python-module-repoze python-module-repoze.who python-module-repoze.who-testutil python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-module-yaml python-module-zope.interface python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-modules-wsgiref python-tools-2to3 python3 python3-base
BuildRequires: python-module-alabaster python-module-django python-module-docutils python-module-html5lib python-module-objects.inv python-module-repoze.what python3-module-setuptools rpm-build-python3 time

%description
This is an extras plugin for repoze.what which provides optional and
handy utilities for Django applications using this authorization
framework.

%package -n python3-module-%oname
Summary: Django plugin for repoze.what authorization framework
Group: Development/Python3
Requires: python3-module-django
%py3_requires repoze.what.plugins repoze.what twod.wsgi decorator

%description -n python3-module-%oname
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

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%prepare_sphinx docs
ln -s ../objects.inv docs/source/

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

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

%if_with python3
pushd ../python3
%python3_install
popd
%ifarch x86_64
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
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

%if_with python3
%files -n python3-module-%oname
%doc README.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/tests
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0a1-alt2.git20100310.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.0a1-alt2.git20100310.1
- NMU: Use buildreq for BR.

* Wed Jul 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0a1-alt2.git20100310
- Added module for Python 3

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0a1-alt1.git20100310.1.1
- Rebuild with Python-2.7

* Thu Jun 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0a1-alt1.git20100310.1
- Added necessary requirements
- Excluded *.pth

* Fri Jun 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0a1-alt1.git20100310
- Initial build for Sisyphus

