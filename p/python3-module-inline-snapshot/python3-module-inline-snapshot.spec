%define pypi_name inline-snapshot
%define mod_name inline_snapshot

%def_with check

Name:    python3-module-%pypi_name
Version: 0.17.1
Release: alt1

Summary: Create and update inline snapshots in your python tests
License: MIT
Group:   Development/Python3
URL:     https://github.com/15r10nk/inline-snapshot

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel
BuildRequires: python3-module-hatchling

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-executing
BuildRequires: python3-module-asttokens
BuildRequires: python3-module-black
BuildRequires: python3-module-rich
BuildRequires: python3-module-hypothesis
BuildRequires: python3-module-pydantic
BuildRequires: python3-module-pytest-subtests
BuildRequires: python3-module-dirty-equals
BuildRequires: python3-module-mypy
BuildRequires: python3-module-pytest-freezer
BuildRequires: python3-module-pytest-xdist
BuildRequires: python3-module-pytest-mock
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
%pyproject_run_pytest -k "not pyright"

%files
%doc *.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Thu Dec 19 2024 Alexander Burmatov <thatman@altlinux.org> 0.17.1-alt1
- New version 0.17.1.

* Wed Jul 17 2024 Alexander Burmatov <thatman@altlinux.org> 0.11.0-alt1
- Initial build for Sisyphus.
