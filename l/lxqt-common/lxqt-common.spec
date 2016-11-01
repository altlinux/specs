Name: lxqt-common
Version: 0.11.0
Release: alt1.1
Serial: 1

Summary: Default configuration files for LXQt desktop session
License: LGPL
Group: Graphical desktop/Other

Url: http://lxqt.org
Source: %name-%version.tar
Packager: Michael Shigorin <mike@altlinux.org>

BuildArch: noarch

BuildRequires: gcc-c++ cmake rpm-macros-cmake
BuildRequires: liblxqt-devel qt5-base-devel qt5-tools-devel libqtxdg-devel
BuildRequires: kf5-kwindowsystem-devel
BuildRequires: rpm-build-xdg

Requires: dbus-tools-gui
Requires: lxqt-l10n

Provides: razorqt = %version
Obsoletes: razorqt < 0.7.0

Provides: razorqt-desktop = %version
Obsoletes: razorqt-desktop < 0.7.0

%description
%summary

%prep
%setup
# https://bugzilla.altlinux.org/32657
sed -i 's,Exec=,Exec=%_bindir/,' xsession/lxqt.desktop.in

%build
%cmake_insource
%make_build

%install
%makeinstall_std

%files
%_man1dir/*
%_bindir/*
%_xdgconfigdir/*/*
%_datadir/kdm/sessions/*.desktop
%_datadir/xsessions/*.desktop
%_datadir/lxqt/
%_datadir/desktop-directories/lxqt-*.directory
%_iconsdir/*/*/*/*

%changelog
* Tue Oct 25 2016 Michael Shigorin <mike@altlinux.org> 1:0.11.0-alt1.1
- tweak desktop file differently (closes: #32657)

* Mon Oct 03 2016 Michael Shigorin <mike@altlinux.org> 1:0.11.0-alt1
- 0.11.0
- R: lxqt-l10n for translations

* Mon Nov 02 2015 Michael Shigorin <mike@altlinux.org> 1:0.10.0-alt1
- 0.10.0

* Wed Oct 07 2015 Michael Shigorin <mike@altlinux.org> 1:0.9.0-alt1.1
- rollback to 0.9.0 for the time being (regressions)

* Tue Aug 04 2015 Michael Shigorin <mike@altlinux.org> 0.9.1-alt1
- 0.9.1

* Sun Feb 08 2015 Michael Shigorin <mike@altlinux.org> 0.9.0-alt1
- 0.9.0

* Wed Dec 10 2014 Michael Shigorin <mike@altlinux.org> 0.8.0-alt2
- tweaked xsession file for runwm compatibility (see runwm --list)

* Wed Oct 15 2014 Michael Shigorin <mike@altlinux.org> 0.8.0-alt1
- 0.8.0

* Wed May 14 2014 Michael Shigorin <mike@altlinux.org> 0.7.0-alt4
- replace razorqt, razorqt-desktop

* Tue May 13 2014 Michael Shigorin <mike@altlinux.org> 0.7.0-alt3
- noarch

* Fri May 09 2014 Michael Shigorin <mike@altlinux.org> 0.7.0-alt2
- added missing Requires:

* Thu May 08 2014 Michael Shigorin <mike@altlinux.org> 0.7.0-alt1
- initial release

