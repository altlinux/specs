Name: enscript
Version: 1.6.4
Release: alt3.qa1

Packager: Stanislav Ievlev <inger@altlinux.org>

Summary: Converts plain ASCII to PostScript
License: GPL
Group: Publishing
Url: http://people.ssh.fi/mtr/genscript/


Source0: ftp://ftp.gnu.org/pub/gnu/%name/%name-%version.tar.bz2

Patch1: enscript-1.6.3-rh-mail.patch
Patch2: enscript-1.6.1-rh-locale.patch
Patch3: enscript-1.6.3-alt-fontpath.patch
Patch4: enscript-1.6.3-alt-default-enc.patch  
Patch5: enscript-1.6.3-alt-encodings.patch
Patch6: enscript-1.6.4-alt-build.patch
Patch7: enscript-1.6.3-deb-CAN-2004-1184.patch
Patch8: enscript-1.6.3-deb-CAN-2004-1185.patch
Patch9: enscript-1.6.3-deb-CAN-2004-1186.patch

BuildPreReq: rpm-build >= 4.0.4-alt10, automake_1.7, autoconf_2.50
%set_automake_version 1.7
%set_autoconf_version 2.5

Obsoletes: nenscript

# Automatically added by buildreq on Tue Sep 16 2003
BuildRequires: flex

%description
Enscript is a print filter. It can take ASCII input
and format it into PostScript output. At the same time,
it can also do nice transformations like putting two
ASCII pages on one physical page (side by side) or
changing fonts.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1

%autoreconf

%build
%add_optflags -D_GNU_SOURCE
%configure --with-media=Letter
%make_build

%install
#strange hack
cd po
%__ln_s ../mkinstalldirs mkinstalldirs
cd -

%makeinstall

%__install -pm755 -d $RPM_BUILD_ROOT%_sysconfdir/%name
%__install -pm644 $RPM_BUILD_ROOT/%_datadir/%name/afm/font.map $RPM_BUILD_ROOT%_sysconfdir/%name/font.map
cd $RPM_BUILD_ROOT/%_datadir/%name
%__ln_s  %_sysconfdir/%name/font.map
cd -

%find_lang %name

%__ln_s %_bindir/enscript $RPM_BUILD_ROOT%_bindir/nenscript

%files -f %name.lang
%doc AUTHORS ChangeLog NEWS README README.ESCAPES THANKS TODO
%config(noreplace) %_sysconfdir/enscript.cfg
%config(noreplace) %_sysconfdir/enscript/font.map
%_bindir/*
%_mandir/man?/*
%_datadir/%name
%_infodir/*.info*


%changelog
* Thu Nov 12 2009 Repocop Q. A. Robot <repocop@altlinux.org> 1.6.4-alt3.qa1
- NMU (by repocop): the following fixes applied:
  * obsolete-call-in-post-install-info for enscript
  * postclean-05-filetriggers for spec file

* Wed Jan 16 2008 Stanislav Ievlev <inger@altlinux.org> 1.6.4-alt3
- fix build in Sisyphus

* Mon Apr 16 2007 ALT QA Team Robot <qa-robot@altlinux.org> 1.6.4-alt2.0
- Automated rebuild.

* Tue Jan 25 2005 Stanislav Ievlev <inger@altlinux.org> 1.6.4-alt2
- CAN-2004-1184,CAN-2004-1185,CAN-2004-1186

* Fri Oct 08 2004 Stanislav Ievlev <inger@altlinux.org> 1.6.4-alt1
- 1.6.4

* Tue Sep 16 2003 Stanislav Ievlev <inger@altlinux.ru> 1.6.3-alt3
- fix build in hasher

* Wed Oct 23 2002 Stanislav Ievlev <inger@altlinux.ru> 1.6.3-alt2
- rebuild with gcc3

* Fri Aug 16 2002 Stanislav Ievlev <inger@altlinux.ru> 1.6.3-alt1
- 1.6.3
- return our encodings
- added encoding autodetection. Now we can remove another file from etcskel

* Fri Jan 18 2002 Dmitry V. Levin <ldv@alt-linux.org> 1.6.1-ipl18mdk
- Fixed tmp race.

* Fri Nov 30 2001 Stanislav Ievlev <inger@altlinux.ru> 1.6.1-ipl17mdk
- fix packager tag ;)

* Thu Nov 6 2000 AEN <aen@logic.ru>
- koi8{u,r}, cp1251, pt154 support added
* Wed Aug 30 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.6.1-15mdk
- licence: GNU -> GPL

* Wed Aug 23 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.6.1-14mdk
- automatically added packager tag

* Mon Aug 14 2000 Pablo Saratxaga <pablo@mandrakesoft.com> 1.6.1-13mdk
- added Irish catalog

* Mon Jul 17 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.6.1-12mdk
- macros, cleanup
- make ewt's marking of /usr/share/enscript/font.map work (Perl rules)

* Thu Mar 23 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.6.1-11mdk
- new groups
- fixed non-existent URL

* Tue Nov 23 1999 François PONS <fpons@mandrakesoft.com>
- Build release.

* Tue May 11 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Mandrake adaptions

* Wed Mar 24 1999 Erik Troan <ewt@redhat.com>
- marked /usr/share/enscript/font.map as a config file

* Mon Mar 22 1999 Preston Brown <pbrown@redhat.com>
- added documentation to the RPM

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 5)

* Fri Mar 19 1999 Jeff Johnson <jbj@redhat.com>
- strip binaries.
- include i18n locales.

* Wed Feb 24 1999 Preston Brown <pbrown@redhat.com>
- Injected new description and group.

* Wed Nov 11 1998 Preston Brown <pbrown@redhat.com>
- translations ripped out, slight cleanup to build section.

* Mon Nov 09 1998 Preston Brown <pbrown@redhat.com>
- initial build of GNU enscript to replace nenscript.
