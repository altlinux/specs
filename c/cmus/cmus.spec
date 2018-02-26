# -*- coding: utf-8; mode: rpm-spec -*-
# $Id: cmus.spec,v 1.34 2006/08/20 13:58:03 eugene Exp $

%define name cmus
%define version 2.4.2
%define release alt1

Name: %name
Version: %version
Release: %release.1
Summary: CMus - C* Music Player
License: GPL
Group: Sound
Url: http://cmus.sourceforge.net/

Packager: Eugene Vlasov <eugvv@altlinux.ru>

AutoReq: yes, nopython

Source0: %name-%version.tar
Source2: cmus.desktop

# Patch0: cmus-vorbis_includes.patch
# Temporary disable build with ncursesw - removed. Now cmus use ncurses if
# ncursesw not available
# Patch1: %name-with_ncurses.patch
Patch2: %name-alt-libav-0.8.patch

# User interface
BuildRequires(build): libtinfo-devel
BuildRequires(build): libncursesw-devel
# Output
BuildRequires(build): libalsa-devel
BuildRequires(build): libao-devel
BuildRequires(build): libpulseaudio-devel
# Input
BuildRequires(build): libmad-devel
BuildRequires(build): libogg-devel
BuildRequires(build): libvorbis-devel
BuildRequires(build): libflac-devel
BuildRequires(build): libmodplug-devel
BuildRequires(build): libmpcdec-devel
BuildRequires(build): libfaad-devel
BuildRequires(build): libmikmod-devel
BuildRequires(build): libmpeg4ip-devel
BuildRequires(build): libavcodec-devel
BuildRequires(build): libavformat-devel
BuildRequires(build): libavutil-devel
BuildRequires(build): libwavpack-devel

# Automatically added by buildreq on Sat Jul 28 2007
BuildRequires: libstdc++-devel

%description
CMus is a small and fast text mode music player.
Track metadata cache makes adding files to playlist very fast and separate
playlist loader thread keeps UI always usable. cmus is also fast to use;
most commands require just one keypress, more complex commands are
executed in vi-style command mode.
Features
  * Input
    o FLAC
    o Ogg/Vorbis
    o MP3 (libmad)
    o Wav
    o .mod, .s3m, ... (libmodplug, libmikmod)
    o .mpc, .mpp, .mp+ (libmpcdec)
    o MPEG-4 AAC (.mp4, .m4a, .m4b)
    o AAC (.aac, audio/aac, audio/aacp)
    o FFMPEG (.wma files, could extend to support more)
    o WavPack (.wv)
  * Output
    o ALSA
    o OSS
    o libao
  * Playing
    o Album/artist modes; playing within one album or artist
    o Play queue
    o MP3 and Ogg streaming (Shoutcast/Icecast)
    o Powerful playlist filters
  * Interface
    o Easy to use directory browser
    o Customizable colors
    o Dynamic keybindings, you can bind a key to any command
    o Vi/less style search mode
    o Vi style command mode with tabulator expansion
  * Misc
    o Can run external commands for the selected files (tag-editor for
      example)
    o UTF-8 support
    o Can be controlled via UNIX socket using cmus-remote command

%description -l ru_RU.UTF-8
CMus - маленький и быстрый музыкальный проигрыватель, использующий
библиотеку ncurses.
Кэширование данных треков делает добавление файлов в список
воспроизведения очень быстрым, фоновая загрузка файлов в список не
блокирует воспроизведение и интерфейс пользователя.
Для выполнения большинства команд достаточно нажатия на одну клавишу,
более сложные команды отдаются в стиле редактора Vi.
Особенности
  * Входные форматы:
    o FLAC
    o Ogg/Vorbis
    o MP3 (libmad)
    o Wav
    o .mod, .s3m, ... (libmodplug, libmikmod)
    o .mpc, .mpp, .mp+ (libmpcdec)
    o MPEG-4 AAC (.mp4, .m4a, .m4b)
    o AAC (.aac, audio/aac, audio/aacp)
    o FFMPEG (.wma, возможность поддержки многих форматов)
    o WavPack (.wv)
  * Выход:
    o ALSA
    o OSS
    o libao
  * Воспроизведение
    o Режимы альбом/исполнитель. Воспроизведение целого альбома или
      полностью исполнителя
    o Очередь воспроизведения
    o Потоковое воспроизведение MP3 и Ogg (Shoutcast/Icecast)
    o Фильтры списков воспроизведения
  * Интерфейс
    o Легкая в использовании навигация по каталогам
    o Настраиваемые цвета
    o Переопределяемые комбинации клавиш, возможность задать клавишу для
      любой команды
    o Режим поиска в тиле vi/less
    o Командный режим в стиле vi с поддержкой дополнения строк
  * Прочее
    o Возможность запуска внешних команд для выбранных файлов (например,
      редактора тегов)
    o Поддержка UTF-8
    o Может управлятся через сокет UNIX (используя команду cmus-remote)

%package in-flac
Summary: FLAC plugin for CMus
Group: Sound

Requires: %name = %version-%release

%description in-flac
CMus is a small and fast music player using the ncurses library.

This package contains FLAC plugin.

%description -l ru_RU.UTF-8 in-flac
CMus - маленький и быстрый музыкальный проигрыватель, использующий
библиотеку ncurses.

Этот пакет содержит расширение для воспроизведения FLAC.


%package in-vorbis
Summary: Ogg/Vorbis plugin for CMus
Group: Sound

Requires: %name = %version-%release

%description in-vorbis
CMus is a small and fast music player using the ncurses library.

This package contains Ogg/Vorbis plugin.

%description -l ru_RU.UTF-8 in-vorbis
CMus - маленький и быстрый музыкальный проигрыватель, использующий
библиотеку ncurses.

Этот пакет содержит расширение для воспроизведения Ogg/Vorbis.


%package in-modplug
Summary: libmodplug plugin for CMus (.mod, .x3m, ...)
Group: Sound

Requires: %name = %version-%release

%description in-modplug
CMus is a small and fast music player using the ncurses library.

This package contains modules plugin (libmodplug).

%description -l ru_RU.UTF-8 in-modplug
CMus - маленький и быстрый музыкальный проигрыватель, использующий
библиотеку ncurses.

Этот пакет содержит расширение для модулей (libmodplug).

%package in-mpc
Summary: MPC plugin for CMus
Group: Sound

Requires: %name = %version-%release

%description in-mpc
CMus is a small and fast music player using the ncurses library.

This package contains plugin for .mpc, .mpp, .mp+ files (libmpcdec).

%description -l ru_RU.UTF-8 in-mpc
CMus - маленький и быстрый музыкальный проигрыватель, использующий
библиотеку ncurses.

Этот пакет содержит расширение для воспроизведения файлов .mpc, .mpp,
.mp+ (libmpcdec).

%package in-mikmod
Summary: libmikmod plugin for CMus (.mod, .x3m, ...)
Group: Sound

Requires: %name = %version-%release

%description in-mikmod
CMus is a small and fast music player using the ncurses library.

This package contains modules plugin (libmikmod).

%description -l ru_RU.UTF-8 in-mikmod
CMus - маленький и быстрый музыкальный проигрыватель, использующий
библиотеку ncurses.

Этот пакет содержит расширение для модулей (libmikmod).

%package in-mp4
Summary: MPEG-4 AAC plugin for CMus (.mp4, .m4a, .m4b)
Group: Sound

Requires: %name = %version-%release

%description in-mp4
CMus is a small and fast music player using the ncurses library.

This package contains plugin for MPEG-4 AAC (.mp4, .m4a, .m4b) files.

%description -l ru_RU.UTF-8 in-mp4
CMus - маленький и быстрый музыкальный проигрыватель, использующий
библиотеку ncurses.

Этот пакет содержит расширение для воспроизведения файлов MPEG-4 AAC
(.mp4, .m4a, .m4b).

%package in-aac
Summary: AAC plugin for CMus (.aac, audio/aac, audio/aacp)
Group: Sound

Requires: %name = %version-%release

%description in-aac
CMus is a small and fast music player using the ncurses library.

This package contains plugin for AAC (.aac, audio/aac, audio/aacp) files.

%description -l ru_RU.UTF-8 in-aac
CMus - маленький и быстрый музыкальный проигрыватель, использующий
библиотеку ncurses.

Этот пакет содержит расширение для воспроизведения файлов AAC (.aac,
audio/aac, audio/aacp).

%package in-wavpack
Summary: WavPack plugin for CMus (.wv, audio/x-wavpack)
Group: Sound

Requires: %name = %version-%release

%description in-wavpack
CMus is a small and fast music player using the ncurses library.

This package contains plugin for WavPack (.wv, audio/x-wavpack) files.

%description -l ru_RU.UTF-8 in-aac
CMus - маленький и быстрый музыкальный проигрыватель, использующий
библиотеку ncurses.

Этот пакет содержит расширение для воспроизведения файлов WavPack (.wv, 
audio/x-wavpack).

%package in-ffmpeg
Summary: FFMPEG plugin for CMus (.shn, .wma)
Group: Sound

Requires: %name = %version-%release

%description in-ffmpeg
CMus is a small and fast music player using the ncurses library.

This package contains plugin for FFMPEG support (.wma files, could extend
to support more).

%description -l ru_RU.UTF-8 in-aac
CMus - маленький и быстрый музыкальный проигрыватель, использующий
библиотеку ncurses.

Этот пакет содержит расширение для поддержки FFMPEG (дает возможность
воспроизведения .wma и других форматов).


%package out-alsa
Summary: ALSA output plugin for CMus
Group: Sound

Requires: %name = %version-%release

%description out-alsa
CMus is a small and fast music player using the ncurses library.

This package contains ALSA output plugin.

%description -l ru_RU.UTF-8 out-alsa
CMus - маленький и быстрый музыкальный проигрыватель, использующий библиотеку ncurses.

Этот пакет содержит расширение для воспроизведения через ALSA.


%package out-pulse
Summary: PulseAudio output plugin for CMus
Group: Sound

Requires: %name = %version-%release

%description out-pulse
CMus is a small and fast music player using the ncurses library.

This package contains PulseAudio output plugin.

%description -l ru_RU.UTF-8 out-pulse
CMus - маленький и быстрый музыкальный проигрыватель, использующий библиотеку ncurses.

Этот пакет содержит расширение для воспроизведения через PulseAudio.


%package out-ao
Summary: libao output plugin for CMus
Group: Sound

Requires: %name = %version-%release

%description out-ao
CMus is a small and fast music player using the ncurses library.

This package contains libao output plugin.

%description -l ru_RU.UTF-8 out-ao
CMus - маленький и быстрый музыкальный проигрыватель, использующий библиотеку ncurses.

Этот пакет содержит расширение для воспроизведения через libao.


%prep
%setup -q
# %patch0 -p1
# %patch1 -p1
%patch2 -p0


%build
CFLAGS="${CFLAGS:--pipe -Wall -O2 -g}" ; export CFLAGS
CXXFLAGS="${CXXFLAGS:--pipe -Wall -O2 -g}" ; export CXXFLAGS
./configure \
        prefix=%prefix \
        CONFIG_FLAC=y \
        CONFIG_MAD=y \
        CONFIG_MODPLUG=y \
        CONFIG_MPC=y \
        CONFIG_VORBIS=y \
        CONFIG_WAV=y \
        CONFIG_MIKMOD=y \
        CONFIG_AAC=y \
        CONFIG_MP4=y \
        CONFIG_WAVPACK=y \
        CONFIG_FFMPEG=y \
        CONFIG_ALSA=y \
        CONFIG_ARTS=n \
        CONFIG_AO=y \
        CONFIG_OSS=y
%make_build
# make man
# make html


%install
make DESTDIR=%buildroot install

# Menu entry
# %__mkdir_p %buildroot%_menudir
# cat > %buildroot%_menudir/%name <<EOF
# ?package(cmus):\
#  	command="%_bindir/%name" needs="text" icon="sound_section.png" \
#   	section="Multimedia/Sound" title="CMus" \
#         longtitle="CMus - C* Music Player"
# EOF
install -d %buildroot%_desktopdir
install -m 644 %SOURCE2 %buildroot%_desktopdir/%name.desktop

mkdir examples
mv cmus-status-display examples


%files
%_bindir/cmus*
%dir %_libexecdir/%name
%dir %_libexecdir/%name/ip
%dir %_libexecdir/%name/op
%_libexecdir/%name/ip/mad.so
%_libexecdir/%name/ip/wav.so
%_libexecdir/%name/op/oss.so
# %_menudir/%name
%_desktopdir/%name.desktop
%_datadir/%name
%exclude %_datadir/doc/%name
%doc AUTHORS README examples contrib TODO
%_man1dir/cmus.1.*
%_man1dir/cmus-remote.1.*


%files in-flac
%_libexecdir/%name/ip/flac.so


%files in-vorbis
%_libexecdir/%name/ip/vorbis.so


%files in-modplug
%_libexecdir/%name/ip/modplug.so


%files in-mpc
%_libexecdir/%name/ip/mpc.so


%files in-mikmod
%_libexecdir/%name/ip/mikmod.so


%files in-mp4
%_libexecdir/%name/ip/mp4.so


%files in-aac
%_libexecdir/%name/ip/aac.so


%files in-wavpack
%_libexecdir/%name/ip/wavpack.so


%files in-ffmpeg
%_libexecdir/%name/ip/ffmpeg.so


%files out-alsa
%_libexecdir/%name/op/alsa.so


%files out-pulse
%_libexecdir/%name/op/pulse.so


%files out-ao
%_libexecdir/%name/op/ao.so


%changelog
* Tue Feb 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.2-alt1.1
- Fixed built with libav 0.8

* Sun Aug 14 2011 Eugene Vlasov <eugvv@altlinux.ru> 2.4.2-alt1
- 2.4.2

* Sat May 28 2011 Eugene Vlasov <eugvv@altlinux.ru> 2.4.1-alt1
- 2.4.1

* Sun Apr 24 2011 Eugene Vlasov <eugvv@altlinux.ru> 2.4.0-alt1
- 2.4.0

* Fri Apr 15 2011 Eugene Vlasov <eugvv@altlinux.ru> 2.4.0-alt0.1.rc0
- 2.4.0-rc0

* Fri Feb 11 2011 Eugene Vlasov <eugvv@altlinux.ru> 2.3.4-alt1
- New version

* Sat Jan 29 2011 Eugene Vlasov <eugvv@altlinux.ru> 2.3.3-alt1
- New version
- Removed arts output plugin

* Thu Apr 01 2010 Eugene Vlasov <eugvv@altlinux.ru> 2.3.1-alt1
- New version
- Audioscrobbler patch temporarily removed (AS support in upstream TODO)
- Added subpackage for pulse plugin (gns@)

* Tue Jun 02 2009 Eugene Vlasov <eugvv@altlinux.ru> 2.2.0-alt4
- Fix broken xing header recognition (evg@, Alt#19681)
- Removed deprecated post/postun update_menus calls
- Fixed Categories and Icon section in desktop file, removed deprecated
  Encoding key

* Tue Sep 02 2008 Eugene Vlasov <eugvv@altlinux.ru> 2.2.0-alt3
- Updated to git 2008-06-01-ed1b8ff4
- Applied Frank Terbeck's Audioscrobbler/Last.fm patch
- Fixed build requires: added libavcodec-devel and libavutil-devel, 
  removed linux-libc-headers
- Added README.Last.fm doc file
- Menu file replaced by desktop entry

* Tue Jan 29 2008 Eugene Vlasov <eugvv@altlinux.ru> 2.2.0-alt2
- Rebuild with libavformat.so.52

* Sat Jul 28 2007 Eugene Vlasov <eugvv@altlinux.ru> 2.2.0-alt1
- New version
- Added wavpack and ffmpeg input plugins
- Added contrib doc dir with samples of display scripts and zsh completion
- Updated build requires
- Removed %%__ macro
- Removed make install-man (no more needed)

* Sat Mar 03 2007 Eugene Vlasov <eugvv@altlinux.ru> 2.1.0-alt2
- Rebuild with flac 1.1.4
- Added Packager tag

* Fri Dec 22 2006 Eugene Vlasov <eugvv@altlinux.ru> 2.1.0-alt1
- New version, added settings view (:view 7), cmus-remote now supports
  TCP/IP (only recommended over LAN)
- Added mikmod, aac and mp4 plugins
- Fixed modplug plugin summary
- Fixed build requires

* Sun Aug 20 2006 Eugene Vlasov <eugvv@altlinux.ru> 2.0.4-alt1
- New version

* Sun Jun 18 2006 Eugene Vlasov <eugvv@altlinux.ru> 2.0.3-alt1
- New version

* Wed Jun 14 2006 Eugene Vlasov <eugvv@altlinux.ru> 2.0.2-alt2
- Build with ncursesw

* Thu Apr 20 2006 Eugene Vlasov <eugvv@altlinux.ru> 2.0.2-alt1
- New version, many bugfixes

* Fri Mar 03 2006 Eugene Vlasov <eugvv@altlinux.ru> 2.0.0-alt2
- Fixed build for x86_64

* Fri Feb 24 2006 Eugene Vlasov <eugvv@altlinux.ru> 2.0.0-alt1
- New version
- Build separate libao output plugin package
- HTML documentation not packaged - use man pages

* Sat Jan 14 2006 Eugene Vlasov <eugvv@altlinux.ru> 1.6.8-alt1
- New version
- Build separate MPC plugin package
- Fixed description

* Sun Jan 08 2006 Eugene Vlasov <eugvv@altlinux.ru> 1.6.7-alt1
- New version, bugfix release

* Mon Jan 02 2006 Eugene Vlasov <eugvv@altlinux.ru> 1.6.6-alt1
- New version
- Updated Url
- Updated description

* Sat Dec 10 2005 Eugene Vlasov <eugvv@altlinux.ru> 1.6.5-alt1
- New version
- Removed fix for build without ncursesw

* Fri Nov 25 2005 Eugene Vlasov <eugvv@altlinux.ru> 1.6.4-alt1
- New version

* Mon Nov 07 2005 Eugene Vlasov <eugvv@altlinux.ru> 1.6.3-alt1
- New version

* Mon Oct 24 2005 Eugene Vlasov <eugvv@altlinux.ru> 1.6.2-alt1
- New version

* Fri Sep 30 2005 Eugene Vlasov <eugvv@altlinux.ru> 1.5.8-alt1
- New version

* Thu Sep 22 2005 Eugene Vlasov <eugvv@altlinux.ru> 1.5.7-alt1
- New version

* Sat Sep 17 2005 Eugene Vlasov <eugvv@altlinux.ru> 1.5.6-alt1
- New version
- Build with ncurses, not ncursesw

* Thu Aug 25 2005 Eugene Vlasov <eugvv@altlinux.ru> 1.5.5-alt1
- New version
- Removed vorbis headers hack

* Mon Aug 22 2005 Eugene Vlasov <eugvv@altlinux.ru> 1.5.4-alt1
- New version

* Thu Aug 04 2005 Eugene Vlasov <eugvv@altlinux.ru> 1.5.2-alt1
- New version
- ALSA output plugin moved into separate package - %name-out-alsa

* Wed Jul 13 2005 Eugene Vlasov <eugvv@altlinux.ru> 1.5.1-alt1
- New version, bugfix release
- All fixes added in 1.5.0-alt2 merged into upstream
- Fixed vorbis includes

* Mon Jul 11 2005 Eugene Vlasov <eugvv@altlinux.ru> 1.5.0-alt2
- Fixes from GIT repository:
  * Don't spawn zombie processes
  * Fix mem leak in do_http_get
  * Reorder *_exit() calls
  * Misc cleanups
  * Simplify db.c

* Fri Jul 08 2005 Eugene Vlasov <eugvv@altlinux.ru> 1.5.0-alt1
- First build for Sisyphus

