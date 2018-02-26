%define major 2.3

Name: ical
Version: 2.3.3
Release: alt3

Summary: An X Window System-based calendar program
License: BSD-Style
Group: Office
Url: http://www.annexia.org/freeware/ical/

Source: %name-%version-%release.tar

BuildRequires: gcc-c++ libstdc++-devel tk-devel >= 8.5.0 libXScrnSaver-devel libXft-devel

Requires: tk >= 8.5.0

%description
Ical is an X Window System based calendar program. Ical will easily
create/edit/delete entries, create repeating entries, remind you about
upcoming appointments, print and list item occurrences, and allow
shared calendars between different users.

%prep
%setup

%build
%autoreconf
%configure --with-tclconfig=%_libdir
make OPTF="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS"

%install
%makeinstall \
	MKDIR="mkdir -p" \
	ILIBDIR=%buildroot%_datadir/%name/v%major \
	MANDIR=%buildroot/%_mandir
install -pm0644 -D %name.desktop %buildroot%_desktopdir/%name.desktop
find icons -type f|cpio -pmd %buildroot%_datadir

rm -rf %buildroot%_datadir/%name/v%major/contrib
rm -f contrib/ical.spec

%files
%doc doc/ical.html doc/ical.doc doc/interface.html doc/interface.doc
%doc contrib
%_bindir/%name-%major
%_bindir/%name
%_datadir/%name
%_iconsdir/%name.xpm
%_iconsdir/*/%name.xpm
%_desktopdir/%name.desktop
%_mandir/man1/%name.1*

%changelog
* Mon May 11 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.3.3-alt3
- rebuilt with recent gcc

* Sun Dec  7 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.3.3-alt2
- obsolete by filetriggers macros removed

* Sun Dec 23 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.3.3-alt1
- 2.3.3 released

* Tue Jan 18 2005 ALT QA Team Robot <qa-robot@altlinux.org> 2.3.1-alt2.1
- Rebuilt with libstdc++.so.6.

* Mon Jul  5 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.3.1-alt2
- FR #4416

* Mon Jun  7 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.3.1-alt1
- 2.3.1

* Sat Sep 20 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 2.2-ipl23mdk
- rebuilt in new env

* Tue Oct  1 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 2.2-ipl22mdk
- rebuilt with tcl 8.4

* Fri Jun 14 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 2.2-ipl21mdk
- rebuilt in new env

* Tue Mar 05 2002 Stanislav Ievlev <inger@altlinux.ru> 2.2-ipl20mdk
- Rebuilt

* Fri Dec 08 2000 AEN <aen@logic.ru>
- build for RE

* Tue Nov 21 2000 Egil Moeller <redhog@mandrakesoft.com> 2.2-18mdk
- Changed the "copyright" field of the .spec-file to refelct
  what's really in COPYING and to make rpmlint happy...
- Fix to icons-dir-ownership

* Fri Nov 17 2000 David BAUDENS <baudens@mandrakesoft.com> 2.2-17mdk
- Rebuild with gcc-2.96 & glibc-2.2

* Mon Oct 09 2000 Daouda Lo <daouda@mandrakesoft.com> 2.2-16mdk
- fix icons!

* Sun Sep 03 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 2.2-15mdk
- fixed build with new tcl.
- macrosifications.

* Tue Jul 18 2000 David BAUDENS <baudens@mandrakesoft.com> 2.2-14mdk
- Fix Group and menu

* Fri Mar 31 2000 DindinX <odin@mandrakesoft.com> 2.2-13mdk
- Specs fix
- Change Group
- Add menu and remove wmconfig

* Tue Nov  9 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Fix compilations with gcc2.95.

* Tue May 11 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Mandrake adaptions
- fix glibc21 compilation

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 9)

* Wed Feb 24 1999 Preston Brown <pbrown@redhat.com>
- Injected new description and group.

* Thu Sep 24 1998 Cristian Gafton <gafton@redhat.com>
- patch to build against the latest tcltk

* Thu Aug 13 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Oct 30 1997 Otto Hammersmith <otto@redhat.com>
- fixed wmconfig entry

* Thu Oct 23 1997 Otto Hammersmith <otto@redhat.com>
- replaced references to the version number with %PACKAGE_VERSION

* Wed Oct 22 1997 Otto Hammersmith <otto@redhat.com>
- updated to version 2.2, which is supposed to work with Tcl/Tk 8.0
- added wmconfig entry

* Mon Oct 20 1997 Otto Hammersmith <otto@redhat.com>
- Update version

* Tue Sep 30 1997 Erik Troan <ewt@redhat.com>
- build against tcl/tk 8.0

* Fri Aug 22 1997 Erik Troan <ewt@redhat.com>
- built against glibc

