Name: lxqt-powermanagement
Version: 0.8.0
Release: alt2

Summary: Powermanagement module for LXQt
License: LGPL
Group: Graphical desktop/Other

Url: http://lxqt.org
Source: %name-%version.tar
Packager: Michael Shigorin <mike@altlinux.org>

BuildRequires: gcc-c++ cmake rpm-macros-cmake
BuildRequires: liblxqt-devel libqt4-devel
BuildRequires: libqtxdg-devel

Requires: upower

Provides: razorqt-autosuspend = %version
Obsoletes: razorqt-autosuspend < 0.7.0

Provides: razorqt-power = %version
Obsoletes: razorqt-power < 0.7.0

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
%_desktopdir/*.desktop
%_iconsdir/*/*/*/*.svg
%doc AUTHORS

%changelog
* Tue Nov 25 2014 Michael Shigorin <mike@altlinux.org> 0.8.0-alt2
- added Requires: upower (closes: #30507)

* Wed Oct 15 2014 Michael Shigorin <mike@altlinux.org> 0.8.0-alt1
- 0.8.0

* Wed May 14 2014 Michael Shigorin <mike@altlinux.org> 0.7.0-alt2
- replace razorqt-autosuspend, razorqt-power

* Thu May 08 2014 Michael Shigorin <mike@altlinux.org> 0.7.0-alt1
- initial release

