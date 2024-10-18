%define sover 8
%define libk3blib libk3blib%sover
%define libk3bdevice libk3bdevice%sover

%define req_permhelper /usr/sbin/usermod

%define req_std_burning /usr/bin/cdrecord /usr/bin/mkisofs /usr/bin/readcd cdrdao dvd+rw-tools cdrskin
%define req_std_common kde5-runtime %req_permhelper
#define req_multimedia sox-play libsox-fmt-pulseaudio transcode vcdimager normalize lame flac mpc
%define req_multimedia sox-play libsox-fmt-pulseaudio normalize lame flac mpc
%define req_mini %req_std_burning %req_std_common
%define req_all %req_mini %req_multimedia

%define rname k3b
Name: kde5-%rname
Version: 24.02.2
Release: alt1.1
%K5init no_altplace

Group: Archiving/Cd burning
Summary: The CD Kreator (Complete set)
Summary(ru_RU.UTF-8): Программа записи CD (Полный набор)
URL: http://www.k3b.org/
License: GPL-2.0-or-later

Provides: k3b = %version-%release
Requires: %req_all
Conflicts: k3b-mini < 1.0.5-alt7
Provides: kde4-k3b = %version-%release
Obsoletes: kde4-k3b < %version-%release

Source0: %rname-%version.tar
Patch1: alt-permissions.patch
Patch2: alt-return-wodim.patch

# Automatically added by buildreq on Mon May 23 2016 (-bi)
# optimized out: cmake cmake-modules docbook-dtds docbook-style-xsl elfutils gcc-c++ glibc-devel-static gtk-update-icon-cache kf5-kdoctools kf5-kdoctools-devel libEGL-devel libGL-devel libavcodec-devel libavutil-devel libdbusmenu-qt52 libflac-devel libgpg-error libgst-plugins1.0 libjson-c libogg-devel libopencore-amrnb0 libopencore-amrwb0 libp11-kit libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-opengl libqt5-positioning libqt5-printsupport libqt5-qml libqt5-quick libqt5-sensors libqt5-sql libqt5-svg libqt5-test libqt5-webchannel libqt5-webkit libqt5-webkitwidgets libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libxcbutil-keysyms perl pkg-config python-base python-modules python3 python3-base qt5-base-devel rpm-build-python3 ruby ruby-stdlibs shared-mime-info xml-common xml-utils
#BuildRequires: extra-cmake-modules kde5-libkcddb-devel kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcmutils-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kdelibs4support kf5-kdoctools-devel kf5-kfilemetadata-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kio-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-knotifications-devel kf5-knotifyconfig-devel kf5-kservice-devel kf5-kwidgetsaddons-devel kf5-kxmlgui-devel kf5-solid-devel libavdevice-devel libavformat-devel libdvdread-devel libflac++-devel liblame-devel libmad-devel libmpcdec-devel libmusicbrainz-devel libmusicbrainz3-devel libpostproc-devel libsamplerate-devel libsndfile-devel libswscale-devel libtag-devel libvorbis-devel python-module-google python3-dev qt5-multimedia-devel qt5-webkit-devel rpm-build-ruby
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules qt5-multimedia-devel qt5-declarative-devel
BuildRequires: libavdevice-devel libavformat-devel libpostproc-devel libswscale-devel
BuildRequires: libdvdread-devel libflac++-devel liblame-devel libmad-devel libmpcdec-devel
BuildRequires: libmusicbrainz-devel
BuildRequires: libsamplerate-devel libsndfile-devel libtag-devel libvorbis-devel
BuildRequires: kde5-libkcddb-devel
BuildRequires: kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcmutils-devel kf5-kcodecs-devel kf5-kcompletion-devel
BuildRequires: kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kdelibs4support kf5-kdoctools-devel
BuildRequires: kf5-kfilemetadata-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kio-devel kf5-kitemviews-devel kf5-kjobwidgets-devel
BuildRequires: kf5-knotifications-devel kf5-knotifyconfig-devel kf5-kservice-devel kf5-kwidgetsaddons-devel kf5-kxmlgui-devel kf5-solid-devel
BuildRequires: kf5-knewstuff-devel

%description
K3b is a GUI frontend to the cd recording programs. 
It's aim is to provide a very user friendly interface to all the tasks that 
come with cd recording. 
This package contains all requiremnts and libraries necessary for full 
program functionality.
%description -l ru_RU.UTF-8
K3b - это мощная графическая оболочка для программ записи компакт дисков.
Она создана для предоставления дружественного интерфейса ко всем задачам, сопровождающим
процесс записи компакт-дисков. 
Этот пакет cодержит зависимости и библиотеки, необходимые для 
полнофункциональной работы программы.


%package mini
Summary: The CD Creator
Summary(ru_RU.UTF-8): Программа записи CD
Group: Archiving/Cd burning
Requires: %req_mini
%description mini
K3b is a GUI frontend to the cd recording programs. 
It's aim is to provide a very user friendly interface to all the tasks that 
come with cd recording.
Install 'k3b' package to get all of the program's features.
%description mini -l ru_RU.UTF-8
K3b - это мощная графическая оболочка для программ записи компакт дисков.
Она создана для предоставления дружественного интерфейса ко всем задачам, сопровождающим
процесс записи компакт-дисков.
Для полнофункцмональной работы Вы можете установить пакет 'k3b'.


%package devel
Summary: The CD Kreator (Development package.)
Summary(ru_RU.UTF-8): Программа записи CD (Пакет разработчика.)
Group: Development/KDE and QT
%description devel
K3b is a GUI frontend to the cd recording programs. 
It's aim is to provide a very user friendly interface to all the tasks that 
come with cd recording. 
This package contains k3b development files and libraries.
%description devel -l ru_RU.UTF-8
K3b - это мощная графическая оболочка для программ записи компакт дисков.
Она создана для предоставления дружественного интерфейса ко всем задачам, сопровождающим
процесс записи компакт-дисков. 
Этот пакет содержит файлы и библиотеки, необходимые разработчику 
модулей k3b.

%package -n %libk3blib
Summary: KDE 4 library
Group: System/Libraries
Requires: kf5-filesystem
%description -n %libk3blib
KDE 4 library.

%package -n %libk3bdevice
Summary: KDE 4 library
Group: System/Libraries
Requires: kf5-filesystem
%description -n %libk3bdevice
KDE 4 library.

%prep
%setup -q -n %rname-%version
%patch1 -p1
#%patch2 -p1

%build
%K5build \
    -DKDE_INSTALL_INCLUDEDIR=%_K5inc \
    #

%install
%K5install
%K5install_move data k3b solid konqsidebartng knsrcfiles

mv %buildroot/%_K5xdgmime/x-k3b.xml \
    %buildroot/%_K5xdgmime/kde5-x-k3b.xml

if [ -n "`ls -1d %buildroot/%_K5data/knsrcfiles/*k3b*`" ] ; then
    mkdir -p %buildroot/%_K5xdgconf/
    mv %buildroot/%_K5data/knsrcfiles/*k3b* %buildroot/%_K5xdgconf/
fi


%find_lang --with-kde --all-name %name


%files -f %name.lang
%doc LICENSES/* README.txt FAQ.txt PERMISSIONS.txt
%_datadir/qlogging-categories5/*.*categories
%config %_K5xdgconf/*k3b*
%_K5bin/%rname
%_K5plug/k3b_plugins/
%_K5xdgapp/org.kde.%rname.desktop
%_K5data/solid/actions/%{rname}_*.desktop
%_K5data/%rname/
%_K5data/kio/servicemenus/*%{rname}*.desktop
%_K5xdgmime/*%{rname}*.xml
#%_K5srvtyp/%{rname}plugin.desktop
#%_K5xmlgui/%rname/
%_K5notif/%rname.notifyrc
%_K5icon/hicolor/*/apps/%rname.*
%_K5icon/hicolor/*/mimetypes/application-x-%rname.*
%_datadir/metainfo/*k3b*.xml
#
%_K5plug/kf5/kio/videodvd.so
%_K5data/konqsidebartng/virtual_folders/services/videodvd.desktop
# permhelper
#%_K5dbus_sys_srv/org.kde.k3b.service
#%_K5libexecdir/kauth/k3bhelper
#%_K5dbus/system.d/org.kde.k3b.conf
#%_datadir/polkit-1/actions/org.kde.k3b.policy

%files -n %libk3blib
%_K5lib/libk3blib.so.%sover
%_K5lib/libk3blib.so.%sover.*

%files -n %libk3bdevice
%_K5lib/libk3bdevice.so.%sover
%_K5lib/libk3bdevice.so.%sover.*

%files devel
%_K5link/*.so
%_K5inc/k3b*.h

%changelog
* Wed Oct 02 2024 L.A. Kostis <lakostis@altlinux.ru> 24.02.2-alt1.1
- NMU: require apps paths over cdrkit (as cdrecord/mkisofs/readcd
       provided by schilytools).
- NMU: remove ubt cruft.

* Thu May 02 2024 Sergey V Turchin <zerg@altlinux.org> 24.02.2-alt1
- new version

* Thu Apr 11 2024 Sergey V Turchin <zerg@altlinux.org> 24.02.1-alt1
- new version

* Fri Feb 16 2024 Sergey V Turchin <zerg@altlinux.org> 23.08.5-alt1
- new version

* Mon Dec 11 2023 Sergey V Turchin <zerg@altlinux.org> 23.08.4-alt1
- new version

* Fri Nov 10 2023 Sergey V Turchin <zerg@altlinux.org> 23.08.3-alt1
- new version

* Fri Oct 13 2023 Sergey V Turchin <zerg@altlinux.org> 23.08.2-alt1
- new version

* Thu Oct 05 2023 Sergey V Turchin <zerg@altlinux.org> 23.08.1-alt1
- new version

* Fri Jul 14 2023 Sergey V Turchin <zerg@altlinux.org> 23.04.3-alt1
- new version

* Fri Jun 09 2023 Sergey V Turchin <zerg@altlinux.org> 23.04.2-alt1
- new version

* Thu Jun 01 2023 Sergey V Turchin <zerg@altlinux.org> 23.04.1-alt1
- new version

* Mon Mar 06 2023 Sergey V Turchin <zerg@altlinux.org> 22.12.3-alt1
- new version

* Mon Feb 06 2023 Sergey V Turchin <zerg@altlinux.org> 22.12.2-alt1
- new version

* Wed Jan 11 2023 Sergey V Turchin <zerg@altlinux.org> 22.12.1-alt1
- new version

* Wed Nov 30 2022 Sergey V Turchin <zerg@altlinux.org> 22.08.3-alt2
- fix to build with KF-5.100

* Mon Nov 07 2022 Sergey V Turchin <zerg@altlinux.org> 22.08.3-alt1
- new version

* Tue Oct 18 2022 Sergey V Turchin <zerg@altlinux.org> 22.08.2-alt1
- new version

* Thu Sep 15 2022 Sergey V Turchin <zerg@altlinux.org> 22.08.1-alt1
- new version

* Mon Jul 11 2022 Sergey V Turchin <zerg@altlinux.org> 22.04.3-alt1
- new version

* Fri Jun 10 2022 Sergey V Turchin <zerg@altlinux.org> 22.04.2-alt1
- new version

* Fri May 13 2022 Sergey V Turchin <zerg@altlinux.org> 22.04.1-alt1
- new version

* Fri Mar 04 2022 Sergey V Turchin <zerg@altlinux.org> 21.12.3-alt1
- new version

* Mon Jan 17 2022 Sergey V Turchin <zerg@altlinux.org> 21.12.1-alt1
- new version

* Mon Nov 08 2021 Sergey V Turchin <zerg@altlinux.org> 21.08.3-alt1
- new version

* Mon Oct 11 2021 Sergey V Turchin <zerg@altlinux.org> 21.08.2-alt2
- remove permissions helper

* Fri Oct 08 2021 Sergey V Turchin <zerg@altlinux.org> 21.08.2-alt1
- new version

* Thu Sep 02 2021 Sergey V Turchin <zerg@altlinux.org> 21.08.1-alt1
- new version

* Mon Aug 23 2021 Sergey V Turchin <zerg@altlinux.org> 21.08.0-alt1
- new version

* Thu Jul 08 2021 Sergey V Turchin <zerg@altlinux.org> 21.04.3-alt1
- new version

* Thu Jun 10 2021 Sergey V Turchin <zerg@altlinux.org> 21.04.2-alt1
- new version

* Wed May 19 2021 Sergey V Turchin <zerg@altlinux.org> 21.04.1-alt1
- new version

* Thu Mar 11 2021 Sergey V Turchin <zerg@altlinux.org> 20.12.3-alt1
- new version

* Fri Feb 05 2021 Sergey V Turchin <zerg@altlinux.org> 20.12.2-alt1
- new version

* Tue Jan 19 2021 Sergey V Turchin <zerg@altlinux.org> 20.12.1-alt3
- bump release

* Tue Jan 19 2021 Sergey V Turchin <zerg@altlinux.org> 20.12.1-alt2
- remove transcode and vcdimager from requires

* Thu Jan 14 2021 Sergey V Turchin <zerg@altlinux.org> 20.12.1-alt1
- new version

* Fri Dec 18 2020 Sergey V Turchin <zerg@altlinux.org> 20.12.0-alt1
- new version

* Wed Nov 25 2020 Sergey V Turchin <zerg@altlinux.org> 20.08.3-alt1
- new version

* Wed Oct 14 2020 Sergey V Turchin <zerg@altlinux.org> 20.08.2-alt1
- new version

* Fri Sep 18 2020 Sergey V Turchin <zerg@altlinux.org> 20.08.1-alt1
- new version

* Fri Aug 14 2020 Sergey V Turchin <zerg@altlinux.org> 20.04.3-alt1
- new version

* Thu Mar 12 2020 Sergey V Turchin <zerg@altlinux.org> 19.12.3-alt1
- new version

* Fri Feb 14 2020 Sergey V Turchin <zerg@altlinux.org> 19.12.2-alt1
- new version

* Tue Jan 21 2020 Sergey V Turchin <zerg@altlinux.org> 19.12.1-alt1
- new version

* Fri Nov 29 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.3-alt2
- update requires

* Fri Nov 08 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.3-alt1
- new version

* Fri Oct 25 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.2-alt1
- new version

* Tue Sep 10 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.1-alt1
- new version

* Tue Aug 27 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.0-alt1
- new version

* Thu Jul 18 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.3-alt1
- new version

* Mon Jun 10 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.2-alt1
- new version

* Tue Jun 04 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.1-alt1
- new version

* Mon May 06 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.0-alt1
- new version

* Wed Mar 20 2019 Sergey V Turchin <zerg@altlinux.org> 18.12.3-alt1
- new version

* Mon Mar 11 2019 Sergey V Turchin <zerg@altlinux.org> 18.12.2-alt2
- build without musicbrainz

* Tue Feb 19 2019 Sergey V Turchin <zerg@altlinux.org> 18.12.2-alt1
- new version

* Tue Oct 16 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.3-alt2
- fix build

* Tue Jul 24 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.3-alt1%ubt
- new version

* Wed Jul 04 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.2-alt1%ubt
- new version

* Fri Jun 15 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.1-alt2%ubt
- remove requires to transcode

* Tue May 22 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.1-alt1%ubt
- new version

* Mon May 14 2018 Sergey V Turchin <zerg@altlinux.org> 17.12.3-alt2%ubt
- build without qtwebkit

* Wed Mar 14 2018 Sergey V Turchin <zerg@altlinux.org> 17.12.3-alt1%ubt
- new version

* Tue Mar 06 2018 Sergey V Turchin <zerg@altlinux.org> 17.12.2-alt1%ubt
- new version

* Thu Feb 22 2018 Sergey V Turchin <zerg@altlinux.org> 17.08.3-alt2%ubt
- obsolete kde4-k3b

* Mon Nov 13 2017 Sergey V Turchin <zerg@altlinux.org> 17.08.3-alt1%ubt
- new version

* Fri Jul 14 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.3-alt1%ubt
- new version

* Wed Jun 14 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.2-alt1%ubt
- new version

* Tue May 02 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.0-alt1%ubt
- new version

* Wed Apr 05 2017 Sergey V Turchin <zerg@altlinux.org> 17.03.80-alt1%ubt
- new beta

* Mon Nov 07 2016 Sergey V Turchin <zerg@altlinux.org> 2.10.0-alt0.2.M80P.1
- build for M80P

* Mon Nov 07 2016 Sergey V Turchin <zerg@altlinux.org> 2.10.0-alt0.3
- update from master branch

* Mon Sep 26 2016 Sergey V Turchin <zerg@altlinux.org> 2.10.0-alt0.2
- return wodim support

* Thu Sep 22 2016 Sergey V Turchin <zerg@altlinux.org> 2.10.0-alt0.1
- update from master branch

* Fri Jul 29 2016 Sergey V Turchin <zerg@altlinux.org> 2.9.90-alt2
- update from KF5 branch

* Tue May 24 2016 Sergey V Turchin <zerg@altlinux.org> 2.9.90-alt1
- initial build
