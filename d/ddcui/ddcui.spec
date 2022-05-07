Name: ddcui
Version: 0.2.1
Release: alt1

Summary: Graphical utility to query and update monitor settings
Group: System/Configuration/Hardware
License: GPLv2+
Url: http://github.com/rockowitz/%name

Source: %url/archive/v%version/%name-%version.tar.gz

%define ddcutil_ver 1.2.0
%define qt_ver 5.5

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake pkgconfig(glib-2.0)
BuildRequires: libddcutil-devel >= %ddcutil_ver
BuildRequires: pkgconfig(Qt5Widgets) >= %qt_ver
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Help)

%description
%name is a graphical user interface for ddcutil.


%prep
%setup

%build
%cmake \
    -DCMAKE_INSTALL_DOCDIR:STRING="%_defaultdocdir/%name-%version"
%cmake_build

%install
%cmake_install

%files
%_bindir/%name
%_desktopdir/%name.desktop
%_man1dir/%name.1*
%_iconsdir/hicolor/*x*/apps/*.png
%_datadir/metainfo/%name.appdata.xml
%doc AUTHORS NEWS.md README.md CHANGELOG.md

%changelog
* Sat May 07 2022 Yuri N. Sedunov <aris@altlinux.org> 0.2.1-alt1
- first build for Sisyphus


