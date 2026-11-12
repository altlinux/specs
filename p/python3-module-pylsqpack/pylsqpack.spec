%define _unpackaged_files_terminate_build 1
%define pypi_name pylsqpack

%def_with check

Name: python3-module-%pypi_name
Version: 1.1.0
Release: alt1

Summary: Python bindings for ls-qpack
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/pylsqpack
Vcs: https://github.com/aiortc/pylsqpack

Source0: %name-%version.tar
Source1: submodules.tar
Patch: %name-%version-alt.patch

# Upstream builds the extension against the Python 3.11 Limited API.
%pyproject_configure_with_limited_api 3.11
BuildRequires(pre): rpm-macros-pyproject >= 0.3.0
BuildRequires: rpm-build-pyproject
# The tests use only unittest, upstream declares no test dependencies.
%pyproject_configure_without_autodiscovery
%pyproject_configure_pypi_package

%description
Pylsqpack is a wrapper around the ls-qpack library. It provides Python
Decoder and Encoder objects to read or write HTTP/3 headers compressed
with QPACK.

%prep
%setup -a1
%autopatch -p1
%pyproject_setup_deps

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_unittest

%files
%doc README.* LICENSE
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Thu Nov 12 2026 Alexandr Shashkin <dutyrok@altlinux.org> 1.1.0-alt1
- Updated to 1.1.0.

* Wed Oct 28 2026 Alexandr Shashkin <dutyrok@altlinux.org> 1.0.0-alt1
- Updated to 1.0.0.

* Tue Mar 31 2026 Alexandr Shashkin <dutyrok@altlinux.org> 0.3.24-alt1
- Updated to 0.3.24.

* Wed Dec 03 2025 Alexandr Shashkin <dutyrok@altlinux.org> 0.3.23-alt1
- Updated to 0.3.23.

* Sat Jun 21 2025 Alexandr Shashkin <dutyrok@altlinux.org> 0.3.22-alt1
- Updated to 0.3.22.

* Sun Apr 27 2025 Alexandr Shashkin <dutyrok@altlinux.org> 0.3.20-alt1
- Updated to 0.3.20.

* Mon Feb 03 2025 Alexandr Shashkin <dutyrok@altlinux.org> 0.3.19-alt1
- Updated to 0.3.19.

* Wed Feb 14 2024 Alexandr Shashkin <dutyrok@altlinux.org> 0.3.18-alt1
- 0.3.17 -> 0.3.18

* Tue Nov 07 2023 Alexandr Shashkin <dutyrok@altlinux.org> 0.3.17-alt1
- Initial build for ALT Sisyphus

