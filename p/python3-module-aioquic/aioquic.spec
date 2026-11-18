%define _unpackaged_files_terminate_build 1
%define pypi_name aioquic

%def_with check

Name: python3-module-%pypi_name
Version: 1.8.0
Release: alt1

Summary: QUIC and HTTP/3 implementation in Python
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/aioquic
Vcs: https://github.com/aiortc/aioquic

Source0: %name-%version.tar
Patch: %name-%version-alt.patch

# Upstream builds the extension against the Python 3.11 Limited API.
%pyproject_configure_with_limited_api 3.11
BuildRequires(pre): rpm-macros-pyproject >= 0.3.0
BuildRequires: rpm-build-pyproject
BuildRequires: libssl-devel
# The tests use only unittest; requirements/test.txt lists only coverage.
%pyproject_configure_without_autodiscovery
%pyproject_configure_pypi_package

%description
Aioquic is a library for the QUIC network protocol in Python. It features
a minimal TLS 1.3 implementation, a QUIC stack and an HTTP/3 stack.
QUIC was standardised in RFC 9000 and HTTP/3 in RFC 9114. aioquic is
regularly tested for interoperability against other QUIC implementations.

%prep
%setup
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
* Wed Nov 18 2026 Alexandr Shashkin <dutyrok@altlinux.org> 1.8.0-alt1
- Updated to 1.8.0.

* Fri Nov 06 2026 Alexandr Shashkin <dutyrok@altlinux.org> 1.7.2-alt1
- Updated to 1.7.2.

* Wed Oct 28 2026 Alexandr Shashkin <dutyrok@altlinux.org> 1.7.0-alt1
- Updated to 1.7.0.

* Tue Nov 11 2025 Alexandr Shashkin <dutyrok@altlinux.org> 1.3.0-alt1
- Updated to 1.3.0.

* Mon Aug 05 2024 Alexandr Shashkin <dutyrok@altlinux.org> 1.2.0-alt1
- Updated to 1.2.0.

* Fri Jun 28 2024 Alexandr Shashkin <dutyrok@altlinux.org> 1.1.0-alt1
- 1.0.0 -> 1.1.0.

* Wed Apr 03 2024 Alexandr Shashkin <dutyrok@altlinux.org> 1.0.0-alt1
- 0.9.25 -> 1.0.0.

* Mon Feb 12 2024 Alexandr Shashkin <dutyrok@altlinux.org> 0.9.25-alt2
- Fixed FTBFS: adapt test for service-identitity >= 24.

* Tue Jan 09 2024 Alexandr Shashkin <dutyrok@altlinux.org> 0.9.25-alt1
- 0.9.21 -> 0.9.25

* Tue Nov 07 2023 Alexandr Shashkin <dutyrok@altlinux.org> 0.9.21-alt1
- Initial build for ALT Sisyphus

