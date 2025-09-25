%define pypi_name orderly-set
%define mod_name orderly_set

%def_with check

Name:    python3-module-%pypi_name
Version: 5.5.0
Release: alt1

Summary: Orderly Set previously known as Ordered Set
License: MIT
Group:   Development/Python3
URL:     https://github.com/seperman/orderly-set

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel
BuildRequires: python3-module-flit-core

%if_with check
BuildRequires: python3-module-pytest
%endif

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
Orderly Set is a package containing multiple implementations of Ordered Set.

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
* Thu Sep 25 2025 Alexander Burmatov <thatman@altlinux.org> 5.5.0-alt1
- Initial build for Sisyphus.
