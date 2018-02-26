Name: xxkb
Version: 1.11
Release: alt3

Summary: Switcher and indicator of current keyboard layout
Summary(ru_RU.UTF-8): Индикатор и переключатель состояния клавиатуры
License: Artistic
Group: System/Internationalization
Url: http://sourceforge.net/projects/xxkb/

# http://downloads.sourceforge.net/xxkb/xxkb-%version-src.tar.gz
Source: %name-%version-%release.tar
Source1: xxkb-32.png
Source2: xxkb-48.png
Source3: xxkb.desktop

# Automatically added by buildreq on Sun Dec 28 2008
BuildRequires: imake libXext-devel libXpm-devel libXt-devel xorg-cf-files

%description
The xxkb program shows the current keyboard layout (an XKB group) and
allows to switch it with a mouse click.  It has some additional features.
The xxkb remebers the layout for each application window and changes
the keyboard state accordingly when the window gets a focus.  The xxkb
can place an additional button on a window titlebar and that button is
a switcher and an indicator for that separate window.  If the keyboard
map has more than two layouts the xxkb can simplify a switching using a
two_state mode.  In this mode the xxkb allows to choose two layouts, one
as a base layout and another one as an alternative layout and then switch
the keyboard state between them only.  Also the xxkb supports applications
lists which allow to tune its behavior for some separate applications.

The xxkb works with any window manager.

%description -l ru_RU.UTF-8
Эта программа является индикатором и переключателем состояния клавиатуры
("группы" в терминах XKB).

То есть, она
- показывает текущую группу ("картинкой" в своем окне)
- переключает группу "щелчком мыши".
При этом группа может перключаться и "штатным" переключателем - клавишей,
определенной в файлах настройки XKB.

Кроме того xxkb позволяет
- устанавливать отдельно состояние клавиатуры для каждого запущенного
приложения.  Состояние будет автоматически переключаться при изменении
фокуса окна.
- "подвешивать" кнопку ("иконку") на "обрамление" каждого отслеживаемого
окна.  Эта кнопка сама является индикатором и переключателем ("щелчком
мыши" по ней) для данного окна.
- в случае, когда XKB настроен более чем для двух групп, "корректировать"
поведение клавиши переключателя так, чтобы она имела только два состояния
- "основная группа"-"альтернативная группа".  Альтернативную группу
можно устанавливать отдельно для каждого отслеживаемого окна.

Надо заметить, что xxkb может работать с любым Window Manager'ом.

%prep
%setup -n %name-%version-%release

%build
xmkmf
%make_build CDEBUGFLAGS="%optflags" BASEDIR=%prefix PIXMAPDIR=%_datadir/xxkb

%install
mkdir -p %buildroot{%_datadir/xxkb,%_menudir}
install -p -m644 pixmaps/*.xpm %buildroot%_datadir/xxkb/
install -pD -m755 xxkb %buildroot%_bindir/xxkb
install -pD -m644 xxkb.man %buildroot%_man1dir/xxkb.1
install -pD -m644 XXkb.ad %buildroot%_x11appconfdir/XXkb
install -pD -m644 xxkb.xpm %buildroot%_miconsdir/xxkb.xpm
install -pD -m644 %{SOURCE1} %buildroot%_niconsdir/xxkb.png
install -pD -m644 %{SOURCE2} %buildroot%_liconsdir/xxkb.png
install -pD -m644 %{SOURCE3} %buildroot%_desktopdir/%name.desktop

%files
%config(noreplace) %_x11appconfdir/*
%_bindir/*
%_man1dir/*
%_desktopdir/%name.desktop
%_miconsdir/*
%_niconsdir/*
%_liconsdir/*
%_datadir/xxkb
%doc CHANGES.koi8 README.koi8 XXkb.ad

%changelog
* Thu Jul 14 2011 Dmitry V. Levin <ldv@altlinux.org> 1.11-alt3
- Converted debian menu to freedesktop (by Igor Vlasenko).

* Sun Apr 12 2009 Sergey Vlasov <vsu@altlinux.ru> 1.11-alt2
- Fixed undesired docking of xxkb if "Xxkb.mainwindow.type: tray" was not set
  and stalonetray is started after xxkb (ALT #19591).

* Tue Dec 30 2008 Dmitry V. Levin <ldv@altlinux.org> 1.11-alt1
- Updated to 1.11.
- Applied xxkb-evadedock.patch from Konstantin Uvarin (closes: #12119).
- Packaged %_x11appconfdir/XXkb.
- Removed obsolete %%update_menus/%%clean_menus calls.
- Updated build dependencies.

* Sun Jan 16 2005 Dmitry V. Levin <ldv@altlinux.org> 1.10-alt3
- Fixed compilation issues detected by gcc-3.4.3.

* Wed Aug 04 2004 Dmitry V. Levin <ldv@altlinux.org> 1.10-alt2
- Fixed menu entry (#3908).

* Fri Apr 18 2003 Dmitry V. Levin <ldv@altlinux.org> 1.10-alt1
- Updated to 1.10, updated patch.

* Wed Nov 13 2002 Dmitry V. Levin <ldv@altlinux.org> 1.9-alt1
- 1.9

* Sat Oct 26 2002 Dmitry V. Levin <ldv@altlinux.org> 1.8-alt1
- Updated to 1.8
- Added manpage.
- Fixed compilation warnings.
- Updated summary and description.

* Mon Sep 17 2001 AEN <aen@logic.ru> 1.6-alt2
- rebuild with new XFree 

* Wed Mar 28 2001 AEN <aen@logic.ru> 1.6-alt1
- new version

* Tue Jan 23 2001 Dmitry V. Levin <ldv@fandra.org> 1.5.1-ipl5mdk
- Specfile cleanup.

* Wed Dec 13 2000 AEN <aen@logic.ru>
- new version
- cleanup spec

* Wed Jan 12 2000 AEN <aen@logic.ru>
- new version (1.3)

* Wed Jan 5 2000 AEN <aen@logic.ru>
- build for RE
- belarusian xpm added

* Thu Jun  3  1999 Vladimir Bormotov <bor@vb.dn.ua>
- xxkb.spec improvements

* Sat May 26  1999 Vladimir Bormotov <bor@vb.dn.ua>
- create xxkb.spec
