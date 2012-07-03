%define oname repoze.what
Name: python-module-%oname
Version: 1.0.9
Release: alt1.git20110411.1.1
Summary: Authorization for Python/WSGI applications
License: BSD
Group: Development/Python
Url: https://github.com/repoze/repoze.what
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/repoze/repoze.what.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute
BuildPreReq: python-module-sphinx-devel python-module-repoze.who
BuildPreReq: python-module-PasteDeploy python-module-repoze.who-testutil

%py_provides repoze.what
%py_requires repoze repoze.who repoze.who-testutil paste

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
%exclude %python_sitelibdir/%oname/pickle

%files pickles
%python_sitelibdir/%oname/pickle

%files docs
%doc docs/build/html/*

%changelog
* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.9-alt1.git20110411.1.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.9-alt1.git20110411.1
- Added necessary requirements
- Excluded *.pth

* Wed Jun 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.9-alt1.git20110411
- Initial build for Sisyphus

