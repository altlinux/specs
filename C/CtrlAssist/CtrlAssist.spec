Name:    CtrlAssist
Version: 0.4.0
Release: alt1

Summary: Controller Assist for gaming on Linux
License: Apache-2.0
Group:   System/Configuration/Hardware
URL:     https://github.com/ruffsl/CtrlAssist

Source: %name-%version.tar
Source1: %name-development-%version.tar
Patch0: ctrlassist-tray-icon-fix.patch

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: gcc-c++
BuildRequires: libudev-devel libevdev-devel

%description
CtrlAssist brings "controller assist" functionality to Linux gaming by
allowing multiple physical controllers to operate as a single virtual
input device. This enables collaborative play and customizable gamepad
setups, making it easier for players of all ages and abilities to enjoy
games together. While similar features exist on modern game consoles,
CtrlAssist is an open source project that enhances accessibility for PC
gaming, offering additional quality-of-life improvements through virtual
input devices on Linux.

%prep
%setup -a1
%patch0 -p1
%rust_prep

%build
%rust_build

%install
install -Dm755 target/release/ctrlassist %buildroot%_bindir/ctrlassist

install -Dm644 flatpak/io.github.ruffsl.ctrlassist.desktop \
%buildroot%_desktopdir/%name.desktop

install -Dm644 docs/artwork/icon_48.svg \
%buildroot%_iconsdir/hicolor/scalable/apps/io.github.ruffsl.ctrlassist.svg

%files
%doc LICENSE README.md
%_bindir/ctrlassist
%_desktopdir/%name.desktop
%_iconsdir/hicolor/scalable/apps/io.github.ruffsl.ctrlassist.svg

%changelog
* Wed Jun 24 2026 Sergey Palcheh <minergenon@altlinux.org> 0.4.0-alt1
- Initial build for Sisyphus
