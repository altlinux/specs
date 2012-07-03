Summary: Text file format converter
Name: dos2unix
Version: 3.1
Release: alt1
Group: Text tools
License: Freely distributable
Source: %name-%version.tar.bz2
Patch0: %name-%version.patch
Patch1: %name-%version-segfault.patch
Patch2: %name-%version-safeconv.patch
Patch3: %name-%version-manpage-update-57507.patch
Patch4: %name-%version-preserve-file-modes.patch
Patch5: %name-%version-tmppath.patch

%description
%name converts DOS or MAC text files to UNIX format.

%prep
%setup -q
%patch0 -p1 -b .orig
%patch1 -p1 -b .segfault
%patch2 -p1 -b .safeconv
%patch3 -p1 -b .manpage-update-57507
%patch4 -p1 -b .preserve-file-modes
%patch5 -p1 -b .tmppath

for I in *.[ch]; do
    %__subst -p 's,#endif.*,#endif,g' $I
    %__subst -p 's,#else.*,#else,g' $I
done

%build
%make clean
%make_build CFLAGS="$RPM_OPT_FLAGS -D_LARGEFILE_SOURCE $(getconf LFS_CFLAGS)"
%make link

%install
%__mkdir_p %buildroot/{%_bindir,%_man1dir}
%__install -m755 %name %buildroot/%_bindir
%__install -m755 mac2unix %buildroot/%_bindir
%__install -m444 %name.1 %buildroot/%_man1dir
%__install -m444 mac2unix.1 %buildroot/%_man1dir

%files
%doc COPYRIGHT
%_bindir/%name
%_bindir/mac2unix
%_man1dir/*

%changelog
* Fri Apr 27 2007 Serhii Hlodin <hlodin@altlinux.ru> 3.1-alt1
- Initial build

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 3.1-27.1
- rebuild

* Mon Jul 10 2006 Tim Waugh <twaugh@redhat.com> 3.1-27
- Re-encoded spec file in UTF-8 (bug #197817).

* Mon Jun  5 2006 Tim Waugh <twaugh@redhat.com> 3.1-26
- Rebuilt.

* Thu Jun  1 2006 Tim Waugh <twaugh@redhat.com> 3.1-25
- Build with large file support.

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 3.1-24.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 3.1-24.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Wed Apr 13 2005 Tim Waugh <twaugh@redhat.com> 3.1-24
- Fixed tmppath patch (bug #150277).

* Thu Mar  3 2005 Mike A. Harris <mharris@redhat.com> 3.1-23
- Bump and rebuild for FC4, using gcc 4.

* Tue Feb  8 2005 Mike A. Harris <mharris@redhat.com> 3.1-22
- Bump and rebuild for FC4

* Wed Oct 20 2004 Miloslav Trmac <mitr@redhat.com> - 3.1-21
- Don't just delete the original file when destination and current directory
  are on different filesystems (#65548, #123069, patch by James Antill)
- Fix return type of StripDelimiter in dos2unix-3.1-safeconv.patch (#136148)

* Wed Oct  6 2004 Mike A. Harris <mharris@redhat.com> 3.1-20
- Added dos2unix-3.1-manpage-update-57507.patch to fix manpage (#57507)
- Added dos2unix-3.1-preserve-file-modes.patch to properly preserve file
  permissions (#91331,55183,112710,132145)

* Sun Sep 26 2004 Rik van Riel <riel@redhat.com> 3.1-19
- safer conversion w/ mac2unix (fix from bz #57508)

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Feb 05 2003 Elliot Lee <sopwith@redhat.com> 3.1-15
- Remove build dependency on perl, since perl BuildRequires: dos2unix,
  and there's no good reason not to just use sed here.

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Mon Oct  7 2002 Mike A. Harris <mharris@redhat.com> 3.1-13
- All-arch rebuild
- Added BuildRequires: perl

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu Feb 28 2002 Trond Eivind Glomsrød <teg@redhat.com> 3.1-10
- Build in new environment

* Thu Jan 17 2002 Bernhard Rosenkraenzer <bero@redhat.com>
- Fix bug #57700 (segfault)
- Add the mac2unix symlink recommended in README
- Fix compiler warnings

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Sun Jun 24 2001 Elliot Lee <sopwith@redhat.com>
- Bump release + rebuild.

* Wed Jan 10 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- shut up rpmlint

* Fri Nov 17 2000 Tim Powers <timp@redhat.com>
- use mkstemp instead of mktemp. Not much needed to change.

* Thu Nov 16 2000 Tim Powers <timp@redhat.com>
- cleaned up specfile a bit
- built for 7.1

* Tue Jul 07 1999 Peter Soos <sp@osb.hu> 
- Added Hungarian "Summary:" and "%description" 
- Corrected the file and directory attributes to rebuild the package 
  under RedHat Linux 6.0
