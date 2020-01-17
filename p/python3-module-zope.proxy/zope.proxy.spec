%define _unpackaged_files_terminate_build 1
%define oname zope.proxy

%def_with check

Name: python3-module-%oname
Version: 4.3.3
Release: alt1
Summary: Generic Transparent Proxies
License: ZPL
Group: Development/Python3
Url: http://pypi.python.org/pypi/zope.proxy/
#Git: https://github.com/zopefoundation/zope.proxy.git

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python3-module-tox
BuildRequires: python3-module-zope.testrunner
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-repoze.sphinx.autointerface
BuildRequires: python3-module-zope.security
%endif

%py3_requires zope zope.interface

%description
Proxies are special objects which serve as mostly-transparent wrappers
around another object, intervening in the apparent behavior of the
wrapped object only when necessary to apply the policy (e.g., access
checking, location brokering, etc.) for which the proxy is responsible.

%package tests
Summary: Tests for Generic Transparent Proxies
Group: Development/Python3
Requires: %name = %EVR

%description tests
Proxies are special objects which serve as mostly-transparent wrappers
around another object, intervening in the apparent behavior of the
wrapped object only when necessary to apply the policy (e.g., access
checking, location brokering, etc.) for which the proxy is responsible.

This package contains tests for Generic Transparent Proxies.

%prep
%setup

%build
%add_optflags -fno-strict-aliasing
%python3_build

%install
%python3_install

%check
sed -i 's|zope-testrunner |zope-testrunner3 |g' tox.ini
sed -i 's|sphinx-build|py3_sphinx-build|g' tox.ini

sed -i '/\[testenv\]$/a whitelist_externals =\
    \/bin\/cp\
    \/bin\/sed\
setenv =\
    py%{python_version_nodots python3}: _PYTEST_BIN=%_bindir\/zope-testrunner3\
    py%{python_version_nodots python3}: _DOCTEST_BIN=%_bindir\/py3_sphinx-build\
commands_pre =\
    \/bin\/cp {env:_PYTEST_BIN:} \{envbindir\}\/zope-testrunner3\
    \/bin\/sed -i \x271c #!\{envpython\}\x27 \{envbindir\}\/zope-testrunner3\
    \/bin\/cp {env:_DOCTEST_BIN:} \{envbindir\}\/py3_sphinx-build\
    \/bin\/sed -i \x271c #!\{envpython\}\x27 \{envbindir\}\/py3_sphinx-build' tox.ini

tox.py3 --sitepackages -e py%{python_version_nodots python3} -v

%files
%doc *.txt *.rst docs/*.rst
%_includedir/python3*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests

%files tests
%python3_sitelibdir/*/*/tests

%changelog
* Tue Dec 24 2019 Nikolai Kostrigin <nickel@altlinux.org> 4.3.3-alt1
- NMU: 4.2.0 -> 4.3.3
- Remove python2 module build
- Add unittests execution

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 4.2.0-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 4.2.0-alt1
- automated PyPI update

* Fri Mar 18 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.1.6-alt1.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Fri Mar 18 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.1.6-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Aug 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.6-alt1
- Version 4.1.6

* Wed Jul 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.4-alt1
- Version 4.1.4
- Added module for Python 3

* Wed Apr 10 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.3-alt1
- Version 4.1.3

* Thu Jan 03 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.1-alt1
- Version 4.1.1

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 3.6.1-alt2.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.6.1-alt2.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.1-alt2
- Added necessary requirements
- Excluded *.pth

* Tue May 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.1-alt1
- Initial build for Sisyphus

