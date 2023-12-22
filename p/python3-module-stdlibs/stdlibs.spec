%define _unpackaged_files_terminate_build 1
%define pypi_name stdlibs

%def_with check

Name: python3-module-%pypi_name
Version: 2023.12.15
Release: alt1
Summary: List of packages in the stdlib
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/stdlibs
Vcs: https://github.com/omnilib/stdlibs
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
# not packaged in sisyphus, upstream uses attribution to generate __version__.py
%add_pyproject_deps_check_filter attribution
%pyproject_builddeps_metadata_extra dev
%endif

%description
Simple list of top-level packages in Python's stdlib.

Note: If you only need the live module names on 3.10+, just use
sys.stdlib_module_names. This is not exactly a backport, but a static list of
those for most useful Python versions.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

# don't package tests
rm -r %buildroot%python3_sitelibdir/%pypi_name/tests/

%check
%pyproject_run -- python -m %pypi_name.tests -v

%files
%doc README.md
%python3_sitelibdir/stdlibs/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Dec 21 2023 Stanislav Levin <slev@altlinux.org> 2023.12.15-alt1
- 2023.11.2 -> 2023.12.15.

* Thu Nov 09 2023 Stanislav Levin <slev@altlinux.org> 2023.11.2-alt1
- 2022.10.9 -> 2023.11.2.

* Tue Oct 11 2022 Stanislav Levin <slev@altlinux.org> 2022.10.9-alt1
- 2022.6.8 -> 2022.10.9.

* Thu Sep 15 2022 Stanislav Levin <slev@altlinux.org> 2022.6.8-alt1
- 2022.3.16 -> 2022.6.8.

* Fri Apr 01 2022 Stanislav Levin <slev@altlinux.org> 2022.3.16-alt1
- 2022.2.2 -> 2022.3.16.

* Fri Feb 11 2022 Stanislav Levin <slev@altlinux.org> 2022.2.2-alt1
- Initial build for Sisyphus.
