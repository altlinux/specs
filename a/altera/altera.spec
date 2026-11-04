%define _unpackaged_files_terminate_build 1
%ifarch %e2k
%def_with legacy_unix_peer
%else
%def_without legacy_unix_peer
%endif

Name: altera
Version: 1.1.0
Release: alt1

Summary: Altera is a spiritual successor to Alterator written in Rust
License: GPLv2+
Group: System/Configuration/Other
Url: https://altlinux.space/writers/altera.git
Vcs: https://altlinux.space/writers/altera.git
Packager: Artyom Sinyugin <writers@altlinux.org>

Source: %name-%version.tar
%ifarch %e2k
Source1: e2k-%version.tar
%else
Source1: vendor-%version.tar
%endif
Source2: %name.service
Source3: %name

BuildRequires(pre): rpm-build-rust
BuildRequires(pre): rpm-build-python3
BuildRequires: libpam0-devel

Requires: alterator-sh-functions
Requires: %name-sh-functions
Requires: dbus polkit
Requires: %name-common = %EVR

# Conflicts: alterator

%description
%summary.

It is designed as a bridge between backend3 or backend4 modules and modern
frontend applications over persistent connections. Remote control is
available via WebSocket. Altera can also authorize privileged operations
for unprivileged users through predefined Polkit policies.

%package common
Summary: Common package for %name
Group: System/Configuration/Other
Requires: jq

%description common
Altera is a modern replacement for ALT Linux Alterator, written in Rust.

This package contains the common directories for %name.

%package sh-functions
Summary: Shell helper functions for altera backend4 modules
Group: Development/Other
BuildArch: noarch

%description sh-functions
%summary.

%package python-functions
Summary: Python helper functions for altera backend4 modules
Group: Development/Python3
BuildArch: noarch

%description python-functions
%summary.

%prep
%setup -a 1
%rust_prep

%ifarch %e2k
bash e2k_revendor.sh
%endif

%build
%rust_build %{?_with_legacy_unix_peer:--features legacy-unix-peer}

%install
%rust_install -- %name %name-cli
# install directories
install -d \
	%buildroot%_sysconfdir/alterator/{authz/{backend3,backend4,backend5},altera/tls} \
	%buildroot%_libexecdir/alterator/{backend3,backend4,backend5}
# install shell helper for backend4 modules
install -pD -m0644 altera-sh-functions \
	%buildroot%_bindir/altera-sh-functions
# install python helper for backend4 modules
install -pD -m0644 altera_python_functions.py \
	%buildroot%python3_sitelibdir_noarch/altera_python_functions.py
# basic systemd service
install -pD -m0644 %SOURCE2 %buildroot%_unitdir/%name.service
# install PAM configuration
install -pD -m0644 %SOURCE3 \
	%buildroot%_sysconfdir/pam.d/%name

%check
%rust_test %{?_with_legacy_unix_peer:--features legacy-unix-peer}

%post -n %name
%post_service %name

%preun -n %name
%preun_service %name

%files common
# %dir %_sysconfdir/alterator
%dir %_sysconfdir/alterator/authz
%dir %_sysconfdir/alterator/authz/backend3
%dir %_sysconfdir/alterator/authz/backend4
%dir %_sysconfdir/alterator/authz/backend5
%dir %_sysconfdir/alterator/altera
%dir %_sysconfdir/alterator/altera/tls
# %dir %_libexecdir/alterator
%dir %_libexecdir/alterator/backend3
%dir %_libexecdir/alterator/backend4
%dir %_libexecdir/alterator/backend5

%files sh-functions
%_bindir/%name-sh-functions

%files python-functions
%python3_sitelibdir_noarch/altera_python_functions.py
%python3_sitelibdir_noarch/__pycache__/altera_python_functions.*.pyc

%files
%doc README.MD docs/ examples/
%_bindir/%name
%_bindir/%name-cli
%_unitdir/%name.service
%config %_sysconfdir/pam.d/%name

%changelog
* Tue Nov 03 2026 Artyom Sinyugin <writers@altlinux.org> 1.1.0-alt1
- Switch JWT to Opaque Token for auth
- Add /auth/logout path
- Extend debug logging with messages for backend modules
- Fix sources scripts for vendor and e2k vendor

* Sun Nov 01 2026 Artyom Sinyugin <writers@altlinux.org> 1.0.0-alt1
- Initial build.
