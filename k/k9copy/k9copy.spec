%define _unpackaged_files_terminate_build 1

%define rname k9copy

Name: %rname
Version: 3.0.3
Release: alt2
Group: Video
Summary: Copy, split and shrink DVDs
Summary(ru_RU.UTF8): Копирование, разделение и уменьшение DVD-дисков
License: GPL
Url: http://k9copy.sourceforge.net

%K5init no_altplace

Requires: dvdauthor dvd+rw-tools mencoder

Provides: kde4-%rname = %EVR
Obsoletes: kde4-%rname < %EVR

Source: %name-%version.tar

Patch1: %name-%version-alt.patch

BuildRequires(pre): rpm-build-kf5
BuildRequires: cmake
BuildRequires: gcc-c++ libavformat-devel libmpeg2-devel libswscale-devel libxine2-devel libdvdread-devel libdvdnav-devel
BuildRequires: qt5-base-devel qt5-x11extras-devel
BuildRequires: qt5-phonon-devel
BuildRequires: extra-cmake-modules
BuildRequires: kf5-ki18n-devel kf5-kauth-devel kf5-kconfig-devel kf5-kdesu-devel kf5-kpty-devel kf5-kcoreaddons-devel
BuildRequires: kf5-kwidgetsaddons-devel kf5-kdoctools-devel kf5-kxmlgui-devel kf5-solid-devel kf5-kio-devel kf5-kiconthemes-devel

%description
K9Copy is a small utility which allows the copy of DVD on Linux.
The DVD video stream is compressed by the program Vamps. 

Copy without menus :
 In this case, dvdauthor is used to create a new DVD structure.
 It is possible to choose the order in which the video sequences are played. 

Copy with menus :
 As dvdauthor does not make it possible to integrate the original menus,
 K9Copy reproduces the original structure of the DVD. The navigation packs
 as well as IFO files are modified to point on the compressed MPEG stream.

%description -l ru_RU.UTF8
K9Copy - маленькая программа для копирования DVD в Linux.
Видео поток DVD сжимается с помощью программы Vamps.

Копирование без меню:
 В этом случае dvdauthor используется для создания новой структуры DVD.
 Возможно выбирать порядок, в котором видео фрагменты будут воспроизводиться.

Копирование с меню:
 Посколько dvdauthor не позволяет интегрировать оригинальное меню,
 K9Copy воспроизводит оригинальную структуру DVD. Навигационные пакеты, так же как
 и IFO файлы модифицируются для указания мест в сжатом MPEG потоке.

%prep
%setup
%patch1 -p1

# remove bundled libraries
rm -rf src/libdvdnav-NOW src/libdvdread-NOW

%build
%K5build \
	-DQT5_BUILD:BOOL=ON \
	%nil

%install
%K5install
%K5install_move data solid

# this translation is ignored by %%find_lang
rm -f %buildroot%_datadir/locale/sr@Latn/LC_MESSAGES/%{rname}.mo

%find_lang %rname --with-kde --all-name

%files -f %rname.lang
%doc COPYING
%doc README
%_K5bin/*
%_K5xdgapp/*
%_K5icon/hicolor/*/actions/*
%_datadir/%rname
%_K5xmlgui/%rname
%_K5data/solid/actions/%{rname}_*.desktop

%changelog
* Wed Nov 30 2022 Sergey V Turchin <zerg@altlinux.org> 3.0.3-alt2
- fix compile with KF5-5.100

* Thu Apr 29 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 3.0.3-alt1
- Updated to k9copy-reloaded version 3.0.3.
- Rebuilt with qt5.

* Wed Apr 22 2020 Sergey V Turchin <zerg@altlinux.org> 2.3.8-alt10
- fix requires

* Sat Jun 15 2019 Igor Vlasenko <viy@altlinux.ru> 2.3.8-alt9
- NMU: remove %%ubt from release

* Thu Jun 14 2018 Sergey V Turchin <zerg@altlinux.org> 2.3.8-alt8
- rebuild with new ffmpeg

* Thu Jun 15 2017 Sergey V Turchin <zerg@altlinux.org> 2.3.8-alt7
- fix to build with ffmpeg

* Mon Jan 30 2017 Sergey V Turchin <zerg@altlinux.org> 2.3.8-alt6
- fix for gcc6

* Fri Apr 10 2015 Sergey V Turchin <zerg@altlinux.org> 2.3.8-alt5
- rebuild with new libav

* Tue May 27 2014 Sergey V Turchin <zerg@altlinux.org> 2.3.8-alt4
- built with libxine2

* Tue May 27 2014 Sergey V Turchin <zerg@altlinux.org> 2.3.8-alt3
- fix to build with libav10

* Thu Nov 28 2013 Sergey V Turchin <zerg@altlinux.org> 2.3.8-alt1.M70P.1
- built for M70P

* Tue Oct 08 2013 Sergey V Turchin <zerg@altlinux.org> 2.3.8-alt2
- fix to build with new libav
- sync patches with Debian

* Fri Jun 15 2012 Sergey V Turchin <zerg@altlinux.org> 2.3.8-alt0.M60P.1
- built for M60P

* Fri Jun 15 2012 Sergey V Turchin <zerg@altlinux.org> 2.3.8-alt1
- new version

* Tue Aug 09 2011 Sergey V Turchin <zerg@altlinux.org> 2.3.7-alt0.M60P.1
- built for M60P

* Tue Aug 09 2011 Sergey V Turchin <zerg@altlinux.org> 2.3.7-alt1
- new version
- fix to build with libav

* Tue Apr 05 2011 Sergey V Turchin <zerg@altlinux.org> 2.3.6-alt3
- move to standart place

* Mon Feb 21 2011 Sergey V Turchin <zerg@altlinux.org> 2.3.6-alt2
- fix to compile

* Thu Aug 26 2010 Sergey V Turchin <zerg@altlinux.org> 2.3.6-alt0.M51.1
- built for M51

* Thu Aug 26 2010 Sergey V Turchin <zerg@altlinux.org> 2.3.6-alt1
- new version

* Wed May 12 2010 Sergey V Turchin <zerg@altlinux.org> 2.3.5-alt0.M51.1
- build for M51

* Wed May 12 2010 Sergey V Turchin <zerg@altlinux.org> 2.3.5-alt1
- new version

* Thu Dec 10 2009 Sergey V Turchin <zerg@altlinux.org> 2.3.4-alt0.M51.1
- built for M51

* Thu Dec 10 2009 Sergey V Turchin <zerg@altlinux.org> 2.3.4-alt1
- new version

* Tue Aug 25 2009 Sergey V Turchin <zerg@altlinux.org> 2.3.3-alt1
- new version

* Fri Aug 07 2009 Sergey V Turchin <zerg@altlinux.org> 2.3.2-alt0.M50.1
- built for M50

* Mon Jul 20 2009 Sergey V Turchin <zerg@altlinux.org> 2.3.2-alt1
- initial specfile
