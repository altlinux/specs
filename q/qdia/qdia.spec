%define _unpackaged_files_terminate_build 1

Name: qdia
Version: 0.64
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
sed -i 's|^Categories=.*|Categories=Graphics;Publishing;|' resources/qdia.desktop

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
* Fri Jun 12 2026 Nikolay Strelkov <snk@altlinux.org> 0.64-alt1
- New version 0.64.

* Thu May 28 2026 Nikolay Strelkov <snk@altlinux.org> 0.63-alt1
- New version 0.63.

* Sat Jan 31 2026 Nikolay Strelkov <snk@altlinux.org> 0.60-alt1
- New version 0.60.

* Wed Dec 31 2025 Nikolay Strelkov <snk@altlinux.org> 0.58-alt1
- New version 0.58.

* Sun Oct 26 2025 Nikolay Strelkov <snk@altlinux.org> 0.57-alt1
- New version 0.57.

* Thu Jul 31 2025 Nikolay Strelkov <snk@altlinux.org> 0.55-alt1
- New version 0.55.

* Sat Jul 12 2025 Nikolay Strelkov <snk@altlinux.org> 0.54-alt1
- New version 0.54.

* Fri Jun 27 2025 Nikolay Strelkov <snk@altlinux.org> 0.53-alt2
- Applied repocop fix for freedesktop-categories

* Sat Jun 14 2025 Nikolay Strelkov <snk@altlinux.org> 0.53-alt1
- Initial build for Sisyphus
