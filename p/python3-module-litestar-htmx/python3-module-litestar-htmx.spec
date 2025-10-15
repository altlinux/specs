%define pypi_name litestar-htmx
%define mod_name litestar_htmx

%def_with check

Name:    python3-module-%pypi_name
Version: 0.5.0
Release: alt1

Summary: Litestar plugin for HTMX
License: MIT
Group:   Development/Python3
URL:     https://github.com/litestar-org/litestar-htmx

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel
BuildRequires: python3-module-hatchling

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-litestar
BuildRequires: python3-module-jinja2
BuildRequires: python3-module-mako
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
* Wed Oct 15 2025 Alexander Burmatov <thatman@altlinux.org> 0.5.0-alt1
- New 0.5.0 version.

* Fri Jun 06 2025 Alexander Burmatov <thatman@altlinux.org> 0.4.1-alt2
- Fix build.

* Wed May 28 2025 Alexander Burmatov <thatman@altlinux.org> 0.4.1-alt1
- Initial build for Sisyphus.
