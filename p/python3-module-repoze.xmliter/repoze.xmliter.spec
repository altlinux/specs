%define oname repoze.xmliter

Name: python3-module-%oname
Version: 0.6.1
Release: alt1

Summary: Wrapper for lxml trees which serializes to string upon iteration

License: BSD
Group: Development/Python3
Url: https://github.com/repoze/repoze.xmliter

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildRequires(pre): rpm-build-intro >= 2.2.5
BuildRequires(pre): rpm-build-python3

BuildPreReq: python3-devel python3-module-setuptools python3-tools

%py3_requires repoze lxml


%description
This package provides a wrapper for ``lxml`` trees which serializes to
string on iteration, but otherwise makes the tree available in an
attribute.

The primary for this is WSGI middleware which may avoid
needless XML parsing and serialization.


%prep
%setup
find . -type f -name '*.py' -exec python3-2to3 -w -n '{}' +

%build
%python3_build

%install
%python3_install
%python3_prune
%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
rm -fv %buildroot%python3_sitelibdir/*.pth
rm -fv %buildroot%python3_sitelibdir/repoze/xmliter/tests.py

%files
%doc *.txt
%python3_sitelibdir/*

%changelog
* Tue Apr 05 2022 Vitaly Lipatov <lav@altlinux.ru> 0.6.1-alt1
- new version 0.6.1 (with rpmrb script)

* Sun Jul 11 2021 Vitaly Lipatov <lav@altlinux.ru> 0.6-alt2.git20140921
- build python3 module separately

* Tue Apr 30 2019 Grigory Ustinov <grenka@altlinux.org> 0.6-alt1.git20140921.2
- Rebuild with python3.7.

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.6-alt1.git20140921.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.6-alt1.git20140921.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Oct 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6-alt1.git20140921
- Version 0.6

* Wed Jul 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt2.git20120125
- Added module for Python 3

* Thu Apr 04 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt1.git20120125
- Version 0.5

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3-alt1.git20110603.1.1
- Rebuild with Python-2.7

* Thu Jun 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1.git20110603.1
- Added necessary requirements
- Excluded *.pth

* Wed Jun 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1.git20110603
- Initial build for Sisyphus

