# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: lxqt-session
Version: 1.2.0
Release: alt1

Summary: Session manager
License: LGPL
Group: Graphical desktop/Other

Url: https://lxqt.org
Source0: %name-%version.tar
Source1: 08lxqt
Patch: fix_XDG_CONFIG_DIRS.patch
Patch1: alt-settings.patch

BuildRequires: gcc-c++ cmake rpm-macros-cmake git-core
BuildRequires: liblxqt-devel qt5-base-devel qt5-tools-devel
BuildRequires: qtxdg-tools
BuildRequires: kf5-kwindowsystem-devel
BuildRequires: rpm-build-xdg libqtxdg-devel xdg-utils xdg-user-dirs
BuildRequires: libudev-devel
BuildRequires: libprocps-devel

Requires: lxqt-themes
Requires: xdg-utils

Provides: razorqt-session = %version
Obsoletes: razorqt-session < 0.7.0

Conflicts: lxqt-common <= 0.11.0

%description
%summary

%prep
%setup
%autopatch -p1

# https://bugzilla.altlinux.org/32657
sed -i 's,Exec=,Exec=%_bindir/,' xsession/lxqt.desktop.in

%build
%cmake -DPULL_TRANSLATIONS=OFF \
       -DUPDATE_TRANSLATIONS=OFF \
       -DBUNDLE_XDG_UTILS=No
%cmake_build

%install
%cmakeinstall_std
install -pDm644 %SOURCE1 %buildroot%_sysconfdir/X11/wmsession.d/08lxqt

%files
%_man1dir/*
%_bindir/*
%_xdgconfigdir/autostart/lxqt-xscreensaver-autostart.desktop
%_desktopdir/*.desktop
%_datadir/xsessions/*.desktop
%_datadir/lxqt/*
%_sysconfdir/X11/wmsession.d/08lxqt
%doc AUTHORS CHANGELOG LICENSE README.md

%changelog
* Sat Nov 05 2022 Anton Midyukov <antohami@altlinux.org> 1.2.0-alt1
- new version 1.2.0

* Sun Jun 19 2022 Anton Midyukov <antohami@altlinux.org> 1.1.1-alt1
- new version 1.1.1

* Sun Apr 17 2022 Anton Midyukov <antohami@altlinux.org> 1.1.0-alt1
- new version 1.1.0

* Wed Feb 23 2022 Anton Midyukov <antohami@altlinux.org> 1.0.1-alt1
- new version 1.0.1

* Fri Nov 05 2021 Anton Midyukov <antohami@altlinux.org> 1.0.0-alt1
- new version 1.0.0

* Wed Nov 03 2021 Anton Midyukov <antohami@altlinux.org> 0.17.1-alt1
- new version 0.17.1

* Fri Sep 10 2021 Anton Midyukov <antohami@altlinux.org> 0.17.0-alt2
- add /usr/share to XDG_CONFIG_DIRS, if variable is defined (Closes: 40879)

* Fri Apr 16 2021 Anton Midyukov <antohami@altlinux.org> 0.17.0-alt1
- new version 0.17.0

* Thu Nov 05 2020 Anton Midyukov <antohami@altlinux.org> 0.16.0-alt1
- new version 0.16.0

* Sat Apr 25 2020 Anton Midyukov <antohami@altlinux.org> 0.15.0-alt1
- new version 0.15.0

* Fri Mar 08 2019 Anton Midyukov <antohami@altlinux.org> 0.14.1-alt1
- new version 0.14.1

* Sun Jan 27 2019 Anton Midyukov <antohami@altlinux.org> 0.14.0-alt1
- new version 0.14.0

* Fri May 25 2018 Anton Midyukov <antohami@altlinux.org> 0.13.0-alt1
- new version 0.13.0

* Sun Oct 22 2017 Michael Shigorin <mike@altlinux.org> 0.12.0-alt1
- 0.12.0
- tweak desktop file (see also #32657)

* Mon Oct 03 2016 Michael Shigorin <mike@altlinux.org> 0.11.0-alt1
- 0.11.0

* Mon Nov 02 2015 Michael Shigorin <mike@altlinux.org> 0.10.0-alt1
- 0.10.0

* Sun Feb 08 2015 Michael Shigorin <mike@altlinux.org> 0.9.0-alt1
- 0.9.0

* Wed Oct 15 2014 Michael Shigorin <mike@altlinux.org> 0.8.0-alt1
- 0.8.0

* Wed May 14 2014 Michael Shigorin <mike@altlinux.org> 0.7.0-alt3
- replace razorqt-session

* Fri May 09 2014 Michael Shigorin <mike@altlinux.org> 0.7.0-alt2
- added wmsession file

* Thu May 08 2014 Michael Shigorin <mike@altlinux.org> 0.7.0-alt1
- initial release

