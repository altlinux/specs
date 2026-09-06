%define _unpackaged_files_terminate_build 1

%global import_path github.com/Containerpak/cpak

Name: cpak
Version: 2.12.9
Release: alt1

Summary: Fast, decentralized, portable, powerful and low-memory footprint package format for Linux
License: LGPL-2.1-only
Group: System/Configuration/Other
Url: https://github.com/Containerpak/cpak

Source: %name-%version.tar

Source1: %name-development-%version.tar

BuildRequires(pre): rpm-build-golang

BuildRequires: golang
BuildRequires: gcc-c++
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(Qt6Widgets)

Requires: sysctl-conf-userns
Requires: shadow-submap
Requires: fuse-overlayfs
Requires: /usr/bin/slirp4netns

# need go >= 1.26.7
ExcludeArch: riscv64

%description
%summary.

%prep
%setup -a1
sed -i "s|install cpak-linux-amd64 or cpak-linux-arm64, or download a complete application installer from cpak.it|see %_datadir/doc/cpak-%{version}/README.md for details, visit https://cpak.it for graphical installer packages|" cmd/cpak-installer/main.go

%build
make \
     cpak \
     storaged \
     sign \
     installer \
     VERSION=v%{version} SELF_UPDATE_MODE=disabled

%install
install -Dpm755 cpak %buildroot%_bindir/cpak
install -Dpm755 cpak-installer %buildroot%_bindir/cpak-installer
install -Dpm755 cpak-sign %buildroot%_bindir/cpak-sign
install -Dpm755 cpak-storaged %buildroot%_bindir/cpak-storaged

%post
echo "NOTE: %name package requires system configuration, see %_datadir/doc/cpak-%{version}/README.md and"
echo "      https://www.altlinux.org/Podman only about rootless operation, subuid/subgid and fuse-overlayfs."
echo "      Run 'cpak system setup' and 'cpak doctor' to apply and check the configuration."

%files
%doc LICENSE README.md cpak-logo.svg
%_bindir/cpak
%_bindir/cpak-installer
%_bindir/cpak-sign
%_bindir/cpak-storaged

%changelog
* Sun Sep 06 2026 Nikolay Strelkov <snk@altlinux.org> 2.12.9-alt1
- New version 2.12.9.
- Package cpak-installer.

* Sat Sep 05 2026 Nikolay Strelkov <snk@altlinux.org> 2.12.7-alt1
- Initial build for Sisyphus
