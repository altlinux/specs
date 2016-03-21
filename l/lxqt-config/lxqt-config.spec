Name: lxqt-config
Version: 0.10.0
Release: alt2

Summary: LXDE-Qt system configurations (control center)
License: LGPL
Group: Graphical desktop/Other

Url: http://lxqt.org
Source: %name-%version.tar
Packager: Michael Shigorin <mike@altlinux.org>

BuildRequires: gcc-c++ cmake rpm-macros-cmake
BuildRequires: libXau-devel libXcursor-devel libXdmcp-devel libXfixes-devel
BuildRequires: liblxqt-devel libqtxdg-devel qt5-base-devel qt5-tools-devel
BuildRequires: kf5-kwindowsystem-devel kf5-libkscreen-devel qt5-svg-devel
BuildRequires: rpm-build-xdg
BuildRequires: zlib-devel

Provides: razorqt-config = %version
Obsoletes: razorqt-config < 0.7.0

Provides: lxqt-config-randr = %version
Obsoletes: lxqt-config-randr < 0.8.0

%description
%summary

%prep
%setup

%build
# FIXME: 0.10.0 fiddling with liblxqt-config-cursor.so (thx palinek)
%cmake_insource -DCMAKE_SKIP_RPATH:BOOL=OFF -DCMAKE_SKIP_INSTALL_RPATH:BOOL=OFF
%make_build

%install
%makeinstall_std

%files
%_bindir/*
%_libdir/%name/*.so
%_datadir/lxqt/*
%_xdgconfigdir/*/*
%_desktopdir/*.desktop
%doc AUTHORS

%changelog
* Wed Mar 23 2016 Michael Shigorin <mike@altlinux.org> 0.10.0-alt2
- rebuilt against KF5 5.6.0

* Mon Nov 02 2015 Michael Shigorin <mike@altlinux.org> 0.10.0-alt1
- 0.10.0

* Mon Feb 09 2015 Michael Shigorin <mike@altlinux.org> 0.9.0-alt1
- 0.9.0

* Wed Oct 15 2014 Michael Shigorin <mike@altlinux.org> 0.8.0-alt1
- 0.8.0
- lxqt-config-monitor replaces lxqt-config-randr

* Wed May 14 2014 Michael Shigorin <mike@altlinux.org> 0.7.0-alt2
- replace razorqt-config

* Tue May 13 2014 Michael Shigorin <mike@altlinux.org> 0.7.0-alt1
- initial release

