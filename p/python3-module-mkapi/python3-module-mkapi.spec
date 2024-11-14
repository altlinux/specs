%define pypi_name mkapi

%def_with check

Name:    python3-module-%pypi_name
Version: 3.0.22
Release: alt1

Summary: A plugin for MkDocs to generate API documentation
License: MIT
Group:   Development/Python3
URL:     https://github.com/daizutabi/mkapi

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel
BuildRequires: python3-module-hatchling

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-cov
BuildRequires: python3-module-jinja2
BuildRequires: python3-module-mkdocs
BuildRequires: python3-module-mkdocs-material
BuildRequires: python3-module-rich
BuildRequires: python3-module-pytest-xdist
BuildRequires: python3-module-pytest-randomly
%endif

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
MkAPI is a plugin for MkDocs, designed to facilitate the generation of API
documentation for Python projects. MkAPI streamlines the documentation process
by automatically extracting docstrings and organizing them into a structured
format, making it easier for developers to maintain and share their API
documentation.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -k "not test_mkdocs_config"

%files
%doc *.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Mon Nov 11 2024 Alexander Burmatov <thatman@altlinux.org> 3.0.22-alt1
- Initial build for Sisyphus.
