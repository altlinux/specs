Name: verses
Version: 1
Release: alt4
Summary: screensaver using wise verses
Summary(ru_RU.UTF-8): хранитель экрана, показывающий мудрые фразы
License: GPL
Url: http://jesuschrist.ru/software/go.php?sid=49
Group: Graphical desktop/Other
BuildArch: noarch
Provides: xscreensaver-%name
Provides: gnome-screensaver-%name

Requires: fortunes-%name
Requires: fonts-bitmap-terminus

Packager: Ildar Mulyukov <ildar@altlinux.ru>

Source1: verses_def.txt
Source2: html_demo.txt
Source3: Verses-win.tar
Source4: LICENSE
Source5: %name.xss
Source6: %name.xml
Source7: README.OLD
Source8: %name.desktop


# Automatically added by buildreq on Mon Jul 21 2008 (-bi)
BuildRequires: fortune

%description
This screensaver shows verses found in fortunes-%name package.
Choose "Verses" in screensaver list.
Be sure to have cp1251 X fonts installed.
Compatible with XScreenSaver and Gnome2/Mate-Screensaver. More to come!
Enjoy!

%description -l ru_RU.UTF-8
Этот хранитель экрана показывает фразы из пакета fortunes-%name.
В списка заставок выберите "Verses".
Убедитесь, что у Вас установлены X-шрифты с кириллическими глифами в
кодировке cp1251.
Данная заставка совместима с XScreenSaver и Gnome2/Mate-Screensaver. More to come!
Наслаждайтесь!

%package -n fortunes-%name
Summary: collection of wise verses
Summary(ru_RU.UTF-8): коллекция мудрых фраз
License: FDL
Group: Games/Other
Requires: fortune >= 1.0-ipl33mdk

%description -n fortunes-%name
This collection represents the divine wisdom. It's useful for teaching and
self-teaching.
English and russian collections available.
Use example:
	fortune %name

%description -l ru_RU.UTF-8 -n fortunes-%name
Этот сборник представляет божественную мудрость. Он полезен для учения и
самоучения.
Есть сборники на русском и английском языках.
Пример использования:
	fortune %name

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
cat %SOURCE1 | \
	tr -d '\r' | \
	iconv -f cp1251 -t UTF-8 | \
	sed 's|^$|%%|' \
	> %buildroot%_gamesdatadir/fortune/verses_ru
strfile %buildroot%_gamesdatadir/fortune/verses_ru
mkdir -p %buildroot%_gamesdatadir/fortune/ru
ln -s ../verses_ru %buildroot%_gamesdatadir/fortune/ru/verses
ln -s ../verses_ru.dat %buildroot%_gamesdatadir/fortune/ru/verses.dat

cat %SOURCE2 | \
	tail -n +22 | \
	tr -d '\r' | \
	sed 's|^$|%%|' \
	> %buildroot%_gamesdatadir/fortune/verses_en
strfile %buildroot%_gamesdatadir/fortune/verses_en
mkdir -p %buildroot%_gamesdatadir/fortune/en
ln -s ../verses_en %buildroot%_gamesdatadir/fortune/en/verses
ln -s ../verses_en.dat %buildroot%_gamesdatadir/fortune/en/verses.dat

# docs
mkdir docs fortunes-docs
install -m 444 %SOURCE7 docs/
tar xf %SOURCE3 -C fortunes-docs
install -m 444 %SOURCE4 fortunes-docs/

%files
%_prefix/libexec/xscreensaver/%name
%_sysconfdir/X11/xscreensaver/hack.d/%name.*
%_datadir/xscreensaver/config/%name.*
%_desktopdir/screensavers/%name.*
%doc docs/*

%files -n fortunes-%name
%_datadir/games/fortune/%{name}_*
%_datadir/games/fortune/*/%{name}*
%dir %_datadir/games/fortune/ru
%dir %_datadir/games/fortune/en
%doc fortunes-docs/*

%changelog
* Sun Dec 28 2014 Ildar Mulyukov <ildar@altlinux.ru> 1-alt4
- use fonts-bitmap-terminus

* Thu Dec 04 2014 Ildar Mulyukov <ildar@altlinux.ru> 1-alt3
- add Mate screensaver support

* Tue Jul 22 2008 Ildar Mulyukov <ildar@altlinux.ru> 1-alt2
- fixed %name.xss

* Mon Jul 21 2008 Ildar Mulyukov <ildar@altlinux.ru> 1-alt1
- added gnome-screensaver desktop file

* Mon Jul 21 2008 Ildar Mulyukov <ildar@altlinux.ru> 1-alt0.5
- added Xscreensaver

* Thu Jul 17 2008 Ildar Mulyukov <ildar@altlinux.ru> 1-alt0.1
- prepared fortunes for release

