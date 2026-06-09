%define _unpackaged_files_terminate_build 1
%define import_path github.com/nats-io/nats-server/v2

Name: nats-server
Version: 2.14.2
Release: alt1

Summary: High-Performance server for NATS, the cloud and edge native messaging system
License: Apache-2.0
Group: System/Servers
Url: https://nats.io/
Vcs: https://github.com/nats-io/nats-server

ExclusiveArch: %go_arches

Source0: %name-%version.tar
Source1: %name-%version-vendor.tar
Source2: nats-server.conf
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-golang

%description
NATS is a simple, secure and performant communications system for
digital systems, services and devices. NATS is part of the Cloud Native
Computing Foundation (CNCF).

%prep
%setup -a1
%autopatch -p1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
%golang_prepare

cd .build/src/%import_path
%golang_build .

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1
export RPM_BINDIR=%_sbindir
%golang_install

install -Dvpm0644 %SOURCE2 %buildroot%_sysconfdir/nats-server.conf
install -Dvpm0644 util/nats-server.service %buildroot%_unitdir/nats-server.service
install -Dvpm0644 util/nats-server-hardened.service %buildroot%_unitdir/nats-server-hardened.service

mkdir -p %buildroot%_localstatedir/nats
mkdir -p %buildroot%_logdir/nats
mkdir -p %buildroot%_runtimedir/nats

%pre
%_sbindir/groupadd -r -f nats 2>/dev/null ||:
%_sbindir/useradd -r -g nats -d %_localstatedir/nats -s /dev/null -c "NATS server" nats 2>/dev/null ||:

%post
%systemd_post nats-server
%systemd_post nats-server-hardened

%preun
%systemd_preun nats-server
%systemd_preun nats-server-hardened

%files
%config(noreplace) %_sysconfdir/nats-server.conf
%_sbindir/nats-server
%_unitdir/nats-server.service
%_unitdir/nats-server-hardened.service
%dir %attr(0750,nats,nats) %_logdir/nats/
%dir %attr(0750,nats,nats) %_localstatedir/nats/
%dir %attr(0750,nats,nats) %_runtimedir/nats/

%changelog
* Tue Jun 09 2026 Artem Krasovskiy <aibure@altlinux.org> 2.14.2-alt1
- Updated to 2.14.2.

* Wed Apr 01 2026 Alexander Danilov <admsasha@altlinux.org> 2.12.6-alt1
- Updated to 2.12.6.

* Wed Feb 04 2026 Artem Krasovskiy <aibure@altlinux.org> 2.12.4-alt1
- Updated to 2.12.4.

* Tue Jan 27 2026 Artem Krasovskiy <aibure@altlinux.org> 2.12.3-alt1
- Updated to 2.12.3.

* Tue Dec 16 2025 Artem Krasovskiy <aibure@altlinux.org> 2.12.2-alt1
- Updated to 2.12.2.

* Tue Oct 28 2025 Artem Krasovskiy <aibure@altlinux.org> 2.12.1-alt1
- Updated to 2.12.1.

* Fri Aug 22 2025 Anton Zhukharev <ancieg@altlinux.org> 2.11.8-alt1
- Updated to 2.11.8.

* Fri Jun 27 2025 Anton Zhukharev <ancieg@altlinux.org> 2.11.5-alt1
- Packaged for ALT Sisyphus.
