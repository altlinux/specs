%define _unpackaged_files_terminate_build 1
%define oname BTrees

%def_with check
%def_with bootstrap

Name: python3-module-%oname
Version: 4.6.1
Release: alt1

Summary: Scalable persistent object containers
License: ZPL-2.1
Group: Development/Python3
Url: https://pypi.python.org/pypi/BTrees
#Git: https://github.com/zopefoundation/BTrees.git

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-sphinx3

BuildRequires: python3-module-sphinx-devel
BuildRequires: python3-module-repoze.sphinx.autointerface
BuildRequires: python3-module-sphinx_rtd_theme
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-persistent
%if_without bootstrap
BuildRequires: python3-module-ZODB
%endif

%if_with check
BuildRequires: python3-module-tox
BuildRequires: python3-module-zope.testrunner
BuildRequires: python3-module-virtualenv
BuildRequires: python3-module-transaction
%if_without bootstrap
BuildRequires: python3-module-ZODB-tests
%endif
%endif

%py3_requires zope.interface

%define overview							   \
BTrees: scalable persistent components.					   \
									   \
This package contains a set of persistent object containers built around   \
a modified BTree data structure. The trees are optimized for use inside    \
ZODB's "optimistic concurrency" paradigm, and include explicit		   \
resolution of conflicts detected by that mechannism.			   \
									   \
%nil

%description %overview
%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
This package contains documentation for %oname.

%prep
%setup

%prepare_sphinx3 .
ln -s ../objects.inv3 docs/

%build
%add_optflags -fno-strict-aliasing
%python3_build_debug

%install
%python3_install

sed -i "s|SPHINXBUILD   = sphinx-build|SPHINXBUILD   = py3_sphinx-build|" docs/Makefile
export PYTHONPATH=%buildroot%python3_sitelibdir
%make -C docs html

%check
# remove pyproject.toml as it interferes unittests execution
rm ./pyproject.toml
sed -i 's|zope-testrunner |zope-testrunner3 |g' tox.ini
sed -i 's|sphinx-build|#py3_sphinx-build|g' tox.ini

sed -i '/\[testenv\]$/a whitelist_externals =\
    \/bin\/cp\
    \/bin\/sed\
commands_pre =\
    \/bin\/cp {env:_PYTEST_BIN:} \{envbindir\}\/zope-testrunner3\
    \/bin\/sed -i \x271c #!\{envpython\}\x27 \{envbindir\}\/zope-testrunner3\
    \/bin\/cp {env:_DOCTEST_BIN:} \{envbindir\}\/py3_sphinx-build\
    \/bin\/sed -i \x271c #!\{envpython\}\x27 \{envbindir\}\/py3_sphinx-build' tox.ini

sed -i '/setenv =$/a\
    py%{python_version_nodots python3}: _PYTEST_BIN=%_bindir\/zope-testrunner3\
    py%{python_version_nodots python3}: _DOCTEST_BIN=%_bindir\/py3_sphinx-build' tox.ini

tox.py3 --sitepackages -e py%{python_version_nodots python3} -v

%files
%doc *.txt *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files docs
%doc docs/_build/html/*

%files tests
%python3_sitelibdir/*/tests

%changelog
* Mon Jan 13 2020 Nikolai Kostrigin <nickel@altlinux.org> 4.6.1-alt1
- NMU: 4.4.1 -> 4.6.1
- Remove python2 module build
- Rearrange unittest execution
- Fix license

* Mon Apr 08 2019 Grigory Ustinov <grenka@altlinux.org> 4.4.1-alt3
- Bootstrap for python3.7.

* Thu May 10 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 4.4.1-alt2.S1
- (NMU) Rebuilt without bootstrap.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 4.4.1-alt1.S1.1
- (NMU) Rebuilt with python-3.6.4.

* Fri Feb 09 2018 Stanislav Levin <slev@altlinux.org> 4.4.1-alt1.S1
- v4.4.0 -> v4.4.1

* Sun Jan 15 2017 Igor Vlasenko <viy@altlinux.ru> 4.4.0-alt1
- automated PyPI update

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 4.3.2-alt1
- automated PyPI update

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.1.5-alt2.dev0.git20150602.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Wed Jan 27 2016 Mikhail Efremov <sem@altlinux.org> 4.1.5-alt2.dev0.git20150602.1
- NMU: Use buildreq for BR.

* Tue Jan 19 2016 Sergey Alembekov <rt@altlinux.ru> 4.1.5-alt2.dev0.git20150602
- remove ZODB cyrcular dependency

* Sun Aug 30 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.5-alt1.dev0.git20150602
- Version 4.1.5.dev0

* Thu Jan 01 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.2-alt1.dev0.git201411227
- Version 4.1.2.dev0

* Wed Oct 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.9-alt1.dev.git20141008
- Version 4.0.9dev

* Thu Jul 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.8-alt2
- Avoid conflict with ZODB3

* Wed Jul 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.8-alt1
- Initial build for Sisyphus
