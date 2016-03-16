%define oname repoze.what.plugins.ini

%def_with python3

Name: python-module-%oname
Version: 0.2.5
Release: alt2.git20111210.1
Summary: repoze.what pluggin with sources based on INI files
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/repoze.what.plugins.ini/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# git://github.com/jdinuncio/repoze.what.plugins.ini.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

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

%package -n python3-module-%oname
Summary: repoze.what pluggin with sources based on INI files
Group: Development/Python3
%py3_requires repoze.what.plugins repoze.what pyparsing

%description -n python3-module-%oname
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

%if_with python3
cp -fR . ../python3
%endif

%build
export LC_ALL=en_US.UTF-8

%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
export LC_ALL=en_US.UTF-8

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

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/tests

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/tests
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.5-alt2.git20111210.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jul 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.5-alt2.git20111210
- Added module for Python 3

* Tue Dec 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.5-alt1.git20111210
- Version 0.2.5

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2.2-alt1.1
- Rebuild with Python-2.7

* Fri Jul 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.2-alt1
- Initial build for Sisyphus

