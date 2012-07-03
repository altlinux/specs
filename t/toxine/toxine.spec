Name: toxine
Summary: Mediaplayer with console control
Summary(uk_UA.CP1251): Медіапрогравач з консольним керуванням
Summary(ru_RU.CP1251): Медиапроигрыватель с консольным управлением
Version: 0.6.3
Release: alt9
License: %gpl2plus
Group: Video
URL: http://toxine.sourceforge.net/
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Packager: Led <led@altlinux.ru>

BuildRequires(pre): rpm-build-licenses
BuildRequires: libxine-devel >= 1.1.7-alt3
BuildRequires: aalib-devel imake libXtst-devel libcaca-devel
BuildRequires: libgpm-devel libncurses-devel libreadline-devel
BuildRequires: libslang-devel xorg-cf-files libXext-devel libXt-devel
BuildRequires: xorg-inputproto-devel xorg-sdk

%description
%name can be runs in interactive mode, or in a script mode. This
program was originaly designed to test and debug the xine library, but
now, it's a real (small) project, which permit to playback some streams
without X Window (using DXR3/HW+ card, AAlib output).
In interactive mode, you can use real xine's API commands or %name's
commands. In this mode, %name use the readline library, which permit
some completions, commands recall, etc...

%description -l uk_UA.CP1251
%name може виконуватися в інтерактивному режимі або в режимі сценарію.
Ця програма спочатку була розроблена для тестування та відладки
бібліотеки xine, але зараз - це справжній (невеликий) проект, який
дозволяє програвати потоки без X Window (використовуючи карти DXR3/HW+,
вивід AAlib).
В інтерактивному режимі ви можете використовувати справжні команди
xine-API або команди %name. В цьому режимі %name використовує
бібліотеку readline, яка дозволяє деякі завершення, повтори команд і
таке інше...

%description -l ru_RU.CP1251
%name может выполняться в интерактивном режиме или в режиме сценарія.
Эта программа изначально была разработана для тестирования и отладки
библиотеки xine, но сейчас - это настоящий (небольшой) проект, который
позволяет проигрыавать потоки без X Window (используя карти DXR3/HW+,
вывод AAlib).
В интерактивном режиме вы можете использовать настоящие комманды
xine-API или комманди %name. В этом режиме %name использует
библиотеку readline, которая позволяет некоторые завершения, повторы
комманд и тому подобное...


%prep
%setup
%patch -p1


%build
%define _optlevel 3
%configure --with-pic --without-rpath --disable-cacatest
%make_build
bzip2 --best --keep --force -- ChangeLog


%install
%make_install DESTDIR=%buildroot install

#menu
install -d %buildroot%_desktopdir
iconv -f cp1251 -t utf-8 > %buildroot%_desktopdir/%name.desktop <<__MENU__
[Desktop Entry]
Name=%name
GenericName=Console xine player
GenericName[uk]=Консольний xine-програвач
GenericName[ru]=Консольный xine-проигрыватель
Exec=%name
Icon=video_section
Terminal=true
Type=Application
StartupNotify=false
Categories=AudioVideo;Player;ConsoleOnly;
__MENU__


%files
%doc AUTHORS ChangeLog.* README misc/dvdplayer.sh
%_bindir/%name
%_man1dir/*
%_libdir/%name
%_desktopdir/*


%changelog
* Tue Dec 02 2008 Led <led@altlinux.ru> 0.6.3-alt9
- updated BuildRequires
- cleaned up spec

* Thu Aug 07 2008 Led <led@altlinux.ru> 0.6.3-alt8
- fixed %name.desktop

* Fri Apr 04 2008 Led <led@altlinux.ru> 0.6.3-alt7
- fixed License
- cleaned up %name.desktop

* Tue Mar 04 2008 Led <led@altlinux.ru> 0.6.3-alt6
- fixed %name.desktop

* Mon Feb 18 2008 Led <led@altlinux.ru> 0.6.3-alt5
- fixed build
- cleaned up spec
- updated %name-0.6.3-configure.patch
- added %name-0.6.3-setenv.patch (from mainstream CVS)

* Tue May 23 2006 Led <led@altlinux.ru> 0.6.3-alt4
- fixed %name-0.6.3-configure.patch
- fixed spec

* Tue May 16 2006 Led <led@altlinux.ru> 0.6.3-alt3
- added %name-0.6.3-configure.patch
- fixed BuildRequires

* Mon May 15 2006 Led <led@altlinux.ru> 0.6.3-alt2
- added %name-0.6.3-gcc4.patch
- fixed menu

* Thu Feb 16 2006 Led <led@altlinux.ru> 0.6.3-alt1
- initial build
