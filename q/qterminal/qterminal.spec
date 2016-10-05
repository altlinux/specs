Name: qterminal
Version: 0.7.0
Release: alt1

Summary: QT-based multitab terminal emulator
License: GPL
Group: Terminals

Url: http://github.com/qterminal/qterminal
Source: %name-%version.tar
Packager: Michael Shigorin <mike@altlinux.org>

BuildRequires: gcc-c++ cmake git-core
BuildRequires: qt5-base-devel
BuildRequires: libqtermwidget-devel >= %version

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

0.4.0+ is a friendly fork, the original project is still available
at http://qterminal.sourceforge.net/

%prep
%setup

%build
%cmake_insource -DPULL_TRANSLATIONS=OFF -DUPDATE_TRANSLATIONS=OFF \
	-DUSE_SYSTEM_QXT=0 -DQTERMWIDGET_PATH_SHARE=%_datadir/qtermwidget
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc AUTHORS COPYING NEWS README
%_bindir/%name
%_desktopdir/*.desktop
%_pixmapsdir/%name.png

# TODO:
# - package system libqxt (lots of macros missing in rpm-macros-qt4)

%changelog
* Tue Oct 04 2016 Michael Shigorin <mike@altlinux.org> 0.7.0-alt1
- 0.7.0

* Fri Nov 14 2014 Michael Shigorin <mike@altlinux.org> 0.6.0-alt1
- 0.6.0 (closes: #30468)
- updated Url:
- use bundled libqxt

* Wed Mar 07 2012 Michael Shigorin <mike@altlinux.org> 0.4.0-alt1
- moved to gitorius 0.4.0 fork
- spec cleanup

* Mon Jan 24 2011 Andrey Cherepanov <cas@altlinux.org> 0.2.0-alt1
- Initial build in Sisyphus

* Sat Jan 08 2011 TI_Eugene <ti.eugene@gmail.com> 0.2.0
- Next version

* Fri Feb 03 2009 TI_Eugene <ti.eugene@gmail.com> 0.1.4
- Initital build in OBS
