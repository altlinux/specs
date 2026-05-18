%define _unpackaged_files_terminate_build 1

Name: droid-juicer
Version: 0.4.2
Release: alt1
Summary: Extract firmware from Android vendor partitions
License: MIT
Group: System/Kernel and hardware
Url: https://gitlab.com/mobian1/droid-juicer/
VCS: https://gitlab.com/mobian1/droid-juicer.git

Source: %name-%version.tar
Source1: vendor.tar
Patch0: v0.4.2-dhxx-firmware-add-compat-symlinks-for-backwards-compatibi.patch
Patch1: v0.4.2-dhxx-configs-add-new-fw-paths-and-keep-the-original-paths.patch

BuildRequires(pre): rpm-macros-rust
BuildRequires(pre): rpm-macros-systemd
BuildRequires: rpm-build-rust
BuildRequires: clang-devel

%description
droid-juicer is a tool for extracting binary firmware files from vendor
partitions on Android devices. It allows importing the needed firmware into the
Linux system's /lib/firmware folder, avoiding the need to distribute such
firmware and the corresponding legal issues.

%prep
%setup -a1
%rust_prep
%patch0 -p 1
%patch1 -p 1

%build
%rust_build

%install
mkdir -p %buildroot%_datadir/%name
%rust_install
%__install -D -m 644 %name.service %buildroot%_unitdir/%name.service
cp -rv configs %buildroot%_datadir/%name

%files
%doc README.md
%_bindir/%name
%_unitdir/%name.service
%_datadir/%name

%changelog
* Sun May 17 2026 Vasiliy Doylov <neko@altlinux.org> 0.4.2-alt1
- Initial build for ALT
