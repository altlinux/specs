%define pypi_name tdir

%def_with check

Name:    python3-module-%pypi_name
Version: 1.8.2
Release: alt1

Summary: Create, fill a temporary directory
License: MIT
Group:   Development/Python3
URL:     https://github.com/rec/tdir

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel
BuildRequires: python3-module-poetry

%if_with check
BuildRequires: python3-module-dek
%endif

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
Run code inside a temporary directory filled with zero or more files.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_unittest

%files
%doc *.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Fri Aug 09 2024 Alexander Burmatov <thatman@altlinux.org> 1.8.2-alt1
- Initial build for Sisyphus.
