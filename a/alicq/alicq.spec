# -*- rpm-spec -*-
# $Id: alicq.spec,v 1.76 2005/08/04 14:03:06 grigory Exp $

Name: alicq
Version: 0.8.9
Release: alt6.qa3

Summary: alicq - Flexible ICQ client in pure Tcl/Tk
License: GPL
Group: Networking/Instant messaging
URL: http://alicq.sourceforge.net/

BuildArch: noarch
Source0: %name-%version.tar.bz2

Requires: bwidget tk >= 8.3
Requires: tcl-icq >= 0.8.9
BuildRequires: rpm-build >= 4.0.4 tcl >= 8.3 tcllib xsltproc rpm-build-tcl

%description
   Alicq is pure Tcl/Tk implementation of ICQ client with flexible
modularized architecture, support for ICQv8 (ICQ2000/OSCAR) protocol,
and ability to pick up Licq configuration files and user database.

Why would you use it? It is small, about 2500 lines as of release
0.6. It is modular and extendable in best tradition of the Tcl
scripting language. New modules are easy to write, and dozen lines
Tcl module can do a lot. It is crossplatfrom: works on Unix, Windows,
Macintosh, and on any other system supported by Tcl/Tk.


%package -n tcl-icq
Summary: This library gives ability to use ICQ v8 protocol (OSCAR) in tcl programs
Group: Development/Tcl
Requires: tcl >= 8.3

%description -n tcl-icq
Protocol description and some ideas in implementattion were taken from
ICQ2000.pm and ICQ2000_Easy.pm perl modules by
Robin Fisher <robin@phase3solutions.com> and vICQ program by
Alexander Timoshenko

%add_tcl_lib_path %_datadir/%name

%prep
%setup -q -c
sed -i -e 's|check-tcl||g' Makefile

%build

%install 
%makeinstall package=%name tcldatadir=%buildroot%_datadir/%name/lib
%makeinstall -C icq package=tcl-icq tcldatadir=%buildroot%_tcldatadir

# menu stuff JONS GTK
mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%{name}.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=Alicq
Comment=tcl/tk ICQ client
Icon=%{name}
Exec=%name
Terminal=false
Categories=Network;InstantMessaging;
EOF

install -d -m 755 %buildroot%_miconsdir
install -p -m 0644 %name.xpm %buildroot%_miconsdir/%name.xpm

%files
%doc doc/{changelog,INSTALL,README,TODO,alicqrc.sample}
%dir %_datadir/%name
%dir %_datadir/%name/lib
%_bindir/*
%_datadir/%name/*
%_desktopdir/%{name}.desktop
%_miconsdir/%name.xpm
#%_man1dir/*
#%_man5dir/*

%files -n tcl-icq
%doc icq/examples/* icq/doc/{changelog,README,TODO}
%dir %_tcldatadir/tcl-icq
%_tcldatadir/tcl-icq/*
%_mandir/mann/*

%changelog
* Sat Apr 09 2011 Igor Vlasenko <viy@altlinux.ru> 0.8.9-alt6.qa3
- NMU: menu converted to .desktop file

* Wed Feb 03 2010 Repocop Q. A. Robot <repocop@altlinux.org> 0.8.9-alt6.qa2
- NMU (by repocop): the following fixes applied:
  * update_menus for alicq
  * postclean-05-filetriggers for spec file

* Thu Apr 10 2008 Igor Vlasenko <viy@altlinux.ru> 0.8.9-alt6.qa1
- NMU (by repocop): the following fixes applied:
 * update_menus for alicq

* Mon Nov 12 2007 Grigory Milev <week@altlinux.ru> 0.8.9-alt6
- fix build requires

* Wed Feb 15 2006 Grigory Milev <week@altlinux.ru> 0.8.9-alt5
- new CVS version 2006.15.02

* Thu Aug  4 2005 Grigory Milev <week@altlinux.ru> 0.8.9-alt4
- fix Makefile

* Wed May 04 2005 Grigory Milev <week@altlinux.ru> 0.8.9-alt3
- cvs update

* Tue Dec 07 2004 Grigory Milev <week@altlinux.ru> 0.8.9-alt2
- Tree performance fixes

* Mon Oct 18 2004 Grigory Milev <week@altlinux.ru> 0.8.9-alt1
- Rebuild for ALT Linux

* Tue Oct 12 2004 Ihar Viarheichyk <iverg@optifacio.com> 0.8.9-alt1
- RC

* Wed Oct 06 2004 Ihar Viarheichyk <iverg@optifacio.com> 0.8.8-alt9
- Release candidate for 0.8.9

* Thu Sep 23 2004 Grigory Milev <week@altlinux.ru> 0.8.8-alt8
- rebuild for ALT Linux

* Mon Sep 20 2004 Ihar Viarheichyk <iverg@optifacio.com> 0.8.8-alt7
- Dialogs fixes

* Mon Aug 16 2004 Grigory Milev <week@altlinux.ru> 0.8.8-alt6
- Shows status of authorized contacts when server blocks old status requests

* Wed Jul 14 2004 Grigory Milev <week@altlinux.ru> 0.8.8-alt5
- Direct connections

* Tue Apr 27 2004 Grigory Milev <week@altlinux.ru> 0.8.8-alt4
- added module emoticons for drawing graphic smiles

* Thu Apr 15 2004 Grigory Milev <week@altlinux.ru> 0.8.8-alt3
- fix build requires

* Wed Apr 14 2004 Ihar Viarheichyk <iverg@optifacio.com> 0.8.8-alt2
- Final build for 0.8.8 release. See changes in /usr/share/alicq/doc/changelog
  after installation.

* Wed Mar 31 2004 Grigory Milev <week@altlinux.ru> 0.8.8-alt1
- change alicq lib dir

* Mon Dec 22 2003 Grigory Milev <week@altlinux.ru> 0.8.7-alt10
- rebuild for ALT Linux

* Mon Dec 22 2003 Igor Viarheichyk <iverg@mail.ru> 0.8.7-alt9
- automatical rebuild

* Mon Dec 22 2003 Ihar Viarheichyk <iverg@optifacio.com> 0.8.7-alt8
- build dependance on tcllib added

* Mon Dec 22 2003 Ihar Viarheichyk <iverg@optifacio.com> 0.8.7-alt7
- build dependance on tcl added

* Mon Dec 22 2003 Ihar Viarheichyk <iverg@optifacio.com> 0.8.7-alt6
- test build in BTE

* Mon Dec 22 2003 Igor Viarheichyk <iverg@mail.ru> 0.8.7-alt5
- automatical rebuild

* Fri Dec 19 2003 Igor Viarheichyk <iverg@mail.ru> 0.8.7-alt4
- automatical rebuild

* Fri Dec 19 2003 Igor Viarheichyk <iverg@mail.ru> 0.8.7-alt3
- automatical rebuild

* Thu Dec 18 2003 Igor Viarheichyk <iverg@mail.ru> 0.8.7-alt2
- automatical rebuild.

* Thu Dec 18 2003 Igor Viarheichyk <iverg@mail.ru> 0.8.7-alt1
- New upstream release 0.8.7

* Thu Dec  4 2003 Grigory Milev <week@altlinux.ru> 0.8.6-alt4
- new prerelease version 0.8.6-17
- Cd into base directory to make modules life easier.
- Server-side roster support
- Some fixes for service-sie roster support, still incomplete.

* Thu Nov 13 2003 Grigory Milev <week@altlinux.ru> 0.8.6-alt3
- new prerelease version 0.8.6-14 released

* Wed Nov  5 2003 Grigory Milev <week@altlinux.ru> 0.8.6-alt2
- new version released

* Tue Sep 16 2003 Grigory Milev <week@altlinux.ru> 0.8.6-alt1
- new version released
- icq libs moved to separated package and may use with out alicq

* Wed Jul  9 2003 Grigory Milev <week@altlinux.ru> 0.8.5-alt8
- modules/tray.tcl: statup popup in tray module on right click
- modules/: autooffline.tcl, geometry.tcl: autooffline module added

* Wed May 14 2003 Ihar Viarheichyk <iverg@optifacio.com> 0.8.5-alt7
- Fix for GAIM compatibility

* Tue Apr  8 2003 Grigory Milev <week@altlinux.ru> 0.8.4-alt3
- cvs snapshot (fixed some bugs with contacts)

* Fri Apr  4 2003 Grigory Milev <week@altlinux.ru> 0.8.4-alt2
- added Xmenu

* Fri Apr 04 2003 Ihar Viarheichyk <iverg@optifacio.com> 0.8.4-alt1
- New version 0.8.4, which includes all changes since 0.8.3-3
- Added saving of proportions in splitted message windows
- Silent "unknonwn host" error handling

* Thu Mar 20 2003 Ihar Viarheichyk <iverg@optifacio.com> 0.8.3-alt4
- Fixed minor bug when sending empty contact list to server
- Fixed bug in protocol error handling

* Thu Mar 20 2003 Ihar Viarheichyk <iverg@optifacio.com> 0.8.3-alt2
- Fixed bug with encoding in history

* Thu Mar 20 2003 Ihar Viarheichyk <iverg@optifacio.com> 0.8.3-alt1
- This release intended to test new unicode support and protocol
  handling code cleanup.
- Implicit unicode usage when sending messages to unicode-capable 
  clinets.
- Great ICQ protocol handling library code cleanup.
- Fixed bug with losing messages from Miranda IM.
- Automatical recovery from protocol handling errors.
- Automated (not automatical) sendin bug reports to author.
- Key and mouse binding replaced with bindings to virtual events 
  for better customization
- Geometry module reworked to store windows geomery in Xdefaults format
- Added sending keepalive packets (option -keepalive)
- Sending pings to detect network problems added
- Fixed small bug when whitepages info showed UIN and status of 
  local user, not remote one.
- Fixed reconnect when used proxy - more automatic and reliable now.
- Fixed bug when grouping rule was not saved to startup file on exit.

* Fri Jan 31 2003 Ihar Viarheichyk <iverg@optifacio.com> 0.8.2-alt1
- Fixes for starange selection handling in some versions of BWidget
- New resource timeFormat added to allow configure format of time displayed
  in message and history windows
- Small fixes in UI: pack changed to grid in some windows.  
- Some code cleanup  

* Mon Jan 27 2003 Ihar Viarheichyk <iverg@optifacio.com> 0.8.1-alt7
- Fix for BWidget bug with selection on removed node
- Pack method changed to grid method in main window

* Fri Jan 24 2003 Ihar Viarheichyk <iverg@optifacio.com> 0.8.1-alt6
- Grouping and sorting subsystems in tree.tcl reworked
- Fixed bug when 'Node already exists' error appears sometimes when contact
  changes status
- Separate sorting rules for groups and contacts  

* Tue Nov 12 2002 Ihar Viarheichyk <iverg@mail.ru> 0.8.0-alt3
- Baloons, remote client discovery

* Fri Nov  8 2002 Grigory Milev <week@altlinux.ru> 0.8.0-alt1
- new version released

* Wed Nov  6 2002 Ihar Viarheichyk <iverg@mail.ru> 0.7.9-alt5
 - Stable release 

* Thu Oct 31 2002 Ihar Viarheichyk <iverg@mail.ru> 0.7.9-alt5
 - Configurator added. Now most important Alicq parameters can be 
   configured in configurator window.
 - Repair package for converting config file to new format on-the-fly. Can
   also be used for automatical repairing of damaged config in future 
 - Fix in proxy code
 - Fixed bug when selection is on deleted node in main tree
 - Check added for selectiong needed version of BWidget
 - Candidate for upstream release 0.8
 - Firmat of startup file changed
 - New modules infrastructure, based on properties and metadata allows create
   independant modules easier, and add new transports
 - Almost all modules rewritten according to new modules creation rules  
 - Dynamic menu, allowing new items addition without restart
 - Alicq now can save changes in startup file
 - Support of subgroups (groups can include other groups)
 - Membership in several groups
 - Multicast messages to groups
 - Alicq saves state of groups on exit (open or closed)
 - Transport encoding can be specified for each contact besides global one
 - Setup wizard added
 
* Wed Jul 17 2002 Grigory Milev <week@altlinux.ru> 0.6.5-alt4
- added requires
- move icq libs to alicq share dir

* Wed Jul 17 2002 Grigory Milev <week@altlinux.ru> 0.6.5-alt3
- added requires

* Wed Jul 17 2002 Grigory Milev <week@altlinux.ru> 0.6.5-alt2
- changed libs and shares path

* Fri Jun  7 2002 Grigory Milev <week@altlinux.ru> 0.6.5-alt1
- bugs fixes
- new modules

* Thu Apr 18 2002 Grigory Milev <week@altlinux.ru> 0.6.1-alt1
- new version released

* Tue Apr  2 2002 Grigory Milev <week@altlinux.ru> 0.6-alt2
- new cvs snapshot 02.04.2002

* Fri Mar 15 2002 Grigory Milev <week@altlinux.ru> 0.6-alt1
- new version released

* Wed Feb 20 2002 Grigory Milev <week@altlinux.ru> 0.5-alt2
- fix requires
- many bugfixses in alicq (0.6 pre version)

* Thu Feb  7 2002 Grigory Milev <week@altlinux.ru> 0.5-alt1
- Initial build for ALT Linux distribution.
