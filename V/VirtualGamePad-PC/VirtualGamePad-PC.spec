Name:    VirtualGamePad-PC
Version: 0.4.1
Release: alt1

Summary: Windows and Linux server for Virtual Gamepad
License: GPL-3.0
Group:   System/Configuration/Hardware
URL:     https://kitswas.github.io/VirtualGamePad/
VCS:     https://github.com/kitswas/VirtualGamePad-PC

Source: %name-%version.tar
Source1: %name-postsubmodules-%version.tar
Patch: VirtualGamePad-PC-0.4.1-alt-packaging-fixes.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++
BuildRequires: qt6-base-devel libevdev-devel

%description
%summary

%prep
%setup -a1
%patch -p1

%build
%cmake
%cmake_build

%install
%cmake_install

install -Dm644 res/VGamepadPC.desktop %buildroot%_desktopdir/VGamepadPC.desktop
install -Dm644 res/logos/GamepadIcon.svg %buildroot%_iconsdir/hicolor/scalable/apps/VGamepadPC.svg

%files
%doc LICENCE.TXT README.MD
%_bindir/VGamepadPC
%_libdir/libQR_Code_Generator.so*
%_desktopdir/VGamepadPC.desktop
%_iconsdir/hicolor/scalable/apps/VGamepadPC.svg


%changelog
* Wed Jun 24 2026 Sergey Palcheh <minergenon@altlinux.org> 0.4.1-alt1
- Initial build for Sisyphus
