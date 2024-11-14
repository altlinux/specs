%define pypi_name mkdocs-static-i18n
%define mod_name mkdocs_static_i18n

%def_with check

Name:    python3-module-%pypi_name
Version: 1.2.3
Release: alt1

Summary: MkDocs i18n plugin using static translation markdown files
License: MIT
Group:   Development/Python3
URL:     https://github.com/ultrabug/mkdocs-static-i18n

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel
BuildRequires: python3-module-hatchling

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-mkdocs
BuildRequires: python3-module-mkdocs-material
%endif

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
The MkDocs plugin that helps you support multiple language versions of your site
or documentation.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc *.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Mon Nov 11 2024 Alexander Burmatov <thatman@altlinux.org> 1.2.3-alt1
- Initial build for Sisyphus.
