%define oname nbformat

Name: python-module-%oname
Version: 4.4.0
Release: alt3
Summary: The Jupyter Notebook format
License: BSD
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/nbformat

# https://github.com/jupyter/nbformat.git
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-sphinx
BuildRequires: python-devel python-module-setuptools
BuildRequires: python-module-pytest python2.7(testpath)
BuildRequires: python-module-jsonschema python-module-jupyter_core
BuildRequires: python-module-nose python-modules-sqlite3
BuildRequires: python-module-numpydoc python-module-sphinx-devel
BuildRequires: python-module-alabaster python-module-html5lib python-module-objects.inv

%py_provides %oname
%py_requires ipython_genutils traitlets jsonschema jupyter_core sqlite3

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
Group: Development/Python

%description pickles
This package contains the base implementation of the Jupyter Notebook
format, and Python APIs for working with notebooks.

This package contains pickles for %oname.

%prep
%setup
%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%python_build_debug

%install
%python_install

export PYTHONPATH=$PWD
%make -C docs pickle
%make -C docs html
cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py2
done

%check
nosetests -vv

%files
%doc *.md docs/_build/html
%_bindir/*
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle
%exclude %python_sitelibdir/*/tests
%exclude %python_sitelibdir/*/*/tests

%files tests
%python_sitelibdir/*/tests
%python_sitelibdir/*/*/tests

%files pickles
%python_sitelibdir/*/pickle

%changelog
* Thu Sep 17 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 4.4.0-alt3
- Resolved conflict with python3-module-nbformat by renaming binaries.

* Mon Sep 14 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 4.4.0-alt2
- Rebuilt without python-3.

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

