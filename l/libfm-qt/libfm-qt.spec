%define soname 3

Name: libfm-qt
Version: 0.11.1
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

%description devel
This package contains files needed to build applications using LibFM-Qt.

%prep
%setup

%build
%cmake_insource -DPULL_TRANSLATIONS=OFF -DUPDATE_TRANSLATIONS=OFF
%make_build

%install
%makeinstall_std
%find_lang --with-qt %name

# We need to fix this upstream
find %{buildroot} -size 0 -delete

%files -n %name%soname -f libfm-qt.lang
#_xdgconfigdir/*
%_libdir/*.so.*
#_libdir/%name/modules/*.so
#_xdgmimedir/packages/*
#_datadir/%name/

%files devel
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*
%_datadir/cmake/fm-qt/*
%doc AUTHORS

%changelog
* Tue Oct 04 2016 Michael Shigorin <mike@altlinux.org> 0.11.1-alt1
- built for sisyphus (partially based on fedora spec)

