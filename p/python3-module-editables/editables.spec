%define _unpackaged_files_terminate_build 1
%define pypi_name editables

%def_with check

Name: python3-module-%pypi_name
Version: 0.5
Release: alt1.1
Summary: Editable installations
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/editables
Vcs: https://github.com/pfmoore/editables
BuildArch: noarch
Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-flit-core

%if_with check
BuildRequires: python3-module-coverage
BuildRequires: python3-module-pip
BuildRequires: python3-module-pytest
BuildRequires: python3-module-virtualenv
%endif

%description
A Python library for creating "editable wheels".
This library supports the building of wheels which, when installed, will expose
packages in a local directory on sys.path in "editable mode". In other words,
changes to the package source will be reflected in the package visible to
Python, without needing a reinstall.

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -ra -Wignore tests

%files
%doc README.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 0.5-alt1.1
- Demodernized packaging.

* Tue Jul 25 2023 Stanislav Levin <slev@altlinux.org> 0.5-alt1
- 0.4 -> 0.5.

* Fri Jul 21 2023 Stanislav Levin <slev@altlinux.org> 0.4-alt1
- 0.3 -> 0.4.

* Wed Aug 10 2022 Stanislav Levin <slev@altlinux.org> 0.3-alt1
- 0.2 -> 0.3.

* Mon Apr 04 2022 Stanislav Levin <slev@altlinux.org> 0.2-alt1
- Initial build for Sisyphus.
