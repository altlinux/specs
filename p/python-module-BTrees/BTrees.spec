%define _unpackaged_files_terminate_build 1
%define oname BTrees

%def_with check

Name: python-module-%oname
Version: 4.4.1
Release: alt1%ubt

Summary: Scalable persistent object containers
License: ZPLv2.1
Group: Development/Python
# https://github.com/zopefoundation/BTrees.git
Url: https://pypi.python.org/pypi/BTrees

Source: %name-%version.tar

BuildRequires(pre): rpm-build-ubt
BuildRequires(pre): rpm-build-python
BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-sphinx

BuildRequires: python-module-objects.inv
BuildRequires: python-module-repoze.sphinx.autointerface
BuildRequires: python-module-persistent
BuildRequires: python-module-setuptools
BuildRequires: python-module-ZODB
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-persistent
BuildRequires: python3-module-ZODB

%if_with check
BuildRequires: python-module-tox
BuildRequires: python-module-virtualenv
BuildRequires: python-module-transaction
BuildRequires: python-module-ZODB-tests
BuildRequires: python3-module-tox
BuildRequires: python3-module-virtualenv
BuildRequires: python3-module-transaction
BuildRequires: python3-module-ZODB-tests
%endif

%py_requires zope.interface

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
Group: Development/Python
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
This package contains documentation for %oname.

%package -n python3-module-%oname
Summary: Scalable persistent object containers
Group: Development/Python3

%description -n python3-module-%oname
%overview

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
This package contains tests for %oname.

%prep
%setup

rm -rf ../python3
cp -a . ../python3

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%add_optflags -fno-strict-aliasing
%python_build_debug

pushd ../python3
%python3_build_debug
popd

%install
%python_install

pushd ../python3
%python3_install
popd

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C docs html

%check
export PIP_INDEX_URL=http://host.invalid./
export PYTHONPATH=%python_sitelibdir_noarch:%python_sitelibdir
TOX_TESTENV_PASSENV='PYTHONPATH' tox -e py27 -v

pushd ../python3
export PYTHONPATH=%python3_sitelibdir_noarch:%python3_sitelibdir
TOX_TESTENV_PASSENV='PYTHONPATH' tox.py3 -e py35 -v
popd

%files
%doc *.txt *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%files docs
%doc docs/_build/html/*

%files -n python3-module-%oname
%doc *.txt *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests

%changelog
* Fri Feb 09 2018 Stanislav Levin <slev@altlinux.org> 4.4.1-alt1%ubt
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
