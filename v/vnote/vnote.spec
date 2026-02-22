%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: vnote
Version: 3.20.1
Release: alt1

Summary: Pleasant note-taking platform in native C++
License: LGPL-3.0-only
Group: Editors
Url: https://app.vnote.fun/en_us/
Vcs: https://github.com/vnotex/vnote

Source: %name-%version.tar
Source1: submodules-%name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires(pre): cmake

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: qt6-tools-devel
BuildRequires: qt6-tools
BuildRequires: pkgconfig(Qt6)
BuildRequires: pkgconfig(Qt6Core5Compat)
BuildRequires: pkgconfig(Qt6Svg)
BuildRequires: pkgconfig(cups)
BuildRequires: pkgconfig(Qt6WebChannel)
BuildRequires: pkgconfig(Qt6WebEngineWidgets)

Requires: vnote-data = %version-%release

ExcludeArch: %ix86 riscv64

%description
VNote is a Qt-based, free and open source note-taking application,
focusing on Markdown now. VNote is designed to provide a pleasant
note-taking platform with excellent editing experience.

VNote is NOT just a simple editor for Markdown. By providing notes
management, VNote makes taking notes in Markdown simpler. In the future,
VNote will support more formats besides Markdown.

%package data
Summary: data files for VNote
Group: Editors
BuildArch: noarch

%description data
Data files for VNote.

%prep
%setup -a1
%patch -p1
sed -i "s|pics/||g" README.md README_zh_CN.md
sed -i "s|Categories=.*|Categories=Office;WordProcessor;|" src/data/core/vnote.desktop

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc COPYING.LESSER README.md README_zh_CN.md pics/main2.png pics/main.png pics/vnote.png
%_bindir/vnote
%_libdir/libVTextEdit.so

%files data
%_desktopdir/vnote.desktop
%_iconsdir/hicolor/*/apps/vnote.png
%_iconsdir/hicolor/scalable/apps/vnote.svg
%exclude %_datadir/translations/qtbase_ja.qm
%exclude %_datadir/translations/qtbase_zh_CN.qm
%_datadir/translations/qdialogbuttonbox_zh_CN.qm
%_datadir/translations/qtv_ja.qm
%_datadir/translations/qtv_zh_CN.qm
%_datadir/translations/qwebengine_zh_CN.qm
%_datadir/vnote_extra.rcc

%changelog
* Sun Feb 22 2026 Nikolay Strelkov <snk@altlinux.org> 3.20.1-alt1
- Initial build for Sisyphus
