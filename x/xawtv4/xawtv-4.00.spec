%define dirlist app-defaults ru_RU.UTF-8/app-defaults ru_RU.CP1251/app-defaults ru_RU.KOI8-R/app-defaults
%define origname xawtv

%def_disable vdr

Name: %{origname}4
Version: 4.0

%def_enable aa
%def_disable arts

%define dateversion 20081014
%define number 100645
%define cvsversion %dateversion-%number
%define tvtuner tvtuner
%define gtktv gtktv
%define motv motv
%define fbtv fbtv
%define xawtv %origname
Release: alt3.cvs%dateversion.12.qa2

Summary: A X11 program for watching TV
Summary(ru_RU.UTF-8): Программа для просмотра ТВ
License: GPL
Group: Video
Url: http://bytesex.org/xawtv
Packager: Hihin Ruslan <ruslandh@altlinux.ru>

Source0: %origname-%cvsversion.tar.gz
Source1: xawtvrc-paris
Source2: XawTV
Source7: XawVDR
Source8: %name-%version-alt3.1-font.patch
Source9: %name-%version-alt3.1-windowsize.patch
Source10: %name-%version-alt-addon.tar

Patch0: %name-%version-as-need.patch
Patch1: %name-%version-gtkadd.patch
Patch2: %name-%version-delete-static.patch
Patch3: %name-%version-fbtv-fix.patch
Patch4: %name-%version-gcc4.patch
Patch5: %name-%version-aalib-fix.patch
Patch6: %name-%version-libquictime-fix.patch
Patch7: %name-%version-defwintitle.patch
Patch8: %name-%version-vdr.patch
Patch9: %name-%version-russian.patch
Patch10: %name-%version-vdr-russian.patch
Patch11: %name-%version-sint-fix.patch
#Patch12: %name-%version-exp.patch
#Patch12: %name-%version-stations-utf8.patch
Patch100: %name-%version-common-fix.patch
Patch101: %name-%version-x86_64.patch
Patch102: xawtv-4.0-page.patch
Patch103: xawtv-4.0-lx11.patch
Patch104: xawtv4-4.0-alt-DSO.patch

BuildPreReq: fontconfig-devel freetype2-devel gcc-c++ glib-devel
BuildPreReq: glib2 hostinfo libalsa-devel libdv-devel libgpm-devel libjpeg-devel
BuildPreReq: liblirc-devel libncurses-devel libpng-devel libslang-devel
BuildPreReq: libquicktime-devel
BuildPreReq: libtinfo-devel libzvbi-devel pkgconfig  zlib-devel
BuildPreReq: libXt-devel libFS-devel
BuildPreReq: gcc-c++ gccmakedep glib-devel libalsa-devel
BuildPreReq: libgtk+2-devel liblirc-devel libmad-devel
BuildPreReq: libmpeg2-devel libncurses-devel libpng-devel libquicktime-devel
BuildPreReq: libXaw-devel libXinerama-devel
BuildPreReq: libxml2-devel libXv-devel libzvbi-devel xorg-cf-files

BuildPreReq: libalsa-devel gtk2-devel
BuildPreReq: libmpeg2 libmpeg2-devel libpng-devel
BuildPreReq: libxml2 libxml2-devel lirc mad libmad-devel
BuildPreReq: libjpeg libjpeg-devel

BuildPreReq: glibc-devel iconv

BuildPreReq: gccmakedep
BuildPreReq: desktop-file-utils
BuildPreReq: xorg-server-common

Requires: %name-common = %version
Requires: lib%name = %version
Provides: %tvtuner


# Automatically added by buildreq on Mon Mar 28 2011
BuildRequires: aalib-devel gcc-c++ gccmakedep
BuildRequires: imake libFS-devel libXaw-devel libXinerama-devel
BuildRequires: libXp-devel libXpm-devel libXv-devel
BuildRequires: libmad-devel
BuildRequires: libopenmotif-devel

%package common
Summary: Common files for %fbtv/%motv/%xawtv/%gtktv
Summary(ru_RU.UTF-8): Файлы используемые совместно %fbtv/motv/%gtktv/%xawtv/%gtktv
Group: Video
Conflicts: xawtv <= 3.79-alt1
Requires: lib%name = %version

%package -n lib%name
Summary: Common files for %fbtv/%motv/%gtktv/%xawtv
Summary(ru_RU.UTF-8): Файлы используемые совместно %fbtv/%motv/%xawtv/%gtktv
Group: Video
Conflicts: xawtv <= 3.79-alt1

%if_enabled vdr
%package vdr
Summary: A X11 VDR frontend
Summary(ru_RU.UTF-8): X11 оболочка для VDR
Group: Video
Requires: lib%name = %version
Requires: %name-common = %version
Requires: vdr %xawtv
%endif

%package control
Summary: Control video4linux devices
Summary(ru_RU.UTF-8): Управление устройствами video4linux
Group: Video
Requires: lib%name = %version
Requires: %name-common = %version

%package -n %fbtv
Summary: A console program for watching TV
Summary(ru_RU.UTF-8): Консольная программа для просмотра ТВ
Group: Video
Provides: %tvtuner = version
Requires: lib%name = %version
Requires: %name-common = %version

%package misc
Summary: Xawtv miscellous stuff
Summary(ru_RU.UTF-8): Различные утилиты %xawtv
Group: Video
Requires: lib%name = %version
Requires: %name-common = %version

%package radio
Summary: Console radio application
Summary(ru_RU.UTF-8): Прослушивание радио
Group: Sound
Requires: lib%name = %version
Requires: %name-common = %version

%package dvb
Summary: dvb programs
Summary(ru_RU.UTF-8): Прогрммы для DVB
Group: Video
Requires: lib%name = %version
Requires: %name-common = %version

%package -n %motv
Summary: A Motif program for watching TV
Summary(ru_RU.UTF-8): Motif программа для просмотра ТВ
Group: Video
Provides: %tvtuner
Requires: lib%name = %version
Requires: %name-common = %version

%package -n %gtktv
Summary: A X11 program for watching TV
Summary(ru_RU.UTF-8): GTK программа для просмотра ТВ
Group: Video
Provides: %tvtuner
Requires: lib%name = %version
Requires: %name-common = %version

%package -n %xawtv
Summary: A X11 program for watching TV
Summary(ru_RU.UTF-8): X11 программа для просмотра ТВ
Group: Video
Provides: %tvtuner
Requires: lib%name = %version
Requires: %name-common = %version

%package web
Summary: Videotext pages webserver & images capture/upload to a webserver
Summary(ru_RU.UTF-8): Web-сервер страниц видеотекста, а также захват изображений и их передача на web-сервер
Group: Networking/WWW
Requires: lib%name = %version
Requires: %name-common = %version

%description
 tvtuner is a Video4Linux Stream Capture Viewer, that is a X11 program for
watching TV.

When run together with VDR %xawtv is capable of displaying digital
satellite, cable or terrestrial broadcasts.

%description -n %gtktv
 %gtktv is a Video4Linux Stream Capture Viewer, that is a X11 program for
watching TV.

It uses the Athena widgets.
 %gtktv has a nicer GUI which use GTK2 widgets.

When run together with VDR %xawtv is capable of displaying digital
satellite, cable or terrestrial broadcasts.

%description -n %gtktv -l ru_RU.UTF-8
 %gtktv  - программа для просмотра и записи видеопотоков Video4Linux,
то есть программа для просмотра ТВ.

 %gtktv использует набор графических элементов Athena. %gtktv обладает
улучшенным интерфейсом на основе элементов GTK2.

Может использоваться совместно с VDR для просмотра цифрового спутникового,
кабельного и эфирного ТВ формата DVB.

%description -n %xawtv
Xawtv is a Video4Linux Stream Capture Viewer, that is a X11 program for
watching TV.

It uses the Athena widgets.
MoTV has a nicer GUI which use lesstif (motif) widgets.

When run together with VDR %xawtv is capable of displaying digital
satellite, cable or terrestrial broadcasts.

%description -n %xawtv -l ru_RU.UTF-8
Xawtv - программа для просмотра и записи видеопотоков Video4Linux,
то есть программа для просмотра ТВ.

Xawtv использует набор графических элементов Athena. MoTV обладает
улучшенным интерфейсом на основе элементов lesstif (motif).

Может использоваться совместно с VDR для просмотра цифрового спутникового,
кабельного и эфирного ТВ формата DVB.

%description common
These're common files for %fbtv, %motv, %gtktv and %xawtv.
There're:
 * scantv - small text program that look for tv channels
 * streamer - capture tool (images / movies)

%description common -l ru_RU.UTF-8
Программы используемые совместно %fbtv, %motv, %gtktv и %xawtv.
 * scantv - небольшая текстовая программа поиска ТВ-каналов
 * streamer - программа захвата картинок / записи фильмов

%description -n lib%name
lib for %name

%description -n lib%name -l ru_RU.UTF-8
Библиотеки для программ %name %version

%if_enabled vdr
%description vdr
VDR frontend used to watch, record and replay digital TV broadcasts directly on your desktop.
 * %xawtv-vdr - patched version of %xawtv able to pass user input to VDR via SVDRP protocol

%description vdr -l ru_RU.UTF-8
Оболочка VDR предназначенная для просмотра, записи и воспроизведения цифрового ТВ на экране компьютера.
 * %xawtv-vdr - модифицированная версия %xawtv, которая передаёт все нажатия клавиш сервису VDR по протоколу SVDRP.
%endif

%description control
Xawtv-remote and v4lctl can be used to control a video4linux driven TV card.

Xawtv-remote passes the command to a already running %xawtv or %motv instance
using X11 properties.

V4lctl is a command line tool that sets the parameters directly.

%description control -l ru_RU.UTF-8
Xawtv-remote и v4lctl можно использовать для управления ТВ-карт стандарта video4linux.

Xawtv-remote передаёт средствами X11 команды уже запущенным копиям %xawtv и %motv.

V4lctl позволяет изменять параметры video4linux напрямую.

%description -n %fbtv
Fbtv is a program for watching TV with your linux box.
It runs on top of a graphic framebuffer device (/dev/fb0).

The pro is that you don't need X11 in order to watch tv.

fbtv shares the config file ($HOME/.tv) with the %xawtv
application.

Check the xawtv(1) manpage for details about the config file format.

%description -n %fbtv -l ru_RU.UTF-8
Fbtv - программа для просмотра ТВ, использующая графическую консоль
(устройство /dev/fb0). Её достоинство в том, что для просмотра телепрограмм
не требуется X-сервер. Fbtv использует тот же файл настроек ($HOME/.tv/*),
что и основная программа %xawtv.

Формат файла настроек описан в man-странице xawtv(1).

%description misc
This package has a few tools you might find useful.  They
have not to do very much to do with %xawtv.  I've used/wrote
them for debugging:
 * dump-mixers - dump mixer settings to stdout
 * propwatch   - monitors properties of X11 windows.  If you
                 want to know how to keep track of %xawtv's
                 _XAWTV_STATION property, look at this.
 * mtt4        - teletext browser with GTK
 * ntsc-cc     - reads vbi data from /dev/vbi and decodes the enclosed cc data.
 * pia         - play media files
 * record      - console sound recorder.  Has a simple input
                 level meter which might be useful to trouble
                 shoot sound problems.
 * showriff    - display the structure of RIFF files (avi, wav).

%description misc -l ru_RU.UTF-8
Несколько полезных утилит не связанных непосредственно с %xawtv.
 * dump-mixers - Выдаёт настройки микшера на стандартный вывод.
 * propwatch   - Отслеживает свойства окон X11. Может использоваться
                 в качестве примера работы со свойством _XAWTV_STATION.
 * mtt4         - Чтение телетекста для консоли и X11.
 * ntsc-cc     - Получение данных vbi с /dev/vbi и извлечение данных cc.
 * pia         - Проигрывает записанные файлы.
 * record      - Запись звука в консоли. Имеет примитивный индикатор уровня
                 записи, который может пригодиться для разбора проблем записи.
 * showriff    - Показ структуры файлов стандарта RIFF (avi, wav).

%description -n %motv
This is a %motv-based Video4Linux capture viewer.

It is basically %xawtv with a more userfriendly GUI.
It has the same features, uses the same config file, has the same command
line switches, you can control it using %xawtv-remote.
Most keyboards shortcuts are identical too.

%description -n %motv -l ru_RU.UTF-8
Программа просмотра и записи видео %motv. Практически аналог %xawtv с
улучшенным интерфейсом. Обладает теми же возможностями, использует
тот же файл настроек, параметры командной строки, управляется с помощью
%xawtv-remote. Большинство горячих клавиш также совпадают с %xawtv.

%description radio
This is a ncurses-based radio application

%description dvb
This is a dvb application

%description radio -l ru_RU.UTF-8
Консольная программа для управления радиоприемником

%description web
Webcam captures images from a video4linux device like btv,
annotates them and and uploads them to a webserver using ftp
in a endless loop.

Alevtd is http daemon which serves videotext pages as HTML.
Tune in some station with a utility like v4lctl or some TV application.
Then start it and point your browser to http://localhost:5654/

Pages may be requested either in HTML format (http://localhost:5654/<page>/
or http://localhost:5654/<page>/<subpage>.html) or in ASCII text format
(http://localhost:5654/<page>/<subpage>.txt).
Subpage "00" can be used for pages without subpages.

%description web -l ru_RU.UTF-8
Webcam захватывает картинки с устройств video4linux, таких как btv,
аннотирует их и передаёт на web-сервер по ftp в бесконечном цикле.

Alevtd - http демон передающий страницы видеотекста в виде HTML.
Для его использования следует настроиться на станцию при помощи v4lctl
или другой ТВ программы, запустить alevtd и в браузере ввести адрес
http://localhost:5654/.

Страницы могут передаваться в формате HTML (http://localhost:5654/<page>/
or http://localhost:5654/<page>/<subpage>.html) или в виде простого текста
(http://localhost:5654/<page>/<subpage>.txt). Для страниц без "подстраниц"
можно использовать номер "00".

%prep
%setup -q -a10 -n %origname
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
#%patch12 -p1
%patch100  -p1
%patch101  -p1
%patch102  -p1

pushd gtk
mv xawtv.c %gtktv.c
mv mtt.c mtt4.c
mv pia.c pia4.c
popd

%patch103  -p1
%patch104 -p2

%build
%autoreconf
#automake -a -c ||

inst=$(ls	/usr/share/automake*/install-sh \
		/usr/local/share/automake*/install-sh \
		2>/dev/null | head -1)

cp "$inst" .

%configure \
	%{subst_enable aa} \
	%{subst_enable arts}

%make CFLAFS="%optflags"

%install
%make_install DESTDIR=%buildroot \
	     ROOT=%buildroot	\
	     SUID_ROOT="" install

%find_lang %origname %gtktv %motv %fbtv %name

install -pD -m 644 %_builddir/%origname/libng/libng.so %buildroot/%_libdir/

# Fix geometry and fonts
pushd %buildroot/%_sysconfdir/
pwd
cat %SOURCE8 | patch -p1
cat %SOURCE9 | patch -p1
popd

install -m 755 %SOURCE2 %buildroot%_bindir/XawTV
%if_enabled vdr
install -m 755 %SOURCE7 %buildroot%_bindir/XawVDR
%endif

# Menu entries

install -pD -m 644 contrib/%motv-32.png %buildroot%_niconsdir/%motv.png
install -pD -m 644 contrib/%motv-48.png %buildroot%_liconsdir/%motv.png
install -pD -m 644 contrib/%motv-16.png %buildroot%_miconsdir/%motv.png

install -pD -m 644 contrib/%xawtv-32.png %buildroot%_niconsdir/%xawtv.png
install -pD -m 644 contrib/%xawtv-48.png %buildroot%_liconsdir/%xawtv.png
install -pD -m 644 contrib/%xawtv-16.png %buildroot%_miconsdir/%xawtv.png

install -pD -m 644 contrib/xawtv32x32.xpm %buildroot%_niconsdir/%gtktv.png
install -pD -m 644 contrib/xawtv48x48.xpm %buildroot%_liconsdir/%gtktv.png
install -pD -m 644 contrib/xawtv16x16.xpm %buildroot%_miconsdir/%gtktv.png

install -m 644 %SOURCE1 .

install -d %buildroot%_desktopdir/
install -pD -m644 desktop-new/*.desktop %buildroot%_desktopdir/

%files -n %gtktv
%_bindir/%gtktv
%_niconsdir/%{gtktv}*
%_liconsdir/%{gtktv}*
%_miconsdir/%{gtktv}*
%_desktopdir/gtktv.desktop

%files -n lib%name
%dir %_libdir/%name
%_libdir/%name/*.so*
%_libdir/libng.so

%files -n %xawtv
%config(noreplace) %_sysconfdir/X11/%name/app-defaults/Xawtv4
%attr(755,root,root) %_sysconfdir/X11/%name/*/app-defaults/
%config(noreplace) %_sysconfdir/X11/%name/*/app-defaults/Xawtv4
%exclude %_sysconfdir/X11/%name/app-defaults/Xawvdr
%if_enabled vdr
%exclude %_sysconfdir/X11/%name/*/app-defaults/Xawvdr
%endif

%exclude %_sysconfdir/X11/%name/app-defaults/mtt4
%exclude %_sysconfdir/X11/%name/app-defaults/MoTV4
%exclude %_sysconfdir/X11/%name/*/app-defaults/
%exclude %_sysconfdir/X11/%name/*/app-defaults/MoTV4

%_bindir/%xawtv
%_bindir/XawTV
%_niconsdir/%{xawtv}*
%_liconsdir/%{xawtv}*
%_miconsdir/%{xawtv}*
%_desktopdir/xawtv.desktop

%if_enabled vdr
%files vdr
%config(noreplace) %_sysconfdir/X11/%name/app-defaults/Xawvdr
%config(noreplace) %_sysconfdir/X11/%name/*/app-defaults/Xawvdr
%_bindir/XawVDR
%_desktopdir/xawvdr.desktop
%endif

%files common -f %origname.lang
%exclude %_mandir/es
%exclude %_mandir/fr
%attr(4711,root,root) %_bindir/v4l-conf
%_bindir/rootv
%_bindir/scantv
%_bindir/subtitles
%_bindir/v4l-info
%_bindir/record
%_bindir/mtt4
%_bindir/streamer
%_desktopdir/mtt4.desktop
%_desktopdir/scantv.desktop
%_man1dir/alevtd.1*
%_man1dir/dump-mixers.1*
%_man1dir/fbtv.1*
%_man1dir/motv.1*
%_man1dir/mtt.1*
%_man1dir/ntsc-cc.1*
%_man1dir/pia.1*
%_man1dir/propwatch.1*
%_man1dir/radio.1*
%_man1dir/record.1*
%_man1dir/rootv.1*
%_man1dir/scantv.1*
%_man1dir/showriff.1*
%_man1dir/streamer.1*
%_man1dir/subtitles.1*
%_man1dir/ttv.1*
%_man1dir/v4l-info.1*
%_man1dir/v4lctl.1*
%_man1dir/webcam.1*
%_man1dir/xawtv-remote.1*
%_man1dir/xawtv.1*
%_man5dir/xawtvrc.5*
%_man8dir/v4l-conf.8*
%dir %_datadir/xawtv
%_datadir/xawtv/*
%doc contrib/frequencies*
%doc Changes README* TODO
%doc README*
%doc NEW_IN_4
%doc contrib/frequencies*
%doc xawtvrc*
%doc MAKEDEV.v4l
%attr(755,root,root) %_sysconfdir/X11/%name/*/app-defaults/
%exclude %_sysconfdir/X11/%name/app-defaults/mtt4
%exclude %_sysconfdir/X11/%name/app-defaults/MoTV4
%exclude %_sysconfdir/X11/%name/*/app-defaults/
%exclude %_sysconfdir/X11/%name/*/app-defaults/MoTV4
%if_enabled vdr
%exclude %_sysconfdir/X11/%name/app-defaults/Xawvdr
%exclude %_sysconfdir/X11/%name/*/app-defaults/Xawvdr
%endif

%files control
%_bindir/v4lctl
%_bindir/%xawtv-remote

%files -n %fbtv
%_bindir/%fbtv

%files misc
%config(noreplace) %_sysconfdir/X11/%name/app-defaults/mtt4
%_bindir/dump-mixers
%_bindir/ntsc-cc
%_bindir/pia
%_bindir/pia4
%_bindir/propwatch
%_bindir/showriff
%_bindir/showqt
%_bindir/alexplore

%_desktopdir/alexplore.desktop
%_desktopdir/pia.desktop

%files dvb
%_bindir/dvbrowse
%_bindir/dvbradio
%_desktopdir/dvbradio.desktop
%_desktopdir/dvbrowse.desktop

%files -n %motv
%config(noreplace) %_sysconfdir/X11/%name/app-defaults/MoTV4
%attr(755,root,root) %_sysconfdir/X11/%name/*/app-defaults/
%config(noreplace) %_sysconfdir/X11/%name/*/app-defaults/MoTV4
%if_enabled vdr
%exclude %_sysconfdir/X11/%name/app-defaults/Xawvdr
%exclude %_sysconfdir/X11/%name/*/app-defaults/Xawvdr
%endif

%_bindir/%motv
%_niconsdir/%{motv}*
%_liconsdir/%{motv}*
%_miconsdir/%{motv}*
%_desktopdir/motv.desktop

%files radio
%_bindir/radio
%_desktopdir/%xawtv-radio.desktop

%files web
%_bindir/alevtd
%_bindir/webcam

%changelog
* Tue Jun 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0-alt3.cvs20081014.12.qa2
- Fixed build

* Mon Apr 18 2011 Igor Vlasenko <viy@altlinux.ru> 4.0-alt3.cvs20081014.12.qa1
- NMU: fixed desktop file categories; converted menu to desktop files

* Mon Mar 28 2011 Hihin Ruslan <ruslandh@altlinux.ru> 4.0-alt3.cvs20081014.12
- fix BuildRequires

* Sat Feb 19 2011 Hihin Ruslan <ruslandh@altlinux.ru> 4.0-alt3.cvs20081014.11
- disable arts

* Mon Nov 22 2010 Hihin Ruslan <ruslandh@altlinux.ru> 4.0-alt3.cvs20081014.10
- fix build

* Thu Nov 19 2009 Hihin Ruslan <ruslandh@altlinux.ru> 4.0-alt3.cvs20081014.9
- rebuild with libquicktime

* Wed Dec 17 2008 Hihin Ruslan <ruslandh@altlinux.ru> 4.0-alt3.cvs20081014.8
- disable vdr

* Mon Dec 01 2008 Hihin Ruslan <ruslandh@altlinux.ru> 4.0-alt3.cvs20081014.7
- correct BuildRequires

* Thu Nov 20 2008 Hihin Ruslan <ruslandh@altlinux.ru> 4.0-alt3.cvs20081014.6
- correct spec

* Sun Nov 09 2008 Hihin Ruslan <ruslandh@altlinux.ru> 4.0-alt3.cvs20081014.5
- new CVS version

* Mon Jun 09 2008 Hihin Ruslan <ruslandh@altlinux.ru> 4.0-alt3.cvs20070625.5
- rebuild with new libquicktime

* Thu Apr 10 2008 Igor Vlasenko <viy@altlinux.ru> 4.0-alt3.cvs20070625.4.qa1
- NMU (by repocop): the following fixes applied:
 * desktop-mime-entry for xawtv4-misc

* Tue Feb 19 2008 Hihin Ruslan <ruslandh@altlinux.ru> 4.0-alt3.cvs20070625.4
- Remove #include <asm/page.h>

* Tue Feb 19 2008 Hihin Ruslan <ruslandh@altlinux.ru> 4.0-alt3.cvs20070625.3
- add BuildPreReq: kernel-headers

* Wed Sep 26 2007 Hihin Ruslan <ruslandh@altlinux.ru> 4.0-alt3.cvs20070625.2
- replace glibc-kernheaders

* Tue Aug 21 2007 Hihin Ruslan <ruslandh@altlinux.ru> 4.0-alt3.cvs20070625.1
- new CVS version

* Sun Jan 14 2007 Hihin Ruslan <ruslandh@altlinux.ru> 4.0-alt3.cvs20061123.1
- correct patch for /etc/xawtv4

* Fri Jan 12 2007 Hihin Ruslan <ruslandh@altlinux.ru> 4.0-alt3.cvs20061123
- correct for x86_64

* Fri Dec 15 2006 Hihin Ruslan <ruslandh@altlinux.ru> 4.0-alt2.cvs20061123
- new CVS version

* Sun Nov 12 2006 Hihin Ruslan <ruslandh@altlinux.ru> 4.0-alt2.cvs20061011
- new CVS version

* Tue Nov 07 2006 Hihin Ruslan <ruslandh@altlinux.ru> 4.0-alt2.cvs20060816
- replace XawVDR

* Sat Sep 16 2006 Hihin Ruslan <ruslandh@altlinux.ru> 4.0-alt1.cvs20060816
- build for ALTlinux

* Wed Aug 30 2006 Hihin Ruslan <hihin_c@t_narod_dot_ru> 4.0-cvs20060816.alt0
- new cvs version

* Mon Aug 14 2006 Hihin Ruslan <hihin_c@t_narod_dot_ru> 4.0-alt1c.20060615
- add %name-%version-common-fix.patch

* Sun Aug 06 2006 Hihin Ruslan <hihin_c@t_narod_dot_ru> 4.0-alt1b.20060615
- add xawtv4-4.0-sint-fix.patch
- add desktop files

* Tue Aug 01 2006 Hihin Ruslan <hihin_c@t_narod_dot_ru> 4.0-alt1a.20060615
- new version
- add or repaire patchs :
- 	xawtv4-4.0-as-need.patch	- fix dlopen
-	xawtv4-4.0-gtkadd.patch		- fix two %xawtv
-	xawtv-4.0-delete-static.patch   - replace static lib on dinamic lib (libng)
-	xawtv4-4.0-fbtv-fix.patch	- fix %fbtv (no all fix)
- 	xawtv4-4.0-gcc4.patch		- correct from Suse
				    xawtv4-3.999_0.20051018-0.pm.0.src.rpm
- 	xawtv4-4.0-aalib-fix.patch	- delete aalib (bad upstream)
- 	xawtv4-4.0-libquictime-fix.patch - add patch for qt-plugins (Fix mi :) )
- 	xawtv4-4.0-defwintitle.patch	- correct from 3.95
- 	xawtv4-4.0-vdr.patch		- correct from 3.95 + my patch (Fix mi :) )
- 	xawtv4-4.0-russian.patch	- correct from 3.95
- 	xawtv4-4.0-vdr-russian.patch	- correct from 3.95
- Credits :
-		Andrey Rahmatullin <wrar@altlinux.ru>
-		Michael Shigorin <mike@osdn.org.ua>
-		Slava Semushin <php-coder@ngs.ru>
-		Damir Shayhutdinov <lost404@gmail.com>
-		Igor Zubkov <icesik@mail.ru>
-

* Tue Nov 08 2005 Vyacheslav Dikonov <slava@altlinux.ru> 3.95-alt1
- 3.95, fix to use libquicktime headers in /usr/include/lqt

* Sat Jan 08 2005 Vyacheslav Dikonov <slava@altlinux.ru> 3.93-alt2
- Russian translation

* Fri Jan 07 2005 Vyacheslav Dikonov <slava@altlinux.ru> 3.93-alt1
- 3.93
- 768x576 (PAL) default window size
- small caps work as hotkeys
- thinner font
- improved VDR support

* Mon Jun 07 2004 Yuri N. Sedunov <aris@altlinux.ru> 3.90-alt2.1
- rebuild against libdv-0.102.
- %xawtv-vdr subpackage requires vdr (slava@).

* Sat Dec 06 2003 Vyacheslav Dikonov <slava@altlinux.ru> 3.90-alt2
- bugfixes

* Mon Dec 01 2003 Vyacheslav Dikonov <slava@altlinux.ru> 3.90-alt1
- 3.90, VDR support enabled

* Tue Apr 29 2003 Kachalov Anton <mouse@altlinux.ru> 3.80-alt4
- remove checking for remote host for v4l-conf

* Mon Jan 20 2003 Kachalov Anton <mouse@altlinux.ru> 3.80-alt3
- fixed bug #0001906 (lose BuildRequires - motif)

* Mon Dec 23 2002 Kachalov Anton <mouse@altlinux.ru> 3.80-alt2
- russian description & summary

* Fri Dec 06 2002 Kachalov Anton <mouse@altlinux.ru> 3.80-alt1
- version 3.80

* Tue Nov 26 2002 Alexander Belov <asbel@mail.ru> 3.79-alt2
- Adding russian channel freq.
- Mandrake2ALT adaptation
- partial merge with Rider's 3.79-alt1 spec
- Fixing Mandrake error with missing /usr/share/%xawtv
- Adding quicktime support
- Changing names of some packages for prefix '%xawtv' at all
- Fixing BuildRequests
- Version 3.79

* Fri Nov 22 2002 Rider <rider@altlinux.ru> 3.79-alt1
- new version

* Tue Oct 08 2002 Rider <rider@altlinux.ru> 3.76-alt2
- specfile bugfix
- menu item for xawtv-radio

* Thu Oct 03 2002 Rider <rider@altlinux.ru> 3.76-alt1
- 3.76

* Tue Apr 09 2002 Rider <rider@altlinux.ru> 3.73-alt1
- 3.73

* Sun Feb 24 2002 Rider <rider@altlinux.ru> 3.72-alt1
- 3.72

* Tue Feb 19 2002 Rider <rider@altlinux.ru> 3.71-alt1
- 3.71

* Sat Feb 09 2002 Rider <rider@altlinux.ru> 3.70-alt1
- 3.70

* Sun Feb 03 2002 Rider <rider@altlinux.ru> 3.69-alt1
- 3.69

* Thu Jan 31 2002 Rider <rider@altlinux.ru> 3.68-alt1
- 3.68

* Sun Dec 09 2001 Rider <rider@altlinux.ru> 3.65-alt1
- 3.65

* Sat Nov 03 2001 Rider <rider@altlinux.ru> 3.64-alt1
- 3.64

* Fri Oct 12 2001 AEN <aen@logic.ru> 3.62-alt3
- rebuilt with libpng.so.3

* Thu Oct 11 2001 Rider <rider@altlinux.ru> 3.62-alt2
- updated east europe channels list (patch from svb@altlinux.ru)

* Tue Oct 09 2001 Rider <rider@altlinux.ru> 3.62-alt1
- 3.62

* Sat Aug 18 2001 Rider <rider@altlinux.ru> 3.60-alt1
- 3.60

* Wed Jun 27 2001 Sergie Pugachev <fd_rag@altlinux.ru> 3.52-alt1
- new version

* Thu Jun 04 2001 Rider <rider@altlinux.ru>
- 3.50

* Wed May 23 2001 Rider <rider@altlinux.ru>
- 3.48

* Mon May 07 2001 Rider <rider@altlinux.ru>
- 3.46

* Wed Apr 10 2001 Rider <rider@altlinux.ru>
- 3.39

* Sun Mar 18 2001 Rider <rider@altlinux.ru>
- 3.38
- added France and Russia sample config files

* Wed Feb 14 2001 AEN <aen@logic.ru>
- 3.34

* Wed Jan 17 2001 AEN <aen@logic.ru>
- RE adaptation

* Sun Dec 31 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 3.27-1mdk
- new and shiny source.
- remove .bz2 extension for man-pages and change it to wildcard.

* Tue Nov 21 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 3.24-1mdk
- new release
- make rpmlint happier

* Fri Oct 27 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 3.23-1mdk
- new release

* Tue Oct 17 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 3.22-1mdk
- new release

* Tue Oct 03 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 3.21-3mdk
- enable DPMS
- fix buildrequires
- disable mouse pointer on v4l buffer
- provide example config file for Paris inhabitants
- add alevtd, rootv, scantv and webcam

* Mon Sep 18 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 3.21-2mdk
- fix menu entry

* Wed Sep 13 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 3.21-1mdk
- new release

* Wed Sep 13 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 3.20-3mdk
- really fix ressources (i know, i've sucked :-( )
- add a menu entry

* Tue Sep 12 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 3.20-2mdk
- fix ressources
- spec file is now shrt-crct compliant :-)

* Wed Sep 06 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 3.20-1mdk
- new release

* Wed Aug 23 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 3.19-1mdk
- new release

* Tue Aug 22 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 3.18-1mdk
- fix url
- new release
- compile for XF4 (if you load v4l in module section of /etc/X11/XFconfig-4,
  you can do color conversion and image scaling in hardware on g200/g400
  with hackkernel).

* Wed Jul 26 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 3.17-3mdk
- BM
- fix build as non-root

* Mon Jul 17 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 3.17-2mdk
- little spec cleaning

* Tue Jun 27 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 3.17-1mdk
- new release
- package chmouelization :
	* use %%_mandir, %%prefix
	* use spechelper
	* use %%makeinstall, %%configure

* Mon Jun 19 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 3.16-1mdk
- new release (mainly a smaller SRPM)

* Thu Jun 08 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 3.15-1mdk
- new release

* Tue Apr 18 2000 J. Nick Koston <bdraco@darkorb.net> 3.12-1mdk
- Madrakeified

