%define rname kturtle

Name: kde5-%rname
Version: 22.12.2
Release: alt1
%K5init no_appdata

Group: Education
Summary: An educational programming environment
Url: http://www.kde.org
License: GPL-2.0-only or GPL-2.0-or-later

Source: %rname-%version.tar
Patch1: alt-def-language.patch

# Automatically added by buildreq on Thu Mar 17 2016 (-bi)
# optimized out: cmake cmake-modules docbook-dtds docbook-style-xsl elfutils gcc-c++ gtk-update-icon-cache kf5-attica-devel kf5-kdoctools-devel libEGL-devel libGL-devel libgpg-error libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-printsupport libqt5-svg libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libxcbutil-keysyms python-base python-modules python3 python3-base qt5-base-devel rpm-build-python3 xml-common xml-utils
#BuildRequires: extra-cmake-modules kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdelibs4support kf5-kdoctools kf5-kdoctools-devel kf5-ki18n-devel kf5-kio-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-knewstuff-devel kf5-kservice-devel kf5-ktextwidgets-devel kf5-kwidgetsaddons-devel kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel python-module-google python3.3-site-packages qt5-svg-devel ruby ruby-stdlibs
BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
BuildRequires: extra-cmake-modules qt5-base-devel qt5-svg-devel
BuildRequires: kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel
BuildRequires: kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdelibs4support kf5-kdoctools kf5-kdoctools-devel
BuildRequires: kf5-ki18n-devel kf5-kio-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-knewstuff-devel kf5-kservice-devel
BuildRequires: kf5-ktextwidgets-devel kf5-kwidgetsaddons-devel kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel

%description
KTurtle is an educational programming environment for the KDE Desktop.
KTurtle aims to make programming as easy and touchable as possible, and
therefore can be used to teach kids the basics of math, geometry
and... programming.

%prep
%setup -n %rname-%version
%patch1 -p1

%build
%K5build

%install
%K5install
%K5install_move data katepart kturtle
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc LICENSES/*
%config(noreplace) %_K5xdgconf/kturtle.knsrc
%_K5bin/kturtle
%_K5icon/*/*/apps/kturtle.*
%_K5xmlgui/kturtle/
%_K5xdgapp/org.kde.kturtle.desktop
#%_K5data/katepart/syntax/*logo*.xml
#%_K5data/kturtle/

%changelog
* Fri Feb 03 2023 Sergey V Turchin <zerg@altlinux.org> 22.12.2-alt1
- new version

* Thu Jan 19 2023 Sergey V Turchin <zerg@altlinux.org> 22.12.1-alt1
- new version

* Mon Nov 07 2022 Sergey V Turchin <zerg@altlinux.org> 22.08.3-alt1
- new version

* Tue Oct 18 2022 Sergey V Turchin <zerg@altlinux.org> 22.08.2-alt1
- new version

* Wed Sep 21 2022 Sergey V Turchin <zerg@altlinux.org> 22.08.1-alt1
- new version

* Tue Jul 12 2022 Sergey V Turchin <zerg@altlinux.org> 22.04.3-alt1
- new version

* Fri Jun 10 2022 Sergey V Turchin <zerg@altlinux.org> 22.04.2-alt1
- new version

* Mon May 23 2022 Sergey V Turchin <zerg@altlinux.org> 22.04.1-alt1
- new version

* Sat Mar 05 2022 Sergey V Turchin <zerg@altlinux.org> 21.12.3-alt1
- new version

* Tue Jan 18 2022 Sergey V Turchin <zerg@altlinux.org> 21.12.1-alt1
- new version

* Mon Nov 08 2021 Sergey V Turchin <zerg@altlinux.org> 21.08.3-alt1
- new version

* Fri Oct 08 2021 Sergey V Turchin <zerg@altlinux.org> 21.08.2-alt1
- new version

* Mon Sep 06 2021 Sergey V Turchin <zerg@altlinux.org> 21.08.1-alt1
- new version

* Fri Aug 27 2021 Sergey V Turchin <zerg@altlinux.org> 21.08.0-alt1
- new version

* Fri Jul 09 2021 Sergey V Turchin <zerg@altlinux.org> 21.04.3-alt1
- new version

* Tue May 25 2021 Sergey V Turchin <zerg@altlinux.org> 21.04.1-alt1
- new version

* Fri Mar 12 2021 Sergey V Turchin <zerg@altlinux.org> 20.12.3-alt1
- new version

* Wed Feb 17 2021 Sergey V Turchin <zerg@altlinux.org> 20.12.2-alt1
- new version

* Tue Dec 22 2020 Sergey V Turchin <zerg@altlinux.org> 20.12.0-alt1
- new version

* Wed Nov 25 2020 Sergey V Turchin <zerg@altlinux.org> 20.08.3-alt1
- new version

* Thu Oct 15 2020 Sergey V Turchin <zerg@altlinux.org> 20.08.2-alt1
- new version

* Wed Sep 23 2020 Sergey V Turchin <zerg@altlinux.org> 20.08.1-alt1
- new version

* Wed Aug 19 2020 Sergey V Turchin <zerg@altlinux.org> 20.04.3-alt1
- new version

* Fri Mar 13 2020 Sergey V Turchin <zerg@altlinux.org> 19.12.3-alt1
- new version

* Thu Jan 23 2020 Sergey V Turchin <zerg@altlinux.org> 19.12.1-alt1
- new version

* Wed Nov 27 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.3-alt1
- new version

* Tue Sep 10 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.1-alt1
- new version

* Thu Aug 29 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.0-alt1
- new version

* Fri Jul 19 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.3-alt1
- new version

* Thu Jun 06 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.1-alt1
- new version

* Wed May 08 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.0-alt1
- new version

* Thu Mar 21 2019 Sergey V Turchin <zerg@altlinux.org> 18.12.3-alt1
- new version

* Thu Feb 28 2019 Sergey V Turchin <zerg@altlinux.org> 18.12.2-alt1
- new version

* Thu Jul 26 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.3-alt1%ubt
- new version

* Thu Jul 05 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.2-alt1%ubt
- new version

* Fri May 25 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.1-alt1%ubt
- new version

* Tue Mar 13 2018 Sergey V Turchin <zerg@altlinux.org> 17.12.3-alt1%ubt
- new version

* Tue Nov 14 2017 Sergey V Turchin <zerg@altlinux.org> 17.08.3-alt1%ubt
- new version

* Fri Jul 14 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.3-alt1%ubt
- new version

* Thu Jun 15 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.2-alt1%ubt
- new version

* Wed Jun 07 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.1-alt1%ubt
- new version

* Thu Apr 06 2017 Sergey V Turchin <zerg@altlinux.org> 16.12.3-alt1%ubt
- new version

* Thu Sep 22 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.1-alt1
- new version

* Mon Jul 04 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.2-alt1
- new version

* Thu May 12 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.1-alt1
- new version

* Thu Mar 17 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.2-alt1
- initial build
