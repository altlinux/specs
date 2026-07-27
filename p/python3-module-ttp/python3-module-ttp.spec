%define pypi_name ttp

%def_with check

Name:    python3-module-%pypi_name
Version: 0.10.1
Release: alt1

Summary: Template Text Parser
License: MIT
Group:   Development/Python3
URL:     https://github.com/dmulyalin/ttp

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-poetry

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-openpyxl
BuildRequires: python3-module-tabulate
BuildRequires: python3-module-ttp_templates
BuildRequires: python3-module-jinja2
BuildRequires: python3-module-yaml
BuildRequires: python3-module-deepdiff
BuildRequires: python3-module-cerberus
%endif

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
TTP is a Python library for semi-structured text parsing using templates.

%prep
%setup -n %pypi_name-%version
sed -i 's/version = "0.10.0"/version = "%version"/' pyproject.toml

%build
%pyproject_build

%install
%pyproject_install

%check
pushd test/pytest
python3 -m pytest . -k 'not (yangson or test_inputs or test_adding_data_from_files)'
popd

%files
%doc *.md
%_bindir/%pypi_name
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Fri Jul 24 2026 Alexander Burmatov <thatman@altlinux.org> 0.10.1-alt1
- New 0.10.1 version.

* Wed Nov 15 2023 Alexander Burmatov <thatman@altlinux.org> 0.9.5-alt2
- Enable check.

* Tue Nov 14 2023 Alexander Burmatov <thatman@altlinux.org> 0.9.5-alt1
- Initial build for Sisyphus.
