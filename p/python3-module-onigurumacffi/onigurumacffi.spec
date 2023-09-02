%define _unpackaged_files_terminate_build 1
%define pypi_name onigurumacffi

%def_with check

Name: python3-module-%pypi_name
Version: 1.2.0
Release: alt1

Summary: python cffi bindings for the oniguruma regex engine
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/onigurumacffi/
Vcs: https://github.com/asottile/onigurumacffi

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
BuildRequires: liboniguruma-devel
%pyproject_builddeps_build

%if_with check
%pyproject_builddeps_check
%endif

%description
python cffi bindings for the oniguruma regex engine

%prep
%setup

# Edit setup.cfg for setuptools (actual for 1.2.0)
sed -i -e 's/license_file/license_files/' setup.cfg
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%if_with check
%pyproject_deps_resync_check_pipreqfile requirements-dev.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc README.md LICENSE
%python3_sitelibdir/__pycache__/*
%python3_sitelibdir/%pypi_name.py
%python3_sitelibdir/_%pypi_name.abi3.so
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Sat Sep 02 2023 Vladislav Glinkin <smasher@altlinux.org> 1.2.0-alt1
- Initial build for ALT

