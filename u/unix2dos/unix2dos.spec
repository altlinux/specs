Summary: unix2dos - UNIX to DOS text file format converter
Name: unix2dos
Version: 2.2
Release: alt1
License: distributable
Group: Text tools
Source: %name-%version.src.tar.gz
Patch0: %name-mkstemp.patch
Patch1: %name-%version-segfault.patch
Patch2: %name-%version-manpage.patch
Patch3: %name-%version-mode.patch
Patch4: %name-%version-tmppath.patch

%description
A utility that converts plain text files in UNIX format to DOS format.

%prep
%setup -q -c
%patch -p1 -b .sec
%patch1 -p1 -b .segf
%patch2 -p1 -b .man
%patch3 -p1 -b .mode
%patch4 -p1 -b .tmppath

for I in *.[ch]; do
    %__subst -p 's,#endif.*,#endif,g' $I
    %__subst -p 's,#else.*,#else,g' $I
done

%build
%__cc -Wall $RPM_OPT_FLAGS -o %name %name.c

%install
%__mkdir_p %buildroot/{%_bindir,%_man1dir}
%__install -m755 %name %buildroot/%_bindir
%__install -m755 %name.1 %buildroot/%_man1dir

%files
%doc COPYRIGHT
%_bindir/%name
%_man1dir/*

%changelog
* Fri Apr 27 2007 Serhii Hlodin <hlodin@altlinux.ru> 2.2-alt1
- Initial release 

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 2.2-26.2.2
- rebuild

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 2.2-26.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 2.2-26.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Wed Apr 13 2005 Tim Waugh <twaugh@redhat.com>
- Merge last fix into tmppath patch, which introduced the original problem.

* Tue Apr 12 2005 Tim Waugh <twaugh@redhat.com> 2.2-26
- Removed inappropriate strcpy (bug #153079).  Patch from Neil Horman.

* Thu Mar  3 2005 Mike A. Harris <mharris@redhat.com> 2.2-25
- Rebuild with gcc 4 for FC4

* Wed Oct 20 2004 Miloslav Trmac <mitr@redhat.com> 2.2-24
- Don't just delete the original file when destination and current directory
  are on different filesystems 

* Mon Oct 11 2004 Tim Waugh <twaugh@redhat.com> 2.2-23
- Apply H J Lu's patch to preserve file mode (bug #91332).

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Mon Oct  7 2002 Mike A. Harris <mharris@redhat.com> 2.2-18
- All-arch rebuild

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Tue Mar  5 2002 Bernhard Rosenkraenzer <bero@redhat.com> 2.2-15
- rebuild

* Thu Jan 17 2002 Bernhard Rosenkraenzer <bero@redhat.com> 2.2-14
- Fix up the mkstemp patch, don't segfault with lacking write permissions
  (#57700)
- Fix up man page (part 2 of #57700)
- Fix compiler warnings

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Sun Jun 24 2001 Elliot Lee <sopwith@redhat.com>
- Bump release + rebuild.

* Fri Nov 17 2000 Tim Powers <timp@redhat.com>
- patched to use mkstemp, not much had to be done.

* Thu Nov 16 2000 Tim Powers <timp@redhat.com>
- minor spec file cleanups
- built for 7.1
- use predefined RPM macros whenever possible
- use RPM_OPT_FLAGS when building

* Tue Jul 07 1999 Peter Soos <sp@osb.hu> 
- Added Hungarian "Summary:" and "%description" 
- Corrected the file and directory attributes to rebuild the package 
  under RedHat Linux 6.0 
 
* Thu Jul 09 1998 Arkadiusz Mikkkkkkiewicz <misiek@misiek.eu.org> 
- Recompiled under RedHat Linux 5.1 
- Small changes in %build and %files 
- Added "Vendor:" 
- Added Polish "Summary:" and "%description" 
 
* Thu Jun 18 1998 Peter Soos <sp@osb.hu> 
- Corrected the spec file for rpm 2.5 
 
* Fri Dec 5 1997 Peter Soos <sp@osb.hu> 
- Recompiled under RedHat Linux 5.0
