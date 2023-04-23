%define pypi_name pystache

%def_without check

Name:    python3-module-%pypi_name
Version: 0.6.0
Release: alt1

Summary: Mustache in Python
License: MIT
Group:   Development/Python3
URL:     https://github.com/sarnold/pystache

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools python3-module-wheel

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
Pystache is a Python implementation of Mustache. Mustache is a
framework-agnostic, logic-free templating system inspired by ctemplate and et.
Like ctemplate, Mustache "emphasizes separating logic from presentation: it is
impossible to embed application logic in this template language."

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
%doc *.md
%_bindir/%{pypi_name}*
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Thu Apr 13 2023 Andrey Cherepanov <cas@altlinux.org> 0.6.0-alt1
- Initial build for Sisyphus.
