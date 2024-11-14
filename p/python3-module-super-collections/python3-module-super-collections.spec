%define pypi_name super-collections
%define mod_name super_collections

%def_with check

Name:    python3-module-%pypi_name
Version: 0.5.3
Release: alt1

Summary: Python SuperDictionaries (with attributes) and SuperLists
License: MIT
Group:   Development/Python3
URL:     https://github.com/fralau/super-collections

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-hjson
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
