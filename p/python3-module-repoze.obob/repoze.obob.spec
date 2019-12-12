%define oname repoze.obob

Name: python3-module-%oname
Version: 0.4
Release: alt4

Summary: Zope-like publisher as WSGI application
License: BSD
Group: Development/Python3
Url: http://pypi.python.org/pypi/repoze.obob/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3

%py3_requires repoze paste.script WSGIUtils


%description
repoze.obob is a reconstruction of the "bobo" precursor of Zope (the
"object publisher" portion), stripped down to be used as a possible
application endpoint in the 'repoze' stack.

%package tests
Summary: Tests for repoze.obob
Group: Development/Python3
Requires: %name = %version-%release

%description tests
repoze.obob is a reconstruction of the "bobo" precursor of Zope (the
"object publisher" portion), stripped down to be used as a possible
application endpoint in the 'repoze' stack.

This package contains tests for repoze.obob.

%prep
%setup

cp -fR . ../python3
find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build

%install
%python3_install

%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
    %buildroot%python3_sitelibdir/
%endif

%files
%doc *.txt doc/*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests
%exclude %python3_sitelibdir/*/*/*/*/*/tests*

%files tests
%python3_sitelibdir/*/*/tests
%python3_sitelibdir/*/*/*/*/*/tests*


%changelog
* Thu Dec 12 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.4-alt4
- build for python2 disabled

* Tue Apr 30 2019 Grigory Ustinov <grenka@altlinux.org> 0.4-alt3.2
- Rebuild with python3.7.

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4-alt3.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jul 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4-alt2.1
- Rebuild with Python-2.7

* Thu Jun 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt2
- Added necessary requirements
- Excluded *.pth

* Thu Jun 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1
- Initial build for Sisyphus

