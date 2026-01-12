%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: maui-clip
Version: 4.0.2
Release: alt1

Summary: Video player and video collection manager based on Maui framework
License: LGPL-3.0-only
Group: Graphical desktop/Other
Url: https://invent.kde.org/maui/clip

Source: %name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-cmake

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: extra-cmake-modules
BuildRequires: pkgconfig(Qt6)
BuildRequires: pkgconfig(Qt6Qml)
BuildRequires: pkgconfig(Qt6Multimedia)
BuildRequires: kf6-ki18n-devel
BuildRequires: kf6-kcoreaddons-devel
BuildRequires: pkgconfig(taglib)
BuildRequires: kf6-kdbusaddons-devel
BuildRequires: pkgconfig(libavfilter)
BuildRequires: pkgconfig(libavdevice)
BuildRequires: pkgconfig(libpostproc)
BuildRequires: libmauikit-devel
BuildRequires: libmauikit-filebrowsing-devel

# no libqt6-webviewquick
ExcludeArch: %ix86 riscv64

Requires: libqt6-multimediaquick
Requires: libmauikit
Requires: libmauikit-filebrowsing
Requires: maui-vvave
Requires: libqt6-webviewquick

%description
%summary.

%prep
%setup
%patch -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%find_lang clip

# prevent file conflict with other packages
mv -v %buildroot%_bindir/clip %buildroot%_bindir/org.kde.clip
sed -i "s|Exec=clip|Exec=org.kde.clip|" %buildroot%_desktopdir/org.kde.clip.desktop

%files -f clip.lang
%_bindir/org.kde.clip
%_desktopdir/org.kde.clip.desktop
%_iconsdir/hicolor/scalable/apps/clip.svg
%_datadir/metainfo/org.kde.clip.appdata.xml

%changelog
* Fri Jan 09 2026 Nikolay Strelkov <snk@altlinux.org> 4.0.2-alt1
- Initial build for Sisyphus
