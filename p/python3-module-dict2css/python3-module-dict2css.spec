%define pypi_name dict2css

%def_without check

Name:    python3-module-%pypi_name
Version: 0.6.0
Release: alt1

Summary: A library for constructing cascading style sheets from Python dictionaries
License: MIT
Group:   Development/Python3
URL:     https://github.com/sphinx-toolbox/dict2css

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-whey

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
%summary

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
#%%tox_create_default_config
%tox_check_pyproject

%files
%doc *.rst
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Sat Jun 06 2026 Andrey Cherepanov <cas@altlinux.org> 0.6.0-alt1
- Initial build for Sisyphus.
