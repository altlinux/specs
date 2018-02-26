%define major 3.2
Name: drwright
Version: %major.5
Release: alt1

Summary: A program that reminds you to take wrist breaks
Summary(be_BY.UTF-8):	Праграма, якая нагадвае пра неабходнасьць адпачынку для рук
Summary(ru_RU.UTF-8):	Программа, которая напоминает об необходимости перерыва для рук
Summary(uk_UA.UTF-8):	Програма, що нагадує про необхідність перерви для рук

License: GPL
Group: Graphical desktop/GNOME
Url: http://developer.imendio.com/wiki/DrWright

# Typical environment for GNOME program
Requires(post): GConf2
Requires(post,postun): desktop-file-utils
BuildPreReq: libGConf2-devel
BuildPreReq: desktop-file-utils

Source: http://ftp.gnome.org/pub/GNOME/sources/drwright/%major/%name-%version.tar

# Automatically added by buildreq on Thu Apr 12 2012
# optimized out: fontconfig fontconfig-devel glib2-devel gtk-builder-convert libICE-devel libX11-devel libatk-devel libcairo-devel libcairo-gobject libcairo-gobject-devel libcanberra-devel libcanberra-gtk-common-devel libcanberra-gtk3 libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libgtk+3-devel libpango-devel libwayland-client libwayland-server perl-Encode perl-XML-Parser pkg-config python-base python-module-distribute python-module-peak python-modules python-modules-encodings python-modules-xml time xml-common xml-utils xorg-scrnsaverproto-devel xorg-xproto-devel
BuildRequires: db2latex-xsl glibc-devel-static gnome-settings-daemon-devel intltool libSM-devel libXScrnSaver-devel libXext-devel libcanberra-gtk3-devel libnotify-devel python-module-PyXML python-module-mwlib python-module-paste

%description
DrWright is a program that reminds you to take wrist breaks to rest your hands.

%description -l be_BY.UTF-8
DrWright гэта праграма, якая нагадвае пра неабходнасьць перарыву для адпачынку вашых рук.

%description -l uk_UA.UTF-8
DrWright -- це програма, що нагадує про необхідність перерви для відпочинку рук.

description -l ru_RU.UTF-8
DrWright это программа, которая напоминает про необходимость перерыва для отдыха ваших рук.

%prep
%setup -n %name-%version

%build
%configure --disable-schemas-install
%make_build

%install
%makeinstall_std

%find_lang %name --with-gnome
desktop-file-install --dir %buildroot%_desktopdir \
	--remove-category=Application \
	%buildroot%_desktopdir/gnome-typing-break-panel.desktop

#%post
#gconf2_install %name

#%preun
#if [ $1 = 0 ]; then
#gconf2_uninstall %name
#fi

%files -f %name.lang
%doc AUTHORS ChangeLog NEWS
#_sysconfdir/gconf/schemas/*
%_libexecdir/%name/
%_libdir/control-center-1/panels/*
%_libdir/gnome-settings-daemon-3.0/*
%_datadir/glib-2.0/schemas/*
%_iconsdir/hicolor/48x48/apps/typing-monitor.png
%_iconsdir/hicolor/scalable/apps/typing-monitor.svg
%_desktopdir/*
%_datadir/%name/

%changelog
* Thu Apr 12 2012 Vitaly Lipatov <lav@altlinux.ru> 3.2.5-alt1
- new version 3.2.5 (with rpmrb script) (ALT bug #27192)

* Wed May 25 2011 Repocop Q. A. Robot <repocop@altlinux.org> 0.18-alt6.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for drwright
  * altlinux-policy-obsolete-buildreq for drwright

* Tue Apr 19 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.18-alt6
- fix build

* Wed Dec 02 2009 Repocop Q. A. Robot <repocop@altlinux.org> 0.18-alt5.qa1
- NMU (by repocop): the following fixes applied:
  * update_menus for drwright
  * obsolete-call-in-post-scrollkeeper-update for drwright
  * postclean-05-filetriggers for spec file

* Sun Dec 24 2006 Vitaly Lipatov <lav@altlinux.ru> 0.18-alt5
- cleanup spec, change packager, remove COPYING, enable SMP build

* Mon May 29 2006 Vitaly Lipatov <lav@altlinux.ru> 0.18-alt4
- build fixes

* Sat Sep 10 2005 Vitaly Lipatov <lav@altlinux.ru> 0.18-alt3
- rebuld without D-BUS

* Thu Feb 10 2005 Vitaly Lipatov <lav@altlinux.ru> 0.18-alt2
- rebuild with GNOME 2.8

* Sun Nov 07 2004 Vitaly Lipatov <lav@altlinux.ru> 0.18-alt1
- new version
- cleanup spec

* Sat Jun 19 2004 Vitaly Lipatov <lav@altlinux.ru> 0.17-alt3
- rebuild with new libgnome
- add russian translation

* Mon Feb 16 2004 Vital Khilko <vk@altlinux.ru> 0.17-alt2
- rebuild with gcc-3.3.3

* Thu Dec 11 2003 Vital Khilko <vk@altlinux.ru> 0.17-alt1
- initial build for ALT Linux Sisyphus
- added belarusian translation
