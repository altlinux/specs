%define _unpackaged_files_terminate_build 1
%define oname zope.security

%def_without check
%def_without docs

Name: python3-module-%oname
Version: 5.1.1
Release: alt2.1
Summary: Zope Security Framework
License: ZPL-2.1
Group: Development/Python3
Url: http://pypi.python.org/pypi/zope.security/
#Git: https://github.com/zopefoundation/zope.security.git

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-sphinx3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-zope.proxy
%if_with docs
BuildRequires: python3-module-sphinx-devel
BuildRequires: python3-module-repoze.sphinx.autointerface
%endif
BuildRequires: python3-module-zope.schema
BuildRequires: python3-module-zope.location
BuildRequires: time

%if_with check
BuildRequires: python3-module-tox
BuildRequires: python3-module-virtualenv
BuildRequires: python3-module-BTrees
BuildRequires: python3-module-zope.testing
BuildRequires: python3-module-zope.testrunner
BuildRequires: python3-module-zope.component-tests
%endif

%py3_requires zope.i18nmessageid
%py3_requires zope.component zope.interface zope.location zope.proxy
%py3_requires zope.schema zope.configuration

%description
The Security framework provides a generic mechanism to implement
security policies on Python objects.

%package examples
Summary: Examples for Zope Security Framework
Group: Development/Python3
Requires: %name = %EVR

%add_python3_self_prov_path %buildroot%python3_sitelibdir/zope/security/examples/sandbox.py

%description examples
The Security framework provides a generic mechanism to implement
security policies on Python objects.

This package contains examples for Zope Security Framework.

%package tests
Summary: Tests for Zope Security Framework
Group: Development/Python3
Requires: %name = %EVR
%py3_requires zope.testing

%description tests
The Security framework provides a generic mechanism to implement
security policies on Python objects.

This package contains tests for Zope Security Framework.

%package pickles
Summary: Pickles for Zope Security Framework
Group: Development/Python3

%description pickles
The Security framework provides a generic mechanism to implement
security policies on Python objects.

This package contains pickles for Zope Security Framework.

%package docs
Summary: Documentation for Zope Security Framework
Group: Development/Documentation
BuildArch: noarch

%description docs
The Security framework provides a generic mechanism to implement
security policies on Python objects.

This package contains documentation for Zope Security Framework.

%prep
%setup

%if_with docs
%prepare_sphinx3 .
ln -s ../objects.inv3 docs/
%endif

%build
%add_optflags -fno-strict-aliasing
%python3_build

%install
%python3_install
install -p -m644 src/zope/security/*.zcml \
	%buildroot%python3_sitelibdir/zope/security/

%if_with docs
export PYTHONPATH=$PWD/src
sed -i "s|SPHINXBUILD   = sphinx-build|SPHINXBUILD   = py3_sphinx-build|" docs/Makefile
%make -C docs pickle
%make -C docs html

install -d %buildroot%python3_sitelibdir/%oname
cp -fR docs/_build/pickle %buildroot%python3_sitelibdir/%oname/
%endif

%check
sed -i '/\[testenv\]$/a whitelist_externals =\
    \/bin\/cp\
    \/bin\/sed\
commands_pre =\
    \/bin\/cp {env:_PYTEST_BIN:} \{envbindir\}\/zope-testrunner3\
    \/bin\/sed -i \x271c #!\{envpython\}\x27 \{envbindir\}\/zope-testrunner3' tox.ini
sed -i '/setenv =$/a\
    py%{python_version_nodots python3}: _PYTEST_BIN=%_bindir\/zope-testrunner3' tox.ini

sed -i 's|zope-testrunner |zope-testrunner3 |g' tox.ini
# cancel docbuild tests
sed -i 's|sphinx-build|#py3_sphinx-build|g' tox.ini

tox.py3 --sitepackages -e py%{python_version_nodots python3} -v

%files
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/test*
%exclude %python3_sitelibdir/*/*/*/test*
%exclude %python3_sitelibdir/*/*/examples
%if_with docs
%exclude %python3_sitelibdir/*/pickle
%endif

%files examples
%python3_sitelibdir/*/*/examples

%files tests
%python3_sitelibdir/*/*/test*
%python3_sitelibdir/*/*/*/test*

%if_with docs
%files pickles
%python3_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*
%endif

%changelog
* Sun Nov 13 2022 Daniel Zagaynov <kotopesutility@altlinux.org> 5.1.1-alt2.1
- NMU: used %%add_python3_self_prov_path macro to skip self-provides from dependencies.

* Mon Nov 23 2020 Grigory Ustinov <grenka@altlinux.org> 5.1.1-alt2
- Bootstrap for python3.9.

* Wed Apr 01 2020 Nikolai Kostrigin <nickel@altlinux.org> 5.1.1-alt1
- 5.1.0 -> 5.1.1
- Reenable check and docs sections; switch back to uniform def_with macro
- Rearrange check section according to upstream changes

* Fri Mar 06 2020 Anton Farygin <rider@altlinux.ru> 5.1.0-alt2
- temporary  disabled check and docs sections to avoid cyclic dependencies
  on zope.component when building python-3.8

* Wed Mar 04 2020 Nikolai Kostrigin <nickel@altlinux.org> 5.1.0-alt1
- 5.0 -> 5.1.0
- Fix license

* Mon Dec 23 2019 Nikolai Kostrigin <nickel@altlinux.org> 5.0-alt1
- NMU: 4.0.4 -> 5.0
- Remove python2 module build
- Cleanup excessive commented BRs
- Add unittests execution

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 4.0.4-alt1.dev0.git20150602.1.1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Fri Mar 18 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0.4-alt1.dev0.git20150602.1.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Fri Mar 18 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0.4-alt1.dev0.git20150602.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 4.0.4-alt1.dev0.git20150602.1
- NMU: Use buildreq for BR.

* Wed Aug 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.4-alt1.dev0.git20150602
- Version 4.0.4.dev0

* Fri Jul 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.2-alt2.dev.git20140319
- Python 3: moved examples into separate package

* Thu Jul 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.2-alt1.dev.git20140319
- Version 4.0.2dev
- Added module for Python 3

* Tue Sep 24 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt1.dev.git20130709
- Version 4.0.1dev

* Wed Apr 10 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt3.b2.dev0.git20130327
- Version 4.0.0b2.dev0

* Thu Jan 03 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt2.bzr20120517
- Added necessary .zcml files (ALT #28301)

* Sun Jun 03 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt1.bzr20120517
- Version 4.0.0dev

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 3.8.3-alt1.1
- Rebuild to remove redundant libpython2.7 dependency

* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8.3-alt1
- Version 3.8.3

* Tue Nov 01 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.8.1-alt3.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8.1-alt3
- Added necessary requirements for tests

* Sun Jun 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8.1-alt2
- Added necessary requirements
- Excluded *.pth

* Tue May 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8.1-alt1
- Initial build for Sisyphus

