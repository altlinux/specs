# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: lxqt-archiver
Version: 1.0.0
Release: alt1

Summary: A simple & lightweight desktop-agnostic Qt file archiver
License: GPL-2.0
Group: Graphical desktop/Other

Url: https://github.com/lxqt/lxqt-archiver
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: gcc-c++ cmake
BuildRequires: qt6-base-devel qt6-tools-devel
BuildRequires: libfm-qt6-devel
BuildRequires: lxqt2-build-tools
BuildRequires: libgio-devel
BuildRequires: libjson-glib-devel

%description
%summary.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%_bindir/*
%_datadir/%name
%_iconsdir/hicolor/*/apps/*
%_desktopdir/%name.desktop
%doc AUTHORS CHANGELOG LICENSE README.md

%changelog
* Thu Jun 13 2024 Anton Midyukov <antohami@altlinux.org> 1.0.0-alt1
- New version 1.0.0

* Thu Feb 22 2024 Anton Midyukov <antohami@altlinux.org> 0.9.1-alt1
- New version 0.9.1

* Mon Nov 06 2023 Anton Midyukov <antohami@altlinux.org> 0.9.0-alt1
- New version 0.9.0.

* Sun Apr 16 2023 Anton Midyukov <antohami@altlinux.org> 0.8.0-alt1
- New version 0.8.0.

* Sat Nov 05 2022 Anton Midyukov <antohami@altlinux.org> 0.7.0-alt1
- new version 0.7.0

* Sat May 07 2022 Anton Midyukov <antohami@altlinux.org> 0.6.0-alt1
- new version 0.6.0

* Thu Dec 23 2021 Anton Midyukov <antohami@altlinux.org> 0.5.0-alt1
- new version 0.5.0

* Wed Nov 03 2021 Anton Midyukov <antohami@altlinux.org> 0.4.0-alt1
- new version 0.4.0

* Thu Nov 05 2020 Anton Midyukov <antohami@altlinux.org> 0.3.0-alt1
- new version 0.3.0

* Fri May 22 2020 Anton Midyukov <antohami@altlinux.org> 0.2.0-alt1
- new version 0.2.0

* Sat Apr 25 2020 Anton Midyukov <antohami@altlinux.org> 0.1.1-alt1
- Initial build
