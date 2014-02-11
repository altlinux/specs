BuildRequires: desktop-file-utils
Name: gnome-alsamixer
Version: 0.9.7
Release: alt6

Summary: %name is an ALSA mixer for GNOME
Summary(ru_RU.UTF-8): ALSA-микшер для GNOME
License: GPL
Group: Sound

Url: http://git.gnome.org/browse/gnome-alsamixer/

Source: %name.tar

BuildRequires: gnome-common libalsa-devel libgtk+2-devel libGConf-devel intltool

Requires(post,pre): GConf

%description
This package provides %name - a sound mixer for GNOME which supports
ALSA drivers.

%description -l ru_RU.UTF-8
В этом пакете находится %name - звуковой
микшер для GNOME с поддержкой драйверов
ALSA.

%prep
%setup -q -n %name

%build
%autoreconf
%configure --disable-schemas-install
%make update-po -C po
%make_build

%install
%makeinstall_std

%find_lang %name
desktop-file-install --dir %buildroot%_desktopdir \
	--add-category=Audio \
	--add-category=Mixer \
	--add-category=GTK \
	%buildroot%_desktopdir/gnome-alsamixer.desktop

%post
%gconf2_install %name

%preun
if [ $1 = 0 ]; then
%gconf2_uninstall %name
fi

%files -f %name.lang
%_bindir/*
%_datadir/applications/*
%_datadir/pixmaps/*
%config %_sysconfdir/gconf/*/*
%doc AUTHORS ChangeLog

%changelog
* Tue Feb 11 2014 Yuri N. Sedunov <aris@altlinux.org> 0.9.7-alt6
- explicitly link against libm

* Mon Apr 01 2013 Yuri N. Sedunov <aris@altlinux.org> 0.9.7-alt5
- fixed build

* Mon Aug 27 2012 Repocop Q. A. Robot <repocop@altlinux.org> 0.9.7-alt4.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for gnome-alsamixer

* Tue Apr 10 2012 Yuri N. Sedunov <aris@altlinux.org> 0.9.7-alt4
- modernized build system
- fixed desktop-file
- updated translations

* Mon Apr 09 2012 Yuri N. Sedunov <aris@altlinux.org> 0.9.7-alt3
- removed libgnome{,ui} dependencies
- updated russian translation

* Thu May 05 2011 Yuri N. Sedunov <aris@altlinux.org> 0.9.7-alt2
- fixed build

* Thu Jan 14 2010 Repocop Q. A. Robot <repocop@altlinux.org> 0.9.7-alt1.qa2
- NMU (by repocop): the following fixes applied:
  * update_menus for gnome-alsamixer
  * postclean-05-filetriggers for spec file

* Thu Apr 10 2008 Igor Vlasenko <viy@altlinux.ru> 0.9.7-alt1.qa1
- NMU (by repocop): the following fixes applied:
 * update_menus for gnome-alsamixer

* Sun Dec 24 2006 Vyacheslav Dikonov <slava@altlinux.ru> 0.9.7-alt1
- GNOME CVS version 2006-12-24

* Sun Nov 21 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.9.6-alt1
- 0.9.6

* Mon Sep 08 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.9.5-alt1
- 0.9.5

* Fri Aug 29 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.9.4-alt1
- First build for Sisyphus.
