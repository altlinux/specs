%define _unpackaged_files_terminate_build 1
%define pypi_name aioquic

%def_with check

Name: python3-module-%pypi_name
Version: 1.1.0
Release: alt1

Summary: QUIC and HTTP/3 implementation in Python
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/aioquic
Vcs: https://github.com/aiortc/aioquic

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
BuildRequires: libssl-devel
%pyproject_builddeps_build

%if_with check
%pyproject_builddeps_metadata
%endif

%description
Aioquic is a library for the QUIC network protocol in Python. It features
a minimal TLS 1.3 implementation, a QUIC stack and an HTTP/3 stack.
QUIC was standardised in RFC 9000 and HTTP/3 in RFC 9114. aioquic is
regularly tested for interoperability against other QUIC implementations.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_unittest

%files
%doc README.*
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
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

