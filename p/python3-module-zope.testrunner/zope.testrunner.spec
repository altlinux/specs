%define _unpackaged_files_terminate_build 1
%define oname zope.testrunner

%def_with check

Name: python3-module-%oname
Version: 5.4.0
Release: alt1

Summary: Zope testrunner script

License: ZPL-2.1
Group: Development/Python3
# Source-git: https://github.com/zopefoundation/zope.testrunner.git
Url: https://pypi.org/project/zope.testrunner/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%if_with check
# install_requires=
BuildRequires: python3(six)
BuildRequires: python3(setuptools)
BuildRequires: python3(zope.exceptions)
BuildRequires: python3(zope.interface)

BuildRequires: python3(zope.testing)

BuildRequires: python3(tox)
%endif

Conflicts: python-module-%oname

%py3_requires zope

%description
This package provides a flexible test runner with layer support.

%prep
%setup

%build
%python3_build

%install
%python3_install

%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
install -d %buildroot%python3_sitelibdir
mv %buildroot{%python3_sitelibdir_noarch/*,%python3_sitelibdir}
%endif

cp -al %buildroot%_bindir/zope-testrunner{,3}

%check
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages -vvr -s false --develop

%files
%doc *.rst
%_bindir/zope-testrunner
%_bindir/zope-testrunner3
%python3_sitelibdir/zope/testrunner/
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info/
%python3_sitelibdir/%oname-%version-py%_python3_version-nspkg.pth

%exclude %python3_sitelibdir/zope/testrunner/tests/

%changelog
* Wed Mar 30 2022 Stanislav Levin <slev@altlinux.org> 5.4.0-alt1
- 5.3.0 -> 5.4.0.

* Tue Jul 06 2021 Vitaly Lipatov <lav@altlinux.ru> 5.3.0-alt2
- pack zope-testrunner3 for compatibility

* Tue Jul 06 2021 Vitaly Lipatov <lav@altlinux.ru> 5.3.0-alt1
- new version 5.3.0 (with rpmrb script)
- don't pack tests

* Tue Jul 06 2021 Vitaly Lipatov <lav@altlinux.ru> 5.2-alt3
- build python3 module separately

* Wed Sep 09 2020 Stanislav Levin <slev@altlinux.org> 5.2-alt2
- Disabled testing against Python2.

* Thu Aug 27 2020 Grigory Ustinov <grenka@altlinux.org> 5.2-alt1
- Automatically updated to 5.2.

* Thu Jan 09 2020 Grigory Ustinov <grenka@altlinux.org> 5.1-alt1
- Build new version 5.1.
- Fix license.

* Fri Apr 19 2019 Grigory Ustinov <grenka@altlinux.org> 5.0-alt1
- Build new version.

* Sat Jun 09 2018 Stanislav Levin <slev@altlinux.org> 4.8.1-alt3.S1
- Fix namespace package import ( python3 subpackage )

* Wed Feb 14 2018 Stanislav Levin <slev@altlinux.org> 4.8.1-alt2.S1
- Fix a wrong logic of packaging for non x86_64 arch

* Mon Feb 12 2018 Stanislav Levin <slev@altlinux.org> 4.8.1-alt1.S1
- v4.4.9 -> v4.8.1

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.4.9-alt1.1.1.1
- (AUTO) subst_x86_64.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.4.9-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 4.4.9-alt1.1
- NMU: Use buildreq for BR.

* Wed Aug 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.4.9-alt1
- Version 4.4.9

* Sat Feb 14 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.4.6-alt1
- Version 4.4.6

* Wed Jan 07 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.4.5-alt1
- Version 4.4.5

* Mon Dec 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.4.4-alt1
- Version 4.4.4

* Sun Jul 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.4.3-alt1
- Version 4.4.3

* Tue Sep 24 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.4.1-alt1
- Version 4.4.1

* Mon Apr 08 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.3.3-alt1
- Version 4.3.3

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 4.0.4-alt2.1
- Rebuild with Python-3.3

* Thu Apr 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.4-alt2
- Added module for Python 3

* Thu Dec 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.4-alt1
- Version 4.0.4

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 4.0.3-alt3.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.3-alt3
- Added necessary requirements
- Excluded *.pth

* Thu May 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.3-alt2
- Set as archdep package

* Tue May 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.3-alt1
- Initial build for Sisyphus

