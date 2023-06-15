%define _unpackaged_files_terminate_build 1
%define pypi_name usort
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 1.0.7
Release: alt1
Summary: A small, safe import sorter
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/usort
Vcs: https://github.com/facebook/usort
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%endif

%description
usort is a safe, minimal import sorter. Its primary goal is to make no
"dangerous" changes to code. This is achieved by detecting distinct "blocks" of
imports that are the most likely to be safely interchangeable, and only
reordering imports within these blocks without altering formatting. Code style
is left as an exercise for linters and formatters.

%package -n %pypi_name
Summary: Executable for %pypi_name
Group: Development/Python3
Requires: %name

%description -n %pypi_name
%summary

%prep
%setup
%autopatch -p1
%pyproject_scm_init
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run -- python3 -m %mod_name.tests -v

%files
%doc README.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%files -n %pypi_name
%_bindir/%pypi_name

%changelog
* Tue Jun 13 2023 Stanislav Levin <slev@altlinux.org> 1.0.7-alt1
- 1.0.6 -> 1.0.7.

* Wed May 10 2023 Stanislav Levin <slev@altlinux.org> 1.0.6-alt1
- 1.0.5 -> 1.0.6.

* Thu Sep 15 2022 Stanislav Levin <slev@altlinux.org> 1.0.5-alt1
- 1.0.2 -> 1.0.5.

* Fri Apr 01 2022 Stanislav Levin <slev@altlinux.org> 1.0.2-alt1
- 1.0.1 -> 1.0.2.

* Thu Feb 10 2022 Stanislav Levin <slev@altlinux.org> 1.0.1-alt1
- Initial build for Sisyphus.
