%define _unpackaged_files_terminate_build 1
%define oname persistent

%def_with check

Name: python3-module-%oname
Version: 4.5.1
Release: alt1

Summary: Translucent persistent objects
License: ZPL-2.1
Group: Development/Python3
Url: http://www.zope.org/Products/ZODB
#Git: https://github.com/zopefoundation/persistent.git

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-sphinx3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-alabaster 
BuildRequires: python3-module-docutils
BuildRequires: python3-module-html5lib
BuildRequires: python3-module-objects.inv
BuildRequires: python3-module-repoze.sphinx.autointerface
BuildRequires: python3-dev
%if_with check
BuildRequires: python3-module-nose
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-zope
BuildRequires: python3-module-tox
BuildRequires: python3-module-virtualenv
BuildRequires: python3-module-zope.testrunner
BuildRequires: python3-module-manuel
BuildRequires: python3-module-manuel-tests
%endif

%py3_provides persistent.TimeStamp

%description
This package contains a generic persistence implementation for Python.
It forms the core protocol for making objects interact "transparently"
with a database such as the ZODB.

%package docs
Summary: Documentation for translucent persistent objects
Group: Development/Documentation
BuildArch: noarch

%description docs
This package contains documentation for persistence implementation for
Python. It forms the core protocol for making objects interact
"transparently" with a database such as the ZODB.

%package tests
Summary: Tests for translucent persistent objects
Group: Development/Python3
Requires: %name = %EVR

%description tests
This package contains a generic tests persistence implementation for
Python. It forms the core protocol for making objects interact
"transparently" with a database such as the ZODB.

%prep
%setup

sed -i 's|sphinx-build|py3_sphinx-build|' docs/Makefile
%prepare_sphinx3 .
ln -s ../objects.inv3 docs/

%build
%add_optflags -fno-strict-aliasing
%python3_build

%install
%python3_install
install -p -m644 persistent/_compat.h \
	%buildroot%_includedir/python%_python3_version%_python3_abiflags/

export PYTHONPATH=%buildroot%python3_sitelibdir
%make -C docs html

%check
export PIP_INDEX_URL=http://host.invalid./
export PYTHONPATH=%python3_sitelibdir:%python3_sitelibdir_noarch
sed -i 's|zope-testrunner|zope-testrunner3|g' tox.ini
sed -i '/\[testenv\]$/a whitelist_externals =\
    \/bin\/cp\
    \/bin\/sed\
setenv =\
    py%{python_version_nodots python3}: _PYTEST_BIN=%_bindir\/zope-testrunner3\
commands_pre =\
    \/bin\/cp {env:_PYTEST_BIN:} \{envbindir\}\/zope-testrunner3\
    \/bin\/sed -i \x271c #!\{envpython\}\x27 \{envbindir\}\/zope-testrunner3' tox.ini

TOX_TESTENV_PASSENV='PYTHONPATH' tox.py3 -e py%{python_version_nodots python3} -v

%files
%doc *.txt
%_includedir/python%_python3_version%_python3_abiflags
%python3_sitelibdir/%oname/
%exclude %python3_sitelibdir/%oname/test*
%python3_sitelibdir/*.egg-info

%files docs
%doc docs/_build/html/*

%files tests
%python3_sitelibdir/%oname/test*

%changelog
* Tue Jan 14 2020 Nikolai Kostrigin <nickel@altlinux.org> 4.5.1-alt1
- NMU: 4.2.4.2 -> 4.5.1
- Remove python2 module build
- Rearrange unittests execution
- Fix license

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 4.2.4.2-alt1.1.1.qa1
- NMU: applied repocop patch

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 4.2.4.2-alt1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 4.2.4.2-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Oct 17 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 4.2.4.2-alt1
- Updated to upstream version 4.2.4.2.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.1.1-alt2.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 4.1.1-alt2.1
- NMU: Use buildreq for BR.

* Fri Aug 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.1-alt2
- Really version 4.1.1

* Wed Aug 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.1-alt1
- Version 4.1.1

* Thu Jul 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.8-alt2
- Avoid conflict with ZODB3

* Wed Jul 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.8-alt1
- Version 4.0.8

* Thu Nov 28 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.6-alt1.1
- Fixed build

* Wed Mar 13 2013 Aleksey Avdeev <solo@altlinux.ru> 4.0.6-alt1
- Initial build for ALT Linux Sisyphus
