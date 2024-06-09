Name:     asusctl
Version:  5.0.9
Release:  alt2.1

%define user_service %_unitdir/user

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


BuildRequires(pre): rpm-macros-rust rpm-macros-systemd >= 5
BuildRequires(pre): rust-cargo

# Automatically added by buildreq on Mon Oct 31 2022
# optimized out: ca-trust cmake-modules fontconfig glibc-kernheaders-generic glibc-kernheaders-x86 libfreetype-devel libgpg-error libsasl2-3 libstdc++-devel llvm14.0-libs pkg-config python3 python3-base python3-dev rust sh4
BuildRequires: libgtk+3-devel libudev-devel python3-module-setuptools python3-module-zope rust-cargo
Buildrequires: git libayatana-indicator-devel libappindicator-gtk3 libxkbcommon-x11-devel 

# For Version 6.x BuildRequires: libgbm-devel libinput-devel libseat1-devel libxkbcommon-devel python3-module-setuptools python3-module-zope rust-cargo

BuildRequires: cmake

BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(cairo-gobject)
BuildRequires: pkgconfig(atk)
BuildRequires: pkgconfig(gdk-pixbuf-2.0)
BuildRequires: pkgconfig(pango)
BuildRequires: pkgconfig(gdk-3.0)


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
%setup -a2
#%%patch1 -p1

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
%rust_build

%install
export RUSTFLAGS="%rustflags"

install -m644 %SOURCE1 %_builddir/%name-%version
%makeinstall_std

mkdir -p %buildroot/%user_service
mv %buildroot/usr/lib/systemd/user/asusd-user.service %buildroot/%user_service/asusd-user.service
mkdir -p %buildroot/%_unitdir
mv %buildroot/usr/lib/systemd/system/asusd.service %buildroot/%_unitdir/asusd.service
mkdir -p %buildroot/%_udevrulesdir
mv %buildroot/usr/lib/udev/rules.d/99-asusd.rules %buildroot/%_udevrulesdir/99-asusd.rules


%files
%_bindir/*
%exclude %_bindir/rog-control-center
%doc README.ru *.md
%_datadir/asusd
%_datadir/dbus-1/system.d/*.conf
%_udevrulesdir/*.rules

%_unitdir/*.service

%user_service/*.service
%_iconsdir/hicolor/512x512/apps/*
%exclude %_iconsdir/hicolor/512x512/apps/rog-control-center.png
%_iconsdir/hicolor/scalable/*

%files rog-gui
%_bindir/rog-control-center
%_desktopdir/rog-control-center.desktop

%_iconsdir/hicolor/512x512/apps/rog-control-center.png
%_datadir/rog-gui/*

%changelog
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
