%global import_path github.com/piraeusdatastore/linstor-csi
%define _unpackaged_files_terminate_build 1

Name:    linstor-csi
Version: 1.11.2
Release: alt1

Summary: CSI plugin for LINSTOR
License: Apache-2.0
Group:   Other
Url:     https://github.com/piraeusdatastore/linstor-csi
Vcs:     https://github.com/piraeusdatastore/linstor-csi

Source: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-macros-golang rpm-macros-systemd
BuildRequires: golang rpm-build-golang

%description
This CSI plugin allows for the use of LINSTOR volumes on Container Orchestrators that implement CSI, such as Kubernetes.

%package -n piraeus-csi-nfs-server
Summary: CSI NFS server helper utilities
Group: System/Servers
Requires: drbd-reactor nfs-ganesha nfs-ganesha-vfs psmisc e2fsprogs xfsprogs mount
ExcludeArch: %ix86

%description -n piraeus-csi-nfs-server
%summary.

%prep
%setup -a 1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export LDFLAGS="-w -s -X github.com/piraeusdatastore/linstor-csi/pkg/driver.Version=%version"
export GOFLAGS="-trimpath"

%golang_prepare

%golang_build ./cmd/*

%install
# fix unmet dependencies
sed -i 's|/usr/bin/chmod|/bin/chmod|' nfs/service/chmod@.service
sed -i 's|/usr/bin/umount|/bin/umount|' nfs/service/mount-recovery@.service 
sed -i 's|/usr/bin/umount|/bin/umount|' nfs/service/mount-export@.service 

install -d %buildroot/%_unitdir
install -m 644 \
    nfs/service/nfs-ganesha@.service nfs/service/growfs@.service \
    nfs/service/growfs@.timer nfs/service/mount-export@.service \
    nfs/service/mount-recovery@.service nfs/service/chmod@.service \
    nfs/service/prepare-device-links@.service nfs/service/advertise-nfs-endpoint@.service \
    nfs/service/clean-nfs-endpoint@.service nfs/service/start-stop-reactor.service \
    %buildroot/%_unitdir

install -d %buildroot/%_unitdir/drbd@.service.d
install -m 644 nfs/service/drbd@.service.override.conf %buildroot/%_unitdir/drbd@.service.d/container.conf

install -d %buildroot/%_unitdir/drbd-demote-or-escalate@.service.d
install -m 644 nfs/service/drbd-demote-or-escalate@.service.override.conf \
    %buildroot/%_unitdir/drbd-demote-or-escalate@.service.d/container.conf

install -d %buildroot/%_sysconfdir/nfs-helper
install -m 644 nfs/service/default-config.tmpl %buildroot/%_sysconfdir/nfs-helper/default-config.tmpl

install -d %buildroot/%_sysconfdir/systemd/journald.conf.d
install -m 644 nfs/service/journald.conf \
    %buildroot/%_sysconfdir/systemd/journald.conf.d/10-piraeus-csi-nfs-server.conf


export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

%post -n piraeus-csi-nfs-server
%post_systemd_postponed start-stop-reactor.service

%preun -n piraeus-csi-nfs-server
%preun_systemd start-stop-reactor.service

%check
%gotest ./...

%files -n piraeus-csi-nfs-server
%dir %_sysconfdir/nfs-helper
%dir %_sysconfdir/systemd/journald.conf.d
%config(noreplace) %_sysconfdir/nfs-helper/default-config.tmpl
%config(noreplace) %_sysconfdir/systemd/journald.conf.d/10-piraeus-csi-nfs-server.conf
%_unitdir/*
%_bindir/nfs-helper

%files
%doc LICENSE README.md
%_bindir/%name

%changelog
* Fri May 15 2026 Ivan Pepelyaev <fl0pp5@altlinux.org> 1.11.2-alt1
- New version 1.11.2
- Add subpackage piraeus-csi-nfs-server.

* Thu Mar 19 2026 Nadezhda Fedorova <fedor@altlinux.org> 1.10.6-alt1
- Initial build for Sisyphus.

