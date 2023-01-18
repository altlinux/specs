%define rname dolphin-plugins

Name: kde5-%rname
Version: 22.12.1
Release: alt1
%K5init altplace no_appdata

Group: Graphical desktop/KDE
Summary: KDE Dolphin plugins
Url: http://www.kde.org
License: GPL-2.0-or-later

Source: %rname-%version.tar

# Automatically added by buildreq on Tue Jan 12 2016 (-bi)
# optimized out: cmake cmake-modules elfutils gcc-c++ kf5-kdoctools-devel libEGL-devel libGL-devel libdbusmenu-qt52 libgpg-error libjson-c libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-printsupport libqt5-script libqt5-svg libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libxcbutil-keysyms python-base python-modules python3 python3-base ruby ruby-stdlibs
#BuildRequires: extra-cmake-modules kde5-dolphin-devel kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdelibs4support kf5-kdelibs4support-devel kf5-kdesignerplugin-devel kf5-kdoctools kf5-kdoctools-devel kf5-kemoticons-devel kf5-kguiaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kinit-devel kf5-kio-devel kf5-kitemmodels-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-knotifications-devel kf5-kparts-devel kf5-kservice-devel kf5-ktexteditor-devel kf5-ktextwidgets-devel kf5-kunitconversion-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel python-module-google qt5-base-devel rpm-build-python3 rpm-build-ruby
BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
BuildRequires: extra-cmake-modules qt5-base-devel
BuildRequires: kde5-dolphin-devel
BuildRequires: kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel
BuildRequires: kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel
BuildRequires: kf5-kdelibs4support kf5-kdelibs4support-devel
BuildRequires: kf5-kdesignerplugin-devel kf5-kdoctools kf5-kdoctools-devel kf5-kemoticons-devel kf5-kguiaddons-devel
BuildRequires: kf5-ki18n-devel kf5-kiconthemes-devel kf5-kinit-devel kf5-kio-devel kf5-kitemmodels-devel kf5-kitemviews-devel
BuildRequires: kf5-kjobwidgets-devel kf5-knotifications-devel kf5-kparts-devel kf5-kservice-devel kf5-ktexteditor-devel
BuildRequires: kf5-ktextwidgets-devel kf5-kunitconversion-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel
BuildRequires: kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel kf5-syntax-highlighting-devel

%description
%summary.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf5-filesystem
%description common
%name common package


%prep
%setup -n %rname-%version

%build
%K5build

%install
%K5install
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc LICENSES/*
%_K5plug/dolphin/vcs/*fileview*.so
%_K5plug/kf5/kfileitemaction/*.so
%_K5cfg/fileview*pluginsettings.kcfg
#%_K5srv/fileview*plugin.desktop

%changelog
* Tue Jan 17 2023 Sergey V Turchin <zerg@altlinux.org> 22.12.1-alt1
- new version

* Mon Nov 07 2022 Sergey V Turchin <zerg@altlinux.org> 22.08.3-alt1
- new version

* Tue Oct 18 2022 Sergey V Turchin <zerg@altlinux.org> 22.08.2-alt1
- new version

* Tue Sep 20 2022 Sergey V Turchin <zerg@altlinux.org> 22.08.1-alt1
- new version

* Mon Jul 11 2022 Sergey V Turchin <zerg@altlinux.org> 22.04.3-alt1
- new version

* Fri Jun 10 2022 Sergey V Turchin <zerg@altlinux.org> 22.04.2-alt1
- new version

* Thu May 19 2022 Sergey V Turchin <zerg@altlinux.org> 22.04.1-alt1
- new version

* Fri Mar 04 2022 Sergey V Turchin <zerg@altlinux.org> 21.12.3-alt1
- new version

* Tue Jan 18 2022 Sergey V Turchin <zerg@altlinux.org> 21.12.1-alt1
- new version

* Mon Nov 08 2021 Sergey V Turchin <zerg@altlinux.org> 21.08.3-alt1
- new version

* Fri Oct 08 2021 Sergey V Turchin <zerg@altlinux.org> 21.08.2-alt1
- new version

* Thu Sep 02 2021 Sergey V Turchin <zerg@altlinux.org> 21.08.1-alt1
- new version

* Thu Aug 26 2021 Sergey V Turchin <zerg@altlinux.org> 21.08.0-alt1
- new version

* Thu Jul 08 2021 Sergey V Turchin <zerg@altlinux.org> 21.04.3-alt1
- new version

* Fri Jun 11 2021 Sergey V Turchin <zerg@altlinux.org> 21.04.2-alt1
- new version

* Thu May 20 2021 Sergey V Turchin <zerg@altlinux.org> 21.04.1-alt1
- new version

* Fri Mar 12 2021 Sergey V Turchin <zerg@altlinux.org> 20.12.3-alt1
- new version

* Wed Feb 17 2021 Sergey V Turchin <zerg@altlinux.org> 20.12.2-alt2
- update build requries

* Fri Feb 05 2021 Sergey V Turchin <zerg@altlinux.org> 20.12.2-alt1
- new version

* Fri Jan 15 2021 Sergey V Turchin <zerg@altlinux.org> 20.12.1-alt1
- new version

* Mon Dec 21 2020 Sergey V Turchin <zerg@altlinux.org> 20.12.0-alt1
- new version

* Wed Nov 25 2020 Sergey V Turchin <zerg@altlinux.org> 20.08.3-alt1
- new version

* Wed Oct 14 2020 Sergey V Turchin <zerg@altlinux.org> 20.08.2-alt1
- new version

* Tue Sep 22 2020 Sergey V Turchin <zerg@altlinux.org> 20.08.1-alt1
- new version

* Fri Aug 14 2020 Sergey V Turchin <zerg@altlinux.org> 20.04.3-alt1
- new version

* Thu Mar 12 2020 Sergey V Turchin <zerg@altlinux.org> 19.12.3-alt1
- new version

* Fri Feb 14 2020 Sergey V Turchin <zerg@altlinux.org> 19.12.2-alt1
- new version

* Thu Jan 23 2020 Sergey V Turchin <zerg@altlinux.org> 19.12.1-alt1
- new version

* Tue Sep 10 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.1-alt1
- new version

* Wed Aug 28 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.0-alt1
- new version

* Thu Jul 18 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.3-alt1
- new version

* Mon Jun 10 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.2-alt1
- new version

* Tue Jun 04 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.1-alt1
- new version

* Tue May 07 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.0-alt1
- new version

* Wed Mar 20 2019 Sergey V Turchin <zerg@altlinux.org> 18.12.3-alt1
- new version

* Mon Feb 25 2019 Sergey V Turchin <zerg@altlinux.org> 18.12.2-alt1
- new version

* Tue Jul 24 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.3-alt1%ubt
- new version

* Thu Jul 05 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.2-alt1%ubt
- new version

* Fri May 25 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.1-alt1%ubt
- new version

* Mon Mar 12 2018 Sergey V Turchin <zerg@altlinux.org> 17.12.3-alt1%ubt
- new version

* Tue Nov 14 2017 Sergey V Turchin <zerg@altlinux.org> 17.08.3-alt1%ubt
- new version

* Fri Jul 14 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.3-alt1%ubt
- new version

* Fri Jun 09 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.2-alt1%ubt
- new version

* Thu May 04 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.0-alt1%ubt
- new version

* Tue Apr 04 2017 Sergey V Turchin <zerg@altlinux.org> 16.12.3-alt1%ubt
- new version

* Mon Dec 05 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.3-alt1%ubt
- new version

* Mon Sep 19 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.1-alt1
- new version

* Thu Jul 14 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.3-alt1
- new version

* Mon Jul 04 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.2-alt1
- new version

* Wed May 11 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.1-alt1
- new version

* Fri Apr 01 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.3-alt1
- new version

* Fri Feb 26 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.2-alt1
- new version

* Wed Jan 20 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.1-alt1
- new version

* Tue Jan 12 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.0-alt1
- initial build
