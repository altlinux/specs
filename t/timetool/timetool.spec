Name: timetool
Version: 2.8
Release: alt7.qa2

Summary: A utility for setting the system's date and time
Summary(ru_RU.CP1251): Инструментарий для установки системного времени и даты.
License: GPL
Group: System/Configuration/Other
BuildArch: noarch
Packager: Aleksandr Blokhin <sass@altlinux.ru>

Source0: %name-%version.tar.bz2
Source1: icons-%name.tar.bz2
Source3: loopy.tar.bz2
Source4: dialog.tcl
Patch0: %name.patch

%description
The %name utility provides a graphical user interface for setting
the current date and time on your system.

%description -l ru_RU.CP1251
%name предоставляет графический интерфейс пользователя для установки
текущей даты и времени в вашей системе.

%prep
%setup -q
%patch0 -p1

%install
%__mkdir_p $RPM_BUILD_ROOT%_bindir
%__mkdir_p $RPM_BUILD_ROOT%_niconsdir/{large,mini}
%__mkdir_p $RPM_BUILD_ROOT%_libexecdir/%name/loopy
%make_install install PREFIX=$RPM_BUILD_ROOT%prefix
%__install -p -m644 %SOURCE4 $RPM_BUILD_ROOT%_libexecdir/%name
tar xjf %SOURCE3 -C $RPM_BUILD_ROOT%_libexecdir/%name/loopy
tar xjf %SOURCE1 
install -D -m644 %name.xpm $RPM_BUILD_ROOT%_niconsdir/%name.xpm
install -D -m644 large/%name.xpm $RPM_BUILD_ROOT%_liconsdir/%name.xpm
install -D -m644 mini/%name.xpm $RPM_BUILD_ROOT%_miconsdir/%name.xpm

mkdir -p $RPM_BUILD_ROOT%_desktopdir
cat > $RPM_BUILD_ROOT%_desktopdir/%{name}.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=Timetool
GenericName=Set Time and Date
Comment=%{summary}
Icon=%{name}
Exec=%{name}
Terminal=false
Categories=Settings;HardwareSettings;
EOF

%files
%dir %_libexecdir/%name
%_bindir/*
%_desktopdir/*
%_niconsdir/%name.xpm
%_liconsdir/%name.xpm
%_miconsdir/%name.xpm
%_libexecdir/%name/*

%changelog
* Sat Mar 26 2011 Igor Vlasenko <viy@altlinux.ru> 2.8-alt7.qa2
- converted debian menu to freedesktop

* Tue Nov 24 2009 Repocop Q. A. Robot <repocop@altlinux.org> 2.8-alt7.qa1
- NMU (by repocop): the following fixes applied:
  * pixmap-in-deprecated-location for timetool
  * update_menus for timetool
  * postclean-05-filetriggers for spec file

* Wed Mar 08 2006 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 2.8-alt7
- changes in spec

* Wed Mar 01 2006 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 2.8-alt6
- Changed icons paths

* Sat Nov 05 2005 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 2.8-alt5
- some fixes in dialog.tcl

* Mon Oct 31 2005 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 2.8-alt4
- fixed path

* Tue Mar 30 2004 Aleksandr Blokhin (Sass) <sass@altlinux.ru> 2.8-alt3
- removed russian translation.

* Mon Oct 14 2002 Aleksandr Blokhin (Sass) <sass@altlinux.ru> 2.8-alt2
- fixed filepaths

* Mon Jul 08 2002 Aleksandr Blokhin <sass@altlinux.ru> 2.8-alt1
- 2.8
- translated to russian language
- added Source3, Source4, Patch0

* Tue Feb 06 2001 Dmitry V. Levin <ldv@fandra.org> 2.7.4-ipl2mdk
- Fixed requires.

* Thu Jan 18 2001 Dmitry V. Levin <ldv@fandra.org> 2.7.4-ipl1mdk
- 2.7.4

* Wed Jan 17 2001 Dmitry V. Levin <ldv@fandra.org> 2.7-ipl8mdk
- RE adaptions.

* Sat Oct 07 2000 Daouda Lo <daouda@mandrakesoft.com> 2.7-8mdk
- embedded menu
- fix icons

* Mon Oct 02 2000 DindinX <odin@mandrakesoft.com> 2.7-7mdk
- remove "icon=none" from menu description

* Tue Sep 26 2000 Daouda Lo <daouda@mandrakesoft.com> 2.7-6mdk
- menu title should begin with capital letter.

* Mon Sep 25 2000 Daouda Lo <daouda@mandrakesoft.com> 2.7-5mdk
- add icons for menu system.

* Fri Jul 28 2000 Francis Galiegue <fg@mandrakesoft.com> 2.7-4mdk

- BMacros
- Spec file fixes
- Added menu entry to %files list ;)

* Fri Mar 31 2000 DindinX <odin@mandrakesoft.com> 2.7-3mdk
- Spec update
- fix Group
- Add Menu

* Fri Nov 26 1999 Pixel <pixel@linux-mandrake.com>
- fixed Requires (rhsuk)

* Fri Nov 12 1999 Damien Krotkine <damien@mandrakesoft.com>
- 2.7

* Tue Aug 17 1999 Bill Nottingham <notting@redhat.com>
- fix utc negotiation

* Fri Jun 11 1999 Preston Brown <pbrown@redhat.com>
- better leapyear fix from  jrs@math.lsa.umich.ed

* Wed May 05 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Mandrake adaptions

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 5)

* Tue Mar 09 1999 Preston Brown <pbrown@redhat.com>
- fixed Y2K leapyear bug

* Fri Dec 18 1998 Preston Brown <pbrown@redhat.com>
- bumped spec number for initial rh 6.0 build

* Fri Aug  7 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Fri Nov 07 1997 Michael K. Johnson <johnsonm@redhat.com>
- wmconfig only for root

* Thu Oct 30 1997 Otto Hammersmith <otto@redhat.com>
- fixed control-panel icon

* Fri Oct 24 1997 Marc Ewing <marc@redhat.com>
- wmconfig

* Thu Jul 31 1997 Erik Troan <ewt@redhat.com>
- made a noarch package

* Mon Mar 03 1997 Erik Troan <ewt@redhat.com>
- requires control-panel (doesn't start properly from the command line)
- didn't switch to 24 hour time properly
