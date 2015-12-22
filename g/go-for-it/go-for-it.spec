Name: go-for-it
Version: 1.4
Release: alt2

Summary: Go For It! is a simple and stylish to-do list
License: GPLv3
Group: Office
Url: https://github.com/mank319/Go-For-It

Packager: Konstantin Artyushkin <akv@altlinux.org>
Source: %name-%version.tar

BuildPreReq: cmake rpm-macros-cmake libvala-devel libgtk+3-devel libnotify-devel
BuildRequires: gcc5-c++ gtk-update-icon-cache libpixman-devel libharfbuzz-devel
#BuildRequires: libexpat-devel libdrm-devel libXdmcp-devel libXdamage-devel 
#BuildRequires: libxshmfence-devel libXxf86vm-devel  libpng-devel libXinerama-devel 

%description
_Go For It!_ is free and open source software licensed under the GPLv3.
It has been written in _Vala_ making heavy use of the _GTK_ framework.

%prep
%setup

%build
%cmake
pushd BUILD
%make_build # VERBOSE=1
popd

%install
pushd BUILD
%makeinstall_std
popd
%find_lang %name

%files -f %name.lang
%doc AUTHORS README.md  COPYING
%_bindir/*
%_desktopdir/go-for-it.desktop
%_datadir/go-for-it/style/go-for-it.css
%_iconsdir/hicolor/*/apps/go-for-it.svg
%_iconsdir/hicolor/24x24/actions/go-for-it-open-menu-fallback.svg

%changelog
* Sat Dec 19 2015 Konstantin Artyushkin <akv@altlinux.org> 1.4-alt2
- initial build for ALT Linux Sisyphus

