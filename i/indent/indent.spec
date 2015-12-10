Name: indent
Version: 2.2.11
Release: alt3

Summary: A GNU program for formatting C code
License: GPLv3+
Group: Development/C
Url: http://indent.isidore-it.eu/beautify.html

# http://indent.isidore-it.eu/%name-%version.tar.gz
Source: %name-%version.tar

Patch1: indent-2.2.11-alt-i18n.patch
Patch2: indent-2.2.11-alt-man.patch
Patch3: indent-2.2.11-deb-texinfo.patch
Patch4: indent-2.2.11-alt-lfs.patch
Patch5: indent-2.2.11-rh-Do-not-split-decimal-float-suffix-from-constant.patch
Patch6: indent-2.2.11-rh-Return-non-zero-exit-code-on-tests-failure.patch
Patch7: indent-2.2.11-rh-Fix-compiler-warnings.patch
Patch8: indent-2.2.11-rh-Allow-64-bit-stat.patch
Patch9: indent-2.2.11-rh-Fix-copying-overlapping-comment.patch
Patch10: indent-2.2.11-rh-Support-hexadecimal-floats.patch
Patch11: indent-2.2.11-rh-Modernize-texi2html-arguments.patch
Patch12: indent-2.2.11-rh-doc-Correct-a-typo-about-enabling-control-comment.patch
Patch13: indent-2.2.11-rh-Fix-nbdfa-and-nbdfe-typo.patch

BuildRequires: gperf makeinfo

%description
Indent is a GNU program for formatting C code so that it is easier to
read.  Indent can also convert from one C writing style to a different
one.  This can be helpful when porting code to various 'odd' platforms.
Indent has a limited understanding of C syntax, but tries its best to
handle things properly.

%prep
%setup
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
rm src/gperf*.c
rm po/*.gmo
sed -i 's/^\(all-local\|install-data-local\):.*/\1:/' doc/Makefile.*

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std
rm %buildroot%_bindir/texinfo2man
%find_lang %name

%check
make -C regression

%files -f %name.lang
%_bindir/indent
%_mandir/man?/*.*
%_infodir/*.info*
%doc AUTHORS ChangeLog NEWS README

%changelog
* Thu Dec 10 2015 Dmitry V. Levin <ldv@altlinux.org> 2.2.11-alt3
- Merged fixes from Fedora indent-2.2.11-19.

* Fri Apr 19 2013 Dmitry V. Levin <ldv@altlinux.org> 2.2.11-alt2
- Merged fixes from Fedora.
- Enabled LFS support.
- Enabled regression testing during build.

* Thu Oct 07 2010 Dmitry V. Levin <ldv@altlinux.org> 2.2.11-alt1
- Updated to 2.2.11 (closes: #19289).

* Mon Nov 09 2009 Dmitry V. Levin <ldv@altlinux.org> 2.2.9-alt6
- Remove obsolete %%install_info/%%uninstall_info calls.

* Fri Apr 13 2007 Dmitry V. Levin <ldv@altlinux.org> 2.2.9-alt5
- Uncompressed tarball.

* Sun Dec 11 2005 Dmitry V. Levin <ldv@altlinux.org> 2.2.9-alt4
- Updated URL (fixes #8553).
- Imported texinfo2man fix from Debian.

* Tue Jan 06 2004 Dmitry V. Levin <ldv@altlinux.org> 2.2.9-alt3
- Added a missing call to check_lab_size() in src/indent.c (deb).

* Tue Sep 09 2003 Dmitry V. Levin <ldv@altlinux.org> 2.2.9-alt2
- Fixed SMP build.
- Fixed build with -Werror.

* Mon Feb 24 2003 Dmitry V. Levin <ldv@altlinux.org> 2.2.9-alt1
- Updated to 2.2.9
- Removed mdk-texinfo2man patch (merged upstream).

* Mon Sep 23 2002 Dmitry V. Levin <ldv@altlinux.org> 2.2.8-alt4
- Updated buildrequires.

* Tue Sep 17 2002 AEN <aen@altlinux.ru> 2.2.8-alt3
- rebuilt with gcc-3.2

* Wed Jul 03 2002 Dmitry V. Levin <ldv@altlinux.org> 2.2.8-alt2
- Fixed translations.

* Wed Jun 05 2002 Dmitry V. Levin <ldv@altlinux.org> 2.2.8-alt1
- 2.2.8
- Really run man/texinfo2man (mdk).

* Tue Jan 15 2002 Dmitry V. Levin <ldv@altlinux.org> 2.2.7-alt2
- Resurrected texinfo patch.

* Mon Jan 14 2002 Dmitry V. Levin <ldv@altlinux.org> 2.2.7-alt1
- 2.2.7

* Tue Nov 21 2000 Dmitry V. Levin <ldv@fandra.org> 2.2.6-ipl1mdk
- 2.2.6
- Fixed texinfo documentation.

* Mon Jun 26 2000 Dmitry V. Levin <ldv@fandra.org>
- 2.2.5
- RE adaptions.

* Wed Nov 10 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- 2.2.4.

* Fri Nov 5 1999 Damien Krotkine <damien@mandrakesoft.com>
- Mandrake release

* Sun Aug  1 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- 2.2.0

* Thu Jul 15 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>

- Insert PO-Traduction.
- 2.1.1

* Thu Jul 08 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- 2.1.0

* Tue May 11 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Mandrake adaptions
- handle RPM_OPT_FLAGS

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 11)

* Fri Dec 18 1998 Bill Nottingham <notting@redhat.com>
- build for 6.0 tree

* Thu Aug 13 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Tue Oct 21 1997 Otto Hammersmith <otto@redhat.com>
- use install-info

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc
