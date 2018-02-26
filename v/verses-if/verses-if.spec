Name: verses-if
Version: 1
Release: alt1
Summary: screensaver showing verses from Amy Carmichael's "If" book
Summary(ru_RU.UTF-8): хранитель экрана, показывающий фразы из книги Эми Кармайкл "Если"
License: GPL
Group: Graphical desktop/Other
BuildArch: noarch
Provides: xscreensaver-%name
Provides: gnome-screensaver-%name

Requires:fortunes-%name

Packager: Ildar Mulyukov <ildar@altlinux.ru>

Source1: http://books.agape.ru/booktext/esli.htm
Source2: If.txt
Source5: %name.xss
Source6: %name.xml
Source8: %name.desktop


# Automatically added by buildreq on Fri Sep 19 2008 (-bi)
BuildRequires: elinks fortune

%description
This screensaver shows verses found in fortunes-%name package.
Choose "Verses-If" in screensaver list.
Be sure to have cp1251 X fonts installed.
Compatible with XScreenSaver and Gnome-Screensaver. More to come!
Enjoy!

%description -l ru_RU.UTF-8
Этот хранитель экрана показывает фразы из пакета fortunes-%name.
В списка заставок выберите "Verses-If".
Убедитесь, что у Вас установлены X-шрифты с кириллическими глифами в
кодировке cp1251.
Данная заставка совместима с XScreenSaver и Gnome-Screensaver. More to come!
Наслаждайтесь!

%package -n fortunes-%name
Summary: collection of verses from Amy Carmichael's "If" book
Summary(ru_RU.UTF-8): коллекция фраз из книги Эми Кармайкл "Если"
License: AGAPE publishers
Group: Games/Other
Requires: fortune >= 1.0-ipl33mdk

%description -n fortunes-%name
This collection is the booklet of Amy Beatrice Carmichael (16 December 1867 -
18 January 1951), called "If" (1953). English collection is only the Part 1 of
the booklet.
English and Russian collections available.
Use example:
	fortune if

%description -l ru_RU.UTF-8 -n fortunes-%name
Этот сборник представляет собой буклет миссионерки Эми Кармайкл (16 дек. 1867 –
18 янв. 1951) под названием "Если" (1953). На английском языке присутствует
только первая часть книги.
Есть сборники на русском и английском языках.
Пример использования:
	fortune if

%install
#screensaver
mkdir -p %buildroot%_prefix/libexec/xscreensaver/
ln -s phosphor %buildroot%_prefix/libexec/xscreensaver/%name
mkdir -p %buildroot%_sysconfdir/X11/xscreensaver/hack.d/
install -m 644 %SOURCE5 %buildroot%_sysconfdir/X11/xscreensaver/hack.d/
mkdir -p %buildroot%_datadir/xscreensaver/config/
install -m 644 %SOURCE6 %buildroot%_datadir/xscreensaver/config/
mkdir -p %buildroot%_desktopdir/screensavers/
install -m 644 %SOURCE8 %buildroot%_desktopdir/screensavers/

# fortunes
mkdir -p %buildroot%_gamesdatadir/fortune
elinks -dump-width 65530 -dump-charset UTF-8 -dump 1 -force-html \
		-eval 'set document.html.display_tables = 0' \
	%SOURCE1 \
	> esli.txt
csplit esli.txt '/ *Часть/' '{*}'
tail -n +2 xx01 | \
	sed '40d;
		s|^$|%%|;
		s|^ *Если|Если|' \
	> %buildroot%_gamesdatadir/fortune/if_ru
mkdir -p %buildroot%_docdir/%name-%version %buildroot%_docdir/fortunes-%name-%version
install -m 444 xx00 %buildroot%_docdir/fortunes-%name-%version/If-foreword.txt
install -m 444 xx02 %buildroot%_docdir/fortunes-%name-%version/If-part-2.txt

sed 's|^$|%%|' %SOURCE2 \
	> %buildroot%_gamesdatadir/fortune/if_en

strfile %buildroot%_gamesdatadir/fortune/if_ru
strfile %buildroot%_gamesdatadir/fortune/if_en

mkdir -p %buildroot%_gamesdatadir/fortune/ru
ln -s ../if_ru %buildroot%_gamesdatadir/fortune/ru/if
ln -s ../if_ru.dat %buildroot%_gamesdatadir/fortune/ru/if.dat
mkdir -p %buildroot%_gamesdatadir/fortune/en
ln -s ../if_en %buildroot%_gamesdatadir/fortune/en/if
ln -s ../if_en.dat %buildroot%_gamesdatadir/fortune/en/if.dat

# from the xscreensaver.spec
%define _update_xscreensaver_bin %_bindir/update-xscreensaver
%define update_xscreensaver [ "$1" = 1 -a -x %_update_xscreensaver_bin ] && %_update_xscreensaver_bin ||:
%define clean_xscreensaver [ -x %_update_xscreensaver_bin ] && %_update_xscreensaver_bin ||:

%post
%update_xscreensaver

%postun
%clean_xscreensaver

%files
%_prefix/libexec/xscreensaver/%name
%_sysconfdir/X11/xscreensaver/hack.d/%name.*
%_datadir/xscreensaver/config/%name.*
%_desktopdir/screensavers/%name.*

%files -n fortunes-%name
%_datadir/games/fortune/if_*
%_datadir/games/fortune/*/if*
%doc %_docdir/fortunes-%name-%version
# might be wrong
%dir %_datadir/games/fortune/ru
%dir %_datadir/games/fortune/en

%changelog
* Fri Sep 19 2008 Ildar Mulyukov <ildar@altlinux.ru> 1-alt1
- 1st build for ALTLinux
