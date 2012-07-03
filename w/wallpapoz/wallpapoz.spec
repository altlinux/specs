%define svnversion  svn20100424

Name: wallpapoz
Version: 0.4.1
Release: alt1.%svnversion.1
Group: Graphical desktop/GNOME
License: GPLv2+
Packager: Hihin Ruslan <ruslandh@altlinux.ru>

Url: http://wallpapoz.akbarhome.com

Source0: %name-%svnversion.tar.bz2
Source10: daemon_wallpapoz-wrapper
Source11: wallpapoz-autostart.desktop


BuildRequires:  python-module-pygtk-libglade python-module-pygtk 
BuildRequires:  python-module-pygnome python-module-imaging

Requires:  python-module-pygtk-libglade python-module-pygtk 
Requires:  python-module-pygnome python-module-imaging
Requires:  xwininfo

BuildArch: noarch

Summary: Gnome Desktop wallpaper configuration tool

%description
Wallpapoz application enables you to configure Gnome desktop wallpapers
in unique way. You could have Gnome desktop wallpaper changes when the
specified time has passed.


%prep
%setup -n %name-%svnversion 

%install
mkdir -p %buildroot%prefix
./setup.py install --installdir %buildroot%prefix

install -dp -m755 %buildroot%_libexecdir
mv %buildroot%_bindir/daemon_wallpapoz \
	%buildroot%_libexecdir
install -p -m755 %SOURCE10 \
	%buildroot%_bindir/daemon_wallpapoz

install -dp -m755 %buildroot%_sysconfdir/xdg/autostart

install -p -m644 %SOURCE11  %buildroot%_sysconfdir/xdg/autostart 

%find_lang %name --with-gnome

%files -f %name.lang
%doc README CHANGELOG
%_bindir/daemon_wallpapoz
%_bindir/wallpapoz
%_libexecdir/daemon_wallpapoz
%_datadir/wallpapoz
%_datadir/pixmaps/wallpapoz.png
%_datadir/applications/wallpapoz.desktop
%_sysconfdir/xdg/autostart/wallpapoz-autostart.desktop


%changelog
* Fri Oct 28 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4.1-alt1.svn20100424.1
- Rebuild with Python-2.7

* Sat Apr 24 2010 Hihin Ruslan <ruslandh@altlinux.ru> 0.4.1-alt1.svn20100424
- Build for ALTLinux

* Sun Sep 20 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.4.1-5mdv2010.0
+ Revision: 445731
- rebuild
