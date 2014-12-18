Name: kcpuload
Version: 1.99
Release: alt5
Serial: 1

Group: Monitoring
Summary: Small applet which displays cpu time for KDE kicker (KDE3/TDE)
License: %gpl2only

Source0: %name-%version.tar.bz2
Patch1: kcpuload.desktop.patch

BuildRequires: rpm-build-licenses rpm-macros-kde-common-devel rpm-macros-qt3

# Automatically added by buildreq on Thu Dec 18 2014
# optimized out: fontconfig gnu-config imake kdebase-common kdelibs libICE-devel libSM-devel libX11-devel libXext-devel libXt-devel libarts-devel libpng-devel libqt3-devel libqt3-settings libstdc++-devel libtqt-devel xml-utils xorg-cf-files xorg-xproto-devel zlib-devel
BuildRequires: gcc-c++ kde-i18n-ru kdelibs-devel libjpeg-devel xdg-user-dirs

%description
This is a small program for the KDE Kicker (the startmenu).
It will show the CPU usage in form of one or two configurable diagrams.
There are settings for colors and some different styles.
Note that it isn't the real system load that's shown, but the percent
used of the total CPU power, which is calculated from the number of
CPU ticks.

To bring up the settings menu, simply rightclick on the diagram.
Use a slower update interval to get a more stable and accurate
diagram without flicker.

If there are more than one CPU on the system, the total CPU usage from
both can be shown, or you can choose to have one separate diagram for
each of the CPU's.
Leftclick on the diagram to bring up a small information box which will
show the exact CPU usage in text form.

%prep
%setup -q
%patch1 -p1

#subst "s/\-lkdeui/-lkdeui -lpthread/g" configure
#subst "s/\.la/.so/g" configure

%build

export PATH="%_K3bindir:$PATH"
%add_optflags -I%_includedir/tqtinterface -lkdecore -L%_qt3dir/lib -lqt-mt

%configure \
	--disable-rpath \
	--disable-static \
	--disable-debug \
	--program-transform-name="" \
	--enable-final

%make_build

%install
%makeinstall kde_htmldir=%buildroot/%_K3doc

mkdir -p %buildroot/%_Kmenudir
mv %buildroot/%_datadir/applnk/System/*.desktop %buildroot/%_Kmenudir/

%post
%_update_menus_bin

%postun
%_update_menus_bin

%files
%_bindir/*
%_datadir/apps/%name
%_datadir/icons/*/*/*/*
%_Kmenudir/*.desktop
%doc %_K3doc/en/%name

%changelog
* Thu Dec 18 2014 Sergey Y. Afonin <asy@altlinux.ru> 1:1.99-alt5
- returned to Sisyphus

* Mon Jan 23 2006 Sergey V Turchin <zerg at altlinux dot org> 1:1.99-alt4
- remove menu-file

* Thu Jan 27 2005 Sergey V Turchin <zerg at altlinux dot org> 1:1.99-alt3
- rebuild with gcc3.4

* Thu Apr 29 2004 Sergey V Turchin <zerg at altlinux dot org> 1:1.99-alt2
- fix build without /usr/lib/*.la

* Tue Sep 30 2003 Sergey V Turchin <zerg at altlinux dot org> 1:1.99-alt1
- new version
- fix build requires

* Thu Sep 12 2002 Sergey V Turchin <zerg@altlinux.ru> 1:1.9.1-alt2
- rebuild with gcc3.2

* Fri Apr 26 2002 Sergey V Turchin <zerg@altlinux.ru> 1:1.9.1-alt1
- new version
- build with KDE3

* Tue Oct 30 2001 Sergey V Turchin <zerg@altlinux.ru> 1.90-ipl6mdk
- fix BuildRequires

* Fri Oct 12 2001 Sergey V Turchin <zerg@altlinux.ru> 1.90-ipl5mdk
- rebuild with new libpng
- cleanup spec

* Fri Mar 2 2001 AEN <aen@logic.ru>
- rebuild with KDE-2.1
* Fri Dec 09 2000 AEN <aen@logic.ru>
- build for RE

* Fri Nov 17 2000 David BAUDENS <baudens@mandrakesoft.com> 1.90-2mdk
- Rebuild with gcc-2.96 & glibc-2.2

* Mon Oct  9 2000 Vincent Saugey <vince@mandrakesoft.com> 1.90-1mdk
- Firt mdk release
