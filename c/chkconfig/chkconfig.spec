Name: chkconfig
Version: 1.3.59
Release: alt3

Summary: A system tool for maintaining the /etc/rc*.d hierarchy
License: GPLv2
Group: System/Configuration/Boot and Init
%define srcname %name-%version-%release
# git://git.altlinux.org/gears/c/chkconfig.fit
Source: %srcname.tar
BuildRequires: libpopt-devel

%description
Chkconfig is a basic system utility.  It updates and queries runlevel
information for system services.  Chkconfig manipulates the numerous
symbolic links in /etc/rc.d, to relieve system administrators of some
of the drudgery of manually editing the symbolic links.

%prep
%setup -n %srcname

%build
%make_build chkconfig subdirs

%install
install -pDm755 chkconfig %buildroot/sbin/chkconfig
install -pDm644 chkconfig.8 %buildroot%_man8dir/chkconfig.8
%makeinstall_std -C po
%find_lang %name

%files -f %name.lang
/sbin/chkconfig
%_man8dir/chkconfig.*

%changelog
* Fri May 18 2012 Dmitry V. Levin <ldv@altlinux.org> 1.3.59-alt3
- chkconfig: Fixed systemd .service symlinks support.

* Fri May 18 2012 Dmitry V. Levin <ldv@altlinux.org> 1.3.59-alt2
- chkconfig: Fixed systemd .service symlinks support.

* Thu May 17 2012 Dmitry V. Levin <ldv@altlinux.org> 1.3.59-alt1
- Updates to 1.3.59-2-g9e77a17.
- chkconfig: Added systemd .service symlinks support (by Igor Vlasenko).

* Wed Jan 25 2012 Dmitry V. Levin <ldv@altlinux.org> 1.3.57-alt1
- Updated to 1.3.57-1-g3c9dcf4 (closes: #17461, #25179).
- chkconfig.8: Removed references to missing manpages (closes: #16535).

* Thu Apr 12 2007 Dmitry V. Levin <ldv@altlinux.org> 1.3.29-alt2
- Uncompressed tarball, reduced macro abuse in specfile.

* Thu Jun 01 2006 Dmitry V. Levin <ldv@altlinux.org> 1.3.29-alt1
- Updated to 1.3.29.

* Sat Feb 04 2006 Dmitry V. Levin <ldv@altlinux.org> 1.3.26-alt1
- Updated to 1.3.26.

* Thu Dec 22 2005 Dmitry V. Levin <ldv@altlinux.org> 1.3.25-alt1
- Updated to 1.3.25, synced with 1.3.25-owl1.
- Disabled build and packaging of ntsysv.

* Fri Oct 31 2003 Dmitry V. Levin <ldv@altlinux.org> 1.2.24-alt5
- ntsysv: check service files (S_ISREG, S_IXUSR) where appropriate.

* Wed Oct 29 2003 Dmitry V. Levin <ldv@altlinux.org> 1.2.24-alt4
- chkconfig: check service files (S_ISREG, S_IXUSR) where appropriate.

* Mon Oct 28 2002 Stanislav Ievlev <inger@altlinux.ru> 1.2.24-alt3
- rebuild with gcc3

* Tue Feb 05 2002 Stanislav Ievlev <inger@altlinux.ru> 1.2.24-alt2
- dropped MDK color patch
- added patch for installers

* Sat Jan 26 2002 Dmitry V. Levin <ldv@altlinux.org> 1.2.24-alt1
- 1.2.24, redone patches, updated russian translations.
- Linked chkconfig utility dynamically with libpopt.

* Sun Feb 11 2001 Dmitry V. Levin <ldv@fandra.org> 1.2.19-ipl1mdk
- 1.2.19 (bugfixes).

* Wed Dec 27 2000 Dmitry V. Levin <ldv@fandra.org> 1.2.17-ipl2mdk
- Fixed two segvs.

* Sun Dec 10 2000 Dmitry V. Levin <ldv@fandra.org> 1.2.17-ipl1mdk
- 1.2.17.
- xinetd support patch.

* Wed Sep 20 2000 Dmitry V. Levin <ldv@fandra.org> 1.2.12-ipl1mdk
- 1.2.12 (from RH).
- Fixes (from MDK).
- Automatically added BuildRequires.

* Mon Jun 26 2000 Dmitry V. Levin <ldv@fandra.org> 1.1.4-ipl1mdk
- 1.1.4
- use FHS-compatible macros.

* Tue May 30 2000 Geoffrey Lee <snailtalk@linux-mandrake.com> 1.0.8-9mdk
- patch: doesn't update runlevel stuff if you are not root

* Fri Apr 14 2000 Yoann Vandoorselaere <yoann@mandrakesoft.com> 1.0.8-8mdk
- Change printf on secure level error to reflect the new msec location.

* Fri Mar 24 2000 Frederic Lepied <flepied@mandrakesoft.com> 1.0.8-7mdk
- group fix.

* Wed Mar 08 2000 Yoann Vandoorselaere <yoann@mandrakesoft.com>
- Modified the msec patch to use the new filesystem hierarchy used by msec.
  %name will no use /etc/security/msec/server.[45]
- Require msec 0.10

* Thu Dec 30 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Add standard mandrake colors.

* Thu Nov 25 1999 Yoann Vandoorselaere <yoann@mandrakesoft.com>
- Added the --msec option, used when called from
  Mandrake Security scripts.

* Thu Nov 25 1999 Yoann Vandoorselaere <yoann@mandrakesoft.com>
- Oops, fixed a little problem.

* Thu Nov 25 1999 Yoann Vandoorselaere <yoann@mandrakesoft.com>
- Hacked %name to interoperate with Mandrake security package.

* Tue Nov  2 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- 1.0.8.

* Tue Oct 19 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Build Release.

* Fri Oct  1 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- 1.0.7

* Fri Aug 06 1999 Pablo Saratxaga <pablo@mandrakesoft.com>
- corrected indonesian language code (it has changed from 'in' to 'id')

* Thu Apr 29 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Mandrake adaptations.

* Mon Apr 19 1999 Cristian Gafton <gafton@redhat.com>
- release for Red Hat 6.0

* Thu Apr  8 1999 Matt Wilson <msw@redhat.com>
- added support for a "hide: true" tag in initscripts that will make
  services not appear in ntsysv when run with the "--hide" flag

* Thu Apr  1 1999 Matt Wilson <msw@redhat.com>
- added --hide flag for ntsysv that allows you to hide a service from the
  user.

* Mon Mar 22 1999 Bill Nottingham <notting@redhat.com>
- fix glob, once and for all. Really. We mean it.

* Thu Mar 18 1999 Bill Nottingham <notting@redhat.com>
- revert fix for services@levels, it's broken
- change default to only edit the current runlevel

* Mon Mar 15 1999 Bill Nottingham <notting@redhat.com>
- don't remove scripts that don't support %name

* Tue Mar 09 1999 Erik Troan <ewt@redhat.com>
- made glob a bit more specific so xinetd and inetd don't cause improper matches

* Thu Feb 18 1999 Matt Wilson <msw@redhat.com>
- removed debugging output when starting ntsysv

* Thu Feb 18 1999 Preston Brown <pbrown@redhat.com>
- fixed globbing error
- fixed ntsysv running services not at their specified levels.

* Tue Feb 16 1999 Matt Wilson <msw@redhat.com>
- print the value of errno on glob failures.

* Sun Jan 10 1999 Matt Wilson <msw@redhat.com>
- rebuilt for newt 0.40 (ntsysv)

* Tue Dec 15 1998 Jeff Johnson <jbj@redhat.com>
- add ru.po.

* Thu Oct 22 1998 Bill Nottingham <notting@redhat.com>
- build for Raw Hide (slang-1.2.2)

* Wed Oct 14 1998 Cristian Gafton <gafton@redhat.com>
- translation updates

* Thu Oct 08 1998 Cristian Gafton <gafton@redhat.com>
- updated czech translation (and use cs instead of cz)

* Tue Sep 22 1998 Arnaldo Carvalho de Melo <acme@conectiva.com.br>
- added pt_BR translations
- added more translatable strings
- support for i18n init.d scripts description

* Sun Aug 02 1998 Erik Troan <ewt@redhat.com>
- built against newt 0.30
- split ntsysv into a separate package

* Thu May 07 1998 Erik Troan <ewt@redhat.com>
- added numerous translations

* Mon Mar 23 1998 Erik Troan <ewt@redhat.com>
- added i18n support

* Sun Mar 22 1998 Erik Troan <ewt@redhat.com>
- added --back
