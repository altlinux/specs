Name: lxqt-config
Version: 0.9.0
Release: alt1

Summary: LXDE-Qt system configurations (control center)
License: LGPL
Group: Graphical desktop/Other

Url: http://lxqt.org
Source: %name-%version.tar
Packager: Michael Shigorin <mike@altlinux.org>

BuildRequires: gcc-c++ cmake rpm-macros-cmake
BuildRequires: libXau-devel libXcursor-devel libXdmcp-devel libXfixes-devel
BuildRequires: liblxqt-devel libqtxdg-devel qt5-base-devel qt5-tools-devel
BuildRequires: kf5-kwindowsystem-devel
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
%cmake_insource
%make_build

%install
%makeinstall_std

%files
%_bindir/*
%_libdir/*.so
%_datadir/lxqt/*
%_xdgconfigdir/*/*
%_desktopdir/*.desktop
%doc AUTHORS

%changelog
* Mon Feb 09 2015 Michael Shigorin <mike@altlinux.org> 0.9.0-alt1
- 0.9.0

* Wed Oct 15 2014 Michael Shigorin <mike@altlinux.org> 0.8.0-alt1
- 0.8.0
- lxqt-config-monitor replaces lxqt-config-randr

* Wed May 14 2014 Michael Shigorin <mike@altlinux.org> 0.7.0-alt2
- replace razorqt-config

* Tue May 13 2014 Michael Shigorin <mike@altlinux.org> 0.7.0-alt1
- initial release

