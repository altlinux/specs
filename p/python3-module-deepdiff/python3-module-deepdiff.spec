%define pypi_name deepdiff

%def_with check

Name:    python3-module-%pypi_name
Version: 6.6.0
Release: alt1

Summary: Deep Difference and search of any Python object/data
License: MIT
Group:   Development/Python3
URL:     https://github.com/seperman/deepdiff

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-cov
BuildRequires: python3-module-numpy
BuildRequires: python3-module-ordered-set
BuildRequires: python3-module-click
BuildRequires: python3-module-yaml
BuildRequires: python3-module-numpy-testing
BuildRequires: python3-module-tomli_w
BuildRequires: python3-module-dateutil
BuildRequires: python3-module-jsonpickle
BuildRequires: python3-module-pydantic
%endif

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
DeepDiff: Deep Difference and search of any Python object/data.
DeepHash: Hash of any object based on its contents.
Delta: Use deltas to reconstruct objects by adding deltas together.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest --cov=deepdiff --cov-report term-missing

%files
%doc *.md
%_bindir/deep
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Mon Nov 13 2023 Alexander Burmatov <thatman@altlinux.org> 6.6.0-alt1
- Initial build for Sisyphus.
