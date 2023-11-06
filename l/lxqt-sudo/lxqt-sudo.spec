# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name:     lxqt-sudo
Version:  1.4.0
Release:  alt1

Summary:  GUI frontend for sudo/su
License:  LGPL-2.1
Group:    Graphical desktop/Other
Url:      https://github.com/lxqt/lxqt-sudo

Source:   %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: qt5-base-devel
BuildRequires: liblxqt-devel
BuildRequires: qt5-tools-devel
BuildRequires: kf5-kwindowsystem-devel

%description
%summary

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc *.md
%_bindir/*
%_datadir/lxqt/translations/%name/
%_man1dir/*

%changelog
* Sun Nov 05 2023 Anton Midyukov <antohami@altlinux.org> 1.4.0-alt1
- New version 1.4.0.

* Sat Apr 15 2023 Anton Midyukov <antohami@altlinux.org> 1.3.0-alt1
- New version 1.3.0.

* Sat Nov 05 2022 Anton Midyukov <antohami@altlinux.org> 1.2.0-alt1
- new version 1.2.0

* Sun Apr 17 2022 Anton Midyukov <antohami@altlinux.org> 1.1.0-alt1
- new version 1.1.0

* Fri Nov 05 2021 Anton Midyukov <antohami@altlinux.org> 1.0.0-alt1
- new version 1.0.0

* Fri Apr 16 2021 Anton Midyukov <antohami@altlinux.org> 0.17.0-alt1
- new version 0.17.0

* Thu Nov 05 2020 Anton Midyukov <antohami@altlinux.org> 0.16.0-alt1.1
- Fix Group tag
- Unpackaged files in buildroot should terminate build enable

* Thu Nov 05 2020 Anton Midyukov <antohami@altlinux.org> 0.16.0-alt1
- new version 0.16.0

* Sat Apr 25 2020 Anton Midyukov <antohami@altlinux.org> 0.15.0-alt1
- Initial build for Sisyphus
