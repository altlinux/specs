%define _unpackaged_files_terminate_build 1

Name: iptux
Version: 0.9.4
Release: alt1

Summary: A software for sharing in LAN
License: GPL-2.0
Group: Networking/Chat
Url: https://github.com/iptux-src/iptux

Source: %name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: gcc-c++
BuildRequires: pkgconfig(ayatana-appindicator3-0.1)
BuildRequires: pkgconfig(jsoncpp)
BuildRequires: pkgconfig(libglog)
BuildRequires: pkgconfig(gflags)
BuildRequires: pkgconfig(sigc++-2.0)
BuildRequires: /usr/bin/appstreamcli

%description
Intranet communication tool for Linux

iptux is an "IP Messenger" client for Linux.

It can:
- auto-detect other clients on the intranet.
- send message to other clients.
- send file to other clients.

It is (supposedly) compatible with Feige and FeiQ from China, and with
the original "IP Messenger" clients from Japan as listed on 
http://ipmsg.org .

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %EVR

%description devel
This package provides the development files for %name.

%prep
%setup
%patch -p1

%build
export CXXFLAGS="$CXXFLAGS -DGLOG_USE_GLOG_EXPORT -DGLOG_USE_GFLAGS"
%meson
%meson_build

%install
%meson_install
install -pDm 644 %name.1 %buildroot%_man1dir/%name.1

%find_lang %name

%files -f %{name}.lang
%doc ChangeLog LICENSE NEWS NEWS.md README.md
%_bindir/*
%_desktopdir/*.desktop
%_man1dir/*
%_iconsdir/hicolor/*/apps/*
%dir %_datadir/iptux
%_datadir/iptux/*
%_datadir/metainfo/*.metainfo.xml
%_libdir/*.so.*

%files devel
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*.pc

%changelog
* Sat Mar 15 2025 Nikolay Strelkov <snk@altlinux.org> 0.9.4-alt1
- Initial build for Sisyphus
