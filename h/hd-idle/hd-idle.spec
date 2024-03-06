%global _unpackaged_files_terminate_build 1
%global import_path github.com/adelolmo/hd-idle

Name: hd-idle
Version: 1.21
Release: alt2

Summary: Hard Disk Idle Spin-Down Utility
License: GPL-3.0
Group: System/Configuration/Hardware
Url: https://github.com/adelolmo/hd-idle

Source0: %name-%version.tar

Patch: %name-alt-arches.patch

ExclusiveArch: %go_arches

BuildRequires(pre): rpm-build-golang
BuildRequires: /proc

%description
hd-idle is a utility program for spinning-down external disks after a period of
idle time. Since most external IDE disk enclosures don't support setting the
IDE idle timer, a program like hd-idle is required to spin down idle disks
automatically.

%prep
%setup
%patch -p1

%build
export CGO_CFLAGS=$CFLAGS
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export GOFLAGS="-mod=vendor"
export GOROOT="%_libexecdir/golang"

%golang_prepare
pushd .gopath/src/%import_path
%golang_build .
popd

%install
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path:$PWD"
export RELEASE_VERSION=v%version
export RELEASE_NUMBER=%version

pushd .gopath/src/%import_path
%makeinstall DESTDIR=%buildroot
popd

mkdir -p %buildroot{%_unitdir,%_sysconfdir/sysconfig}
install -pm644 debian/%name.service %buildroot%_unitdir/
subst 's,%_sysconfdir\/default,%_sysconfdir/sysconfig,g' %buildroot/%_unitdir/%name.service
install -pm644 debian/%name.default %buildroot%_sysconfdir/sysconfig/%name

%files
%doc LICENSE README.md
%_sbindir/%name
%config(noreplace) %_sysconfdir/sysconfig/%name
%_unitdir/%name.service
%_man8dir/%{name}*

%changelog
* Wed Mar 06 2024 Alexey Sheplyakov <asheplyakov@altlinux.org> 1.21-alt2
- NMU: fixed FTBFS on LoongArch.

* Tue Mar 05 2024 L.A. Kostis <lakostis@altlinux.ru> 1.21-alt1
- Initial build for ALTLinux.

