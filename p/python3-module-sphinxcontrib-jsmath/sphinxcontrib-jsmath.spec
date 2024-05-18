%define  oname sphinxcontrib-jsmath

%def_with check

Name:    python3-module-%oname
Version: 1.0.1
Release: alt2

Summary: A sphinx extension which renders display math in HTML via JavaScript

License: BSD-2-Clause
Group:   Development/Python3
URL:     https://pypi.org/project/sphinxcontrib-jsmath
VCS:     https://github.com/sphinx-doc/sphinxcontrib-jsmath

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-sphinx-tests
%endif

Source: %name-%version.tar
Patch: sphinx5.patch

%description
%summary

%prep
%setup
%patch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check_pyproject

%files
%doc LICENSE README.rst CHANGES
%python3_sitelibdir/sphinxcontrib/*
%python3_sitelibdir/sphinxcontrib_jsmath-%{version}*.dist-info
%python3_sitelibdir/*.pth

%changelog
* Sat May 18 2024 Grigory Ustinov <grenka@altlinux.org> 1.0.1-alt2
- Build with check.

* Mon Sep 23 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.1-alt1
- Initial build for ALT.
