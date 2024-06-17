%define _unpackaged_files_terminate_build 1
%define pypi_name pygls
%define mod_name %pypi_name

%def_with check

%define add_python_extra() \
%{expand:%%package -n %%name+%1 \
Summary: %%summary \
Group: Development/Python3 \
Requires: %%name \
%{expand:%%pyproject_runtimedeps_metadata -- --extra %1} \
%%description -n %%name+%1' \
Extra "%1" for %%pypi_name. \
%%files -n %%name+%1 \
}

Name: python3-module-%pypi_name
Version: 1.3.1
Release: alt1
Summary: A pythonic generic language server
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/pygls
Vcs: https://github.com/openlawlibrary/pygls
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
# manually manage extra dependencies with metadata
AutoReq: yes, nopython3
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%add_python_extra ws

%description
%pypi_name (pronounced like "pie glass") is a pythonic generic implementation of
the Language Server Protocol for use as a foundation for writing your own
Language Servers in just a few lines of code.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_poetry test
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -ra

%files
%doc README.*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Mon Jun 17 2024 Stanislav Levin <slev@altlinux.org> 1.3.1-alt1
- Initial build for Sisyphus.
