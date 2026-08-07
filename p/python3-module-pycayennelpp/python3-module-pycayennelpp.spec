%define _unpackaged_files_terminate_build 1
%define pypi_name pycayennelpp
%define mod_name cayennelpp

%def_with check

Name: python3-module-%pypi_name
Version: 2.4.0
Release: alt1
Summary: A Cayenne Low Power Payload (CayenneLPP) decoder and encoder for Python
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pycayennelpp
VCS: https://github.com/smlng/pycayennelpp.git

BuildArch: noarch

Source: %name-%version.tar

# PyPI wellknown name
%py3_provides %pypi_name

BuildRequires(pre): rpm-macros-python3
BuildRequires: rpm-build-python3
BuildRequires: python3(setuptools)

%if_with check
BuildRequires: python3(pytest)
%endif

%description
%summary.

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%doc README.*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Aug 05 2026 Vasiliy Doylov <neko@altlinux.org> 2.4.0-alt1
- Initial build for ALT.
