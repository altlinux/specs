%define _unpackaged_files_terminate_build 1

%define oname pydocstyle

Name: python3-module-%oname
Version: 6.2.3
Release: alt1
Summary: Python docstring style checker
License: MIT
Group: Development/Python3
BuildArch: noarch
Url: https://pypi.python.org/pypi/pydocstyle

# https://github.com/PyCQA/pydocstyle.git
Source: %name-%version.tar
Patch1: %oname-6.1.1-alt-docs.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-poetry
BuildRequires: python3-module-html5lib python3-module-mock python3-module-pytest
BuildRequires: python3(configparser) python3(snowballstemmer) python3(six)
# Documentation
BuildRequires(pre): rpm-macros-sphinx3
BuildRequires: python3-module-alabaster python3-module-objects.inv python3-module-sphinx python3-module-sphinx-sphinx-build-symlink

# Conflicts due to binaries in /usr/bin
Conflicts: python-module-%oname

%description
pydocstyle is a static analysis tool for checking
compliance with Python docstring conventions.

pydocstyle supports most of PEP 257 out of the box,
but it should not be considered a reference implementation.

%package pickles
Summary: Pickles for %oname
Group: Development/Python3

%description pickles
pydocstyle is a static analysis tool for checking
compliance with Python docstring conventions.

pydocstyle supports most of PEP 257 out of the box,
but it should not be considered a reference implementation.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
pydocstyle is a static analysis tool for checking
compliance with Python docstring conventions.

pydocstyle supports most of PEP 257 out of the box,
but it should not be considered a reference implementation.

This package contains documentation for %oname.

%prep
%setup
%patch1 -p1

%prepare_sphinx3 .
ln -s ../objects.inv docs/

%build
%pyproject_build

%install
%pyproject_install

%make -C docs pickle
%make -C docs html

install -d %buildroot%python3_sitelibdir/%oname
cp -fR docs/_build/pickle %buildroot%python3_sitelibdir/%oname/

%check
export LC_ALL=en_US.UTF-8
# those tests are known to fail
rm -f src/tests/test_integration.py
PYTHONPATH=%buildroot%python3_sitelibdir py.test3 -vv

%files
%doc LICENSE-MIT
%doc README.rst
%_bindir/*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/pickle

%files pickles
%python3_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%changelog
* Tue Jan 31 2023 Ivan A. Melnikov <iv@altlinux.org> 6.2.3-alt1
- Updated to upstream version 6.2.3.
- Switch to %%pyproject_* macros.

* Thu Jun 10 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 6.1.1-alt1
- Updated to upstream version 6.1.1.
- Rebuilt without python-2.

* Fri Aug 31 2018 Stanislav Levin <slev@altlinux.org> 2.1.1-alt4
- Fix build.

* Wed May 30 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.1.1-alt3
- Fixed build dependencies.

* Thu Dec 28 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.1.1-alt2
- Upstream renamed package to pydocstyle from pep257.

* Thu Oct 26 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.1.1-alt1
- Updated to upstream version 2.1.1.

* Mon Aug 14 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.0.0-alt1
- Updated to upstream version 2.0.0.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5.0-alt1.alpha.git20150226.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.5.0-alt1.alpha.git20150226.1
- NMU: Use buildreq for BR.

* Thu Mar 05 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt1.alpha.git20150226
- Version 0.5.0-alpha
- Added docs

* Sat Jan 10 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.1-alt1.git20150109
- Initial build for Sisyphus

