%define nameB QDiskInfo

Name: qdiskinfo
Version: 0.4
Release: alt1

Summary: QDiskInfo is a frontend for smartctl. It provides a user experience similar to CrystalDiskInfo.

License: GPL-3.0-only
Group: System/Configuration/Hardware

Url: https://github.com/edisionnano/QDiskInfo
Vcs: https://github.com/edisionnano/QDiskInfo

Source: %name-%version.tar

BuildRequires(Pre): rpm-macros-cmake rpm-build-cmake
BuildRequires: cmake clang libstdc++-devel qt6-base-devel ctest qt6-tools-devel

%description
QDiskInfo is a frontend for smartctl (part of the smartmontools package). It provides a user experience
similar to CrystalDiskInfo. It shows the SMART (Self-Monitoring, Analysis, and Reporting Technology)
data of modern hard disk drives.

%prep
%setup

%build
export CC=clang
export CXX=clang++
%cmake -DENABLE_TRANSLATIONS=ON
%cmake_build

%check
%ctest

%install
%cmake_install

%files
%_bindir/%nameB
%_datadir/applications/%nameB.desktop
%_iconsdir/hicolor/scalable/apps/%nameB.svg
%doc *.md LICENSE

%changelog
* Fri May 30 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.4-alt1
- 0.3 -> 0.4

* Tue May 13 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.3-alt2
- update git.3416cc7ac1
- enabled translations

* Mon May 12 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.3-alt1
- Initial build for ALT Linux.
