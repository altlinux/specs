Name: sed
Version: 4.2.1
Release: alt3
Epoch: 1

Summary: A GNU stream text editor
Group: Editors
License: GPLv3+
Url: http://www.gnu.org/software/sed/

%define srcname %name-%version-%release
# git://git.altlinux.org/people/ldv/packages/sed refs/heads/sed-current
Source0: %srcname.tar
# git://git.altlinux.org/people/ldv/packages/sed refs/heads/po-current
Source1: po-%version-%release.tar
Source2: subst.tar
# git://git.altlinux.org/people/ldv/packages/sed sed-current..sed-alt
Patch: %srcname.patch

%def_enable selinux

BuildRequires: gnulib >= 0.0.6780.bfacc22

# for acl copying support.
BuildRequires: libacl-devel

%{?_enable_selinux:BuildRequires: libselinux-devel}

%description
The sed (Stream EDitor) editor is a stream or batch (non-interactive)
editor.  Sed takes text as input, performs an operation or set of
operations on the text and outputs the modified text.  The operations
that sed performs (substitutions, deletions, insertions, etc.) can be
specified in a script file or from the command line.

%prep
%setup -n %srcname -a1 -a2
%patch -p1

# Build scripts expect to find coreutils version in this file.
echo -n %version-%release > .tarball-version

# Fix "gettext infrastructure mismatch" error.
sed -i 's/^\(AM_GNU_GETTEXT_VERSION\).*/\1('"$(gettext --version | sed -n 's/^gettext.* \([0-9][^ ]*\)$/\1/p')"')/' configure.ac

# Generate LINGUAS file.
ls po/*.po 2>/dev/null |
	sed 's|.*/||; s|\.po$||' >po/LINGUAS

# Compress docs for packaging.
bzip2 -9 doc/*.txt
bzip2 -9k NEWS

%build
%make_build -C subst
./subst/subst -p 's,@DOCDIR@,%_docdir/%name-%version,' \
	doc/sed-in.texi doc/sed.x

./autoboot --skip-po --gnulib-srcdir=%_datadir/gnulib
%configure --bindir=/bin --without-included-regex %{subst_enable selinux}
%make_build -C po update-po
%make_build

%install
%makeinstall_std
%makeinstall_std -C subst

%check
%make_build -k check

%find_lang %name

%files -f %name.lang
/bin/*
%_bindir/*
%_mandir/man?/*
%_infodir/*.info*
%doc BUGS NEWS.bz2 README THANKS doc/*.txt.bz2

%changelog
* Thu Jan 19 2012 Dmitry V. Levin <ldv@altlinux.org> 1:4.2.1-alt3
- Updated sed to 4.2.1-42-g727d6fa.
- Updated translations from translationproject.org.
- Changed build to use external gnulib package.

* Wed Aug 18 2010 Dmitry V. Levin <ldv@altlinux.org> 1:4.2.1-alt2
- sed: updated to 4.2.1-18-ge1c76b0.
- gnulib: updated to v0.0-4045-gafc6cbe.
- Updated translations from translationproject.org.
- subst: rewritten using "sed -i --follow-symlinks".
- sed: enabled SELinux support.

* Wed Sep 09 2009 Dmitry V. Levin <ldv@altlinux.org> 1:4.2.1-alt1
- Updated sed to 4.2.1
- Updated gnulib to current.
- Moved "make check" to %%check section.

* Sun Jun 07 2009 Dmitry V. Levin <ldv@altlinux.org> 1:4.2-alt1
- Updated to 4.2 (closes: #19889).
- Enabled acl copying support.
- Removed explicit provides.
- Removed obsolete %%install_info/%%uninstall_info calls.

* Tue Apr 10 2007 Dmitry V. Levin <ldv@altlinux.org> 1:4.1.5-alt2
- Applied upstream utf8 performance fix.

* Fri Feb 10 2006 Dmitry V. Levin <ldv@altlinux.org> 1:4.1.5-alt1
- Updated sed to 4.1.5
- Updated sed1line.txt to version 5.5
- Corrected sedfaq.txt (#8682).
- Fixed compilation warnings.

* Wed Mar 02 2005 Dmitry V. Levin <ldv@altlinux.org> 1:4.1.4-alt2
- Updated to cvs snapshot 20050210.

* Sun Jan 30 2005 Dmitry V. Levin <ldv@altlinux.org> 1:4.1.4-alt1
- Updated to 4.1.4

* Wed Jan 19 2005 Dmitry V. Levin <ldv@altlinux.org> 1:4.1.2-alt3
- Corrected ed(1) manpage.

* Mon Jan 03 2005 Dmitry V. Levin <ldv@altlinux.org> 1:4.1.2-alt2
- Applied fixes from Debian:
  + fix \l and \u replacement modifier bug;
  + fix it.po segfault.

* Sun Sep 12 2004 Dmitry V. Levin <ldv@altlinux.org> 1:4.1.2-alt1
- Updated sed to 4.1.2
- Updated sed1line.txt to version 5.4

* Mon Aug 09 2004 Dmitry V. Levin <ldv@altlinux.org> 1:4.1.1-alt1
- Updated to 4.1.1

* Fri Jun 25 2004 Dmitry V. Levin <ldv@altlinux.org> 1:4.0.9-alt2
- Removed Provides added in 1:3.02-alt2 release.
- Use bundled subst during build (#4490).

* Tue Mar 02 2004 Dmitry V. Levin <ldv@altlinux.org> 1:4.0.9-alt1
- Updated to 4.0.9
- Updated patches.
- Added the sed FAQ.

* Thu Oct 31 2002 Dmitry V. Levin <ldv@altlinux.org> 1:3.02-alt2
- Provides: %name = 0:3.02-ipl12mdk.

* Wed Aug 28 2002 Dmitry V. Levin <ldv@altlinux.org> 1:3.02-alt1
- Minor specfile cleanup; changed release numbering.
- Additional convention enforcement on patch file names.
- Implemented and added to this package: %_bindir/subst.
- Removed stale URLs from documentation (rh).
- Added run of testcase after build.

* Mon Mar 04 2002 Stanislav Ievlev <inger@altlinux.ru> 3.02-ipl11mdk
- Rebuilt.

* Tue Jan 16 2001 Dmitry V. Levin <ldv@fandra.org> 3.02-ipl10mdk
- RE adaptions.
- Fixed texinfo documentation.

* Thu Jul 27 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 3.02-10mdk
- BM
- let spechelper compress info & manpages
- remove packager tag

* Sun Jun 18 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 3.02-9mdk
- Use makeinstall macros.

* Thu Apr 13 2000 Enzo Maggi <enzo@mandrakesoft.com> 3.02-8mdk
- Changed group, little fixes in the spec.

* Tue Oct 26 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Build release.

* Sat Apr 10 1999 Bernhard Rosenkraenzer <bero@linux-mandrake.com>
- Mandrake adaptions
- bzip2 man/info pages
- add de locale

* Tue Aug 18 1998 Jeff Johnson <jbj@redhat.com>
- update to 3.02

* Sun Jul 26 1998 Jeff Johnson <jbj@redhat.com>
- update to 3.01

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Oct 23 1997 Donnie Barnes <djb@redhat.com>
- removed references to the -g option from the man page that we add

* Fri Oct 17 1997 Donnie Barnes <djb@redhat.com>
- spec file cleanups
- added BuildRoot

* Mon Jun 02 1997 Erik Troan <ewt@redhat.com>
- built against glibc
