%define realname go-for-it

Name: go-for-it
Version: 1.6.3
Release: alt1

Summary: Go For It! is a simple and stylish to-do list
License: GPLv3
Group: Office
Url: https://github.com/mank319/Go-For-It

Source: %name-%version.tar

BuildRequires: cmake rpm-macros-cmake libvala-devel libgtk+3-devel libnotify-devel
BuildRequires: gcc5-c++ gtk-update-icon-cache libpixman-devel libharfbuzz-devel
BuildRequires: intltool

%description
_Go For It!_ is free and open source software licensed under the GPLv3.
It has been written in _Vala_ making heavy use of the _GTK_ framework.

%prep
%setup

%build
%cmake -DAPP_SYSTEM_NAME:STRING="go-for-it"
%cmake_build # VERBOSE=1

%install
%cmakeinstall_std
%find_lang %realname

%files -f %realname.lang
%doc AUTHORS README.md  COPYING
%_bindir/*
%_desktopdir/%realname.desktop
%_datadir/%realname/*
%_datadir/metainfo/%realname.appdata.xml
%_iconsdir/hicolor/*/apps/%realname.svg
%_iconsdir/hicolor/24x24/actions/%realname-open-menu-fallback.svg

%changelog
* Mon Jan 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.6.3-alt1
- Updated to upstream version 1.6.3.

* Sat Dec 19 2015 Konstantin Artyushkin <akv@altlinux.org> 1.4-alt2
- initial build for ALT Linux Sisyphus

