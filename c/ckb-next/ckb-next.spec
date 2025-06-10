Name:    ckb-next
Version: 0.6.2
Release: alt1

Summary: RGB driver for Corsair keyboard and mice
License: GPL-2.0
Group:   System/Configuration/Hardware
Url:     https://github.com/ckb-next/ckb-next
VCS:     https://github.com/ckb-next/ckb-next.git

Source: %name-%version.tar
Patch:  ckb-next-animations.patch
Patch1: ckb-next-no-cmake-modules.patch
Patch2: ckb-next-systemd.patch
Patch3: ckb-next-udev.patch
Patch4: ckb-next-use-run.patch
Patch5: harden_ckb-next-daemon.service.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++ git-core
BuildRequires: libudev-devel libpulseaudio-devel zlib-devel qt5-base-devel
BuildRequires: qt5-base-devel quazip-qt5-devel qt5-x11extras-devel
BuildRequires: libxcbutil-icccm-devel libdbusmenu-qt5-devel qt5-tools-devel

%description
ckb is a driver for Corsair keyboards and mice. It brings the features
of their proprietary CUE software to the Linux operating system.
This project supports much of the same functionality, including full
RGB animations.

%prep
%setup
%patch -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
%cmake \
    -DDISABLE_UPDATER=1 \
    -DCMAKE_INSTALL_LIBEXECDIR=%_libexecdir \
    -DUDEV_RULE_DIRECTORY=%_udevrulesdir

%cmake_build

%install
%cmake_install

%files
%doc LICENSE README.md
%_bindir/ckb-next*
%_libexecdir/ckb-next-animations/
%_libexecdir/ckb-next-sinfo
%_libexecdir/ckb-next-daemon
%_unitdir/ckb-next-daemon.service
%_udevrulesdir/99-ckb-next-daemon.rules
%_desktopdir/ckb-next.desktop
%_iconsdir/hicolor/*/apps/*.png
%_iconsdir/hicolor/*/status/*.png

%changelog
* Mon Jun 09 2025 Sergey Palcheh <minergenon@altlinux.org> 0.6.2-alt1
- Initial build for Sisyphus

