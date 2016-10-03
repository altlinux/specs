Name: lxqt-powermanagement
Version: 0.11.0
Release: alt1

Summary: Powermanagement module for LXQt
License: LGPL
Group: Graphical desktop/Other

Url: http://lxqt.org
Source: %name-%version.tar
Packager: Michael Shigorin <mike@altlinux.org>

BuildRequires: gcc-c++ cmake rpm-macros-cmake git-core
BuildRequires: liblxqt-devel qt5-base-devel qt5-tools-devel qt5-svg-devel
BuildRequires: kf5-kwindowsystem-devel kf5-solid-devel kf5-kidletime-devel
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
%cmake_insource -DPULL_TRANSLATIONS=OFF -DUPDATE_TRANSLATIONS=OFF
%make_build

%install
%makeinstall_std

%files
%_bindir/*
%_desktopdir/*.desktop
%_iconsdir/*/*/*/*.svg
%doc AUTHORS

%changelog
* Mon Oct 03 2016 Michael Shigorin <mike@altlinux.org> 0.11.0-alt1
- 0.11.0

* Mon Nov 02 2015 Michael Shigorin <mike@altlinux.org> 0.10.0-alt1
- 0.10.0

* Sun Feb 08 2015 Michael Shigorin <mike@altlinux.org> 0.9.0-alt1
- 0.9.0

* Tue Nov 25 2014 Michael Shigorin <mike@altlinux.org> 0.8.0-alt2
- added Requires: upower (closes: #30507)

* Wed Oct 15 2014 Michael Shigorin <mike@altlinux.org> 0.8.0-alt1
- 0.8.0

* Wed May 14 2014 Michael Shigorin <mike@altlinux.org> 0.7.0-alt2
- replace razorqt-autosuspend, razorqt-power

* Thu May 08 2014 Michael Shigorin <mike@altlinux.org> 0.7.0-alt1
- initial release

