%define pypi_name jsonschema-path
%define mod_name jsonschema_path

%def_with check

Name: python3-module-%pypi_name
Version: 0.3.3
Release: alt1

Summary: Object-oriented JSONSchema
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/jsonschema-path
Vcs: https://github.com/p1c2u/jsonschema-path
BuildArch: noarch
Source: %name-%version.tar

# PEP503 name
%py3_provides %pypi_name

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-poetry-core
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pathable
BuildRequires: python3-module-yaml
BuildRequires: python3-module-responses
BuildRequires: python3-module-referencing
%endif

%description
%summary.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
sed -i '/--cov/d' pyproject.toml
%pyproject_run_pytest -v

%files
%doc README.*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Jun 26 2024 Anton Vyatkin <toni@altlinux.org> 0.3.3-alt1
- New version 0.3.3.

* Thu Nov 16 2023 Anton Vyatkin <toni@altlinux.org> 0.3.2-alt1
- New version 0.3.2.

* Thu Nov 02 2023 Anton Vyatkin <toni@altlinux.org> 0.3.1-alt2
- Fix FTBFS.

* Sat Oct 14 2023 Anton Vyatkin <toni@altlinux.org> 0.3.1-alt1
- Initial build for Sisyphus
