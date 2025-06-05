%define  oname sphinxcontrib-jsmath

%def_with check

Name:    python3-module-%oname
Version: 1.0.1
Release: alt3

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
# https://github.com/sphinx-doc/sphinxcontrib-jsmath/pull/32
Patch1: sphinxcontrib-jsmath-1.0.1--Replace-domain.has_equations-with-context-has_maths.patch

%description
%summary

%prep
%setup
%autopatch -p1
# ship a release version, not a development one
sed -i \
    -e 's/^tag_build[ \t]*=.*/# &/' \
    -e 's/^tag_date[ \t]*=.*/# &/' \
setup.cfg

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check_pyproject

%files
%doc LICENSE README.rst CHANGES
%python3_sitelibdir/sphinxcontrib/*
%python3_sitelibdir/%{pyproject_distinfo %oname}/
%python3_sitelibdir/*.pth

%changelog
* Thu Jun 05 2025 Stanislav Levin <slev@altlinux.org> 1.0.1-alt3
- Fixed FTBFS (sphinx 8.2).
- Shipped stable version.

* Sat May 18 2024 Grigory Ustinov <grenka@altlinux.org> 1.0.1-alt2
- Build with check.

* Mon Sep 23 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.1-alt1
- Initial build for ALT.
