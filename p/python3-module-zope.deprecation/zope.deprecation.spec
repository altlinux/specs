%define oname zope.deprecation

%def_with check

Name: python3-module-%oname
Epoch: 1
Version: 4.4.0
Release: alt2

Summary: Zope 3 Deprecation Infrastructure (Python 3)
License: ZPLv2.1
Group: Development/Python3
Url: http://pypi.python.org/pypi/zope.deprecation/
#Git: https://github.com/zopefoundation/zope.deprecation.git

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python3-module-tox
BuildRequires: python3-module-zope.testrunner
BuildRequires: python3-module-sphinx-devel
%endif

%py3_requires zope

%description
When we started working on Zope 3.1, we noticed that the hardest part of
the development process was to ensure backward-compatibility and
correctly mark deprecated modules, classes, functions, methods and
properties. This package provides a simple function called
'deprecated(names, reason)' to deprecate the previously mentioned Python
objects.

%package tests
Summary: Tests for Zope 3 Deprecation Infrastructure (Python 3)
Group: Development/Python3
Requires: %name = %EVR
%py3_requires zope.testing
%add_python3_req_skip deprecation

%description tests
When we started working on Zope 3.1, we noticed that the hardest part of
the development process was to ensure backward-compatibility and
correctly mark deprecated modules, classes, functions, methods and
properties. This package provides a simple function called
'deprecated(names, reason)' to deprecate the previously mentioned Python
objects.

This package contains tests for Zope 3 Deprecation Infrastructure.

%prep
%setup

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
sed -i 's|coverage run [ -a]\{0,\}-m||g' tox.ini
sed -i 's|coverage|#coverage|g' tox.ini
sed -i 's|zope.testrunner |zope-testrunner3 |g' tox.ini
# cancel docbuild tests
sed -i 's|sphinx|#py3_sphinx|g' tox.ini
sed -i '/\[testenv\]$/a whitelist_externals =\
    \/bin\/cp\
    \/bin\/sed\
commands_pre =\
    \/bin\/cp {env:_PYTEST_BIN:} \{envbindir\}\/zope-testrunner3\
    \/bin\/sed -i \x271c #!\{envpython\}\x27 \{envbindir\}\/zope-testrunner3' tox.ini
sed -i '/setenv =$/a \
    py%{python_version_nodots python3}: _PYTEST_BIN=%_bindir\/zope-testrunner3' tox.ini

tox.py3 --sitepackages -e py%{python_version_nodots python3} -v

%files
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests.*
%exclude %python3_sitelibdir/*/*/__pycache__/tests.*

%files tests
%python3_sitelibdir/*/*/tests.*
%python3_sitelibdir/*/*/__pycache__/tests.*

%changelog
* Wed Dec 25 2019 Nikolai Kostrigin <nickel@altlinux.org> 1:4.4.0-alt2
- NMU: Remove python2 module build
- Add unittests execution

* Wed Feb 27 2019 Andrey Bychkov <mrdrew@altlinux.org> 1:4.4.0-alt1
- Version updated to 4.4.0

* Tue Jun 07 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:4.1.3-alt1.dev0.git20150113.1.1.1
- (AUTO) subst_x86_64.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:4.1.3-alt1.dev0.git20150113.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 1:4.1.3-alt1.dev0.git20150113.1
- NMU: Use buildreq for BR.

* Thu Jan 15 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:4.1.3-alt1.dev0.git20150113
- Version 4.1.3.dev0

* Sat Jul 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:4.1.1-alt1
- Version 4.1.1

* Wed Mar 13 2013 Aleksey Avdeev <solo@altlinux.ru> 4.2.2-alt1
- Version 4.0.2

* Sat May 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.1-alt1
- Version 3.5.1
- Added module for Python 3

* Mon Dec 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.0-alt1
- Version 3.5.0

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.4.0-alt3.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.0-alt3
- Added necessary requirements
- Excluded *.pth

* Sat May 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.0-alt2
- Enable tests

* Sat May 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.0-alt1
- Initial build for Sisyphus
