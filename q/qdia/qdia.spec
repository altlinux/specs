%define _unpackaged_files_terminate_build 1

Name: qdia
Version: 0.53
Release: alt1

Summary: Simple schematic/diagram editor
License: AGPL-3.0
Group: Engineering
Url: https://github.com/sunderme/qdia

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: qt6-base-devel
BuildRequires: qt6-tools-devel
BuildRequires: qt6-svg-devel

%description
Simple schematic/diagram editor with focus on quick diagram generation
with high quality graphics.

Inspired by xcircuit.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

%find_lang %name

%files -f %{name}.lang
%doc LICENSE README.md
%_bindir/*
%_desktopdir/*.desktop
%_iconsdir/hicolor/*/*/*

%changelog
* Sat Jun 14 2025 Nikolay Strelkov <snk@altlinux.org> 0.53-alt1
- Initial build for Sisyphus
