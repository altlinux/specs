%define pypi_name alterator

%def_without check

Name:    python3-module-%pypi_name
Version: 0.2.2
Release: alt0.2

Summary: Python module for new Alterator
License: GPL-3.0
Group:   Development/Python3
URL: https://altlinux.space/alterator

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools python3-module-wheel

BuildArch: noarch

Source: %name-%version.tar

%description
Python module for new Alterator.
Supported modules:

- components

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
#%%tox_create_default_config
%tox_check_pyproject

%files
%doc *.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Mon Jun 09 2025 Andrey Cherepanov <cas@altlinux.org> 0.2.2-alt0.2
- Components: added packages field.

* Fri May 16 2025 Andrey Cherepanov <cas@altlinux.org> 0.2.2-alt0.1
- Added ability to use from alterator import Components.

* Fri May 16 2025 Andrey Cherepanov <cas@altlinux.org> 0.2.1-alt0.1
- components: supported localized comment.

* Tue May 13 2025 Andrey Cherepanov <cas@altlinux.org> 0.2-alt0.1
- Initial build for Sisyphus for new Alterator.
