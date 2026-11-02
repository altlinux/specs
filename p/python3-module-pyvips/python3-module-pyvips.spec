%define pypi_name pyvips

%def_with check

Name:    python3-module-%pypi_name
Version: 3.2.0
Release: alt1

Summary: Python binding for libvips using cffi
License: MIT
Group:   Development/Python3
URL:     https://github.com/libvips/pyvips

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-cffi
BuildRequires: libvips42
%endif

%add_python3_req_skip vdecls

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
%doc *.rst
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Fri Oct 30 2026 Alexander Burmatov <thatman@altlinux.org> 3.2.0-alt1
- Initial build for Sisyphus.
