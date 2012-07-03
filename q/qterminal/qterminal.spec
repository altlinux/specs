Name: qterminal
Version: 0.4.0
Release: alt1

Summary: QT-based multitab terminal emulator
License: GPL
Group: Terminals

Url: http://gitorious.org/qterminal
Source: %name-%version.tar
Packager: Michael Shigorin <mike@altlinux.org>

BuildRequires: gcc-c++, cmake, qt4-devel
BuildRequires: libqtermwidget-devel >= 0.4.0

%description
QT-based multitab terminal emulator based on QTermWidget.

Initially this project was started as an attempt to create relatively
light and stable terminal emulator application like Konsole or
gnome-terminal but without any dependency from such monsters as KDE or
Gnome. I was looking for such kind of application for a long time but
haven't found anything worth while. That's why when I met QTermWidget
and tried it I was really happy! :) That was exactly what I need.
Actually I didn't pay much effort for its improvement, I've just put it
into tab widget, add basic config and some useful actions. Seems that's
pretty much enough for now.

0.4.0 is a friendly fork, the original project is still available
at http://qterminal.sourceforge.net/

%prep
%setup

%build
%cmake -DQTERMWIDGET_PATH_SHARE=%_datadir/qtermwidget
%make_build -C BUILD

%install
%makeinstall_std -C BUILD
%find_lang %name

%files -f %name.lang
%doc AUTHORS COPYING NEWS README
%_bindir/%name
%_datadir/%name
%_desktopdir/*.desktop
%_pixmapsdir/%name.png

%changelog
* Wed Mar 07 2012 Michael Shigorin <mike@altlinux.org> 0.4.0-alt1
- moved to gitorius 0.4.0 fork
- spec cleanup

* Mon Jan 24 2011 Andrey Cherepanov <cas@altlinux.org> 0.2.0-alt1
- Initial build in Sisyphus

* Sat Jan 08 2011 TI_Eugene <ti.eugene@gmail.com> 0.2.0
- Next version

* Fri Feb 03 2009 TI_Eugene <ti.eugene@gmail.com> 0.1.4
- Initital build in OBS
