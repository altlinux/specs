%define _unpackaged_files_terminate_build 1
%define pypi_name jsonschema-spec

%def_with check

Name: python3-module-%pypi_name
Version: 0.2.4
Release: alt1
Summary: JSONSchema Spec with object-oriented paths
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/jsonschema-spec
Vcs: https://github.com/p1c2u/jsonschema-spec.git
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
%py3_provides %pypi_name
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
# not packaged yet
%add_pyproject_deps_check_filter deptry
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
JSONSchema Spec with object-oriented paths.

%prep
%setup
%autopatch -p1
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
%pyproject_run_pytest -ra -o=addopts=''

%files
%doc README.rst
%python3_sitelibdir/jsonschema_spec/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Thu Aug 17 2023 Stanislav Levin <slev@altlinux.org> 0.2.4-alt1
- 0.2.3 -> 0.2.4.

* Thu Jul 20 2023 Anton Vyatkin <toni@altlinux.org> 0.2.3-alt2
- Fix FTBFS (migrate from tox to pyproject_installer).

* Wed Jul 12 2023 Anton Vyatkin <toni@altlinux.org> 0.2.3-alt1
- New version 0.2.3.

* Fri Sep 30 2022 Stanislav Levin <slev@altlinux.org> 0.1.2-alt1
- Initial build for Sisyphus.
