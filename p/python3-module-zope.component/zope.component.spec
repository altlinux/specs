%define _unpackaged_files_terminate_build 1
%define oname zope.component

%def_with check

Name: python3-module-%oname
Version: 4.6
Release: alt1

Summary: Zope Component Architecture (Python3)
License: ZPLv2.1
Group: Development/Python3
Url: http://pypi.python.org/pypi/zope.component
#Git: https://github.com/zopefoundation/zope.component.git

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python3-module-tox
BuildRequires: python3-module-persistent
BuildRequires: python3-module-zope.testing
BuildRequires: python3-module-zope.testrunner
BuildRequires: python3-module-zope.configuration
BuildRequires: python3-module-zope.event
BuildRequires: python3-module-zope.location
BuildRequires: python3-module-zope.deferredimport
BuildRequires: python3-module-zope.hookable
BuildRequires: python3-module-zope.deprecation
%endif

%py3_requires zope

%description
This package is intended to be independently reusable in any Python
project. It is maintained by the Zope Toolkit project.

This package represents the core of the Zope Component Architecture.
Together with the 'zope.interface' package, it provides facilities for
defining, registering and looking up components.

%package tests
Summary: Tests for zope.component (Python 3)
Group: Development/Python3
Requires: %name = %EVR
%py3_requires zope.testing zope.testrunner

%description tests
This package contains tests for %oname

%prep
%setup
%patch0 -p1

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
sed -i 's|zope-testrunner |zope-testrunner3 |g' tox.ini
# cancel docbuild tests
sed -i 's|\.\[docs\]||g' tox.ini
sed -i 's|sphinx-build|#py3_sphinx-build|g' tox.ini
sed -i '/\[testenv\]$/a whitelist_externals =\
    \/bin\/cp\
    \/bin\/sed\
setenv =\
    py%{python_version_nodots python3}: _PYTEST_BIN=%_bindir\/zope-testrunner3\
commands_pre =\
    \/bin\/cp {env:_PYTEST_BIN:} \{envbindir\}\/zope-testrunner3\
    \/bin\/sed -i \x271c #!\{envpython\}\x27 \{envbindir\}\/zope-testrunner3' tox.ini

tox.py3 --sitepackages -e py%{python_version_nodots python3} -v

%files
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/test*
%exclude %python3_sitelibdir/*/*/*/test*

%files tests
%python3_sitelibdir/*/*/test*
%python3_sitelibdir/*/*/*/test*

%changelog
* Fri Dec 20 2019 Nikolai Kostrigin <nickel@altlinux.org> 4.6-alt1
- NMU: 4.5 -> 4.6
- Remove python2 module build
- Remove ubt tag from changelog
- Rearrange unittests execution

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 4.5-alt4
- NMU: remove rpm-build-ubt from BR:

* Tue Mar 05 2019 Andrey Bychkov <mrdrew@altlinux.org> 4.5-alt3
- check disabled for build in p8

* Fri Mar 01 2019 Andrey Bychkov <mrdrew@altlinux.org> 4.5-alt2
- requires fixed

* Wed Feb 27 2019 Andrey Bychkov <mrdrew@altlinux.org> 4.5-alt1
- Version updated to 4.5

* Fri Feb 16 2018 Stanislav Levin <slev@altlinux.org> 4.4.1-alt1
- 4.2.3 -> 4.4.1

* Tue Jun 07 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.2.3-alt1.dev0.git20150604.1.1.1
- (AUTO) subst_x86_64.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.2.3-alt1.dev0.git20150604.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 4.2.3-alt1.dev0.git20150604.1
- NMU: Use buildreq for BR.

* Wed Aug 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.3-alt1.dev0.git20150604
- Version 4.2.3.dev0

* Sun Feb 22 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.2-alt1.dev0.git20150128
- Version 4.2.2.dev0

* Sat Jul 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.1-alt1
- Version 4.2.1

* Mon Apr 15 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.0-alt1.1
- Use 'find... -exec...' instead of 'for ... $(find...'

* Sun Mar 03 2013 Aleksey Avdeev <solo@altlinux.ru> 4.1.0-alt1
- Version 4.1.0-alt1

* Mon Apr 16 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.12.1-alt1
- Version 3.12.1
- Added module for Python 3

* Mon Dec 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.12.0-alt1
- Version 3.12.0

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.10.0-alt4.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.10.0-alt4
- Added necessary requirements for tests

* Sun Jun 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.10.0-alt3
- Add necessary requiresments
- Excludes *.pth

* Thu May 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.10.0-alt2
- Set archdep for package

* Mon May 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.10.0-alt1
- Initial build for Sisyphus
