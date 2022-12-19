%define _unpackaged_files_terminate_build 1

%define oname nbformat

Name: python3-module-%oname
Version: 5.7.0
Release: alt1
Summary: The Jupyter Notebook format
License: BSD-3-Clause
Group: Development/Python3
Url: https://github.com/jupyter/nbformat

BuildArch: noarch

Source: %name-%version.tar
Patch0: nbformat-build-test.patch

BuildRequires(pre): rpm-macros-sphinx3
BuildRequires: rpm-build-python3
BuildRequires: python3-module-hatchling
BuildRequires: python3-dev
BuildRequires: python3-module-pytest python3(testpath)
BuildRequires: python3-module-jsonschema python3-module-jupyter_core
BuildRequires: python3-module-nose python3-modules-sqlite3
BuildRequires: python3(fastjsonschema)
BuildRequires: python3-module-sphinx-devel
BuildRequires: python3-module-sphinx-sphinx-build-symlink
BuildRequires: python3-module-pep440

%py3_provides %oname
%py3_requires ipython_genutils traitlets jsonschema jupyter_core sqlite3

%description
This package contains the base implementation of the Jupyter Notebook
format, and Python APIs for working with notebooks.

%prep
%setup
%patch0 -p1

%prepare_sphinx3 .
ln -s ../objects.inv docs/

# Remove useless test dependencies
sed -i '/"pre-commit",/d' pyproject.toml
sed -i '/"check-manifest",/d' pyproject.toml

# Set version statically
# {VERSION} is a part of Patch0
sed -i "s/{VERSION}/%{version}/" pyproject.toml

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_create_default_config
%tox_check_pyproject

%files
%doc *.md
%_bindir/*
%python3_sitelibdir/*

%changelog
* Sun Dec 04 2022 Anton Farygin <rider@altlinux.ru> 5.7.0-alt1
- 5.1.3 -> 5.7.0

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

