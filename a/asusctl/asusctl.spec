Name:     asusctl
Version:  4.5.0
Release:  alt0_1_rc4 

%define user_service /etc/systemd/user/

Summary:  A control daemon, CLI tools, and a collection of crates for interacting with ASUS ROG laptops 
License:  MPL-2.0
Group:    System/Configuration/Hardware
Url:      https://asus-linux.org
# GiSource   https://gitlab.com/asus-linux/asusctl


ExclusiveArch: x86_64

Packager: Hihin Ruslan <ruslandh@altlinux.ru>

Source:  %name-%version.tar
Source1: README.ru
#Source2: vendors-%version.tar
Patch1: asusctl-4.3.1-systemd.patch


BuildRequires(pre): rpm-macros-rust
BuildRequires(pre): rust-cargo

BuildRequires: cmake

# Automatically added by buildreq on Mon Oct 31 2022
# optimized out: ca-trust cmake-modules fontconfig glibc-kernheaders-generic glibc-kernheaders-x86 libfreetype-devel libgpg-error libsasl2-3 libstdc++-devel llvm14.0-libs pkg-config python3 python3-base python3-dev rust sh4
BuildRequires: cmake fontconfig-devel gcc-c++ libudev-devel python3-module-mpl_toolkits python3-module-setuptools python3-module-zope rust-cargo


%description
asusctl for ASUS ROG
https://asus-linux.org
asusd is a utility for Linux to control many aspects of various ASUS laptops
but can also be used with non-asus laptops with reduced features.

%description -l ru_RU.utf8
asusd - утилита для Linux, позволяющая управлять многими аспектами различных ноутбуков ASUS.
но также может использоваться с ноутбуками сторонних производителей с ограниченными возможностями.
подробнее  https://asus-linux.org

%package rog-gui
Summary: An experimental GUI for %name
Group:    System/Configuration/Hardware
ExclusiveArch: x86_64

%description rog-gui
A one-stop-shop GUI tool for asusd/asusctl. It aims to provide most controls,
a notification service, and ability to run in the background.

Buildrequires: git

%global rustflags -Clink-arg=-Wl,-z,relro,-z,now

%prep
%setup
%patch1 -p1

%build
export RUSTFLAGS="%rustflags"
#RUST_BACKTRACE=1 
%rust_build

%install
export RUSTFLAGS="%rustflags"

install -m644 %SOURCE1 %_builddir/%name-%version

%makeinstall_std

#rm -rf %buildroot/usr/lib/


%files
%_bindir/*
%exclude %_bindir/rog-control-center
%doc README.ru *.md
%_sysconfdir/asusd
%_datadir/asusd
%_datadir/dbus-1/system.d/*.conf
#_datadir/fish/vendor_completions.d/*
#_datadir/zsh/site-functions/*
%_udevrulesdir/*.rules
%_unitdir/*.service
%_sysconfdir/systemd/user/*.service
%_iconsdir/hicolor/512x512/apps/*
%exclude %_iconsdir/hicolor/512x512/apps/rog-control-center.png
%_iconsdir/hicolor/scalable/*

%files rog-gui
%_bindir/rog-control-center
#dir %_desktopdir
%_desktopdir/rog-control-center.desktop

%_iconsdir/hicolor/512x512/apps/rog-control-center.png
%_datadir/rog-gui/*

%changelog
* Mon Oct 31 2022 Hihin Ruslan <ruslandh@altlinux.ru> 4.5.0-alt0_1_rc4
- Update from git (Version 4.5.0-rc4)
- Git commit ba1d3f045d0fca79f125c165fd3cf34da249b506

* Sun Jul 24 2022 Hihin Ruslan <ruslandh@altlinux.ru> 4.3.0-alt1
- Version 4.3.0

* Tue Jun 21 2022 Hihin Ruslan <ruslandh@altlinux.ru> 4.1.1-alt1
- Initial build for Sisyphus
