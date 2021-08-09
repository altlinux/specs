%define _unpackaged_files_terminate_build 1

%define oname nbformat

Name: python3-module-%oname
Version: 5.1.3
Release: alt1
Summary: The Jupyter Notebook format
License: BSD-3-Clause
Group: Development/Python3
Url: https://github.com/jupyter/nbformat

BuildArch: noarch

# https://github.com/jupyter/nbformat.git
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-sphinx3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-pytest python3(testpath)
BuildRequires: python3-module-jsonschema python3-module-jupyter_core
BuildRequires: python3-module-nose python3-modules-sqlite3
BuildRequires: python3(fastjsonschema)
BuildRequires: python3-module-sphinx-devel
BuildRequires: python3-module-sphinx-sphinx-build-symlink

%py3_provides %oname
%py3_requires ipython_genutils traitlets jsonschema jupyter_core sqlite3

%description
This package contains the base implementation of the Jupyter Notebook
format, and Python APIs for working with notebooks.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This package contains the base implementation of the Jupyter Notebook
format, and Python APIs for working with notebooks.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python3

%description pickles
This package contains the base implementation of the Jupyter Notebook
format, and Python APIs for working with notebooks.

This package contains pickles for %oname.

%prep
%setup

%prepare_sphinx3 .
ln -s ../objects.inv docs/

%build
%python3_build_debug

%install
%python3_install

export PYTHONPATH=$PWD
%make -C docs pickle
%make -C docs html
cp -fR docs/_build/pickle %buildroot%python3_sitelibdir/%oname/

%check
py.test3 -vv

%files
%doc *.md docs/_build/html
%_bindir/*
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-py*.egg-info
%exclude %python3_sitelibdir/%oname/pickle
%exclude %python3_sitelibdir/%oname/tests
%exclude %python3_sitelibdir/%oname/*/tests

%files tests
%python3_sitelibdir/%oname/tests
%python3_sitelibdir/%oname/*/tests

%files pickles
%python3_sitelibdir/%oname/pickle

%changelog
* Mon Aug 09 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 5.1.3-alt1
- Updated to upstream version 5.1.3.

* Mon Sep 14 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 5.0.7-alt1
- Updated to upstream version 5.0.7.
- Disabled build for python-2.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 4.4.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Nov 23 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 4.4.0-alt1
- Updated to upstream version 4.4.0.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 4.0.0-alt1.1
- NMU: Use buildreq for BR.

* Sat Aug 22 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt1
- Initial build for Sisyphus

