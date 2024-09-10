%define _unpackaged_files_terminate_build 1
%define pypi_name importlib-resources

%def_with check

Name: python3-module-%pypi_name
Version: 6.4.5
Release: alt1
Summary: Read resources from Python packages
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/importlib-resources
VCS: https://github.com/python/importlib_resources.git
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
Provides: python3-module-importlib_resources = %EVR
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata_extra test
# internal Python tests
BuildRequires: python3-test
%endif

%description
%pypi_name is a backport of Python standard library importlib.resources
module for older Pythons.

The key goal of this module is to replace parts of pkg_resources with a solution
in Python's stdlib that relies on well-defined APIs. This makes reading
resources included in packages easier, with more stable and consistent
semantics.

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

# don't ship tests
rm -r %buildroot%python3_sitelibdir/importlib_resources/tests/

%check
%pyproject_run_pytest -vra

%files
%doc README.rst
%python3_sitelibdir/importlib_resources/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Sep 10 2024 Stanislav Levin <slev@altlinux.org> 6.4.5-alt1
- 6.4.0 -> 6.4.5.

* Fri Mar 22 2024 Stanislav Levin <slev@altlinux.org> 6.4.0-alt1
- 6.3.2 -> 6.4.0.

* Wed Mar 20 2024 Stanislav Levin <slev@altlinux.org> 6.3.2-alt1
- 6.3.1 -> 6.3.2.

* Mon Mar 18 2024 Stanislav Levin <slev@altlinux.org> 6.3.1-alt1
- 6.3.0 -> 6.3.1.

* Wed Mar 13 2024 Stanislav Levin <slev@altlinux.org> 6.3.0-alt1
- 6.1.3 -> 6.3.0.

* Mon Mar 11 2024 Stanislav Levin <slev@altlinux.org> 6.1.3-alt1
- 6.1.2 -> 6.1.3.

* Mon Feb 26 2024 Stanislav Levin <slev@altlinux.org> 6.1.2-alt1
- 6.1.1 -> 6.1.2.

* Tue Nov 07 2023 Stanislav Levin <slev@altlinux.org> 6.1.1-alt1
- 6.1.0 -> 6.1.1.

* Wed Sep 27 2023 Stanislav Levin <slev@altlinux.org> 6.1.0-alt1
- 6.0.1 -> 6.1.0.

* Mon Aug 07 2023 Stanislav Levin <slev@altlinux.org> 6.0.1-alt1
- 6.0.0 -> 6.0.1.

* Wed Jul 19 2023 Stanislav Levin <slev@altlinux.org> 6.0.0-alt1
- 5.12.0 -> 6.0.0.

* Tue Feb 21 2023 Stanislav Levin <slev@altlinux.org> 5.12.0-alt1
- 5.10.2 -> 5.12.0.

* Fri Jan 27 2023 Stanislav Levin <slev@altlinux.org> 5.10.2-alt1
- 5.10.1 -> 5.10.2.

* Wed Dec 07 2022 Stanislav Levin <slev@altlinux.org> 5.10.1-alt1
- 5.10.0 -> 5.10.1.

* Mon Oct 10 2022 Stanislav Levin <slev@altlinux.org> 5.10.0-alt1
- 5.9.0 -> 5.10.0.

* Fri Sep 30 2022 Stanislav Levin <slev@altlinux.org> 5.9.0-alt1
- Restored back for Sisyphus.
