%define _unpackaged_files_terminate_build 1
%define pypi_name babi-grammars

# %check is disabled because python3-module-cson not packaged
%def_without check

Name: python3-module-%pypi_name
Version: 0.0.54
Release: alt1

Summary: grammars for babi
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/babi-grammars/
Vcs: https://github.com/asottile/babi-grammars

BuildArch: noarch
Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
%pyproject_builddeps_check
%pyproject_builddeps_metadata
%endif

%description
grammars for babi

%prep
%setup

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
%python3_sitelibdir/babi_grammars.py
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/
%_datadir/babi/

%changelog
* Sun Nov 05 2023 Vladislav Glinkin <smasher@altlinux.org> 0.0.54-alt1
- Updated to 0.0.54

* Wed Aug 30 2023 Vladislav Glinkin <smasher@altlinux.org> 0.0.52-alt1
- Initial build for ALT

