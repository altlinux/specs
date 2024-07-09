# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: lxqt-session
Version: 2.0.0
Release: alt1

Summary: Session manager
License: LGPL-2.1
Group: Graphical desktop/Other

Url: https://github.com/lxqt/lxqt-session
Source0: %name-%version.tar
Source1: 08lxqt
Patch: fix_XDG_CONFIG_DIRS.patch
Patch1: alt-settings.patch

BuildRequires: gcc-c++ cmake rpm-macros-cmake git-core
BuildRequires: lxqt2-build-tools
BuildRequires: liblxqt-devel >= 2.0.0
BuildRequires: qt6-base-devel qt6-tools-devel
BuildRequires: qtxdg-tools-devel >= 4.0.0
BuildRequires: kf6-kwindowsystem-devel
BuildRequires: libqt6xdg-devel
BuildRequires: rpm-build-xdg xdg-utils xdg-user-dirs
BuildRequires: plasma6-layer-shell-qt-devel
BuildRequires: libudev-devel
BuildRequires: libproc2-devel

Requires: lxqt-themes
Requires: xdg-utils
Requires: qtxdg-tools >= 4.0.0

Provides: razorqt-session = %version
Obsoletes: razorqt-session < 0.7.0

Conflicts: lxqt-common <= 0.11.0

%description
%summary.

%prep
%setup
%autopatch -p1

# https://bugzilla.altlinux.org/32657
sed -i 's,Exec=,Exec=%_bindir/,' xsession/lxqt.desktop.in

%build
%add_optflags -I%_includedir/KF6/ -L%_libdir/kf6/devel/
%cmake -DPULL_TRANSLATIONS=OFF \
       -DUPDATE_TRANSLATIONS=OFF \
       -DBUNDLE_XDG_UTILS=No
%cmake_build

%install
%cmake_install
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
* Mon Jul 08 2024 Anton Midyukov <antohami@altlinux.org> 2.0.0-alt1
- New version 2.0.0

* Tue Apr 16 2024 Anton Midyukov <antohami@altlinux.org> 1.4.0-alt2
- Requires: qtxdg-tools >= 3.12.0-alt2

* Sun Nov 05 2023 Anton Midyukov <antohami@altlinux.org> 1.4.0-alt1
- New version 1.4.0.

* Wed Oct 11 2023 Anton Midyukov <antohami@altlinux.org> 1.3.0-alt2
- rebuild with libproc2-devel

* Sat Apr 15 2023 Anton Midyukov <antohami@altlinux.org> 1.3.0-alt1
- New version 1.3.0.

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

