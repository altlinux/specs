%define _unpackaged_files_terminate_build 1

Name: qweave
Version: 1.2.1
Release: alt1

Summary: Visualization of weaving patterns
License: GPL-3.0
Group: Graphics
Url: https://github.com/sunderme/QWeave

Source: %name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: qt6-base-devel
BuildRequires: qt6-tools-devel
BuildRequires: qt6-svg-devel
BuildRequires: pkgconfig(cups)

%description
%summary

%prep
%setup
%patch -p1

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
* Sat Jun 14 2025 Nikolay Strelkov <snk@altlinux.org> 1.2.1-alt1
- Initial build for Sisyphus
