%define _unpackaged_files_terminate_build 1
%define pypi_name ufmt
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 2.3.0
Release: alt1
Summary: Safe, atomic formatting with black and usort
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/ufmt
Vcs: https://github.com/omnilib/ufmt
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%add_pyproject_deps_check_filter attribution
%pyproject_builddeps_metadata_extra dev
# black is runtime dependency but it's filtered out by default
BuildRequires: python3-module-black
%endif

%description
%pypi_name is a safe, atomic code formatter for Python built on top of black and
usort. %pypi_name formats files in-memory, first with usort and then with black,
before writing any changes back to disk. This enables a combined, atomic step
in CI/CD workflows for checking or formatting files, without any with conflict
or intermediate changes between the import sorter and the code formatter.

%package -n %pypi_name
Summary: Executable for %pypi_name
Group: Development/Python3
Requires: %name

%description -n %pypi_name
%summary

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

# don't ship tests
rm -r %buildroot%python3_sitelibdir/%pypi_name/tests/

%check
%pyproject_run -- python3 -m %mod_name.tests -v

%files
%doc README.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%files -n %pypi_name
%_bindir/%pypi_name

%changelog
* Thu Nov 09 2023 Stanislav Levin <slev@altlinux.org> 2.3.0-alt1
- 2.2.0 -> 2.3.0.

* Wed Aug 02 2023 Stanislav Levin <slev@altlinux.org> 2.2.0-alt1
- 2.1.0 -> 2.2.0.

* Wed May 10 2023 Stanislav Levin <slev@altlinux.org> 2.1.0-alt1
- 2.0.1 -> 2.1.0.

* Wed Nov 16 2022 Michael Shigorin <mike@altlinux.org> 2.0.1-alt2
- Fix BR: requisite for %%build, not just %%check.

* Thu Sep 15 2022 Stanislav Levin <slev@altlinux.org> 2.0.1-alt1
- 1.3.2 -> 2.0.1.

* Fri Feb 25 2022 Stanislav Levin <slev@altlinux.org> 1.3.2-alt1
- 1.3.1 -> 1.3.2.

* Fri Feb 11 2022 Stanislav Levin <slev@altlinux.org> 1.3.1-alt1
- Initial build for Sisyphus.
