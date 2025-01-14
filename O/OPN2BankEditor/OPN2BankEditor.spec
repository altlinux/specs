%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: OPN2BankEditor
Version: 1.3.0.90.git64f4a24
Release: alt2

Summary: a small cross-platform editor for OPN2 FM banks

License: GPL-3.0
Group: Sound
Url: https://github.com/Wohlstand/OPN2BankEditor

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(jack)
BuildRequires: pkgconfig(libpulse-simple)
BuildRequires: pkgconfig(rtaudio)
BuildRequires: pkgconfig(rtmidi)
# cmake(Qt5Widgets), Qt5WidgetsConfig.cmake
BuildRequires: qt5-base-devel
# cmake(Qt5LinguistTools), Qt5LinguistToolsConfig.cmake
BuildRequires: qt5-tools-devel
BuildRequires: zlib-devel

Patch1: Remove-unused-errorCallback-in-openStream-call.patch
Patch2: Adapt-error-handling-to-librtaudio-6.0.1-API-changes.patch

VCS: https://github.com/Wohlstand/OPN2BankEditor
Source: %name-%version.tar

%description
This is a small cross-platform editor for the OPN family of FM synthesis
soundchips (which were widely used in Sega Mega Drive game console),
Fujitsu FM Towns home computer and NEC PC-88 and PC-98 home computer series).

%prep
%setup
%patch1 -p1
%patch2 -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%_bindir/opn2_bank_editor
%_iconsdir/hicolor/*/apps/opn2_bank_editor.*
%_datadir/applications/opn2_bank_editor.desktop
%_datadir/opn2_bank_editor

%changelog
* Mon Jan 13 2025 Denis Rastyogin <gerben@altlinux.org> 1.3.0.90.git64f4a24-alt2
- Fixed compatibility issues with librtaudio (6.0.1).

* Sat Nov 16 2024 Arseny Maslennikov <arseny@altlinux.org> 1.3.0.90.git64f4a24-alt1
- Initial build for ALT Sisyphus.
