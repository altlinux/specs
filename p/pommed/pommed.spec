Name: pommed
Version: 1.39
Release: alt3

Summary: Apple laptops hotkeys event handler
License: GPLv2
Group: System/Kernel and hardware
Url: http://alioth.debian.org/projects/pommed

Source0: %name-%version.tar.gz
Source1: %name.init

Patch0: pommed-1.39-alt-build.patch
Patch1: pommed-1.22-alt-fix-desktop-files.patch
Patch2: pommed-1.39-alt-rpm_opt_flags.patch

Packager: Igor Zubkov <icesik@altlinux.org>

ExclusiveArch: x86_64 %ix86

# Automatically added by buildreq on Mon Apr 16 2012
# optimized out: fontconfig fontconfig-devel glib2-devel libX11-devel libatk-devel libcairo-devel libdbus-devel libdbus-glib libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libpango-devel libwayland-client libwayland-server pkg-config xorg-xextproto-devel xorg-xproto-devel
BuildRequires: libXext-devel libXpm-devel libalsa-devel libaudiofile-devel libconfuse-devel libdbus-glib-devel libgtk+2-devel libpci-devel

%description
pommed handles the hotkeys found on the Apple MacBook Pro, MacBook and
PowerBook laptops and adjusts the LCD backlight, sound volume, keyboard
backlight or ejects the CD-ROM drive accordingly.

pommed also monitors the ambient light sensors to automatically
light up the keyboard backlight on the MacBook Pro and PowerBook.

Optional support for the Apple Remote control is available.

%package -n gpomme
Summary: Graphical client for pommed
Group: Graphical desktop/GNOME

%description -n gpomme
pommed handles the hotkeys found on the Apple MacBook Pro, MacBook and
PowerBook laptops and adjusts the LCD backlight, sound volume, keyboard
backlight or ejects the CD-ROM drive accordingly.

gpomme is a graphical client for pommed. It listens for signals sent by
pommed on DBus and displays the action taken by pommed along with the
current state associated to this action.

%package -n wmpomme
Summary: WindowMaker dockapp client for pommed
Group: Graphical desktop/Window Maker

%description -n wmpomme
pommed handles the hotkeys found on the Apple MacBook Pro, MacBook and
PowerBook laptops and adjusts the LCD backlight, sound volume, keyboard
backlight or ejects the CD-ROM drive accordingly.

wmpomme is a dockapp client for pommed. It displays the current level of
each item controlled by pommed.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%make_build

%install
# Install pommed
mkdir -p %buildroot%_initdir/
install -p -m0755 %SOURCE1 %buildroot%_initdir/pommed

mkdir -p %buildroot%_sbindir/
cp pommed/pommed %buildroot%_sbindir/
mkdir -p %buildroot%_datadir/pommed/
cp pommed/data/*.wav %buildroot%_datadir/pommed/

mkdir -p %buildroot%_sysconfdir/dbus-1/system.d
cp pommed.conf.mactel %buildroot%_sysconfdir/pommed.conf
cp dbus-policy.conf %buildroot%_sysconfdir/dbus-1/system.d/pommed.conf

# Install gpomme
mkdir -p %buildroot%_bindir/
cp gpomme/gpomme %buildroot%_bindir/

mkdir -p %buildroot%_datadir/applications/
cp gpomme/gpomme.desktop %buildroot%_datadir/applications/
cp gpomme/gpomme-c.desktop %buildroot%_datadir/applications/

mkdir -p %buildroot%_niconsdir/
cp icons/gpomme.svg %buildroot%_niconsdir/gpomme.svg 
cp icons/gpomme_32x32.png %buildroot%_niconsdir/gpomme.png 
cp icons/gpomme_32x32.xpm %buildroot%_niconsdir/gpomme.xpm 

mkdir -p %buildroot%_datadir/gpomme/
cp -a gpomme/themes %buildroot%_datadir/gpomme/

rm -rf %buildroot%_datadir/gpomme/themes/CrystalLarge/src
rm -rf %buildroot%_datadir/gpomme/themes/KStyle/src
rm -rf %buildroot%_datadir/gpomme/themes/Tango/src
rm -rf %buildroot%_datadir/gpomme/themes/elegant-bright/src
rm -rf %buildroot%_datadir/gpomme/themes/elegant-dark/src

mkdir -p %buildroot%_datadir/locale/{de,es,fr,it}/
install -m644 gpomme/po/de.mo %buildroot%_datadir/locale/de/gpomme.mo
install -m644 gpomme/po/es.mo %buildroot%_datadir/locale/es/gpomme.mo
install -m644 gpomme/po/fr.mo %buildroot%_datadir/locale/fr/gpomme.mo
install -m644 gpomme/po/it.mo %buildroot%_datadir/locale/it/gpomme.mo

# Install wmpomme
cp wmpomme/wmpomme %buildroot%_bindir/

cp icons/gpomme_32x32.xpm %buildroot%_niconsdir/wmpomme.xpm

%find_lang gpomme

%post
%post_service pommed

%preun
%preun_service pommed

%files
%doc AUTHORS ChangeLog INSTALL README TODO
%config(noreplace) %_sysconfdir/pommed.conf
%config(noreplace) %_sysconfdir/dbus-1/system.d/pommed.conf
%attr(755,root,root) %config(noreplace) %_initdir/pommed
%_sbindir/pommed
%dir %_datadir/pommed
%_datadir/pommed/click.wav
%_datadir/pommed/goutte.wav

%files -f gpomme.lang -n gpomme
%_bindir/gpomme
%_datadir/applications/gpomme.desktop
%_datadir/applications/gpomme-c.desktop
%_niconsdir/gpomme.svg
%_niconsdir/gpomme.png
%_niconsdir/gpomme.xpm
%dir %_datadir/gpomme
%_datadir/gpomme/*

%files -n wmpomme
%_bindir/wmpomme
%_niconsdir/wmpomme.xpm

%changelog
* Tue May 08 2012 Igor Zubkov <icesik@altlinux.org> 1.39-alt3
- use RPM_OPT_FLAGS

* Tue May 08 2012 Igor Zubkov <icesik@altlinux.org> 1.39-alt2
- Add ExclusiveArch: x86_64 %%ix86

* Mon Apr 16 2012 Igor Zubkov <icesik@altlinux.org> 1.39-alt1
- 1.31 -> 1.39

* Mon Jan 18 2010 Igor Zubkov <icesik@altlinux.org> 1.31-alt1
- 1.30 -> 1.31

* Sat Oct 31 2009 Igor Zubkov <icesik@altlinux.org> 1.30-alt1
- 1.28 -> 1.30

* Thu Oct 01 2009 Igor Zubkov <icesik@altlinux.org> 1.28-alt1
- 1.27 -> 1.28

* Sun Sep 13 2009 Igor Zubkov <icesik@altlinux.org> 1.27-alt1
- 1.26 -> 1.27

* Fri Mar 27 2009 Igor Zubkov <icesik@altlinux.org> 1.26-alt2
- apply patch from repocop

* Tue Mar 24 2009 Igor Zubkov <icesik@altlinux.org> 1.26-alt1
- 1.23 -> 1.26

* Wed Dec 03 2008 Igor Zubkov <icesik@altlinux.org> 1.23-alt1
- 1.22 -> 1.23

* Sat Nov 15 2008 Igor Zubkov <icesik@altlinux.org> 1.22-alt1
- 1.18 -> 1.22
- buildreq

* Sat Nov 15 2008 Igor Zubkov <icesik@altlinux.org> 1.18-alt3
- apply patch from repocop

* Fri Jul 11 2008 Igor Zubkov <icesik@altlinux.org> 1.18-alt2
- fix desktop files

* Sun May 18 2008 Igor Zubkov <icesik@altlinux.org> 1.18-alt1
- 1.17 -> 1.18

* Wed Apr 23 2008 Michael Shigorin <mike@altlinux.org> 1.17-alt1.1
- NMU: rebuilt against libpci-3.0.0

* Sat Apr 19 2008 Igor Zubkov <icesik@altlinux.org> 1.17-alt1
- 1.16 -> 1.17

* Thu Apr 03 2008 Igor Zubkov <icesik@altlinux.org> 1.16-alt2
- fix rebuild

* Wed Mar 05 2008 Igor Zubkov <icesik@altlinux.org> 1.16-alt1
- 1.15 -> 1.16

* Wed Mar 05 2008 Igor Zubkov <icesik@altlinux.org> 1.15-alt3
- fix rebuild with fresh pciutils
- buildreq

* Tue Feb 26 2008 Igor Zubkov <icesik@altlinux.org> 1.15-alt2
- add modprobe applesmc before start pommed

* Fri Feb 22 2008 Igor Zubkov <icesik@altlinux.org> 1.15-alt1
- 1.14 -> 1.15

* Sun Dec 16 2007 Igor Zubkov <icesik@altlinux.org> 1.14-alt1
- 1.13 -> 1.14

* Fri Dec 07 2007 Igor Zubkov <icesik@altlinux.org> 1.13-alt1
- 1.12 -> 1.13

* Sat Dec 01 2007 Igor Zubkov <icesik@altlinux.org> 1.12-alt1
- 1.10 -> 1.12

* Sun Oct 21 2007 Igor Zubkov <icesik@altlinux.org> 1.10-alt1
- build for Sisyphus

