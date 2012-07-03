%define		svn svn292

Name:		falf
Version:	1.4
Release:	alt0.4.%svn.1
Summary:	KDE3 media player with tabbed playlists!
Summary(ru_RU.UTF8): Аудиоплеер для KDE3 со несколькими списками воспроизведения в закладках
License: 	GPLv2
Group: 		Sound
Packager:	Motsyo Gennadi <drool@altlinux.ru>
Url:		http://falf.sourceforge.net/
# #Source0:	http://switch.dl.sourceforge.net/sourceforge/falf/%name-%version.tar.bz2
Source0:	%name-%version-%svn.tar.bz2
Patch0:		%name-1.4-alt_destdir.diff

BuildRequires: gcc-c++ kdelibs-devel libXext-devel libqt3-devel libtag-devel libxine-devel libtqt-devel

%description
FALF Player is brand-new, written from scratch
music player for K Desktop Environment 3.

Highlights:
- multiplaylist support
- lyrics support
- m3u support
- last.fm support
- HTTP streams support (radio)
- built-in tags' editor
- built-in equalizer
- easy transfer of tracks to removable device
- high stability
- low memory consumption

%description -l ru_RU.UTF8
Плеер FALF - совершенно новый, написанный с нуля аудиоплеер
для рабочего окружения KDE3 (K Desktop Environment).

Основные особенности:
- несколько списков воспроизведения
- отображение текстов песен
- поддержка формата m3u
- поддержка last.fm
- поддержка HTTP потоков (интернет-радио)
- встроенный редактор тегов
- встроенный эквалайзер
- легкий перенос звуковых дорожек на мобильные носители данных
- высокая стабильность
- малое потребление памяти

%prep
%setup -q -n %name-%version-svn
%patch0 -p1

%build
export PATH=$PATH:%_qt3dir/bin
qmake "QMAKE_CFLAGS+=%optflags" "QMAKE_CXXFLAGS+=%optflags" %name.pro
%make_build CXXFLAGS="-I%_includedir/tqtinterface -DQT_THREAD_SUPPORT"

%install
export DESTDIR="%buildroot%_prefix"
export PATH=$PATH:%_qt3dir/bin
sh ./install.sh

%find_lang %name

%files -f %name.lang
%doc CHANGELOG README
%_bindir/%name
%_desktopdir/%name.desktop
%_datadir/apps/konqueror/servicemenus/%{name}_mnu.desktop
%_datadir/icons/*/*/apps/%name.png

%changelog
* Fri Feb 25 2011 Motsyo Gennadi <drool@altlinux.ru> 1.4-alt0.4.svn292.1
- fix -DQT_THREAD_SUPPORT

* Mon Jan 31 2011 Motsyo Gennadi <drool@altlinux.ru> 1.4-alt0.4.svn292
- fix build with libtqt

* Mon Jan 17 2011 Motsyo Gennadi <drool@altlinux.ru> 1.4-alt0.3.svn292
- svn292

* Sun Nov 22 2009 Motsyo Gennadi <drool@altlinux.ru> 1.4-alt0.3.svn281
- fixed russian locale for Summary

* Wed Oct 28 2009 Motsyo Gennadi <drool@altlinux.ru> 1.4-alt0.2.svn281
- added russian description and summary (fixed #22087). Thanks to Phantom.

* Sat May 02 2009 Motsyo Gennadi <drool@altlinux.ru> 1.4-alt0.1.svn281
- svn281

* Thu Nov 20 2008 Motsyo Gennadi <drool@altlinux.ru> 1.3-alt2
- delete post/postun scripts (new rpm)

* Sun Aug 17 2008 Motsyo Gennadi <drool@altlinux.ru> 1.3-alt1
- 1.3 release

* Thu Jun 26 2008 Motsyo Gennadi <drool@altlinux.ru> 1.2-alt1
- 1.2 release

* Wed Jun 11 2008 Motsyo Gennadi <drool@altlinux.ru> 1.2-alt0.svn245
- new svn 245 version
  * fixed broken increasing volume at startup
  * fixed problem with changing equalizer profile's name
  * GCC 4.3.0 compatibility
  * last.fm playback percent complete can be set in range from 50 to 100%
  * accelerators can be set by user

* Wed Apr 02 2008 Motsyo Gennadi <drool@altlinux.ru> 1.1-alt1.1
- fix desktop-mime-entry

* Mon Feb 25 2008 Motsyo Gennadi <drool@altlinux.ru> 1.1-alt1
- 1.1 release

* Mon Jan 07 2008 Motsyo Gennadi <drool@altlinux.ru> 1.0-alt1
- 1.0 release

* Sat Dec 15 2007 Motsyo Gennadi <drool@altlinux.ru> 1.0-alt0.svn210
- new development version

* Fri Sep 14 2007 Motsyo Gennadi <drool@altlinux.ru> 1.0-alt0.rc6
- initial build for ALT Linux
