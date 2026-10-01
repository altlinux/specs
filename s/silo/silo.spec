%define import_path github.com/minio/minio

Name: silo
Version: 2026.08.06
Release: alt1
Summary: S3-compatible object storage server
License: AGPL-3.0-or-later
Group: System/Servers
Url: https://github.com/pgsty/silo

Source0: %name-%version.tar
Source1: vendor.tar
Source2: silo.sysusers

ExclusiveArch: x86_64 aarch64

BuildRequires(pre): rpm-build-golang
BuildRequires(pre): rpm-macros-systemd
Requires(pre): systemd
BuildRequires: systemd
BuildRequires: golang >= 1.26.5

%description
Silo is an S3-compatible object storage server based on MinIO.

%prep
%setup -q -a1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH=%import_path
export GOTOOLCHAIN=local
export CGO_ENABLED=0
export GOFLAGS=-mod=vendor
export GOPROXY=off

%golang_prepare
cd "$BUILDDIR/src/$IMPORT_PATH"
%golang_build .
mv "$BUILDDIR/bin/minio" "$BUILDDIR/bin/silo"

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

install -Dpm0644 silo.service %buildroot%_unitdir/silo.service
install -Dpm0600 silo.env %buildroot%_sysconfdir/default/silo
install -Dpm0644 %SOURCE2 %buildroot%_sysusersdir/silo.conf
install -dpm0750 %buildroot%_localstatedir/silo/data

%pre
%sysusers_create_package silo %SOURCE2

%post
%post_service silo

%preun
%preun_service silo

%files
%_bindir/silo
%doc README.md LICENSE NOTICE CREDITS
%_unitdir/silo.service
%_sysusersdir/silo.conf
%config(noreplace) %attr(0600,root,root) %_sysconfdir/default/silo
%attr(0750,silo,silo) %dir %_localstatedir/silo
%attr(0750,silo,silo) %dir %_localstatedir/silo/data

%changelog
* Thu Oct 01 2026 Olesya Shuster <lesyafox@altlinux.org> 2026.08.06-alt1
- Initial build for ALT Linux Sisyphus
