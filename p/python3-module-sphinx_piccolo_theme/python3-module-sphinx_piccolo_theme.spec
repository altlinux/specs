%define pypi_name piccolo_theme

%def_without check

Name:    python3-module-sphinx_%pypi_name
Version: 0.24.0
Release: alt1

Summary: A clean and modern Sphinx theme
License: MIT
Group:   Development/Python3
URL:     https://github.com/piccolo-orm/piccolo_theme

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
%summary

%prep
%setup -n %pypi_name-%version

%build
export PYTHONPATH=.
%pyproject_build

%install
%pyproject_install

%check
#%%tox_create_default_config
%tox_check_pyproject

%files
%doc README.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Mon Oct 27 2025 Andrey Cherepanov <cas@altlinux.org> 0.24.0-alt1
- Initial build for Sisyphus.
