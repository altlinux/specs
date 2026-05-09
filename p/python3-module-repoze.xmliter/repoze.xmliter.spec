%define oname repoze.xmliter

%def_with check

Name: python3-module-%oname
Version: 2.0
Release: alt1

Summary: Wrapper for lxml trees which serializes to string upon iteration

License: BSD
Group: Development/Python3
Url: https://pypi.org/project/repoze.xmliter
Vcs: https://github.com/repoze/repoze.xmliter

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
%if_with check
BuildRequires: python3-module-lxml
%endif

%py3_requires repoze lxml


%description
This package provides a wrapper for ``lxml`` trees which serializes to
string on iteration, but otherwise makes the tree available in an
attribute.

The primary for this is WSGI middleware which may avoid
needless XML parsing and serialization.


%prep
%setup

%build
%pyproject_build

%install
%pyproject_install
%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
rm -fv %buildroot%python3_sitelibdir/*.pth
rm -fv %buildroot%python3_sitelibdir/repoze/xmliter/tests.py

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
python3 -m unittest src/repoze/xmliter/tests.py

%files
%doc *.txt
%python3_sitelibdir/*

%changelog
* Sat May 09 2026 Anton Vyatkin <toni@altlinux.org> 2.0-alt1
- new version 2.0

* Fri Oct 31 2025 Anton Vyatkin <toni@altlinux.org> 1.0-alt1
- new version 1.0

* Tue May 02 2023 Anton Vyatkin <toni@altlinux.org> 0.6.1-alt2
- Fix BuildRequires (build with check)

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

