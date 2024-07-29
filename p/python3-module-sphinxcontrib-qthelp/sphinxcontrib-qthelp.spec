%define  oname sphinxcontrib-qthelp

%def_with check

Name:    python3-module-%oname
Version: 2.0.0
Release: alt1

Summary: A sphinx extension which outputs QtHelp document
License: BSD-2-Clause
Group:   Development/Python3
URL:     https://pypi.org/project/sphinxcontrib-qthelp
VCS:     https://github.com/sphinx-doc/sphinxcontrib-qthelp

Source:  %name-%version.tar

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-flit

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-sphinx-tests
%endif

BuildArch: noarch

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check_pyproject

%files
%doc *.rst
%python3_sitelibdir/sphinxcontrib
%python3_sitelibdir/sphinxcontrib_qthelp-%version.dist-info

%changelog
* Mon Jul 29 2024 Grigory Ustinov <grenka@altlinux.org> 2.0.0-alt1
- Automatically updated to 2.0.0.

* Mon Jul 22 2024 Grigory Ustinov <grenka@altlinux.org> 1.0.8-alt1
- Automatically updated to 1.0.8.

* Tue Jan 23 2024 Grigory Ustinov <grenka@altlinux.org> 1.0.7-alt1
- Automatically updated to 1.0.7.

* Mon Sep 11 2023 Grigory Ustinov <grenka@altlinux.org> 1.0.6-alt1
- Automatically updated to 1.0.6.

* Thu Aug 04 2022 Grigory Ustinov <grenka@altlinux.org> 1.0.3-alt2
- Fixed FTBFS.

* Mon Mar 02 2020 Grigory Ustinov <grenka@altlinux.org> 1.0.3-alt1
- Build new version.
- Correct license.
- Build with check.

* Fri Apr 26 2019 Grigory Ustinov <grenka@altlinux.org> 1.0.2-alt1
- Initial build for Sisyphus.
