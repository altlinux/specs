Name: time
Version: 1.7
Release: alt2
Epoch: 1

Summary: The GNU time program for measuring system resource usage
License: GPLv2+
Group: Monitoring
Packager: Dmitry V. Levin <ldv@altlinux.org>

# ftp://ftp.gnu.org/gnu/time/time-%version.tar.gz
Source: time-%version.tar
Patch: time-%version-%release.patch

%description
The GNU time command runs another program, then displays information
about the resources used by that program, collected by the system while
the program was running.  You can select which information is reported
and the format in which it is shown, or have `time' save the information
in a file instead of display it on the screen.

The resources that `time' can report on fall into the general categories
of time, memory, I/O, and IPC calls.

The GNU version can format the output in arbitrary ways by using a
printf-style format string to include various resource measurements.

%prep
%setup -q
%patch -p1

%build
%autoreconf

%configure
%make_build

%install
%makeinstall_std

%files
%_bindir/*
%_infodir/*.info*
%doc AUTHORS NEWS README

%changelog
* Sun May 17 2009 Dmitry V. Levin <ldv@altlinux.org> 1:1.7-alt2
- Removed obsolete %%install_info/%%uninstall_info calls.

* Sat Apr 07 2007 Dmitry V. Levin <ldv@altlinux.org> 1:1.7-alt1
- Patched to use glibc getopt and error facilities.
- Added --quiet option based on patch from Debian.
- Dropped RH shutup patch.

* Fri Feb 27 2004 Stanislav Ievlev <inger@altlinux.org> 1.7-ipl22mdk
- fix building with new autotools

* Tue Jun 17 2003 Stanislav Ievlev <inger@altlinux.ru> 1.7-ipl21mdk
- fix building in bte.

* Tue Oct 22 2002 Stanislav Ievlev <inger@altlinux.ru> 1.7-ipl20mdk
- rebuild with gcc3

* Thu Feb 21 2002 Stanislav Ievlev <inger@altlinux.ru> 1.7-ipl19mdk
- added shut up patch from RH
- turn of linking with getopt, error and getopt1 to reduce program size

* Fri Dec 05 2001 Konstantin Volckov <goldhead@altlinux.ru> 1.7-ipl18mdk
- Rebuild for Sisyphus
- Added patch1 from Mandrake

* Thu Dec 14 2000 Dmitry V. Levin <ldv@fandra.org> 1.7-ipl17mdk
- Fixed texinfo documentation.

* Wed Aug  2 2000 Dmitry V. Levin <ldv@fandra.org> 1.7-ipl16mdk
- RE adaptions.

* Wed Apr 05 2000 John Buswell <johnb@mandrakesoft.com> 1.7-13mdk
- fixed vendor tag

* Thu Mar 30 2000 John Buswell <johnb@mandrakesoft.com> 1.7-12mdk
- Fixed group
- spec-helper

* Tue Oct 26 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Build release.

* Sat Apr 10 1999 Bernhard Rosenkraenzer <bero@linux-mandrake.com>
- Mandrake adaptions
- bzip2 man/info pages
- add de locale

* Mon Aug 10 1998 Erik Troan <ewt@redhat.com>
- buildrooted and defattr'd

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Mon Oct 27 1997 Cristian Gafton <gafton@redhat.com>
- fixed info handling

* Thu Oct 23 1997 Cristian Gafton <gafton@redhat.com>
- updated the spec file; added info file handling

* Mon Jun 02 1997 Erik Troan <ewt@redhat.com>
- built against glibc
