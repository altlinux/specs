%global _unpackaged_files_terminate_build 1
%global import_path github.com/henrygd/beszel
%define hub_service %name-hub.service
%define agent_service %name-agent.service
%define hub_conf %name-hub.conf
%define agent_conf %name-agent.conf

%define _beszel_user _beszel
%define _beszel_group _beszel
%define _beszel_home %_localstatedir/beszel

#Disabling tests due to the need to use the network,
#but it is not available in the build environment.
%def_without check

Name: beszel
Version: 0.18.7
Release: alt1
Summary: Lightweight server monitoring hub
License: MIT
Group: System/Configuration/Networking
Url: https://beszel.dev/
Vcs: https://github.com/henrygd/beszel

ExclusiveArch: %go_arches

Source0: %name-%version.tar
Source1: vendor.tar
Source2: site-dist.tar
Source3: %hub_service
Source4: %agent_service
Source5: %hub_conf
Source6: %agent_conf
Source7: 50-beszel.preset

Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-golang

%description
Lightweight server monitoring hub with historical data, docker stats,
and alerts. Beszel is a lightweight server monitoring platform that
includes Docker statistics, historical data, and alert functions.
It has a friendly web interface, simple configuration, and is ready to
use out of the box. It supports automatic backup, multi-user, OAuth
authentication, and API access.

%package hub
Summary: Web dashboard for monitoring systems with Beszel
Group: System/Configuration/Networking
Provides: beszel = %EVR
Obsoletes: beszel < %EVR

%description hub
Web-based dashboard built on PocketBase that allows users to view
and manage connected systems and collect metrics from agents.

%package agent
Summary: System monitoring agent for Beszel hub
Group: System/Configuration/Networking

%description agent
Lightweight agent that runs on monitored systems and sends system
metrics and status information to the Beszel hub.

%prep
%setup -a1 -a2
%autopatch -p1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare
%golang_build $BUILDDIR/src/%import_path/internal/cmd/agent
%golang_build $BUILDDIR/src/%import_path/internal/cmd/hub

%install
export BUILDDIR="$PWD/.build"
mkdir -p %buildroot%_sysconfdir
mkdir -p %buildroot%_sysconfdir/beszel.d/tls
mkdir -p %buildroot%_beszel_home/agent
mkdir -p %buildroot%_beszel_home/hub/data

install -Dm755 $BUILDDIR/bin/agent %buildroot%_bindir/%name-agent
install -Dm755 $BUILDDIR/bin/hub %buildroot%_bindir/%name-hub
install -Dm644 %SOURCE3 %buildroot%_unitdir/%hub_service
install -Dm644 %SOURCE4 %buildroot%_unitdir/%agent_service
install -Dm644 %SOURCE5 %buildroot%_sysconfdir/%hub_conf
install -Dm644 %SOURCE6 %buildroot%_sysconfdir/%agent_conf
install -Dm644 %SOURCE7 %buildroot%_presetdir/50-beszel.preset

%post hub
%systemd_post %hub_service

%preun hub
%systemd_preun %hub_service

%postun hub
%systemd_postun_with_restart %hub_service

%post agent
%systemd_post %agent_service

%preun agent
%systemd_preun %agent_service

%postun agent
%systemd_postun_with_restart %agent_service

%pre hub
%_sbindir/groupadd -r -f %_beszel_group 2>/dev/null || :

%_sbindir/useradd -r -g %_beszel_group \
    -c "Beszel Service User" \
    -d %_beszel_home \
    -M \
    -s /sbin/nologin \
    %_beszel_user >/dev/null 2>&1 || :

%pre agent
%_sbindir/groupadd -r -f %_beszel_group 2>/dev/null || :

%_sbindir/useradd -r -g %_beszel_group \
    -c "Beszel Service User" \
    -d %_beszel_home \
    -M \
    -s /sbin/nologin \
    %_beszel_user >/dev/null 2>&1 || :

%check
export GOEXPERIMENT=synctest
go test -tags=testing ./...

%files hub
%_bindir/beszel-hub
%_unitdir/beszel-hub.service
%config(noreplace) %attr(0750, root, %_beszel_group) %_sysconfdir/%hub_conf
%_presetdir/50-beszel.preset
%dir %_sysconfdir/beszel.d
%dir %_sysconfdir/beszel.d/tls
%dir %attr(0750, %_beszel_user, %_beszel_group) %_beszel_home
%dir %attr(0750, %_beszel_user, %_beszel_group) %_beszel_home/hub
%dir %attr(0750, %_beszel_user, %_beszel_group) %_beszel_home/hub/data
%doc LICENSE readme.md

%files agent
%_bindir/beszel-agent
%_unitdir/beszel-agent.service
%_presetdir/50-beszel.preset
%config(noreplace) %attr(0750, root, %_beszel_group) %_sysconfdir/%agent_conf
%dir %attr(0750, %_beszel_user, %_beszel_group) %_beszel_home
%dir %attr(0750, %_beszel_user, %_beszel_group) %_beszel_home/agent
%doc LICENSE readme.md

%changelog
* Wed Jun 10 2026 Alexandr Shashkin <dutyrok@altlinux.org> 0.18.7-alt1
- Updated to 0.18.7.
- Removed self-update command incompatible with Sisyphus idea (Closes: #59273).
- Added ALT Linux install command to agent setup dialog (Closes: #59226).
- Prevented creation of skeleton files in /var/lib/beszel (Closes: #59275).

* Tue Apr 21 2026 Timofei Fedotov <sovtouch@altlinux.org> 0.18.2-alt2
- Improved package structure.

* Wed Jan 28 2026 Timofei Fedotov <sovtouch@altlinux.org> 0.18.2-alt1
- Initial built for ALT Sisyphus.
