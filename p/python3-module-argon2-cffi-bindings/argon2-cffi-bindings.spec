%define pypi_name argon2-cffi-bindings

%def_with check

Name:    python3-module-%pypi_name
Version: 21.2.0
Release: alt1

Summary: Low-level Python CFFI Bindings for Argon2

License: MIT
Group:   Development/Python3
URL:     https://pypi.org/project/argon2-cffi-bindings
VCS:     https://github.com/hynek/argon2-cffi-bindings

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-setuptools-scm
BuildRequires: python3-module-wheel
BuildRequires: python3-module-cffi
BuildRequires: libargon2-devel

Source: %name-%version.tar

%description
%summary

%prep
%setup

%build
export ARGON2_CFFI_USE_SYSTEM=1
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_build

%install
%pyproject_install

%check
%tox_check_pyproject

%files
%doc LICENSE *.md
%python3_sitelibdir/_argon2_cffi_bindings
%python3_sitelibdir/argon2_cffi_bindings-%version.dist-info

%changelog
* Sat May 25 2024 Grigory Ustinov <grenka@altlinux.org> 21.2.0-alt1
- Initial build for Sisyphus.
