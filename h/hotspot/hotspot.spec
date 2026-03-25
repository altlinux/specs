%define _unpackaged_files_terminate_build 1
%define _libexecdir %prefix/libexec

Name: hotspot
Version: 1.6.0
Release: alt1

Summary: The Linux perf GUI for performance analysis
License: GPL-2.0
Group: Development/Other
Url: https://github.com/KDAB/hotspot
Vcs: https://github.com/KDAB/hotspot

Source0: %name-%version.tar
Source1: %name-vendors-%version.tar

Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-macros-qt6
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: qt6-qtbase
BuildRequires: qt6-base-devel
BuildRequires: qt6-svg-devel
BuildRequires: qt6-declarative-devel
BuildRequires: extra-cmake-modules
BuildRequires: kf6-threadweaver-devel
BuildRequires: kf6-kconfigwidgets-devel
BuildRequires: kf6-kcoreaddons-devel
BuildRequires: kf6-kitemmodels-devel
BuildRequires: kf6-kitemviews-devel
BuildRequires: kf6-kio-devel
BuildRequires: kf6-solid-devel
BuildRequires: kf6-kwindowsystem-devel
BuildRequires: kf6-knotifications-devel
BuildRequires: kf6-kiconthemes-devel
BuildRequires: kf6-kparts-devel
BuildRequires: kf6-ki18n-devel
BuildRequires: libkddockwidgets-qt6-devel
BuildRequires: libappstream-glib
BuildRequires: elfutils-devel
BuildRequires: libzstd-devel
BuildRequires: binutils
BuildRequires: kf6-syntax-highlighting-devel
BuildRequires: kgraphviewer-devel
BuildRequires: gettext

%description
This project is a KDAB R&D effort to create a standalone GUI for performance
data. As the first goal, we want to provide a UI like KCachegrind around Linux
perf. Looking ahead, we intend to support various other performance data
formats under this umbrella.

%prep
%setup -a 1
%autopatch1 -p1

%build
%Q6build -DQT6_BUILD=TRUE

%install
ln -sf %_licensedir/GPL-2.0 LICENSE.GPL.txt
DESTDIR=%buildroot cmake --install BUILD --prefix /usr
appstream-util validate-relax --nonet %buildroot%_datadir/metainfo/*.appdata.xml
desktop-file-validate %buildroot%_datadir/applications/com.kdab.hotspot.desktop

%files
%doc --no-dereference LICENSE.GPL.txt
%doc README.md
%_bindir/hotspot
%_iconsdir/hicolor/*/*/hotspot*
%_libexecdir/hotspot-perfparser
%_desktopdir/com.kdab.hotspot.desktop
%_datadir/metainfo/com.kdab.Hotspot.appdata.xml
%_datadir/knotifications6/hotspot.notifyrc
%_datadir/mime/packages/com.kdab.hotspot.xml

%changelog
* Tue Mar 03 2026 Maxim Tulskiy <tulskijms@altlinux.org> 1.6.0-alt1
- Updated to new version v1.6.0.

* Tue Jan 27 2026 Maxim Tulskiy <tulskijms@altlinux.org> 1.5.1-alt1
- Initial build for ALT Sisyphus.
