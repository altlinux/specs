%define pypi_name sphinx_design
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 0.7.0
Release: alt1
Summary: A sphinx extension for designing beautiful, view size responsive web components
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/sphinx_design
Vcs: https://github.com/executablebooks/sphinx-design
BuildArch: noarch
Source0: %name-%version.tar
# mapping from PyPI name
# https://www.altlinux.org/Management_of_Python_dependencies_sources#Mapping_project_names_to_distro_names
Provides: python3-module-%{pep503_name %pypi_name} = %EVR
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-flit-core
%if_with check
BuildRequires: python3-module-defusedxml
BuildRequires: python3-module-myst-parser
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-cov
BuildRequires: python3-module-pytest-regressions
BuildRequires: python3-module-sphinx
# tests/conftest.py
BuildRequires: python3-module-sphinx-tests
%endif

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -ra

%files
%doc *.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Thu Feb 05 2026 Grigory Ustinov <grenka@altlinux.org> 0.7.0-alt1
- Automatically updated to 0.7.0.

* Mon May 27 2024 Stanislav Levin <slev@altlinux.org> 0.6.0-alt2
- Mapped PyPI name to distro's one.

* Mon May 27 2024 Stanislav Levin <slev@altlinux.org> 0.6.0-alt1
- 0.2.0 -> 0.6.0.

* Thu Nov 10 2022 Stanislav Levin <slev@altlinux.org> 0.2.0-alt2
- Fixed FTBFS (flit_core 3.7.1).

* Wed Jun 15 2022 Fr. Br. George <george@altlinux.org> 0.2.0-alt1
- Autobuild version bump to 0.2.0

* Wed Jun 15 2022 Fr. Br. George <george@altlinux.org> 0.0.1-alt1
- Initial version for ALT
