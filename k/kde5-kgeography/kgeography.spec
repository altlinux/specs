%define rname kgeography

Name: kde5-%rname
Version: 22.12.2
Release: alt1
%K5init no_appdata

Group: Education
Summary: Geography learning program
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Source: %rname-%version.tar
Source2: data.tar
Patch: alt-fix-borders.patch

# Automatically added by buildreq on Fri Apr 01 2016 (-bi)
# optimized out: cmake cmake-modules docbook-dtds docbook-style-xsl elfutils gcc-c++ gtk-update-icon-cache kf5-kdoctools kf5-kdoctools-devel libEGL-devel libGL-devel libgpg-error libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-printsupport libqt5-svg libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libxcbutil-keysyms python-base python-modules python3 rpm-build-python3 xml-common xml-utils
#BuildRequires: extra-cmake-modules kf5-kauth-devel kf5-kcodecs-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kdelibs4support kf5-kdoctools-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kitemviews-devel kf5-kservice-devel kf5-kwidgetsaddons-devel kf5-kxmlgui-devel python-module-google python3-base qt5-base-devel ruby ruby-stdlibs
BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
BuildRequires: extra-cmake-modules qt5-base-devel
BuildRequires: kf5-kauth-devel kf5-kcodecs-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel
BuildRequires: kf5-kdelibs4support kf5-kdoctools-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kitemviews-devel
BuildRequires: kf5-kservice-devel kf5-kwidgetsaddons-devel kf5-kxmlgui-devel kf5-kcrash-devel

%description
%summary.

%prep
%setup -n %rname-%version
tar -xvf %SOURCE2 data/
%patch -p2

mv data/flags/{ukraine/Crimea,russia/crimea}.png
mv data/flags/{ukraine/Donetsk,russia/donetsk}.png
mv data/flags/{ukraine/Lugansk,russia/lugansk}.png
mv data/flags/{ukraine/Zaporizhya,russia/zaporozhye}.png
mv data/flags/{ukraine/Kherson,russia/kherson}.png
mv data/flags/{ukraine/Sevastopol-city,russia/sevastopol}.png

%build
%K5build

%install
%K5install
%K5install_move data kgeography
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc COPYING*
%_datadir/locale/*/LC_SCRIPTS/kgeography/
%_K5bin/kgeography
%_K5data/kgeography/
%_K5xmlgui/kgeography/
%_K5icon/*/*/apps/kgeography.*
%_K5xdgapp/org.kde.kgeography.desktop
%_K5cfg/kgeography.kcfg


%changelog
* Fri Feb 03 2023 Sergey V Turchin <zerg@altlinux.org> 22.12.2-alt1
- new version

* Thu Jan 19 2023 Sergey V Turchin <zerg@altlinux.org> 22.12.1-alt1
- new version

* Tue Jan 10 2023 Oleg Solovyov <mcpain@altlinux.org> 22.08.3-alt2
- update country borders

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

* Fri Dec 05 2019 Oleg Solovyov <mcpain@altlinux.org> 19.08.0-alt3
- Crimea: fix Europe and Asia maps

* Thu Dec 05 2019 Oleg Solovyov <mcpain@altlinux.org> 19.08.0-alt2
- Move Crimea to Russia

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
