%define pypi_name mkdocs-redirects
%define mod_name mkdocs_redirects

%def_with check

Name:    python3-module-%pypi_name
Version: 1.2.1
Release: alt1

Summary: Open source plugin for Mkdocs page redirects
License: MIT
Group:   Development/Python3
URL:     https://github.com/mkdocs/mkdocs-redirects

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
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
* Thu Oct 26 2023 Alexander Burmatov <thatman@altlinux.org> 1.2.1-alt1
- Initial build for Sisyphus.
