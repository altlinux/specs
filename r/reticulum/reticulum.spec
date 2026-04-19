%define _unpackaged_files_terminate_build 1
%define pypi_name rns
%def_without check

Name: reticulum
Version: 1.1.5
Release: alt1

Summary: The cryptography-based networking stack for building unstoppable networks with LoRa, Packet Radio, WiFi and everything in between
License: Reticulum
Group: Development/Python3
Url: https://reticulum.network/
Vcs: https://github.com/markqvist/Reticulum

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%package -n python3-module-%pypi_name
Summary: Python module for reticulum
Group: Development/Python3
BuildArch: noarch
Requires: %name = %EVR

%description
Reticulum is the cryptography-based networking stack for building local and
wide-area networks with readily available hardware. It can operate even with
very high latency and extremely low bandwidth. Reticulum allows you to build
wide-area networks with off-the-shelf tools, and offers end-to-end encryption
and connectivity, initiator anonymity, autoconfiguring cryptographically backed
multi-hop transport, efficient addressing, unforgeable delivery acknowledgements
and more.

%description -n python3-module-%pypi_name
Python module for reticulum.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run -- python3 -m tests.all

%files
%doc Changelog.md README.md
%_bindir/rncp
%_bindir/rnid
%_bindir/rnir
%_bindir/rnodeconf
%_bindir/rnpath
%_bindir/rnprobe
%_bindir/rnsd
%_bindir/rnstatus
%_bindir/rnx
%_bindir/rnpkg

%files -n python3-module-%pypi_name
%python3_sitelibdir/CRNS
%python3_sitelibdir/RNS
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}
%doc LICENSE

%changelog
* Fri Apr 17 2026 Artem Krasovskiy <aibure@altlinux.org> 1.1.5-alt1
- Updated to 1.1.5.

* Tue Mar 17 2026 Artem Krasovskiy <aibure@altlinux.org> 1.1.4-alt1
- Updated to 1.1.4.

* Wed Feb 04 2026 Artem Krasovskiy <aibure@altlinux.org> 1.1.3-alt1
- Updated to 1.1.3.

* Tue Jan 13 2026 Artem Krasovskiy <aibure@altlinux.org> 1.1.2-alt1
- Initial build for Sisyphus.
