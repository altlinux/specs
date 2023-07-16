%define _unpackaged_files_terminate_build 1
%define pypi_name jsonschema-spec

%def_with check

Name: python3-module-%pypi_name
Version: 0.2.3
Release: alt1

Summary: JSONSchema Spec with object-oriented paths
License: Apache-2.0
Group: Development/Python3
# Source-git: https://github.com/p1c2u/jsonschema-spec.git
Url: https://pypi.org/project/jsonschema-spec

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

# build backend and its deps
BuildRequires: python3(poetry-core)

%if_with check
# deps
BuildRequires: python3(pathable)
BuildRequires: python3(yaml)
BuildRequires: python3(jsonschema)
BuildRequires: python3(referencing)
BuildRequires: python3(responses)

BuildRequires: python3(pytest)
%endif

BuildArch: noarch

%py3_provides %pypi_name

%description
JSONSchema Spec with object-oriented paths.

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_create_default_config
%tox_check_pyproject

%files
%doc README.rst
%python3_sitelibdir/jsonschema_spec/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Jul 12 2023 Anton Vyatkin <toni@altlinux.org> 0.2.3-alt1
- New version 0.2.3.

* Fri Sep 30 2022 Stanislav Levin <slev@altlinux.org> 0.1.2-alt1
- Initial build for Sisyphus.
