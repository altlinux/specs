%define rname kdenlive
%define current_ver_mlt %{get_version mlt-utils}
%define is_ffmpeg %([ -n "`rpmquery --qf '%%{SOURCERPM}' libavformat-devel 2>/dev/null | grep -e '^libav'`" ] && echo 0 || echo 1)

Name: kdenlive
Version: 24.08.3
Release: alt2
%K6init no_altplace man appdata
%add_python3_path %_datadir/%name/scripts

Summary: KDE Non Linear Video Editor
Summary(ru_RU.utf8): Редактор нелинейного видео монтажа для KDE
Summary(ru_UA.utf8): Редактор нелінійного монтажу для KDE
License: GPL-3.0-or-later
Group: Video
URL: http://kdenlive.org/

AutoReq: yes, nopython
AutoProv: yes, nopython nopython3
%add_python3_req_skip opentimelineio
%add_python3_req_skip srt
%add_python3_req_skip vosk
%add_python3_req_skip torch
%add_python3_req_skip whisper
Requires: mlt-utils >= %current_ver_mlt frei0r-plugins
Requires: recordmydesktop dvdauthor dvgrab genisoimage
Requires: mediainfo
Requires: icon-theme-breeze kde-runtime kio-extras
Requires: kf6-kirigami
%if %is_ffmpeg
Requires: /usr/bin/ffmpeg /usr/bin/ffplay /usr/bin/ffprobe
%else
Requires: /usr/bin/avconv /usr/bin/avplay /usr/bin/avprobe
%endif

Source: %name-%version.tar
Source1: rttr.tar
Patch2: alt-find-lumas.patch
Patch3: alt-ffmpegaudiothumbnails.patch

BuildRequires(pre): rpm-build-kf6
BuildRequires(pre): libavformat-devel
BuildRequires(pre): mlt-utils
BuildRequires: rpm-build-python3
BuildRequires: extra-cmake-modules
BuildRequires: qt6-declarative-devel qt6-svg-devel qt6-declarative-devel qt6-multimedia-devel qt6-declarative-devel qt6-networkauth-devel
BuildRequires: shared-mime-info libEGL-devel libGLU-devel libv4l-devel
BuildRequires: mlt7-devel mlt7xx-devel
BuildRequires: kf6-karchive-devel kf6-kauth-devel kf6-kbookmarks-devel kf6-kcodecs-devel kf6-kcompletion-devel kf6-kconfig-devel kf6-kconfigwidgets-devel
BuildRequires: kf6-kcoreaddons-devel kf6-kdbusaddons-devel kf6-kdoctools kf6-kdoctools-devel kf6-kguiaddons-devel kf6-ki18n-devel
BuildRequires: kf6-kiconthemes-devel kf6-kio-devel kf6-kitemviews-devel kf6-kjobwidgets-devel kf6-knewstuff-devel kf6-knotifications-devel
BuildRequires: kf6-knotifyconfig-devel kf6-kplotting-devel kf6-kservice-devel kf6-ktextwidgets-devel kf6-kwidgetsaddons-devel kf6-kxmlgui-devel
BuildRequires: kf6-solid-devel kf6-sonnet-devel kf6-kcrash-devel kf6-kfilemetadata-devel kf6-purpose-devel
BuildRequires: kf6-kdeclarative-devel kf6-kpackage-devel

%description
Kdenlive is a non-linear video editor for GNU/Linux, which supports
DV, HDV and AVCHD(not complete yet) editing.

%description -l ru_RU.utf8
Редактор нелинейного видео монтажа для GNU/Linux

%description -l ru_UA.utf8
Редактор нелінійного монтажу для GNU/Linux

%prep
%setup -q
#%patch2 -p1
%if %is_ffmpeg
%else
%patch3 -p1
%endif

install -m 0644 %SOURCE1 .
sed -i "s|URL.*github.*rttr.*|URL file://${PWD}/rttr.tar|" rttr.CMakeLists.txt

%build
%K6build

%install
%K6install

%find_lang %name --with-kde --all-name
sed -i '/[[:space:]]\/.*[[:space:]]/s|[[:space:]]\(\/.*$\)| "\1"|' %name.lang

%files -f %name.lang
%doc AUTHORS LICENSES/*
%_K6bin/*
%_K6plug/kf6/thumbcreator/*mlt*.so
%_K6xdgapp/*.desktop
%_datadir/%name
%_K6cfg/*kdenlive*
%_iconsdir/*/*/*/*.*
%_K6notif/*rc
%_K6xdgmime/*.xml
%_man1dir/kdenlive*
%_datadir/metainfo/org.kde.kdenlive.appdata.xml
%_datadir/qlogging-categories6/*.categories
%_datadir/knsrcfiles/*.knsrc



%changelog
* Tue Nov 12 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.3-alt2
- fix start from main menu (closes: 52021)

* Mon Nov 11 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.3-alt1
- new version

* Tue Oct 29 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.2-alt1
- new version

* Wed Feb 21 2024 Sergey V Turchin <zerg@altlinux.org> 23.08.5-alt1
- new version

* Wed Dec 13 2023 Sergey V Turchin <zerg@altlinux.org> 23.08.4-alt2
- update requires

* Tue Dec 12 2023 Sergey V Turchin <zerg@altlinux.org> 23.08.4-alt1
- new version

* Tue Jul 18 2023 Sergey V Turchin <zerg@altlinux.org> 23.04.3-alt1
- new version

* Fri Jun 30 2023 Sergey V Turchin <zerg@altlinux.org> 22.12.3-alt3
- fix russian translation (closes: 46570)

* Tue Apr 18 2023 Sergey V Turchin <zerg@altlinux.org> 22.12.3-alt2
- require kde5-kio-extras (closes: 45888)
- require kcm and kirigami qml modules (closes: 45890)
- fix python requires (closes: 45891)

* Mon Apr 10 2023 Sergey V Turchin <zerg@altlinux.org> 22.12.3-alt1
- new version

* Mon Nov 28 2022 Sergey V Turchin <zerg@altlinux.org> 22.08.3-alt1
- new version

* Wed Jul 13 2022 Sergey V Turchin <zerg@altlinux.org> 22.04.3-alt1
- new version

* Thu Mar 10 2022 Sergey V Turchin <zerg@altlinux.org> 21.12.3-alt1
- new version

* Fri Dec 10 2021 Sergey V Turchin <zerg@altlinux.org> 21.08.3-alt2
- require mlt version (closes 39476)

* Tue Nov 09 2021 Sergey V Turchin <zerg@altlinux.org> 21.08.3-alt1
- new version

* Tue Aug 31 2021 Sergey V Turchin <zerg@altlinux.org> 21.08.0-alt1
- new version

* Wed Jul 14 2021 Sergey V Turchin <zerg@altlinux.org> 21.04.3-alt1
- new version

* Fri Mar 19 2021 Sergey V Turchin <zerg@altlinux.org> 20.12.3-alt1
- new version

* Wed Feb 17 2021 Sergey V Turchin <zerg@altlinux.org> 20.12.2-alt1
- new version

* Wed Nov 25 2020 Sergey V Turchin <zerg@altlinux.org> 20.08.3-alt1
- new version

* Mon Jun 15 2020 Sergey V Turchin <zerg@altlinux.org> 20.04.2-alt1
- new version

* Thu Jun 11 2020 Sergey V Turchin <zerg@altlinux.org> 20.04.1-alt1
- new version

* Thu Mar 12 2020 Sergey V Turchin <zerg@altlinux.org> 19.12.3-alt1
- new version

* Fri Jan 24 2020 Sergey V Turchin <zerg@altlinux.org> 19.12.1-alt1
- new version

* Fri Nov 22 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.3-alt1
- new version

* Wed Oct 23 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.2-alt1
- new version

* Tue Jul 16 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.3-alt1
- new version

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 19.04.2-alt2
- NMU: remove rpm-build-ubt from BR:

* Mon Jun 10 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.2-alt1
- new version

* Mon Jun 03 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.1-alt1
- new version

* Wed May 08 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.0-alt1
- new version

* Mon Mar 18 2019 Sergey V Turchin <zerg@altlinux.org> 18.12.3-alt1
- new version

* Fri Feb 15 2019 Sergey V Turchin <zerg@altlinux.org> 18.12.2-alt1
- new version

* Thu Jan 24 2019 Sergey V Turchin <zerg@altlinux.org> 18.12.1-alt1
- new version

* Fri Nov 09 2018 Sergey V Turchin <zerg@altlinux.org> 18.08.3-alt1
- new version

* Mon Oct 15 2018 Sergey V Turchin <zerg@altlinux.org> 18.08.2-alt1
- new version

* Tue Sep 11 2018 Sergey V Turchin <zerg@altlinux.org> 18.08.1-alt1
- new version

* Thu Aug 23 2018 Sergey V Turchin <zerg@altlinux.org> 18.08.0-alt1
- new version

* Tue Aug 07 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.3-alt1
- new version

* Thu Jul 12 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.2-alt1
- new version

* Wed May 16 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.1-alt1
- new version

* Fri Mar 16 2018 Sergey V Turchin <zerg@altlinux.org> 17.12.3-alt1
- new version

* Fri Dec 22 2017 Sergey V Turchin <zerg@altlinux.org> 17.12.0-alt1
- new version

* Thu Nov 09 2017 Sergey V Turchin <zerg@altlinux.org> 17.08.3-alt1
- new version

* Tue Oct 31 2017 Sergey V Turchin <zerg@altlinux.org> 17.08.2-alt1
- new version

* Thu Jul 20 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.3-alt1
- new version

* Thu Jun 15 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.2-alt1
- new version

* Tue Jun 06 2017 Sergey V Turchin <zerg@altlinux.org> 16.12.3-alt2
- rebuild with ffmpeg

* Tue Apr 04 2017 Sergey V Turchin <zerg@altlinux.org> 16.12.3-alt1
- new version

* Fri Nov 25 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.3-alt0.M80P.1
- build for M80P

* Fri Nov 25 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.3-alt1
- new version

* Thu Oct 20 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.2-alt1.M80P.1
- build for M80P

* Thu Oct 20 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.2-alt2
- don't use ffmpeg for audio thumbnails by default(ALT#32544)

* Tue Oct 18 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.2-alt0.M80P.1
- build for M80P

* Fri Oct 14 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.2-alt1
- new version

* Tue Sep 27 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.1-alt1.M80P.1
- build for M80P

* Tue Sep 27 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.1-alt2
- fix requires (ALT#32534)

* Mon Sep 12 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.1-alt1
- new version

* Mon Aug 22 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.0-alt1
- new version

* Thu Jul 07 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.2-alt1
- new version

* Fri May 13 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.1-alt1
- new version

* Tue Apr 26 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.0-alt3
- update from 16.04 branch

* Fri Apr 22 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.0-alt2
- fix build requires

* Thu Apr 21 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.0-alt1
- new version

* Fri Mar 04 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.2-alt1
- new version

* Mon Jan 25 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.1-alt1
- new version

* Mon Dec 21 2015 Sergey V Turchin <zerg@altlinux.org> 15.12.0-alt1
- new version

* Wed Nov 11 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.3-alt2
- update from 15.08 branch

* Thu Nov 05 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.3-alt1
- new version

* Thu Oct 15 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.2-alt1
- new version

* Wed Sep 16 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.1-alt1
- new version

* Thu Sep 10 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.0-alt2
- fix find kdenlive lumas

* Thu Sep 10 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.0-alt1
- new version

* Mon Jul 27 2015 Sergey V Turchin <zerg@altlinux.org> 15.04.3-alt1
- new version

* Tue Jun 16 2015 Sergey V Turchin <zerg@altlinux.org> 0.9.10-alt2
- rebuild with new mlt

* Thu Apr 16 2015 Sergey V Turchin <zerg@altlinux.org> 0.9.10-alt0.M70P.1
- build for M70P

* Fri Oct 17 2014 Sergey V Turchin <zerg@altlinux.org> 0.9.10-alt1
- new version

* Fri Oct 17 2014 Sergey V Turchin <zerg@altlinux.org> 0.9.8-alt2.M70P.1
- built for M70P

* Fri Jun 06 2014 Sergey V Turchin <zerg@altlinux.org> 0.9.8-alt3
- prefer vlc for preview

* Tue May 27 2014 Sergey V Turchin <zerg@altlinux.org> 0.9.8-alt2
- rebuilt with new mlt

* Thu May 15 2014 Sergey V Turchin <zerg@altlinux.org> 0.9.8-alt1
- new version

* Thu May 23 2013 Sergey V Turchin <zerg@altlinux.org> 0.9.6-alt2
- fix requires

* Mon Apr 15 2013 Sergey V Turchin <zerg@altlinux.org> 0.9.6-alt1
- new version

* Thu Jan 31 2013 Sergey V Turchin <zerg@altlinux.org> 0.9.4-alt1
- new version

* Wed May 30 2012 Sergey V Turchin <zerg@altlinux.org> 0.9.2-alt1
- new version

* Thu May 17 2012 Sergey V Turchin <zerg@altlinux.org> 0.9-alt1
- new version

* Tue Mar 13 2012 Sergey V Turchin <zerg@altlinux.org> 0.8.2.1-alt3.M60P.1
- built for M60P

* Tue Mar 13 2012 Sergey V Turchin <zerg@altlinux.org> 0.8.2.1-alt4
- update russian translation; thanks azol@alt (ALT#27051)

* Sat Feb 04 2012 Sergey V Turchin <zerg@altlinux.org> 0.8.2.1-alt3
- fix requires

* Fri Feb 03 2012 Sergey V Turchin <zerg@altlinux.org> 0.8.2.1-alt2
- fix compile

* Thu Dec 29 2011 Sergey V Turchin <zerg@altlinux.org> 0.8.2.1-alt0.M60P.1
- built for M60P

* Mon Dec 12 2011 Sergey V Turchin <zerg@altlinux.org> 0.8.2.1-alt1
- new version (ATL#26350)

* Wed Aug 24 2011 Sergey V Turchin <zerg@altlinux.org> 0.8-alt1.M60P.1
- built for M60P

* Wed Aug 24 2011 Sergey V Turchin <zerg@altlinux.org> 0.8-alt2
- fix detect mlt-0.7.4

* Wed Apr 27 2011 Sergey V Turchin <zerg@altlinux.org> 0.8-alt1
- new version

* Wed Sep 29 2010 Sergey V Turchin <zerg@altlinux.org> 0.7.8-alt2
- fix requires (ATL#20019)

* Thu Sep 16 2010 Sergey V Turchin <zerg@altlinux.org> 0.7.8-alt0.M51.1
- built for M51

* Wed Sep 15 2010 Sergey V Turchin <zerg@altlinux.org> 0.7.8-alt1
- new version

* Thu Jun 17 2010 Sergey V Turchin <zerg@altlinux.org> 0.7.7.1-alt1.M51.1
- build for M51

* Thu Jun 17 2010 Sergey V Turchin <zerg@altlinux.org> 0.7.7.1-alt2
- build for sisyphus

* Wed Apr 14 2010 Maxim Ivanov <redbaron at altlinux.org> 0.7.7.1-alt1
- Update to 0.7.7.1

* Thu Nov 12 2009 Maxim Ivanov <redbaron at altlinux.org> 0.7.6-alt1
- Update to 0.7.6

* Sun Aug 30 2009 Maxim Ivanov <redbaron at altlinux.org> 0.7.5-alt2
- Rebuild with new mlt

* Sat Aug 29 2009 Maxim Ivanov <redbaron at altlinux.org> 0.7.5-alt1
- Update to 0.7.5 (ALT #21144)

* Mon Jul 20 2009 Maxim Ivanov <redbaron at altlinux.org> 0.7.4-alt1.git.ec1704579b6fh4
- Update to 0.7.4

* Sun Apr 19 2009 Maxim Ivaniv <redbaron at altlinux.org> 0.7.3-alt1.svn3320
- 0.7.3

* Thu Dec 11 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.6-alt1
- 0.6

* Sun Nov 23 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.5-alt6
- removed obsolete %%update_menus/%%clean_menus calls

* Sun Oct 26 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.5-alt5
- fixed build with gcc4.3

* Mon Jan 28 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.5-alt4
- fix crash on exit

* Thu Dec 20 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.5-alt3
- rebuild for mlt-0.2.5
- fixed menu

* Mon Oct 29 2007 Alexey Morsov <swi@altlinux.ru> 0.5-alt2
- add russian translate (from Alexandra Panyukova)

* Mon Sep 03 2007 Alexey Morsov <swi@altlinux.ru> 0.5-alt1
- 0.5-1

* Wed Feb 14 2007 Alexey Morsov <swi@altlinux.ru> 0.4-alt0.2
- clean files section
- add summary, description for ru(ua) in utf8

* Tue Feb 13 2007 Led <led@altlinux.ru> 0.4-alt0.1
- initial build
