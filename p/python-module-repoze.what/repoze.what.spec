%define oname repoze.what

%def_with python3

Name: python-module-%oname
Version: 1.0.9
Release: alt3.git20110411.1
Summary: Authorization for Python/WSGI applications
License: BSD
Group: Development/Python
Url: https://github.com/repoze/repoze.what
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/repoze/repoze.what.git
Source: %name-%version.tar

#BuildPreReq: python-devel python-module-setuptools
#BuildPreReq: python-module-sphinx-devel python-module-repoze.who
#BuildPreReq: python-module-PasteDeploy python-module-repoze.who-testutil
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python-tools-2to3
%endif

%py_provides repoze.what
%py_requires repoze repoze.who repoze.who-testutil paste

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-PasteDeploy python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-paste python-module-pytz python-module-repoze python-module-repoze.who python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-module-zope python-module-zope.interface python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-modules-wsgiref python-tools-2to3 python3 python3-base python3-module-setuptools
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib python-module-objects.inv python-module-repoze.who-testutil python3-module-pytest rpm-build-python3 time

%description
`repoze.what` is an `authorization framework` for WSGI applications,
based on `repoze.who` (which deals with `authentication` and
`identification`).

On the one hand, it enables an authorization system based on the groups to 
which the `authenticated or anonymous` user belongs and the permissions 
granted to such groups by loading these groups and permissions into the 
request on the way in to the downstream WSGI application.

And on the other hand, it enables you to manage your groups and permissions
from the application itself or another program, under a backend-independent 
API. For example, it would be easy for you to switch from one back-end to 
another, and even use this framework to migrate the data.

This is just the authorization pattern it supports out-of-the-box, but you
can may it support other authorization patterns with your own
predicates. It's highly extensible, so it's very unlikely that it will get 
in your way -- Among other things, you can extend it to check for many 
conditions (such as checking that the user comes from a given country, based 
on her IP address, for example).

%package -n python3-module-%oname
Summary: Authorization for Python/WSGI applications
Group: Development/Python3
%py3_provides repoze.what
%py3_requires repoze repoze.who repoze.who-testutil paste

%description -n python3-module-%oname
`repoze.what` is an `authorization framework` for WSGI applications,
based on `repoze.who` (which deals with `authentication` and
`identification`).

On the one hand, it enables an authorization system based on the groups to 
which the `authenticated or anonymous` user belongs and the permissions 
granted to such groups by loading these groups and permissions into the 
request on the way in to the downstream WSGI application.

And on the other hand, it enables you to manage your groups and permissions

%package pickles
Summary: Pickles for repoze.what
Group: Development/Python

%description pickles
`repoze.what` is an `authorization framework` for WSGI applications,
based on `repoze.who` (which deals with `authentication` and
`identification`).

This package contains pickles for repoze.what.

%package docs
Summary: Documentation for repoze.what
Group: Development/Documentation
BuildArch: noarch

%description docs
`repoze.what` is an `authorization framework` for WSGI applications,
based on `repoze.who` (which deals with `authentication` and
`identification`).

This package contains documentation for repoze.what.

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
touch %buildroot%python_sitelibdir/repoze/what/__init__.py

%if_with python3
pushd ../python3
%python3_install
popd
%ifarch x86_64
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
touch %buildroot%python3_sitelibdir/repoze/what/__init__.py
%endif

install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/build/pickle %buildroot%python_sitelibdir/%oname/

%files
%doc README.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
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
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.0.9-alt3.git20110411.1
- NMU: Use buildreq for BR.

* Wed Jul 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.9-alt3.git20110411
- Added repoze/what/__init__.py

* Mon Jul 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.9-alt2.git20110411
- Added module for Python 3

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.9-alt1.git20110411.1.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.9-alt1.git20110411.1
- Added necessary requirements
- Excluded *.pth

* Wed Jun 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.9-alt1.git20110411
- Initial build for Sisyphus

