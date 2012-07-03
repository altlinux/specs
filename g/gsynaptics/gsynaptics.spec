Name: gsynaptics
Version: 0.9.16
Release: alt3

Summary: a settings tool for Synaptics touchpad driver
License: GPL v2
Group: System/Configuration/Hardware
Url: http://gsynaptics.sourceforge.jp
Packager: Alex V. Myltsev <avm@altlinux.ru>

Source: %name-%version.tar
Patch1: gsynaptics-0.9.13-translation-ru.patch
Patch2: gsynaptics-0.9.16-desktop.patch
Patch3: gsynaptics-0.9.16-float-format.patch

BuildRequires: libgtk+2-devel libglade2-devel libgnomeui-devel libSM-devel gnome-doc-utils intltool

%description
%name is a GTK-based graphical configuration tool
for the Synaptics touchpad driver.

%prep
%setup -q
%patch1 -p2
%patch2 -p1
%patch3 -p2

%build
%configure
%make

%install
%makeinstall

mkdir -p %buildroot%_sysconfdir/xdg/autostart
mv %buildroot%_datadir/gnome/autostart/%name-init.desktop \
	%buildroot%_sysconfdir/xdg/autostart

%find_lang %name

%files -f %name.lang
%_sysconfdir/xdg/autostart/%name-init.desktop
%_bindir/*
%_datadir/%name
%_datadir/applications/%name.desktop
%_man1dir/%{name}*
%_datadir/gnome/help/%name
%_pixmapsdir/touchpad.png

%changelog
* Sat May 29 2010 Alexander Myltsev <avm@altlinux.ru> 0.9.16-alt3
- BuildRequire intltool.

* Tue Sep 01 2009 Alexander Myltsev <avm@altlinux.ru> 0.9.16-alt2
- Fix a bug with locale-dependent float formatting (closes #21312).

* Sun Aug 23 2009 Alexander Myltsev <avm@altlinux.ru> 0.9.16-alt1
- New version: bug fixes.
- Fixed desktop file categories (closes #20898), thanks to ktirf@.

* Wed Jan 16 2008 Alex V. Myltsev <avm@altlinux.ru> 0.9.13-alt1
- New version: AccelFactor support, bug fixes.

* Sun Sep 09 2007 Alex V. Myltsev <avm@altlinux.ru> 0.9.12-alt1
- 0.9.12: translations updated.

* Fri Sep 29 2006 Alex V. Myltsev <avm@altlinux.ru> 0.9.9-alt1
- Initial build for Sisyphus.

