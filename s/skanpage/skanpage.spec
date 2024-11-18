
%define rname skanpage

Name: %rname
Version: 24.08.3
Release: alt1
%K6init

Group: Graphics
Summary: Multi-page scanning application
Url: http://www.kde.org
License:  GPL-2.0-or-later

ExcludeArch: %not_qt6_qtwebengine_arches

Provides:  kde5-skanpage = %EVR
Obsoletes: kde5-skanpage < %EVR

Requires: qt6-imageformats kde6-kquickimageeditor

Source: %rname-%version.tar
Patch1: alt-def-no-ocr.patch

BuildRequires(pre): rpm-build-kf6 rpm-macros-qt6-webengine
BuildRequires: extra-cmake-modules
BuildRequires: qt6-declarative-devel qt6-svg-devel qt6-wayland-devel
# libqt6-pdf from qt6-webengine
BuildRequires: qt6-webengine-devel
BuildRequires: libgomp-devel libleptonica-devel tesseract-devel
BuildRequires: kf6-kconfig-devel kf6-kcoreaddons-devel kf6-kcrash-devel kf6-ki18n-devel kf6-kirigami-devel
BuildRequires: kf6-purpose-devel kf6-kxmlgui-devel kf6-kcolorscheme-devel
BuildRequires: ksanecore-devel
BuildRequires: kde6-kquickimageeditor-devel

%description
Skanpage is a multi-page scanning application built using the libksane library and a QML interface.
It supports saving to image and PDF files.

%prep
%setup -n %rname-%version
%patch1 -p1

sed -i 's|#include <KSaneCore/|#include <KSaneCore6/|' src/*.{h,cpp}

%build
%K6build

%install
%K6install
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc LICENSES/*
%_K6bin/skanpage
%_K6xdgapp/*skanpage*.desktop
%_K6icon/hicolor/*/apps/*skanpage*
%_datadir/qlogging-categories6/*.*categories
%_datadir/metainfo/*.xml


%changelog
* Mon Nov 18 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.3-alt1
- new version

* Thu Oct 17 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.2-alt1
- initial build

