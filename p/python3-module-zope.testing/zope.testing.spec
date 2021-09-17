%define _unpackaged_files_terminate_build 1
%define oname zope.testing

%def_with check
%def_enable light_version

Name: python3-module-%oname
Version: 4.9
Release: alt1
Summary: Zope testing helpers
License: ZPL-2.1
Group: Development/Python3
Url: https://pypi.org/project/zope.testing/

# https://github.com/zopefoundation/zope.testing.git
Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3(tox)
BuildRequires: python3(tox_console_scripts)
BuildRequires: python3(zope.testrunner)
%endif

%py3_requires zope.exceptions zope.interface
%if_disabled light_version
%py3_requires zope.testrunner
%endif

%description
This package provides a number of testing frameworks. It includes a
flexible test runner, and supports both doctest and unittest.

%prep
%setup
%autopatch -p1

%build
%python3_build

%install
%python3_install

%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif

%check
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages --console-scripts -vvr -s false

%files
%doc *.txt *.rst
%python3_sitelibdir/zope/testing/
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info/
%exclude %python3_sitelibdir/*.pth

%changelog
* Fri Sep 17 2021 Stanislav Levin <slev@altlinux.org> 4.9-alt1
- 4.4.0 -> 4.9.

* Wed Jul 07 2021 Grigory Ustinov <grenka@altlinux.org> 4.4.0-alt3
- Drop python2 support.

* Tue Apr 30 2019 Grigory Ustinov <grenka@altlinux.org> 4.4.0-alt2.git20150825.2
- Rebuild with python3.7.

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.4.0-alt2.git20150825.1.1.1
- (AUTO) subst_x86_64.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.4.0-alt2.git20150825.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 4.4.0-alt2.git20150825.1
- NMU: Use buildreq for BR.

* Tue Jan 19 2016 Sergey Alembekov <rt@altlinux.ru> 4.4.0-alt2.git20150825
- Rebuild light version to break cycle

* Wed Aug 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.4.0-alt1.git20150825
- Version 4.4.0

* Mon Feb 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.4-alt2.dev0.git20150128
- Version 4.1.4.dev0

* Wed Oct 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.4-alt1.dev.git20140319
- Version 4.1.4dev

* Sun Jul 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.3-alt1
- Version 4.1.3

* Wed Apr 10 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.2-alt1
- Version 4.1.2

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 4.1.1-alt1.1
- Rebuild with Python-3.3

* Thu Apr 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.1-alt1
- Version 4.1.1
- Added module for Python 3

* Thu Dec 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt1
- Version 4.0.0

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.10.2-alt3.1
- Rebuild with Python-2.7

* Sun Jun 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.10.2-alt3
- Added necessary requirements
- Excluded *.pth

* Thu May 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.10.2-alt2
- Set as archdep package

* Tue May 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.10.2-alt1
- Initial build for Sisyphus

