Name: verses
Version: 1
Release: alt2
Summary: screensaver using wise verses
Summary(ru_RU.UTF-8): хранитель экрана, показывающий мудрые фразы
License: GPL
Url: http://jesuschrist.ru/software/go.php?sid=49
Group: Graphical desktop/Other
BuildArch: noarch
Provides: xscreensaver-%name
Provides: gnome-screensaver-%name

Requires:fortunes-%name

Packager: Ildar Mulyukov <ildar@altlinux.ru>

Source1: verses_def.txt
Source2: html_demo.txt
Source3: Verses-win.tar
Source4: LICENCE
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
Compatible with XScreenSaver and Gnome-Screensaver. More to come!
Enjoy!

%description -l ru_RU.UTF-8
Этот хранитель экрана показывает фразы из пакета fortunes-%name.
В списка заставок выберите "Verses".
Убедитесь, что у Вас установлены X-шрифты с кириллическими глифами в
кодировке cp1251.
Данная заставка совместима с XScreenSaver и Gnome-Screensaver. More to come!
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
mkdir -p %buildroot%_docdir/%name-%version %buildroot%_docdir/fortunes-%name-%version
install -m 444 %SOURCE7 %buildroot%_docdir/%name-%version
tar xf %SOURCE3 -C %buildroot%_docdir/fortunes-%name-%version
install -m 444 %SOURCE4 %buildroot%_docdir/fortunes-%name-%version

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
%doc %_docdir/%name-%version

%files -n fortunes-%name
%_datadir/games/fortune/%{name}_*
%_datadir/games/fortune/*/%{name}*
# might be wrong
%dir %_datadir/games/fortune/ru
%dir %_datadir/games/fortune/en
%doc %_docdir/fortunes-%name-%version

%changelog
* Tue Jul 22 2008 Ildar Mulyukov <ildar@altlinux.ru> 1-alt2
- fixed %name.xss

* Mon Jul 21 2008 Ildar Mulyukov <ildar@altlinux.ru> 1-alt1
- added gnome-screensaver desktop file

* Mon Jul 21 2008 Ildar Mulyukov <ildar@altlinux.ru> 1-alt0.5
- added Xscreensaver

* Thu Jul 17 2008 Ildar Mulyukov <ildar@altlinux.ru> 1-alt0.1
- prepared fortunes for release

