%define _unpackaged_files_terminate_build 1

Name: matekbd-keyboard-display
Version: 23.11.1
Release: alt1

Summary: Display keyboard layouts in MATE
License: LGPLv3+
Group: Graphical desktop/MATE
Url: https://github.com/tari01/matekbd-keyboard-display

Source: %name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-cmake

BuildRequires: cmake
BuildRequires: libmatekbd-devel

%description
An application that allows you to preview keyboard layouts on MATE desktop. It uses the libmatekbd library, similarly to gkbd-keyboard-display and libgnomekbd.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

%find_lang %name

%files -f %name.lang
%doc AUTHORS CHANGELOG.md COPYING README.md
%_bindir/%name
%_desktopdir/%name.desktop
%_iconsdir/hicolor/scalable/apps/*
%_man1dir/*.1*

%changelog
* Sun Jan 19 2025 Nikolay Strelkov <snk@altlinux.org> 23.11.1-alt1
- Initial build for Sisyphus
