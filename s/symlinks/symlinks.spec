Name: symlinks
Version: 1.4
Release: alt1.1
Epoch: 1

Summary: A utility which maintains a system's symbolic links
License: Copyright only
Group: File tools
Url: http://www.ibiblio.org/pub/Linux/utils/file/

# http://ibiblio.org/pub/Linux/utils/file/%name-%version.tar.gz
Source: %name-%version.tar
# http://packages.debian.org/changelogs/pool/main/s/symlinks/symlinks_1.2-4.2/symlinks.copyright
Source1: symlinks-LICENSE.txt
Patch1: symlinks-coverity-readlink.patch
Patch2: symlinks-coverity-overrun-dynamic.patch

%description
The symlinks utility performs maintenance on symbolic links.  Symlinks
checks for symlink problems, including dangling symlinks which point to
nonexistent files.  Symlinks can also automatically convert absolute
symlinks to relative symlinks.

%prep
%setup
%patch1 -p1
%patch2 -p1
install -pm644 %SOURCE1 .

%build
%make_build CFLAGS="%optflags $(getconf LFS_CFLAGS)"

%install
install -Dpm755 symlinks %buildroot%_bindir/symlinks
install -Dpm644 symlinks.8 %buildroot%_man1dir/symlinks.1

%files
%_bindir/*
%_man1dir/*
%doc symlinks-LICENSE.txt

%changelog
* Thu Mar 15 2018 Igor Vlasenko <viy@altlinux.ru> 1:1.4-alt1.1
- NMU: added URL

* Wed Apr 17 2013 Dmitry V. Levin <ldv@altlinux.org> 1:1.4-alt1
- Updated to 1.4, synced patches with Fedora.

* Wed Apr 23 2008 Dmitry V. Levin <ldv@altlinux.org> 1:1.2-alt1
- Merged fixes from FC and Debian symlinks packages.
- Updated release numbering.

* Sun Oct 13 2002 Rider <rider@altlinux.ru> 1.2-ipl12mdk
- Russian summary
- rebuild (gcc 3.2)

* Mon Apr 15 2002 Rider <rider@altlinux.ru> 1.2-ipl11mdk
- rebuild

* Fri Jan 19 2001 Dmitry V. Levin <ldv@fandra.org> 1.2-ipl10mdk
- Merged RH patches.
- RE adaptions.

* Wed Jul 26 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.2-10mdk
- use tmppath

* Thu Jul 20 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.2-9mdk
- let spec-helper compress, strip and the like
- BM, macros

* Thu Mar 23 2000 Daouda Lo <daouda@mandrakesoft.com> 1.2-8mdk
- fix group for 7.1

* Tue Nov 30 1999 Florent Villard <warly@mandrakesoft.com>
- built in new environment
- clean Makefile

* Wed May 05 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Mandrake adaptions
- handle RPM_OPT_FLAGS

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 5)

* Wed Feb 24 1999 Preston Brown <pbrown@redhat.com>
- Injected new description and group.

* Fri Dec 18 1998 Preston Brown <pbrown@redhat.com>
- bumped spec number for initial rh 6.0 build

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Mon Oct 20 1997 Otto Hammersmith <otto@redhat.com>
- changed build root to /var/tmp, not /var/lib
- updated to version 1.2

* Wed Jul 09 1997 Erik Troan <ewt@redhat.com>
- built against glibc
- build-rooted
