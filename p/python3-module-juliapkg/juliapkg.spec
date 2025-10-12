%define pypi_name juliapkg

%def_with check

Name:    python3-module-%pypi_name
Version: 0.1.22
Release: alt1

Summary: Manage your Julia dependencies from Python
License: MIT
Group:   Development/Python3
URL:     https://pypi.org/project/juliapkg
VCS:     https://github.com/JuliaPy/pyjuliapkg

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-hatchling

%if_with check
BuildRequires: python3-module-filelock
BuildRequires: python3-module-semver
BuildRequires: python3-module-tomlkit
BuildRequires: python3-module-tomli
%endif

BuildArch: noarch

Source: %name-%version.tar

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
# test_resolve test_executable test_project
# need internet connection
# test_editable_setuptools
# we dont need it in package
%pyproject_run_pytest -k'not test_resolve and not test_executable and not test_project and not test_editable_setuptools'

%files
%doc LICENSE *.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Sun Oct 12 2025 Grigory Ustinov <grenka@altlinux.org> 0.1.22-alt1
- Automatically updated to 0.1.22.

* Wed Sep 17 2025 Grigory Ustinov <grenka@altlinux.org> 0.1.18-alt1
- Automatically updated to 0.1.18.

* Thu Jul 03 2025 Grigory Ustinov <grenka@altlinux.org> 0.1.17-alt1
- Initial build for Sisyphus
