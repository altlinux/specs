%define _unpackaged_files_terminate_build 1

Name: coolreader-ng
Version: 1.1.2
Release: alt1

Summary: Cross-platform open source e-book reader using crengine-ng
License: GPL-2.0-or-later
Group: Books/Computer books
Url: https://gitlab.com/coolreader-ng/crqt-ng
VCS: https://gitlab.com/coolreader-ng/crqt-ng.git

Source: %name-%version.tar
Patch0: %name-%version-alt-ru-l10n.patch

Provides: coolreader
Requires: qt6-translations

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libcrengine-ng-devel
BuildRequires: libfreetype-devel
BuildRequires: libfribidi-devel
BuildRequires: libjpeg-devel
BuildRequires: libpng-devel
BuildRequires: libunibreak-devel
BuildRequires: libutf8proc-devel
BuildRequires: libzstd-devel
BuildRequires: qt6-tools-devel
BuildRequires: qt6-base-devel
BuildRequires: qt6-svg-devel
BuildRequires: zlib-devel

%description
%summary.

%prep
%setup
%patch0 -p1

%build
%cmake \
  -DCMAKE_BUILD_TYPE=Release \
  -DCMAKE_CXX_STANDARD=17 \
  -DUSE_QT=QT6 \
  %nil
%cmake_build

%install
%cmake_install

%files
%doc AUTHORS README.md
%_bindir/crqt
%_datadir/applications/io.gitlab.coolreader_ng.crqt-ng.desktop
%_datadir/crqt/backgrounds
%_datadir/crqt/i18n
%_datadir/crqt/textures
%_datadir/icons/hicolor/*/apps/crqt.png
%_datadir/icons/hicolor/scalable/apps/crqt.svg
%_datadir/metainfo/io.gitlab.coolreader_ng.crqt-ng.metainfo.xml

%changelog
* Mon Nov 23 2026 Anton Farygin <rider@altlinux.org> 1.1.2-alt1
- 1.0.15 -> 1.1.2
- Completed the Russian translation.

* Tue Dec 17 2024 Constantin Sunzow <protvin@altlinux.org> 1.0.15-alt1
- Initial build (ALT bug 52053).
