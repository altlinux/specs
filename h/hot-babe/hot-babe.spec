BuildRequires: desktop-file-utils
Summary: Graphical utility which display the activity in a very special way
Name: hot-babe
Version: 0.2.2
Release: alt2.qa1
Url: http://dindinx.net/hotbabe/
Source0: %name-%version.tar
Source1: %name.desktop
Patch0: %name-0.2.2-noDock.patch
License: GPL
Group: Monitoring

BuildRequires: libgtk+2-devel

%description
Hot-babe is a small graphical utility which display the system
activity in a very special way. When the CPU is idle, it displays a
dressed girl, and when the activity goes up, as the temperature
increases, the girl begins to undress, to finish totally naked when
the system activity reaches 100%%. Of course, if you can be shocked by
nudity, don't use it!

%prep
%setup
%patch0 -p1

%build
%make PREFIX=%prefix

%install
make install PREFIX=/usr  DESTDIR=%buildroot
mkdir -p %buildroot%_niconsdir
mv %buildroot%_datadir/pixmaps/* %buildroot%_niconsdir

# Desktop
install -D -m 644 %SOURCE1 %buildroot%_desktopdir/%name.desktop
desktop-file-install --dir %buildroot%_desktopdir \
	--add-category=Monitor \
	%buildroot%_desktopdir/hot-babe.desktop

%files
%_bindir/%name
%_niconsdir/%name.*
%_datadir/%name
%_man1dir/*
%_desktopdir/%name.desktop
%doc ChangeLog NEWS LICENSE CONTRIBUTORS TODO config.example

%changelog
* Tue Jun 07 2011 Repocop Q. A. Robot <repocop@altlinux.org> 0.2.2-alt2.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for hot-babe

* Sun Jul 18 2010 Terechkov Evgenii <evg@altlinux.ru> 0.2.2-alt2
- Spec cleanup
- menu->desktop
- Build fixed

* Sun Jul 18 2010 Evgenii Terechkov <evg@altlinux.ru> 0.2.2-alt2
- spec macro abuse cleanup

* Thu Nov 19 2009 Repocop Q. A. Robot <repocop@altlinux.org> 0.2.2-alt1.1.qa1
- NMU (by repocop): the following fixes applied:
  * update_menus for hot-babe
  * postclean-05-filetriggers for spec file

* Thu May 24 2007 Terechkov Evgenii <evg@altlinux.ru> 0.2.2-alt1.1
- Patch0 added
- Icon moved from /u/s/pixmaps to %%_niconsdir and added to /u/l/menu/%%name
- Spec cleanup (automatic + %%_datadir/%%name)
- %%post/%%postun added (menu update)
- -D (from Patch0) added to menu command
- buildreqs updated

* Thu Jan 06 2005 Eugene V. Horohorin <genix@altlinux.ru> 0.2.2-alt1
- new release (gdk2 version)

* Tue Oct 26 2004 Eugene V. Horohorin <genix@altlinux.ru> 0.1.4-alt3
- change menu file (longtitle field)

* Tue Oct 12 2004 Eugene V. Horohorin <genix@altlinux.ru> 0.1.4-alt2
- Default option -i added to menu file

* Wed Oct 06 2004 Eugene V. Horohorin <genix@altlinux.ru> 0.1.4-alt1
- Implementation build

