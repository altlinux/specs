%define _unpackaged_files_terminate_build 1
%define pypi_name migate

Name: python3-module-%pypi_name
Version: 1.1.8
Release: alt1

Summary: migate is a simplified Xiaomi authentication gateway for Python projects
License: MIT
Group: Development/Python3

URL: https://github.com/offici5l/migate
VCS: https://github.com/offici5l/migate
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: %python3_setup_buildrequires

BuildArch: noarch

%description
%summary.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir_noarch/%pypi_name
%python3_sitelibdir_noarch/%pypi_name-%version.dist-info
%doc README.md

%changelog
* Fri Jul 10 2026 David Sultaniiazov <x1z53@altlinux.org> 1.1.8-alt1
- Initial build.
