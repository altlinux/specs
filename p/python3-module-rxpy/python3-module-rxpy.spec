%define pypi_name rxpy

%def_without check

Name:    python3-module-%pypi_name
Version: 4.0.4
Release: alt1

Summary: ReactiveX for Python
License: MIT
Group:   Development/Python3
URL:     https://github.com/ReactiveX/RxPY

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-poetry

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
A library for composing asynchronous and event-based programs using observable
collections and query operator functions in Python.

%prep
%setup -n %pypi_name-%version
subst 's/^version.*/version="%version"/' pyproject.toml

%build
%pyproject_build

%install
%pyproject_install

%check
#%%tox_create_default_config
%tox_check_pyproject

%files
%doc *.md
%python3_sitelibdir/reactivex
%python3_sitelibdir/%{pyproject_distinfo reactivex}

%changelog
* Sat Sep 30 2023 Andrey Cherepanov <cas@altlinux.org> 4.0.4-alt1
- Initial build for Sisyphus
