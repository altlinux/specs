Name: unarj
Version: 2.65
Release: alt3

Summary: An uncompressor for .arj format archive files
Group: Archiving/Compression
License: distributable
URL: http://www.arjsoftware.com/files.htm#unarj
Packager: Alexey Voinov <voins@altlinux.ru>

Source: ftp://ibiblio.org/pub/Linux/utils/compress/%name-%version.tar.bz2
Patch0: %name-%version-time.diff
Patch1: %name-%version-overflow.diff
Patch2: %name-%version-path.diff
Patch3: %name-%version-notice.diff
Patch4: %name-2.63c-iconv.patch

%description
The UNARJ program is used to uncompress .arj format archives.
The .arj format archive was mostly used on DOS machines.

%prep
%setup -q
%patch0
%patch1
%patch2
%patch3
%patch4

%define _optlevel 3

%build
make clean
%make_build clean %name CFLAGS="$RPM_OPT_FLAGS -DUNIX"

%install
install -p -m755 -D %name $RPM_BUILD_ROOT%_bindir/%name

%files
%_bindir/*
%doc {%name,technote}.txt

%changelog
* Mon Jun 15 2009 Alexey Voinov <voins@altlinux.ru> 2.65-alt3
- url fixed

* Thu Oct 20 2005 Alexey Voinov <voins@altlinux.ru> 2.65-alt2
-  iconv patch heavily based on same patch for unzip
   by Dmitry Vukolov <dav@altlinux.org>

* Fri Jan 21 2005 Michael Shigorin <mike@altlinux.ru> 2.65-alt1
- 2.65 (security fixes):
  * Fixed table boundaries
  * Added additional header data checks
  * Added chapter and encryption information
- added SuSE patches (mjancar suse cz):
- CAN-2004-0947: buffer overflow
- CAN-2004-1027: directory traversal
- version notice patch regarding these fixes

* Mon Sep 30 2002 Stanislav Ievlev <inger@altlinux.ru> 2.63a-alt1
- 2.63a

* Fri Dec 05 2001 Konstantin Volckov <goldhead@altlinux.ru> 2.43-ipl14mdk
- Rebuild for Sisyphus
- Added O3 optimization

* Sat Dec 09 2000 Dmitry V. Levin <ldv@fandra.org> 2.43-ipl13mdk
- RE adaptions.

* Mon Jul 31 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 2.43-13mdk
- BM

* Sun Apr 02 2000 Jerome Martin <jerome@mandrakesoft.com> 2.43-12mdk
- Fixed group entry
- Specfile cleanup (spec-helper etc.)

* Sun Oct 31 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- SMP check/build

* Wed May 05 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Mandrake adaptions

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 9)

* Thu Dec 17 1998 Michael Maher <mike@redhat.com>
- built package for 6.0

* Tue Aug 11 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Oct 22 1997 Otto Hammersmith <otto@redhat.com>
- fixed src url

* Fri Jul 18 1997 Erik Troan <ewt@redhat.com>
- built against glibc
