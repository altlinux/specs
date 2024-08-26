Name:     asusctl
Version:  6.0.11
Release:  alt1

Summary:  A control daemon, CLI tools, and a collection of crates for interacting with ASUS ROG laptops 
License:  MPL-2.0
Group:    System/Configuration/Hardware
Url:      https://asus-linux.org
# GiSource   https://gitlab.com/asus-linux/asusctl


ExclusiveArch: x86_64

Packager: Hihin Ruslan <ruslandh@altlinux.ru>

Source:  %name-%version.tar
Source1: README.ru
Source2: vendor.tar
Source3: cargo_src.tar
# Patch1: asusctl-6.0.11-sleep.patch


BuildRequires(pre): rpm-macros-rust rpm-macros-systemd >= 5
BuildRequires(pre): rust-cargo

# Automatically added by buildreq on Sun Aug 25 2024
# optimized out: ca-trust glibc-kernheaders-generic glibc-kernheaders-x86 libgpg-error libp11-kit libsasl2-3 libudev-devel libwayland-server llvm17.0-libs pkg-config python3 python3-base python3-dev rust sh5
BuildRequires: libgbm-devel libinput-devel libseat1-devel libxkbcommon-devel python3-module-setuptools python3-module-zope rust-cargo

Buildrequires: git libayatana-indicator-devel libappindicator-gtk3 libxkbcommon-x11-devel 

# For Version 6.x BuildRequires: libgbm-devel libinput-devel libseat1-devel libxkbcommon-devel python3-module-setuptools python3-module-zope rust-cargo

BuildRequires: cmake

BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(cairo-gobject)
BuildRequires: pkgconfig(atk)
BuildRequires: pkgconfig(gdk-pixbuf-2.0)
BuildRequires: pkgconfig(pango)
BuildRequires: pkgconfig(gdk-3.0)

BuildRequires: pkgconfig(libseat)
BuildRequires: pkgconfig(gbm)
BuildRequires: pkgconfig(libinput)

%description
asusd is a utility for Linux to control many aspects of various ASUS laptops
but can also be used with non-asus laptops with reduced features.

Asusctl for ASUS ROG https://asus-linux.org


%description -l ru_RU.utf8
asusd - утилита для Linux, позволяющая управлять многими аспектами различных ноутбуков ASUS.
но также может использоваться с ноутбуками сторонних производителей с ограниченными возможностями.
подробнее  https://asus-linux.org

%package rog-gui
Summary: An experimental GUI for %name
Group:    System/Configuration/Hardware
ExclusiveArch: x86_64
Requires: libappindicator-gtk3 libayatana-appindicator3-1

%description rog-gui
A one-stop-shop GUI tool for asusd/asusctl. It aims to provide most controls,
a notification service, and ability to run in the background.

%global rustflags -Clink-arg=-Wl,-z,relro,-z,now

%prep
%setup -a2 -a3
%__subst "s|/usr/bin/sleep|/bin/sleep|g" ./data//asusd-user.service

#patch1 -p1

mkdir .cargo
cat >.cargo/config.toml <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source."git+https://github.com/emilk/egui?rev=b8e798777de519de3a1878798097ab2ab0bd4def"]
git = "https://github.com/emilk/egui"
rev = "b8e798777de519de3a1878798097ab2ab0bd4def"
replace-with = "vendored-sources"

[source."git+https://github.com/flukejones/notify-rust.git"]
git = "https://github.com/flukejones/notify-rust.git"
replace-with = "vendored-sources"

[source."git+https://gitlab.com/asus-linux/supergfxctl.git"]
git = "https://gitlab.com/asus-linux/supergfxctl.git"

replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
export RUSTFLAGS="%rustflags"
RUST_BACKTRACE=1 

export CARGO_HOME=%_builddir/%name-%version/cargo_src

%rust_build

#    export RUSTFLAGS="${RUSTFLAGS} -g" 
#    cargo build --release -j${NPROCS:-24}


%install
export RUSTFLAGS="%rustflags"

install -m644 %SOURCE1 %_builddir/%name-%version
%makeinstall_std

mkdir -p %buildroot/%_unitdir
mkdir -p %buildroot/%_udevrulesdir
mkdir -p %user_service/
install  data/asusd.service %buildroot/%_unitdir/asusd.service
install  data//asusd-user.service %buildroot/%_user_unitdir/asusd-user.service

#mv data/asusd-user.service %buildroot/%_unitdir/asusd-user.service
#mv %buildroot/usr/lib/udev/rules.d/99-asusd.rules %buildroot/%_udevrulesdir/99-asusd.rules

%files
%_bindir/*
%exclude %_bindir/rog-control-center
%doc README.ru *.md
%_datadir/asusd
%_datadir/dbus-1/system.d/*.conf
%_udevrulesdir/*.rules

%_unitdir/*.service
%_user_unitdir/*.service

%_iconsdir/hicolor/512x512/apps/*
%exclude %_iconsdir/hicolor/512x512/apps/rog-control-center.png
%_iconsdir/hicolor/scalable/*

%files rog-gui
%_bindir/rog-control-center
%_desktopdir/rog-control-center.desktop

%_iconsdir/hicolor/512x512/apps/rog-control-center.png
%_datadir/rog-gui/*

%changelog
* Sun Aug 25 2024 Hihin Ruslan <ruslandh@altlinux.ru> 6.0.11-alt1
- Version 6.0.11

* Sun Jun 16 2024 Hihin Ruslan <ruslandh@altlinux.ru> 5.0.9-alt2.2
- Replace %%user_service to %%_user_unitdir

* Sun Jun 09 2024 Hihin Ruslan <ruslandh@altlinux.ru> 5.0.9-alt2.1
- Fix usrmerge troubles

* Sun Jun 09 2024 Hihin Ruslan <ruslandh@altlinux.ru> 5.0.9-alt2
- Clean and fix spec

* Fri Mar 22 2024 Hihin Ruslan <ruslandh@altlinux.ru> 5.0.9-alt1
- Version 5.0.9

* Mon Feb 12 2024 Hihin Ruslan <ruslandh@altlinux.ru> 5.0.7-alt1
- Version 5.0.7

* Mon Sep 11 2023 Hihin Ruslan <ruslandh@altlinux.ru> 4.7.2-alt1.1
- Update sisyphus

* Sat Sep 09 2023 Evgeniy Kukhtinov <neurofreak@altlinux.org> 4.7.2-alt1
- Version 4.7.2 

* Mon Oct 31 2022 Hihin Ruslan <ruslandh@altlinux.ru> 4.5.0-alt0_1_rc4
- Update from git (Version 4.5.0-rc4)
- Git commit ba1d3f045d0fca79f125c165fd3cf34da249b506

* Sun Jul 24 2022 Hihin Ruslan <ruslandh@altlinux.ru> 4.3.0-alt1
- Version 4.3.0

* Tue Jun 21 2022 Hihin Ruslan <ruslandh@altlinux.ru> 4.1.1-alt1
- Initial build for Sisyphus

