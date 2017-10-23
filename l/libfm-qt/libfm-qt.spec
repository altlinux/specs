%define soname 3

Name: libfm-qt
Version: 0.12.0
Release: alt1

Summary: Core library of PCManFM-Qt file manager
License: LGPLv2+
Group: System/Libraries

Url: http://lxqt.org
Source: %name-%version.tar

BuildPreReq: rpm-build-xdg
BuildRequires: intltool libmenu-cache-devel
BuildRequires: libdbus-glib-devel libudisks2-devel
BuildRequires: glib2-devel libgtk+2-devel gtk-doc
BuildRequires: vala >= 0.13.0
BuildRequires: libexif-devel
BuildRequires: libxslt-devel

BuildRequires: gcc-c++ cmake rpm-macros-cmake git-core
BuildRequires: qt5-base-devel qt5-tools-devel
BuildRequires: libqtxdg-devel

BuildRequires: pkgconfig(Qt5X11Extras)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(gio-unix-2.0)
BuildRequires: pkgconfig(libfm)
BuildRequires: pkgconfig(lxqt) >= 0.11.0
BuildRequires: kf5-kwindowsystem-devel
BuildRequires: pkgconfig(libmenu-cache) >= 0.3.0

%description
LibFM-Qt is a core library of PCManFM-Qt file manager.

%package -n %name%soname
Summary: %summary
Group: System/Libraries

%description -n %name%soname
LibFM-Qt is a core library of PCManFM-Qt file manager.

%package devel
Summary: Development files for %name
Group: Development/Other
Requires: libexif-devel libmenu-cache-devel

%description devel
This package contains files needed to build applications using LibFM-Qt.

%prep
%setup

%build
# FIXME: insource build broken upstream as of 0.12.0:
# https://pastebin.com/ExqvpJVa (notified agaida@)
#cmake_insource -DPULL_TRANSLATIONS=OFF -DUPDATE_TRANSLATIONS=OFF
%cmake -DPULL_TRANSLATIONS=OFF -DUPDATE_TRANSLATIONS=OFF
%make_build -C BUILD

%install
%makeinstall_std -C BUILD
%find_lang --with-qt %name

# We need to fix this upstream
find %buildroot -size 0 -delete

%files -n %name%soname -f libfm-qt.lang
%_libdir/*.so.*
%_datadir/%name/
%_xdgmimedir/*/*

%files devel
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*
%_datadir/cmake/fm-qt/*
%doc AUTHORS

%changelog
* Sun Oct 22 2017 Michael Shigorin <mike@altlinux.org> 0.12.0-alt1
- 0.12.0

* Tue Oct 04 2016 Michael Shigorin <mike@altlinux.org> 0.11.1-alt1
- built for sisyphus (partially based on fedora spec)

