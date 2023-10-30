%define pypi_name mkdocs-gen-files
%define mod_name mkdocs_gen_files

%def_with check

Name:    python3-module-%pypi_name
Version: 0.5.0
Release: alt1

Summary: MkDocs plugin to programmatically generate documentation pages during the build
License: MIT
Group:   Development/Python3
URL:     https://github.com/oprypin/mkdocs-gen-files

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel
BuildRequires: python3-module-hatchling

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-mkdocs
BuildRequires: python3-module-pytest-golden
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
* Wed Oct 25 2023 Alexander Burmatov <thatman@altlinux.org> 0.5.0-alt1
- Initial build for Sisyphus.
