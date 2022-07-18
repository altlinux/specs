%define oname repoze.who

Name:           python3-module-%oname
Version:        2.4.1
Release:        alt1

Summary:        Identification and authentication framework for WSGI

Group:          Development/Python3
License:        BSD-derived
URL:            http://pypi.python.org/pypi/repoze.who/

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildRequires(pre): rpm-build-intro >= 2.2.5
BuildRequires(pre): rpm-build-python3

BuildRequires: python3-module-paste python3-module-setuptools python3-module-zope

%python3_req_hier
%py3_requires paste zope.interface
Requires: python3-module-repoze = %EVR

%description
repoze.who is an identification and authentication framework for
arbitrary WSGI applications. It acts as WSGI middleware.

repoze.who is inspired by Zope 2's Pluggable Authentication Service
(PAS) (but repoze.who is not dependent on Zope in any way; it is useful
for any WSGI application). It provides no facility for authorization
(ensuring whether a user can or cannot perform the operation implied by
the request). This is considered to be the domain of the WSGI
application.

%package -n python3-module-repoze
Summary: Root files for repoze (Python 3)
Group: Development/Python3

%description -n python3-module-repoze
Root files for repoze.

%package tests
Summary: Tests for repoze.who
Group: Development/Python
Requires: %name = %version-%release

%description tests
repoze.who is an identification and authentication framework for
arbitrary WSGI applications. It acts as WSGI middleware.

repoze.who is inspired by Zope 2's Pluggable Authentication Service
(PAS) (but repoze.who is not dependent on Zope in any way; it is useful
for any WSGI application). It provides no facility for authorization
(ensuring whether a user can or cannot perform the operation implied by
the request). This is considered to be the domain of the WSGI
application.

This package contains tests for repoze.who.


%prep
%setup

#prepare_sphinx docs

%build
%python3_build

%install
%python3_install
rm -f %buildroot%python3_sitelibdir/*.pth


%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif

install -p -m644 repoze/__init__.py %buildroot%python3_sitelibdir/repoze
for i in $(find %buildroot%python3_sitelibdir/repoze -type d \! -name '__*')
do
	touch $i/__init__.py
done

%files
%doc *.txt
%python3_sitelibdir/%oname-*
%python3_sitelibdir/repoze/*
%exclude %python3_sitelibdir/repoze/__init__.py*
%exclude %python3_sitelibdir/repoze/__pycache__/__init__.*.py*
%exclude %python3_sitelibdir/repoze/who/tests
%exclude %python3_sitelibdir/repoze/who/plugins/tests

%files -n python3-module-repoze
%dir %python3_sitelibdir/repoze
%python3_sitelibdir/repoze/__init__.py*
%dir %python3_sitelibdir/repoze/__pycache__
%python3_sitelibdir/repoze/__pycache__/__init__.*.py*

%files -n python3-module-%oname-tests
%python3_sitelibdir/repoze/who/tests
%python3_sitelibdir/repoze/who/plugins/tests


%changelog
* Mon Jul 18 2022 Vitaly Lipatov <lav@altlinux.ru> 2.4.1-alt1
- new version 2.4.1 (with rpmrb script)

* Sun Jul 11 2021 Vitaly Lipatov <lav@altlinux.ru> 2.4-alt1
- new version

* Sun Jul 11 2021 Vitaly Lipatov <lav@altlinux.ru> 2.2-alt5.git20140327
- build python3 module separately

* Tue Apr 30 2019 Grigory Ustinov <grenka@altlinux.org> 2.2-alt4.git20140327
- Rebuild with python3.7.

* Mon Oct 31 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.2-alt3.git20140327
- %%python3_req_hier for more precise reqs.

* Tue Jun 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.2-alt2.git20140327
- (.spec) Python3 packaging fixes:
  package corresponding __pycache__/* & sources together.
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.2-alt1.git20140327.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.2-alt1.git20140327.1
- NMU: Use buildreq for BR.

* Tue Jul 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2-alt1.git20140327
- New snapshot

* Mon Dec 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2-alt1.git20131113
- Version 2.2

* Mon Apr 15 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1-alt2.b1
- Use 'find... -exec...' instead of 'for ... $(find...'

* Sun Mar 03 2013 Aleksey Avdeev <solo@altlinux.ru> 2.1-alt1.b1
- Version 2.1b1

* Sat May 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt3
- Added module for Python 3

* Tue Dec 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt2
- Version 2.0

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.0-alt1.b1.3.1
- Rebuild with Python-2.7

* Thu Jun 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt1.b1.3
- Excluded *.pth

* Sun Jun 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt1.b1.2
- Added necessary runtime requirements

* Sat May 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt1.b1.1
- Set as archdep package

* Sat May 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt1.b1
- Version 2.0b1

* Tue May 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt1.a4
- Version 2.0a4

* Tue Apr 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt1.a3.1
- Rebuilt with python-module-sphinx-devel

* Tue Nov 23 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt1.a3
- Version 2.0a3

* Thu Jul 15 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.18-alt1
- Initial build for Sisyphus

