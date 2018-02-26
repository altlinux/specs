Name:		diskmonitor
Version:	0.4.1
Release:	alt1.9
Summary:	Disk Space Monitoring Applet for KDE
Summary(ru_RU.UTF8): Апплет KDE для наблюдения за свободным местом на дисках
Source0:	http://kde-apps.org/content/files/45015-%name-%version.tar.gz
Source1:	%name.png
Url:		http://kde-apps.org/content/show.php?content=45015
Group:		Monitoring
License:	GPLv2
Packager:	Motsyo Gennadi <drool@altlinux.ru>
Patch0:		%name-0.4.1-alt_link.diff
Patch1:		%name-0.4.1-desktop.diff
Patch2:		%name-0.4.1-admin-new-autotools.diff
Patch3:		%name-0.4.1-fix-autoconf-2.64.diff

BuildRequires: /usr/bin/convert gcc-c++ imake kdelibs-devel libXext-devel libXt-devel libqt3-devel xorg-cf-files libtqt-devel

%description
DiskMonitor is a Kicker Applet of KDE that monitors free space of some disks.
It provides a nice and compact view of presentation like LCD and draws itself
with very low flicker.

%description -l ru_RU.UTF8
DiskMonitor - апплет для панели KDE (Kicker), позволяющий наблюдать за количеством
свободного места на дисках. DiskMonitor компактно отображает информацию, иммитируя
жидкокристаллический дисплей (LCD) с быстрой, малозаметной перерисовкой.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%add_optflags -I%_includedir/tqtinterface
make -f admin/Makefile.common
%K3configure --disable-rpath --without-arts

%make_build

%install
%K3install
%__mkdir -p %buildroot/{%_miconsdir,%_niconsdir,%_liconsdir}
convert -resize 16x16 %SOURCE1 %buildroot%_miconsdir/%name.png
convert -resize 32x32 %SOURCE1 %buildroot%_niconsdir/%name.png
convert -resize 48x48 %SOURCE1 %buildroot%_liconsdir/%name.png

%files
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%_libdir/diskmonitor_panelapplet.so
%_libdir/diskmonitor_panelapplet.la
%_K3datadir/apps/kicker/applets/diskmonitor.desktop
%_K3datadir/config.kcfg/diskmonitor.kcfg
%_iconsdir/hicolor/*/apps/%name.png

%changelog
* Thu May 17 2012 Motsyo Gennadi <drool@altlinux.ru> 0.4.1-alt1.9
- fix build with recent automake

* Tue Mar 08 2011 Motsyo Gennadi <drool@altlinux.ru> 0.4.1-alt1.8
- move to alternate place

* Mon Jan 31 2011 Motsyo Gennadi <drool@altlinux.ru> 0.4.1-alt1.7
- fix build with libtqt

* Sun Jan 30 2011 Motsyo Gennadi <drool@altlinux.ru> 0.4.1-alt1.6
- build without aRts

* Mon Mar 22 2010 Motsyo Gennadi <drool@altlinux.ru> 0.4.1-alt1.5
- fix build with autoconf-2.64

* Sun Nov 22 2009 Motsyo Gennadi <drool@altlinux.ru> 0.4.1-alt1.4
- fixed russian locale for Summary

* Wed Oct 28 2009 Motsyo Gennadi <drool@altlinux.ru> 0.4.1-alt1.3
- added russian description and summary (fixed #22072). Thanks to Phantom.

* Mon May 25 2009 Motsyo Gennadi <drool@altlinux.ru> 0.4.1-alt1.2
- fix for automake-1.11

* Tue Dec 25 2007 Motsyo Gennadi <drool@altlinux.ru> 0.4.1-alt1.1
- fix for autotools-2.6 (thanks to wRAR for hints again)

* Sat Oct 20 2007 Motsyo Gennadi <drool@altlinux.ru> 0.4.1-alt1
- build for Sisyphus

* Fri Oct 19 2007 Motsyo Gennadi <drool@altlinux.ru> 0.4.1-alt0.M40.1
- initial build for ALT Linux (M40)
