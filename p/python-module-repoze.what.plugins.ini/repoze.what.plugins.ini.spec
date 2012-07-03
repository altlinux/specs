%define oname repoze.what.plugins.ini
Name: python-module-%oname
Version: 0.2.5
Release: alt1.git20111210
Summary: repoze.what pluggin with sources based on INI files
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/repoze.what.plugins.ini/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# git://github.com/jdinuncio/repoze.what.plugins.ini.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires repoze.what.plugins repoze.what pyparsing

%description
repoze.what is an authorization framework for WSGI applications, based
on repoze.who (which deals with authentication).

On the one hand, it enables an authorization system based on the groups
to which the authenticated or anonymous user belongs and the permissions
granted to such groups by loading these groups and permissions into the
request on the way in to the downstream WSGI application.

And on the other hand, it enables you to manage your groups and
permissions from the application itself or another program, under a
backend-independent API. For example, it would be easy for you to switch
from one back-end to another, and even use this framework to migrate the
data.

%prep
%setup

%build
%python_build

%install
%python_install

%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/tests

%changelog
* Tue Dec 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.5-alt1.git20111210
- Version 0.2.5

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2.2-alt1.1
- Rebuild with Python-2.7

* Fri Jul 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.2-alt1
- Initial build for Sisyphus

