Name:     mupen64plus-qt
Version:  1.17
Release:  alt1

Summary:  A customizable launcher for Mupen64Plus
License:  BSD-3-Clause
Group:    Other
Url:      https://github.com/dh4/mupen64plus-qt

Packager: Artyom Bystrov <arbars@altlinux.org>

Source:   %name-%version.tar
Patch0:   quazip-fix.patch

BuildRequires: qt6-base-devel gcc-c++ cmake quazip-qt6-devel qt6-sql-mysql libSDL2-devel
Requires: mupen64plus qt6-qtbase libquazip1-qt6 qt6-sql-postgresql qt6-sql-interbase qt6-sql-odbc qt6-sql-postgresql
ExcludeArch: armh %ix86

%description
Mupen64Plus-Qt is a customizable launcher for the mupen64plus-ui-console
frontend. It was adapted from CEN64-Qt to work with Mupen64Plus.

See the README at https://www.github.com/dh4/mupen64plus-qt for a detailed
description of its features and usage.

%prep
%setup

#patch0 -p1
# Fix build with Qt6
sed -i s/FILENAME_VARIABLE/OUTPUT_SCRIPT/g CMakeLists.txt

%build
%cmake
%cmake_build

%install
%cmake_install
install -Dm644 "resources/mupen64plus-qt.desktop"   "%{buildroot}%{_datadir}/applications/mupen64plus-qt.desktop"
install -Dm644 "resources/images/mupen64plus.png"   "%{buildroot}%{_datadir}/icons/hicolor/128x128/apps/mupen64plus-qt.png"
install -Dm644 "resources/mupen64plus-qt.6"         "%{buildroot}%{_mandir}/man6/mupen64plus-qt.6"

%files
%doc README.md LICENSE

%{_bindir}/mupen64plus-qt
%{_datadir}/applications/mupen64plus-qt.desktop
%{_datadir}/icons/hicolor/128x128/apps/mupen64plus-qt.png
%{_mandir}/man6/mupen64plus-qt.6*

%changelog
* Mon Jul 13 2026 Artyom Bystrov <arbars@altlinux.org> 1.17-alt1
- New version 1.17.

* Thu Feb  1 2024 Artyom Bystrov <arbars@altlinux.org> 1.15-alt2
- Fix version of quazip in patch

* Mon Jan 02 2023 Artyom Bystrov <arbars@altlinux.org> 1.15-alt1
- Initial build for Sisyphus
