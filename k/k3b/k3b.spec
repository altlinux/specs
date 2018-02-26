%set_verify_elf_method no

%define qtdir %_qt3dir
%define kdedir %_K3prefix

%def_disable hal

%undefine __libtoolize
%define	stable_patchset	1.0.1

%define req_std_burning kdelibs >= 3.2, wodim, cdrkit, cdrdao, mkisofs >= 2.0, dvd+rw-tools, libdvdcss, libdvdread
%if_enabled hal
%define req_std_kde dbus hal
%else
%define req_std_kde dbus
%endif
%define req_std_common libacl, libattr, iceauth
%define req_multimedia libcdparanoia, lame, libmad, libvorbis, libmpcdec, libsndfile, libmusicbrainz, sox, transcode, libflac++, vcdimager >= 0.7, normalize, libtag

%define req_mini %req_std_burning, %req_std_kde, %req_std_common
%define req_all %req_mini, %req_multimedia


Name: k3b
Version: 1.0.5
Release: alt11

Group: Archiving/Cd burning
Summary: The CD Kreator (Complete set)
Summary(ru_RU.UTF-8): Программа записи CD (Полный набор)
License: GPL
Packager: Ilya Mashkin <oddity@altlinux.ru>
URL: http://www.k3b.org/

Source0: %name-%version.tar.bz2

Patch0: %name-%stable_patchset-compile_flags.patch
Patch1: %name-%stable_patchset-messages-alt.patch
Patch2: %name-1.0.4-disk_verify_cdrecord_noeject.patch
Patch3: %name-1.0.4-disk_verify_fallback.patch
Patch4: %name.desktop.patch

Patch6: %name-1.0.5-fix-autoconf-2.64.patch
Patch9: tde-3.5.13-build-defdir-autotool.patch
Patch10: cvs-auto_version_check.patch

Requires: %req_all
Requires: k3b-mini = %version

BuildRequires: flac gcc-c++ gcc-g77 kdelibs-devel libdbus-devel libdbus-tqt-devel libflac++-devel libflac-devel libjpeg-devel liblame-devel libmad-devel libmpcdec-devel libmusicbrainz-devel libpng-devel libsamplerate-devel libtag-devel libvorbis-devel libsndfile-devel qt3-designer xml-utils pkgconfig
%if_enabled hal
BuildRequires: libhal-devel
%endif
BuildRequires: libacl-devel libattr-devel libdvdread-devel
BuildRequires: desktop-file-utils

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
License: GPL
Group: Archiving/Cd burning
Requires: %req_mini
Obsoletes: k3b-minimal

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
License: GPL
Group: Development/KDE and QT
Requires: k3b = %version

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

 
%prep
%setup -q 
# patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p0

%patch6 -p1
%patch9
%patch10

%__subst 's/\.la\>/.so/g' admin/acinclude.m4.in
%__subst 's/\(-Wl,--no-undefined\)/-Wl,--warn-unresolved-symbols \1/g' admin/acinclude.m4.in
#MAKE="%__make" /bin/sh admin/cvs.sh cvs

cp -Rp /usr/share/libtool/aclocal/libtool.m4 admin/libtool.m4.in
cp -Rp /usr/share/libtool/config/ltmain.sh admin/ltmain.sh
make -f admin/Makefile.common

%build
rm -rf %buildroot
export QTDIR=%qtdir
export KDEDIR=%kdedir

export PATH=$QTDIR/bin:$KDEDIR/bin:$PATH

#add_optflags -I%_includedir/tqtinterface
%K3configure \
%if_disabled hal
	--without-hal \
%endif
	--without-k3bsetup
%make_build


%install
%K3install
%K3find_lang --with-kde %name


%files
%_K3lib/*.so
%_K3apps/k3b/cdi
%_K3apps/k3b/extra/*
%_K3apps/k3b/plugins
%_K3apps/konqueror/servicemenus/*audio*
%_K3apps/konqueror/servicemenus/*video*
%_K3apps/%name/servicemenus/*audio*
%_K3apps/%name/servicemenus/*video*
%_K3apps/konqsidebartng/virtual_folders/services/*video*
%_K3srv/video*

%files -f %name.lang mini
%_K3bindir/*
%_K3libdir/lib*.so*
%_K3xdg_apps/*
%_K3applnk/.hidden/*
%dir %_K3apps/%name
%_K3apps/%name/eventsrc
%_K3apps/%name/icons
%_K3apps/%name/k3bui.rc
%_K3apps/%name/pics
%_K3apps/%name/tips
%dir %_K3apps/%name/servicemenus
%_K3apps/%name/servicemenus/*data*
%_K3apps/%name/servicemenus/*image*
%_K3apps/konqueror/servicemenus/*copy*
%_K3apps/konqueror/servicemenus/%{name}_handle_empty*
%_K3srv/kfile*
%_kde3_iconsdir/hicolor/*/apps/*.*
%_K3mimelnk/*/*
%_K3snd/*
%doc README FAQ TODO AUTHORS ChangeLog

%files devel
%_K3includedir/*.h

%changelog
* Thu Apr 26 2012 Roman Savochenko <rom_as@altlinux.ru> 1.0.5-alt11
- Automake version is fixed to 1.11.5 detect.

* Thu Feb 23 2012 Roman Savochenko <rom_as@altlinux.ru> 1.0.5-alt10
- Build for TDE 3.5.13 release

* Mon Oct 24 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.5-alt9
- built without obsolete ffmpeg

* Tue Mar 22 2011 Sergey V Turchin <zerg@altlinux.org> 1.0.5-alt8
- built without hal

* Wed Mar 02 2011 Sergey V Turchin <zerg@altlinux.org> 1.0.5-alt7
- move to alternate place

* Sat May 15 2010 Motsyo Gennadi <drool@altlinux.ru> 1.0.5-alt6.4
- fix build with autoconf-2.64

* Fri Sep 25 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.0.5-alt6.3
- rebuild with libdvdread.so.4

* Tue Aug 11 2009 Ilya Mashkin <oddity@altlinux.ru> 1.0.5-alt6.2
- add cdrdao to requires again (Closes: #20264)

* Tue May 26 2009 Ilya Mashkin <oddity@altlinux.ru> 1.0.5-alt6.1
- fix build

* Fri May 08 2009 Ilya Mashkin <oddity@altlinux.ru> 1.0.5-alt6
- fix build
- remove deprecated macros

* Fri Sep 26 2008 Alexey Lokhin <warframe@altlinux.ru> 1.0.5-alt5
- cdrdao has been removed from requirements list because it's an optional tool and 'cdrdao' package is currently an orphan

* Tue Aug 26 2008 Alexey Lokhin <warframe@altlinux.ru> 1.0.5-alt4
- %name.destop.patch added to apply new tatar messages in k3b.desktop file.

* Mon Jul 21 2008 Alexey Lokhin <warframe@altlinux.ru> 1.0.5-alt3
- k3b-1.0.4-disk_verify_fallback.patch has been brought back due to many bug reports about freeze before disk verification.

* Thu Jun 19 2008 Alexey Lokhin <warframe@altlinux.ru> 1.0.5-alt2
- k3b-1.0.4-disk_verify_cdrecord_noeject.patch has been brought back due to many bug reports about freeze before disk verification.

* Mon Jun 02 2008 Alexey Lokhin <warframe@altlinux.ru> 1.0.5-alt1
- Version 1.0.5 build.
- k3b-1.0.4-disk_verify_cdrecord_noeject.patch has been removed.
- k3b-1.0.4-disk_verify_fallback.patch has been removed.
- 'cdrecord-classic' is not required anymore. Using 'wodim'.
- Added desktop DB entries update/cleaning for k3b-mini (found by repocop).

* Mon Mar 31 2008 Alexey Lokhin <warframe@altlinux.ru> 1.0.4-alt3
- Added a patch from http://bugs.kde.org/show_bug.cgi?id=151816 for 
  1.0.4 act as in previous version during project verification.
- Added a patch from http://bugs.kde.org/show_bug.cgi?id=156684 for
  1.0.4 not to eject disk after writing when using cdrecord.
- Added '--enable-ffmpeg-all-codecs' configure option to build with 
  audio RIFF+MPEG 1 Layer III support for audio projects source files

* Wed Jan 30 2008 Alexey Lokhin <warframe@altlinux.ru> 1.0.4-alt2
- Alt build number incremented to rebuild with new libavformat.

* Mon Nov 26 2007 Alexey Lokhin <warframe@altlinux.ru> 1.0.4-alt1
- Version 1.0.4 build.

* Thu Aug 09 2007 Alexey Lokhin <warframe@altlinux.ru> 1.0.3-alt2
- Added 'k3b_handle_empty_*.desktop' files to filelist.
- According to http://www.freesource.info/wiki/AltLinux/Razrabotchiku/OsobennostiSborkiPaketov removed menu file creation.

* Mon Jul 30 2007 Alexey Lokhin <warframe@altlinux.ru> 1.0.3-alt1
- Version 1.0.3 build.

* Mon Jul 09 2007 Alexey Lokhin <warframe@altlinux.ru> 1.0.2-alt2
- K3b messages patched not to yell about old cdrecord.

* Tue Jul 03 2007 Alexey Lokhin <warframe@altlinux.ru> 1.0.2-alt1
- Version 1.0.2 build.

* Mon Apr 23 2007 Alexey Lokhin <warframe@altlinux.ru> 1.0.1-alt1
- Version 1.0.1 build.

* Mon Mar 19 2007 Alexey Lokhin <warframe@altlinux.ru> 1.0-alt1
- Version 1.0 build.
- Removed patch for flac >= 1.1.3 because it is not needed anymore. 
- Removed format_dvd_+-_rw patch.
- Added requirements for libdvdread and libdvdread-devel.

* Tue Feb 27 2007 Alexey Lokhin <warframe@altlinux.ru> 0.12.17-alt5
- Patch to build with flac >= 1.1.3 (by led@) added.

* Mon Jan 29 2007 Alexey Lokhin <warframe@altlinux.ru> 0.12.17-alt4
- `iceauth' package added to common requirements.

* Tue Dec 26 2006 Alexey Lokhin <warframe@altlinux.ru> 0.12.17-alt3
- Build with new dbus.

* Mon Dec 04 2006 Alexey Lokhin <warframe@altlinux.ru> 0.12.17-alt2
- Closing remarks by greycat@ for bug #9944.

* Fri Nov 17 2006 Alexey Lokhin <warframe@altlinux.ru> 0.12.17-alt1
- Version 0.12.16 build.
- Package again has been again to 'k3b-mini', 'k3b' and 'k3b-devel'.

* Thu Sep 21 2006 Alexey Lokhin <warframe@altlinux.ru> 0.12.16-alt2
- Build with new libffmpeg.

* Mon Jul 03 2006 Alexey Lokhin <warframe@altlinux.ru> 0.12.16-alt1
- Version 0.12.16 build.

* Tue Jun 06 2006 Alexey Lokhin <warframe@altlinux.ru> 0.12.15-alt2
- Build with new libffmpeg.

* Fri Apr 14 2006 Alexey Lokhin <warframe@altlinux.ru> 0.12.15-alt1
- Version 0.12.15 build.

* Wed Mar 08 2006 Alexey Lokhin <warframe@altlinux.ru> 0.12.14-alt1
- Version 0.12.14 build.
- Added requirement for libdvdcss.

* Thu Feb 16 2006 Alexey Lokhin <warframe@altlinux.ru> 0.12.12-alt1
- Version 0.12.12 build.

* Sat Feb 11 2006 Alexey Lokhin <warframe@altlinux.ru> 0.12.11-alt1
- Version 0.12.11 build.

* Mon Feb 06 2006 Alexey Lokhin <warframe@altlinux.ru> 0.12.10-alt2
- Spec file fixed: added requirements for libacl, libattr.

* Tue Dec 20 2005 Alexey Lokhin <warframe@altlinux.ru> 0.12.10-alt1
- Version 0.12.10 build.
- Added patch, correcting translation of "Format DVD+-RW" message - 'format_dvd_+-_rw.patch'.

* Mon Nov 21 2005 Alexey Lokhin <warframe@altlinux.ru> 0.12.7-alt1
- Version 0.12.7 build.

* Fri Oct 07 2005 Alexey Lokhin <warframe@altlinux.ru> 0.12.4a-alt1
- Version 0.12.4a build.
- Menu source file removed from package.

* Thu Jul 28 2005 Alexey Lokhin <warframe@altlinux.ru> 0.12.2-alt1
- Version 0.12.2 build.
- Added libvorbis-devel detection fix for configure.
- Added patch for ALT-specific messages (no K3bSetup2 but ALT Control Center and 'control').
- Optimized buildreq.

* Tue May 24 2005 Alexey Lokhin <warframe@altlinux.ru> 0.11.24-alt1
- Version 0.11.24 build.
- 'Requires' fixed.

* Mon Apr 04 2005 Alexey Lokhin <warframe@altlinux.ru> 0.11.23-alt1
- Version 0.11.22 build
- Joliet now is enabled by default

* Mon Mar 21 2005 Alexey Lokhin <warframe@altlinux.ru> 0.11.22-alt1
- Version 0.11.22 build
- Added 'flac' to 'BuildRequres' for proper FLAC version detection during prep

* Wed Feb 23 2005 Alexey Lokhin <warframe@altlinux.ru> 0.11.20-alt2
- Spec file cleaning
- Added patch to compile with 'FLAC::Metadata::VorbisComment::get_vendor_string()' method in FLAC++-1.1.2

* Wed Feb 16 2005 Alexey Lokhin <warframe@altlinux.ru> 0.11.20-alt1
- Package 'k3b-minimal' has been combined with 'k3b'
- Version 0.11.20 build

* Thu Jan 20 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.11.17-alt3.1
- Rebuilt with libstdc++.so.6.

* Tue Dec 07 2004 Alexey Lokhin <warframe@altlinux.ru> 0.11.17-alt3
- Misapplied patches removed.

* Tue Nov 23 2004 Alexey Lokhin <warframe@altlinux.ru> 0.11.17-alt2
- New 'BuildRequires'.
- Added SCSI detection fix patch (from Fedora Core 3 SRPM).
- Fopen call 'RDWR' flag fixes added (from Fedora Core 3 SRPM).

* Wed Sep 29 2004 Alexey Lokhin <warframe@altlinux.ru> 0.11.17-alt1
- Version 0.11.17.

* Mon Sep 20 2004 Alexey Lokhin <warframe@altlinux.ru> 0.11.16-alt1
- Version 0.11.16 (skipping 0.11.15).

* Sat Aug 14 2004 Alexey Lokhin <warframe@altlinux.ru> 0.11.14-alt1
- Version 0.11.14.

* Mon Jun 28 2004 Alexey Lokhin <warframe@altlinux.ru> 0.11.12-alt1
- Version 0.11.12.
- Package splitted to multiple packages.

* Thu May 27 2004 Alexey Lokhin <warframe@altlinux.ru> 0.11.10-alt1
- Version 0.11.10.
- Spec file changed to compile with gcc-3.2.3.

* Mon Mar 29 2004 Alexey Lokhin <warframe@altlinux.ru> 0.11.9-alt1
- Version 0.11.9.
- Changed 'needs' in menu file from 'kde' to 'x11'.
- Added requirement for flac and lame encoding programs.

* Wed Mar 03 2004 Alexey Lokhin <warframe@altlinux.ru> 0.11.6-alt1
- Version 0.11.6.

* Sun Feb 22 2004 Alexey Lokhin <warframe@altlinux.ru> 0.11.5-alt1
- Version 0.11.5.

* Tue Feb 17 2004 Alexey Lokhin <warframe@altlinux.ru> 0.11.4-alt1
- Version 0.11.4 has been built.

* Sat Feb 14 2004 Alexey Lokhin <warframe@altlinux.ru> 0.11.3-alt1
- Version 0.11.3 has been built.
- Removed requirements for DivX, DVD tools and some audio encoding tools and libraries.

* Fri Jan 23 2004 Alexey Lokhin <warframe@altlinux.ru> 0.10.3-alt3
- Real sources added. Previous build contained custom test sources.

* Sat Jan 10 2004 Alexey Lokhin <warframe@altlinux.ru> 0.10.3-alt2
- Removed .la-files
- Fixed pthreads support during the compilation (patch by Zerg <Zerg@altlinux.org>).

* Mon Dec 08 2003 Alexey Lokhin <warframe@altlinux.ru> 0.10.3-alt1
- Version 0.10.3 has been built

* Mon Nov 10 2003 Alexey Lokhin <warframe@altlinux.ru> 0.10.2-alt1
- Version 0.10.2 has been built

* Tue Oct 28 2003 Alexey Lokhin <warframe@altlinux.ru> 0.10.1-alt1
- Version 0.10.1 has been built without k3bsetup support

* Tue Oct 07 2003 Alexey Lokhin <warframe@altlinux.ru> 0.9-alt1
- Version 0.9 has been built

* Fri Mar 07 2003 Alexey Gladkov <legion@altlinux.ru> 0.8.1-alt2
- x-cue.desktop and x-iso.desktop have been removed to resolve 
  conflicts with other cdrecord applications. They moved to 
  kdelibs package. 

* Sat Mar 01 2003 Alexey Gladkov <legion@altlinux.ru> 0.8.1-alt1
- k3b 0.8.1
- Bugfixes

* Sat Nov 23 2002 Alexey Gladkov <legion@altlinux.ru> 0.7.5-alt1
- 0.7.5

* Mon Nov 11 2002 Alexey Gladkov <legion@altlinux.ru> 0.7.4-alt2
- 0.7.4
- group fix (cdrecording -> cdwriter)

* Thu Oct 31 2002 Alexey Gladkov <legion@altlinux.ru> 0.7.3-alt1
- RPM build
