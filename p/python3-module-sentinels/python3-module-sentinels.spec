%define pypi_name sentinels

Name:    python3-module-%pypi_name
Version: 1.0.0
Release: alt1

Summary: Various objects to denote special meanings in python
License: BSD
Group:   Development/Python3
URL:     https://pypi.org/project/sentinels

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
%summary

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%files
%doc *.rst
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Mon Apr 28 2025 Alexander Burmatov <thatman@altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus.
