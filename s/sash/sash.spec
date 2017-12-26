Name: sash
Version: 3.4
Release: alt2.qa2
Epoch: 1

Summary: A statically linked shell, including some built-in basic commands
License: distributable
Group: Shells
Url: http://www.canb.auug.org.au/~dbell/programs/
Packager: Dmitry V. Levin <ldv@altlinux.org>

Source: sash-%version.tar
Patch: sash-3.4-alt.patch

Requires: terminfo

# Automatically added by buildreq on Sat Jun 29 2002
BuildRequires: libe2fs-devel libreadline-devel-static libtinfo-devel-static zlib-devel-static

%description
Sash is a simple, standalone, statically linked shell which includes
simplified versions of built-in commands like ls, dd and gzip.  Sash
is statically linked so that it can work without shared libraries, so
it is particularly useful for recovering from certain types of system
failures.  Sash can also be used to safely upgrade to new versions of
shared libraries.

%prep
%setup -q
%patch -p1
fgrep -C1 Permission sash.h >copyright

%build
%make_build

%install
%makeinstall sbindir=%buildroot/sbin

%files
/sbin/*
%_mandir/man?/*
%doc copyright

%changelog
* Tue Dec 26 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 1:3.4-alt2.qa2
- Fixed build:
  + with glibc 2.26;
  + on architectures without SIGSTKFLT signal (e.g. mips*).

* Fri Apr 19 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1:3.4-alt2.qa1
- NMU: rebuilt for debuginfo.

* Wed Sep 24 2008 Dmitry V. Levin <ldv@altlinux.org> 1:3.4-alt2
- Use ext2fs/ext2_fs.h instead of linux/ext2_fs.h for build.

* Wed Apr 23 2008 Dmitry V. Levin <ldv@altlinux.org> 1:3.4-alt1
- Updated release numbering.

* Fri May 13 2005 ALT QA Team Robot <qa-robot@altlinux.org> 3.4-ipl11mdk.1
- Rebuilt with glibc-devel-static-2.3.5-alt2.

* Wed May 11 2005 Dmitry V. Levin <ldv@altlinux.org> 3.4-ipl11mdk
- Rebuilt with glibc-2.3.5-alt1.

* Mon Nov 18 2002 Stanislav Ievlev <inger@altlinux.ru> 3.4-ipl10mdk
- rebuild, new version will be after distro release

* Sat Jun 29 2002 Dmitry V. Levin <ldv@altlinux.org> 3.4-ipl9mdk
- Patched to link with libtinfo.

* Tue Feb 12 2002 Dmitry V. Levin <ldv@alt-linux.org> 3.4-ipl8mdk
- Updated buildrequires.

* Mon Jan 14 2002 Dmitry V. Levin <ldv@alt-linux.org> 3.4-ipl7mdk
- Fixed losetup builtin.

* Tue Jan 08 2002 Stanislav Ievlev <inger@altlinux.ru> 3.4-ipl6mdk
- fixed permissions for manual pages (bug #0000303)

* Sat Nov 25 2000 Dmitry V. Levin <ldv@fandra.org> 3.4-ipl5mdk
- Rewritten completely readline support
  (original was unusable beacause of bugs).
- Various fixes.
- Enhanced error reporting.
- Merged patches into one file.

* Thu Aug 24 2000 Dmitry V. Levin <ldv@fandra.org> 3.4-ipl4mdk
- Added readline support
  (by Valery Kornienkov <vlk@dimavb.st.simbirsk.su>).

* Thu Jun 22 2000 Dmitry V. Levin <ldv@fandra.org> 3.4-ipl3mdk
- RE adaptions.

* Sat Mar 25 2000 Pixel <pixel@mandrakesoft.com> 3.4-3mdk
- new group

* Mon Mar 13 2000 Pixel <pixel@mandrakesoft.com> 3.4-2mdk
- new version

* Mon Feb 07 2000 Preston Brown <pbrown@redhat.com>
- rebuild to gzip man page

* Mon Oct 04 1999 Cristian Gafton <gafton@redhat.com>
- rebuild against new glibc in the sparc tree

* Mon Aug  2 1999 Jeff Johnson <jbj@redhat.com>
- upgrade to 3.3 (#4301).

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 4)

* Wed Feb 24 1999 Preston Brown <pbrown@redhat.com>
- Injected new description and group.

* Fri Dec 18 1998 Preston Brown <pbrown@redhat.com>
- bumped spec number for initial rh 6.0 build
