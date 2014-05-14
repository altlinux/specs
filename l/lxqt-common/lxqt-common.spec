Name: lxqt-common
Version: 0.7.0
Release: alt4

Summary: Default configuration files for LXQt desktop session
License: LGPL
Group: Graphical desktop/Other

Url: http://lxqt.org
Source: %name-%version.tar
Packager: Michael Shigorin <mike@altlinux.org>

BuildArch: noarch

BuildRequires: gcc-c++ cmake rpm-macros-cmake
BuildRequires: liblxqt-devel libqt4-devel
BuildRequires: rpm-build-xdg

Requires: dbus-tools-gui

Provides: razorqt = %version
Obsoletes: razorqt < 0.7.0

Provides: razorqt-desktop = %version
Obsoletes: razorqt-desktop < 0.7.0

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
%_xdgconfigdir/*/*
%_datadir/apps/kdm/sessions/*.desktop
%_datadir/xsessions/*.desktop
%_datadir/lxqt/

%changelog
* Wed May 14 2014 Michael Shigorin <mike@altlinux.org> 0.7.0-alt4
- replace razorqt, razorqt-desktop

* Tue May 13 2014 Michael Shigorin <mike@altlinux.org> 0.7.0-alt3
- noarch

* Fri May 09 2014 Michael Shigorin <mike@altlinux.org> 0.7.0-alt2
- added missing Requires:

* Thu May 08 2014 Michael Shigorin <mike@altlinux.org> 0.7.0-alt1
- initial release

