Name: enscript
Version: 1.6.6
Release: alt1.1

Summary: Converts plain ASCII to PostScript
License: GPL
Group: Publishing
Url: http://www.gnu.org/software/enscript/

Source0: %name-%version.tar.gz
Source1: repatch_spec.sh
Source2: repatch_spec.unused

## FC patches
Patch1: FC-1.6.1-locale.patch
Patch2: FC-wrap_header.patch
Patch3: FC-1.6.4-rh457720.patch
Patch4: FC-rh477382.patch
Patch5: FC-build.patch
Patch6: FC-manfixes.patch
Patch7: FC-bufpos-crash.patch

## Ubuntu patches
Patch101: Ubuntu-01_libpaper.patch
Patch102: Ubuntu-03_misc.patch
Patch103: Ubuntu-04_highlighting.patch
Patch104: Ubuntu-339938-hilight-wrapped-function-list.patch
Patch105: Ubuntu-06_debian.patch
Patch106: Ubuntu-07_media.patch
Patch107: Ubuntu-09_appendctrld.patch
Patch108: Ubuntu-344750-no-gecos.patch
Patch109: Ubuntu-147116-ruby-hilight.patch
Patch110: Ubuntu-457244-octave-highlighting.patch

## ALT patches
Patch501: enscript-1.6.4-alt-mail.patch
Patch502: enscript-1.6.3-alt-fontpath.patch
Patch503: enscript-1.6.3-alt-default-enc.patch
Patch504: enscript-1.6.3-alt-encodings.patch

# Automatically added by buildreq on Thu May 29 2014
# optimized out: xz
BuildRequires: flex libpaper-devel
# explicitly added texinfo for info files
BuildRequires: texinfo

%description
Enscript is a print filter. It can take ASCII input
and format it into PostScript output. At the same time,
it can also do nice transformations like putting two
ASCII pages on one physical page (side by side) or
changing fonts.

%prep
%setup

## FC apply patches
%patch1 -p1 -b .locale
%patch2 -p1 -b .wrap_header
%patch3 -p1 -b .rh457720
%patch4 -p1 -b .rh477382
%patch5 -p1 -b .build
%patch6 -p1 -b .manfixes
%patch7 -p1 -b .bufpos-crash

## Ubuntu apply patches
%patch101 -p1
%patch102 -p1
%patch103 -p1
%patch104 -p1
%patch105 -p1
%patch106 -p1
%patch107 -p1
%patch108 -p1
%patch109 -p1
%patch110 -p1

## ALT apply patches
%patch501 -p1
%patch502 -p1
%patch503 -p1
%patch504 -p1

%build
export CPPFLAGS='-DPROTOTYPES'
%autoreconf
%configure --with-media=A4
%make_build

%install
%makeinstall

install -pm755 -d $RPM_BUILD_ROOT%_sysconfdir/%name
install -pm644 $RPM_BUILD_ROOT/%_datadir/%name/afm/font.map $RPM_BUILD_ROOT%_sysconfdir/%name/font.map
cd $RPM_BUILD_ROOT/%_datadir/%name
ln -s  %_sysconfdir/%name/font.map
cd -

%find_lang %name

ln -s %_bindir/enscript $RPM_BUILD_ROOT%_bindir/nenscript

%files -f %name.lang
%doc AUTHORS ChangeLog NEWS README README.ESCAPES THANKS TODO
%config(noreplace) %_sysconfdir/enscript.cfg
%config(noreplace) %_sysconfdir/enscript/font.map
%_bindir/*
%_mandir/man?/*
%_datadir/%name
%_infodir/*.info*

%changelog
* Thu Dec 03 2015 Igor Vlasenko <viy@altlinux.ru> 1.6.6-alt1.1
- NMU: added BR: texinfo

* Wed May 28 2014 Fr. Br. George <george@altlinux.ru> 1.6.6-alt1
- Autobuild version bump to 1.6.6
- Upstream switch
- FC and Ubuntu repatch_spec used
- Minor spec cleanup

* Mon Feb 25 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.6.4-alt4
- fixed build on arm

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
