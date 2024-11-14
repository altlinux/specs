%define pypi_name mkdocs-test
%define mod_name mkdocs_test

%def_with check

Name:    python3-module-%pypi_name
Version: 0.5.3
Release: alt1

Summary: A framework for testing MkDocs projects
License: MIT
Group:   Development/Python3
URL:     https://github.com/fralau/mkdocs-test

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pyaml
BuildRequires: python3-module-beautifulsoup4
BuildRequires: python3-module-super-collections
BuildRequires: python3-module-markdown
BuildRequires: python3-module-pandas
BuildRequires: python3-module-rich
BuildRequires: python3-module-mkdocs
%endif

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
%summary.

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
* Mon Nov 11 2024 Alexander Burmatov <thatman@altlinux.org> 0.5.3-alt1
- Initial build for Sisyphus.
