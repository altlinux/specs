%define _unpackaged_files_terminate_build 1
%define pypi_name magic-filter
%define module_name magic_filter

%def_with check

Name: python3-module-%pypi_name
Version: 1.0.12
Release: alt1.1
Summary: Magic filter based on dynamic attribute getter
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/magic-filter/
Vcs: https://github.com/aiogram/magic-filter.git
BuildArch: noarch

Source0: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-hatchling

%description
magic-filter is a package that provides magic filter based on dynamic
attribute getter. It's used for creating elegant filtering and validation
expressions in Python.

%prep
%setup

# Update the version in __init__.py to match the spec version
sed -i 's/__version__ = "1"/__version__ = "%version"/' magic_filter/__init__.py


%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -ra

%files
%doc README.md LICENSE
%python3_sitelibdir/%module_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 1.0.12-alt1.1
- Demodernized packaging.

* Fri Nov 07 2025 Aleksandr A. Voyt <sobue@altlinux.org> 1.0.12-alt1
- Initial build.
