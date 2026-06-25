%define _unpackaged_files_terminate_build 1
%define pypi_name generic
%define module_name generic

%def_with check

Name: python3-module-%pypi_name
Version: 1.1.7
Release: alt1
Summary: Generic programming library for Python
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/generic
Vcs: https://github.com/gaphor/generic.git
BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
Generic is a production-ready Python library for efficient generic programming,
supporting multiple-dispatch and event-driven architectures out of the box.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_poetry dev
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -ra

%files
%doc README.md
%python3_sitelibdir/%module_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Thu Jun 25 2026 Aleksandr A. Voyt <sobue@altlinux.org> 1.1.7-alt1
- 1.1.5 -> 1.1.7

* Thu Nov 06 2025 Aleksandr A. Voyt <sobue@altlinux.org> 1.1.5-alt1
- 1.1.4 -> 1.1.5

* Thu Apr 17 2025 Aleksandr A. Voyt <sobue@altlinux.org> 1.1.4-alt1
- Initial build
