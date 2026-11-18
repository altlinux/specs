%define _unpackaged_files_terminate_build 1
%ifarch %e2k
%def_with legacy_unix_peer
%else
%def_without legacy_unix_peer
%endif

Name: altera
Version: 1.2.0
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
Source4: %name-web.service
Source5: %name-sessions.service

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
frontend applications over persistent Unix connections. Altera authorizes
privileged operations for unprivileged users through Polkit policies.
Web access is provided by the separate altera-web and altera-sessions packages.

%package cli
Summary: Command-line client for Altera
Group: System/Configuration/Other
Requires: %name = %EVR

%description cli
Command-line client that exchanges JSON Lines with the Altera Unix server.

%package sessions
Summary: Authentication and user sessions for Altera web access
Group: System/Configuration/Other
Requires: %name-cli = %EVR

%description sessions
Privileged service that authenticates users through PAM, manages Bearer
sessions and starts altera-cli with the authenticated user's UID and GID.

%package web
Summary: HTTP and WebSocket web server for Altera
Group: System/Configuration/Other
Requires: %name-sessions = %EVR

%description web
Unprivileged HTTP and WebSocket web server for Altera. Authentication and
user processes are handled by the altera-sessions service.

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
%rust_install -- %name %name-cli %name-web %name-sessions
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
install -pD -m0644 %SOURCE4 %buildroot%_unitdir/%name-web.service
install -pD -m0644 %SOURCE5 %buildroot%_unitdir/%name-sessions.service
# install PAM configuration
install -pD -m0644 %SOURCE3 \
	%buildroot%_sysconfdir/pam.d/%name

%check
%rust_test %{?_with_legacy_unix_peer:--features legacy-unix-peer}

%post -n %name
%post_service %name

%preun -n %name
%preun_service %name

%pre sessions
groupadd -r -f %name > /dev/null 2>&1 ||:
useradd -r -g %name -d %_localstatedir/%name -M -s /dev/null -c "Altera web server" %name > /dev/null 2>&1 ||:

%post sessions
%post_service %name-sessions

%preun sessions
%preun_service %name-sessions

%post web
%post_service %name-web

%preun web
%preun_service %name-web

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
%_unitdir/%name.service

%files cli
%_bindir/%name-cli

%files sessions
%_bindir/%name-sessions
%_unitdir/%name-sessions.service
%config(noreplace) %_sysconfdir/pam.d/%name

%files web
%_bindir/%name-web
%_unitdir/%name-web.service

%changelog
* Tue Nov 17 2026 Artyom Sinyugin <writers@altlinux.org> 1.2.0-alt1
- Use JSON Lines for IPC insteed of WebSocket protocol
- Split CLI, web frontend and session service into separate packages
- Create unprivileged service user for altera web service
- Fix web backdoors
- Unify Altera errors with Alterator exception classes
- MD Book for documentation in repo

* Tue Nov 03 2026 Artyom Sinyugin <writers@altlinux.org> 1.1.0-alt1
- Switch JWT to Opaque Token for auth
- Add /auth/logout path
- Extend debug logging with messages for backend modules
- Fix sources scripts for vendor and e2k vendor

* Sun Nov 01 2026 Artyom Sinyugin <writers@altlinux.org> 1.0.0-alt1
- Initial build.
