#
# spec file for package qtrvsim
#
# Copyright (c) 2017-2019 Karel Koci <cynerd@email.cz>
# Copyright (c) 2019-2023 Pavel Pisa <pisa@cmp.felk.cvut.cz>
# Copyright (c) 2020-2023 Jakub Dupak <dev@jakubdupak.com>
# Copyright (c) 2020-2021 Max Hollmann <hollmmax@fel.cvut.cz>
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for
# more details.

# You should have received a copy of the GNU General Public License along with
# this program. If not, see <https://www.gnu.org/licenses/>
#
# Please submit bugfixes or comments via
#
# issues tracker.
#

Name: qtrvsim
Version: 0.9.6
Release: alt1
Summary: RISC-V CPU simulator for education purposes
License: GPLv3+
Group: Emulators
Url: https://github.com/cvut/qtrvsim
Source: qtrvsim_0.9.6.orig.tar.xz
Patch: qtrvsim-return-type.patch
Patch101: 0001-GUI-fix-crash-when-no-tab-is-selected.patch


# Automatically added by buildreq on Tue Feb 06 2024
# optimized out: bash5 cmake-modules gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 libdouble-conversion3 libglvnd-devel libgpg-error libp11-kit libqt5-core libqt5-gui libqt5-printsupport libqt5-test libqt5-widgets libsasl2-3 libssl-devel libstdc++-devel pkg-config python3 python3-base python3-dev qt5-base-devel sh5 xz
BuildRequires: cmake ctest python3-module-setuptools qt5-svg-devel qt5-virtualkeyboard-devel qt5-wayland-devel 

%ifnarch ppc64le
BuildRequires: qt5-webengine-devel qt5-webglplugin-devel
%endif

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5Test)
BuildRequires: pkgconfig(Qt5PrintSupport)
BuildRequires: hicolor-icon-theme
BuildRequires: desktop-file-utils

%description
RISC-V CPU simulator for education purposes with pipeline and cache visualization.

%prep
%setup
%patch -p1
%patch101 -p1 

%build
%cmake
%cmake_build

%install
%cmake_install

#desktop icon
install -D data/icons/gui.svg %buildroot%_iconsdir/hicolor/scalable/apps/%{name}_gui.svg
install -D data/icons/48x48/gui.png %buildroot%_liconsdir/%{name}_gui.png
install -D %_cmake__builddir/target/qtrvsim.desktop %buildroot%_desktopdir/%name.desktop
install -D %_cmake__builddir/target/cz.cvut.edu.comparch.qtrvsim.metainfo.xml %buildroot%_datadir/metainfo/cz.cvut.edu.comparch.qtrvsim.metainfo.xml

desktop-file-validate %buildroot/usr/share/applications/qtrvsim.desktop

%check
make -C %_cmake__builddir test

%files
/usr/bin/qtrvsim_gui
/usr/bin/qtrvsim_cli
/usr/share/icons/hicolor/scalable/apps/qtrvsim_gui.svg
/usr/share/icons/hicolor/48x48/apps/qtrvsim_gui.png
/usr/share/applications/qtrvsim.desktop
/usr/share/metainfo/cz.cvut.edu.comparch.qtrvsim.metainfo.xml

%doc README.md docs/user/*.md

%changelog
* Tue Feb 06 2024 Fr. Br. George <george@altlinux.ru> 0.9.6-alt1
- Initial build for ALT
