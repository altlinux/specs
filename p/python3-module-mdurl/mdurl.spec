%define _unpackaged_files_terminate_build 1
%define pypi_name mdurl

%def_with check

Name: python3-module-%pypi_name
Version: 0.1.2
Release: alt1
Summary: Markdown URL utilities
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/mdurl
Vcs: https://github.com/executablebooks/mdurl
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
This is a Python port of the JavaScript mdurl package.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipreqfile tests/requirements.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc README.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Mon Apr 24 2023 Stanislav Levin <slev@altlinux.org> 0.1.2-alt1
- Initial build for Sisyphus.
