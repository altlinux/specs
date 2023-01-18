
%define rname skanpage

Name: kde5-%rname
Version: 22.12.1
Release: alt1
%K5init altplace

Group: Graphics
Summary: Multi-page scanning application
Url: http://www.kde.org
License:  GPL-2.0-or-later

Requires: qt5-imageformats

Source: %rname-%version.tar
Patch1: alt-def-no-ocr.patch

# Automatically added by buildreq on Thu Sep 22 2022 (-bi)
# optimized out: cmake cmake-modules debugedit elfutils gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 libctf-nobfd0 libglvnd-devel libgpg-error libleptonica-devel libqt5-concurrent libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-printsupport libqt5-qml libqt5-qmlmodels libqt5-quick libqt5-quickcontrols2 libqt5-widgets libqt5-x11extras libqt5-xml libsasl2-3 libssl-devel libstdc++-devel libxcbutil-keysyms python-modules python2-base python3 python3-base python3-dev python3-module-paste qt5-base-devel qt5-declarative-devel rpm-build-file rpm-build-python3 sh4 tesseract tzdata
#BuildRequires: appstream clang-tools extra-cmake-modules gtk4-update-icon-cache kde5-ksanecore-devel kf5-kconfig-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-ki18n-devel kf5-kirigami-devel kf5-purpose-devel libgomp-devel lua5.3 python3-module-setuptools python3-module-zope qt5-imageformats qt5-quickcontrols2-devel qt5-svg-devel qt5-wayland-devel qt5-webengine-devel tbb-devel tesseract-devel
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules
BuildRequires: qt5-quickcontrols2-devel qt5-svg-devel qt5-wayland-devel
BuildRequires: libgomp-devel libleptonica-devel tesseract-devel
BuildRequires: kf5-kconfig-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-ki18n-devel kf5-kirigami-devel
BuildRequires: kf5-purpose-devel
BuildRequires: kde5-ksanecore-devel

%description
Skanpage is a multi-page scanning application built using the libksane library and a QML interface.
It supports saving to image and PDF files.

%prep
%setup -n %rname-%version
%patch1 -p1

%build
%K5build

%install
%K5install
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc LICENSES/*
%_K5bin/skanpage
%_K5xdgapp/*skanpage*.desktop
%_K5icon/hicolor/*/apps/*skanpage*
%_datadir/qlogging-categories5/*.*categories

%changelog
* Tue Jan 17 2023 Sergey V Turchin <zerg@altlinux.org> 22.12.1-alt1
- new version

* Mon Nov 07 2022 Sergey V Turchin <zerg@altlinux.org> 22.08.3-alt1
- new version

* Tue Oct 18 2022 Sergey V Turchin <zerg@altlinux.org> 22.08.2-alt1
- new version

* Thu Sep 22 2022 Sergey V Turchin <zerg@altlinux.org> 22.08.1-alt2
- disable OCR on save by default

* Thu Sep 22 2022 Sergey V Turchin <zerg@altlinux.org> 22.08.1-alt1
- initial build
