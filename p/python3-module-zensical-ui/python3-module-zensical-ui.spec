%define pypi_name zensical-ui
%define mod_name zensical_ui

Name:    python3-module-%pypi_name
Version: 0.0.42
Release: alt1

Summary: User interface for zensical
License: MIT
Group:   Development/Python3
URL:     https://github.com/zensical/ui

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel
BuildRequires: python3-module-hatchling

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
Templates for Zensical.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%files
%doc *.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Thu Nov 12 2026 Alexander Burmatov <thatman@altlinux.org> 0.0.42-alt1
- Initial build for Sisyphus.
