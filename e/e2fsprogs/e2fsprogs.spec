Name: e2fsprogs
Version: 1.43.7
Release: alt1

Summary: The filesystem utilities for the ext2/ext3 filesystems
License: GPLv2
Group: System/Kernel and hardware
Url: http://e2fsprogs.sourceforge.net/

# git://git.altlinux.org/people/ldv/packages/e2fsprogs.git
Source: %name-%version-%release.tar

%def_enable static
%def_disable libblkid
%def_disable libuuid
%def_disable fsck

Requires: libcom_err = %version-%release
Requires: libe2fs = %version-%release
Requires: libss = %version-%release
%{!?_enable_fsck:Requires: /sbin/fsck}
%{!?_enable_libblkid:BuildRequires: libblkid-devel}
%{!?_enable_libuuid:BuildRequires: libuuid-devel}
%{?_enable_libblkid:Requires: libblkid = %version-%release}
%{?_enable_libuuid:Requires: libuuid = %version-%release}
BuildRequires: makeinfo

%description
This package contains a number of utilities for creating, checking,
modifying and correcting any inconsistencies in EXT2 filesystems.

# libe2p, libext2fs
%package -n libe2fs
Summary: Dynamic ext2/ext3 filesystem libraries
License: LGPLv2
Group: System/Libraries
Conflicts: %name < %version-%release
Requires: libcom_err = %version-%release

%description -n libe2fs
This package contains the shared libraries required by
EXT2/EXT3 filesystem-specific programs.

%package -n libe2fs-devel
Summary: Development ext2/ext3 filesystem libraries and include files
License: LGPLv2
Group: Development/C
Provides: %name-devel = %version
Obsoletes: %name-devel
Requires: libe2fs = %version-%release
%{?_enable_libblkid:Requires: libblkid-devel = %version-%release}
%{?_enable_libuuid:Requires: libuuid-devel = %version-%release}
Requires: libcom_err-devel = %version-%release
Requires: libss-devel = %version-%release

%description -n libe2fs-devel
This package contains the libraries and include files needed to develop
EXT2/EXT3 filesystem-specific programs.

%package -n libe2fs-devel-static
Summary: Static ext2/ext3 filesystem libraries
License: LGPLv2
Group: Development/C
Conflicts: %name-devel < %version
Requires: libe2fs-devel = %version-%release
%{?_enable_libblkid:Requires: libblkid-devel-static = %version-%release}
%{?_enable_libuuid:Requires: libuuid-devel-static = %version-%release}
Requires: libcom_err-devel-static = %version-%release
Requires: libss-devel-static = %version-%release

%description -n libe2fs-devel-static
This package contains the static libraries needed to develop statically
linked EXT2/EXT3 filesystem-specific programs.

# libblkid
%package -n libblkid
Summary: Dynamic block device id library
License: LGPLv2
Group: System/Libraries
Conflicts: %name < %version-%release, libe2fs < %version-%release
%{?_enable_libuuid:Requires: libuuid = %version-%release}

%description -n libblkid
The blkid library which allows system programs like fsck and mount to
quickly and easily find block devices by filesystem UUID and LABEL.

%package -n libblkid-devel
Summary: Development block device id library and include files
License: LGPLv2
Group: Development/C
Provides: %name-devel = %version
Obsoletes: %name-devel
Requires: libblkid = %version-%release

%description -n libblkid-devel
This package contains the library and include files needed to develop
libblkid-based software.

%package -n libblkid-devel-static
Summary: Static block device id library
License: LGPLv2
Group: Development/C
Requires: libblkid-devel = %version-%release
Conflicts: %name-devel < %version, libe2fs-devel < %version-%release
Requires: libuuid-devel-static = %version-%release

%description -n libblkid-devel-static
This package contains the library and include files needed to develop
statically linked libblkid-based software.

# libcom_err
%package -n libcom_err
Summary: Dynamic common error description library
License: MIT-style
Group: System/Libraries
Conflicts: %name < %version-%release, libe2fs < %version-%release

%description -n libcom_err
The com_err library is an attempt to present a common error-handling
mechanism to manipulate the most common form of error code in a fashion
that does not have the problems identified with mechanisms commonly
in use.

%package -n libcom_err-devel
Summary: Development common error description library and include files
License: MIT-style
Group: Development/C
Provides: %name-devel = %version
Obsoletes: %name-devel
Requires: libcom_err = %version-%release

%description -n libcom_err-devel
This package contains the library and include files needed to develop
libcom_err-based software.

%package -n libcom_err-devel-static
Summary: Static common error description library
License: MIT-style
Group: Development/C
Requires: libcom_err-devel = %version-%release
Conflicts: %name-devel < %version, libe2fs-devel < %version-%release

%description -n libcom_err-devel-static
This package contains the library and include files needed to develop
statically linked libcom_err-based software.

# libss
%package -n libss
Summary: Dynamic command-line interface parsing library
License: MIT-style
Group: System/Libraries
Conflicts: %name < %version-%release, libe2fs < %version-%release
Requires: libcom_err = %version-%release

%description -n libss
This package contains the library that parses a command table to generate
a simple command-line interface parser.

%package -n libss-devel
Summary: Development command-line interface parsing library and include files
License: MIT-style
Group: Development/C
Provides: %name-devel = %version
Obsoletes: %name-devel
Requires: libss = %version-%release
Requires: libcom_err-devel = %version-%release

%description -n libss-devel
This package contains the library and include files needed to develop
libss-based software.

%package -n libss-devel-static
Summary: Static command-line interface parsing library
License: MIT-style
Group: Development/C
Conflicts: %name-devel < %version, libe2fs-devel < %version-%release
Requires: libss-devel = %version-%release
Requires: libcom_err-devel-static = %version-%release

%description -n libss-devel-static
This package contains the library and include files needed to develop
statically linked libss-based software.

# libuuid
%package -n libuuid
Summary: Dynamic universally unique id library
License: BSD-style
Group: System/Libraries
Conflicts: %name < %version-%release, libe2fs < %version-%release

%description -n libuuid
The uuid library generates and parses 128-bit universally unique id's
(UUID's).  See RFC 4122 for more information.

%package -n libuuid-devel
Summary: Development universally unique id library and include files
License: BSD-style
Group: Development/C
Provides: %name-devel = %version
Obsoletes: %name-devel
Requires: libuuid = %version-%release

%description -n libuuid-devel
This package contains the library and include files needed to develop
libuuid-based software.

%package -n libuuid-devel-static
Summary: Static universally unique id library
License: BSD-style
Group: Development/C
Requires: libuuid-devel = %version-%release
Conflicts: %name-devel < %version, libe2fs-devel < %version-%release

%description -n libuuid-devel-static
This package contains the library and include files needed to develop
statically linked libuuid-based software.

%prep
%setup -n %name-%version-%release

find -type f -print0 |
	xargs -r0 grep -lZ '^static void usage' -- |
	xargs -r0 sed -i 's/^static void usage/__attribute__ ((noreturn)) &/' --

# Remove these header files just in case.
rm -r include

mv tests/m_no_opt/expect.1{,.ext2}
mv tests/m_no_opt/expect.1{.tmpfs,}

%build
%add_optflags -D_LARGEFILE64_SOURCE -fno-strict-aliasing
# e2fsprogs's LD=$CC breaks autoconf test
export acl_cv_prog_gnu_ld=yes
autoconf
%configure \
	--sbindir=/sbin \
	--disable-uuidd \
	--enable-nls \
	--enable-elf-shlibs \
	%{subst_enable libblkid} \
	%{subst_enable libuuid} \
	%{subst_enable fsck} \
	#

%make_build V=1

%install
mkdir -p %buildroot{/%_lib,%_includedir/e2p}

%makeinstall_std install-libs V=1

ln -snf et/com_err.h %buildroot%_includedir/

sed -i 's,^ET_DIR=.*$,ET_DIR=%_datadir/et,' %buildroot%_bindir/compile_et
sed -i 's,^SS_DIR=.*$,SS_DIR=%_datadir/ss,' %buildroot%_bindir/mk_cmds

mv %buildroot%_libdir/e2initrd_helper %buildroot/sbin/

# Relocate shared libraries from %_libdir/ to /%_lib/.
for f in %buildroot%_libdir/*.so; do
	t=$(readlink "$f")
	ln -snf ../../%_lib/"$t" "$f"
done
mv %buildroot%_libdir/*.so.* %buildroot/%_lib/

# Get rid of duplicate files.
for i in ext2 ext3 ext4 ext4dev; do
	ln -snf e2fsck %buildroot/sbin/fsck.$i
	ln -snf e2fsck.8 %buildroot%_man8dir/fsck.$i.8

	ln -snf mke2fs %buildroot/sbin/mkfs.$i
	ln -snf mke2fs.8 %buildroot%_man8dir/mkfs.$i.8
done

# Prepare docs.
xz -9 RELEASE-NOTES
chmod -R a+rX,go-w %buildroot%_mandir

%find_lang %name

# Ensure that buildroot did not get info installed files.
! fgrep -rl %buildroot %buildroot

%check
rm -r tests/r_64bit_big_expand tests/r_ext4_big_expand
%ifarch %ix86
rm -r tests/r_1024_small_bg
%endif
export PATH=/sbin:/usr/sbin:/bin:/usr/bin
%make_build -k check V=1 && exit ||:
mv tests/m_no_opt/expect.1{,.tmpfs}
mv tests/m_no_opt/expect.1{.ext2,}
%make_build -k check V=1

%files -f %name.lang
%config(noreplace) %_sysconfdir/*.conf
/sbin/*
%_bindir/*attr
%_man1dir/*attr.*
%if_enabled libuuid
%_bindir/uuidgen
%_man1dir/uuidgen.*
%endif # libuuid
%_man5dir/*
%_man8dir/*
%doc README RELEASE*

# libe2p, libext2fs
%files -n libe2fs
/%_lib/libe2p.so.*
/%_lib/libext2fs.so.*

%files -n libe2fs-devel
%_pkgconfigdir/e2p.pc
%_libdir/libe2p.so
%_includedir/e2p
%_pkgconfigdir/ext2fs.pc
%_libdir/libext2fs.so
%_includedir/ext2fs
%_infodir/*.info*

%files -n libe2fs-devel-static
%_libdir/libe2p.a
%_libdir/libext2fs.a

%if_enabled libblkid
# libblkid
%files -n libblkid
/%_lib/libblkid.so.*

%files -n libblkid-devel
%_pkgconfigdir/blkid.pc
%_libdir/libblkid.so
%_includedir/blkid
%_man3dir/libblkid*

%files -n libblkid-devel-static
%_libdir/libblkid.a
%endif # libblkid

# libcom_err
%files -n libcom_err
/%_lib/libcom_err.so.*

%files -n libcom_err-devel
%_pkgconfigdir/com_err.pc
%_libdir/libcom_err.so
%_includedir/et
%_includedir/com_err.h
%_man3dir/com_err*
%_datadir/et
%_bindir/compile_et
%_man1dir/compile_et*

%files -n libcom_err-devel-static
%_libdir/libcom_err.a

# libss
%files -n libss
/%_lib/libss.so.*

%files -n libss-devel
%_pkgconfigdir/ss.pc
%_libdir/libss.so
%_includedir/ss
%_datadir/ss
%_bindir/mk_cmds
%_man1dir/mk_cmds*

%files -n libss-devel-static
%_libdir/libss.a

%if_enabled libuuid
# libuuid
%files -n libuuid
/%_lib/libuuid.so.*
%doc lib/uuid/COPYING

%files -n libuuid-devel
%_pkgconfigdir/uuid.pc
%_libdir/libuuid.so
%_includedir/uuid
%_man3dir/uuid*

%files -n libuuid-devel-static
%_libdir/libuuid.a
%endif # libuuid

%changelog
* Sun Nov 26 2017 Dmitry V. Levin <ldv@altlinux.org> 1.43.7-alt1
- v1.43.4-36-ge251f35 -> v1.43.7.

* Thu May 18 2017 Dmitry V. Levin <ldv@altlinux.org> 1.43.4.0.36.e251-alt1
- v1.42.13-18-g19961cd -> v1.43.4-36-ge251f35 (closes: #33489).

* Wed Dec 02 2015 Dmitry V. Levin <ldv@altlinux.org> 1.42.13-alt2
- Updated to maint v1.42.13-18-g19961cd.

* Tue Nov 17 2015 Dmitry V. Levin <ldv@altlinux.org> 1.42.13-alt1
- Updated to maint v1.42.13-9-gb9ba837.

* Sat Sep 21 2013 Dmitry V. Levin <ldv@altlinux.org> 1.42.8-alt1
- Updated to v1.42.8.

* Fri Mar 08 2013 Dmitry V. Levin <ldv@altlinux.org> 1.42.7-alt1
- Updated to v1.42.7.

* Sat Oct 06 2012 Dmitry V. Levin <ldv@altlinux.org> 1.42.6-alt1
- Updated to v1.42.6.

* Wed Sep 12 2012 Dmitry V. Levin <ldv@altlinux.org> 1.42.5-alt1
- Updated to v1.42.5-7-gab3f5c5.

* Tue May 22 2012 Dmitry V. Levin <ldv@altlinux.org> 1.42.3-alt1
- Updated to v1.42.3-2-g108e658.

* Thu Mar 29 2012 Dmitry V. Levin <ldv@altlinux.org> 1.42.2-alt1
- Updated to v1.42.2 (closes: #27134).

* Sun Mar 25 2012 Dmitry V. Levin <ldv@altlinux.org> 1.42.1-alt1
- Updated to v1.42.1-15-g800766e.

* Sat Oct 29 2011 Dmitry V. Levin <ldv@altlinux.org> 1.42-alt0.1
- Updated to v1.42-WIP-1016 (closes: #26528).

* Sat Feb 05 2011 Dmitry V. Levin <ldv@altlinux.org> 1.41.14-alt1
- Updated to v1.41.14-136-g2696f25.

* Wed Oct 13 2010 Dmitry V. Levin <ldv@altlinux.org> 1.41.12-alt2
- Updated to maint v1.41.12-46-g73fbe23.

* Tue Aug 17 2010 Dmitry V. Levin <ldv@altlinux.org> 1.41.12-alt1
- Updated to maint v1.41.12-34-g61ef247.

* Tue Mar 02 2010 Dmitry V. Levin <ldv@altlinux.org> 1.41.10-alt1
- Updated to maint v1.41.10-2-g4ffafee (closes: #22988).
- Added dependence on /sbin/fsck (closes: #22562).

* Fri Nov 13 2009 Dmitry V. Levin <ldv@altlinux.org> 1.41.9-alt3
- Updated to maint v1.41.9-37-g6eb229d.
- Disabled fsck, libblkid and libuuid.

* Wed Sep 09 2009 Dmitry V. Levin <ldv@altlinux.org> 1.41.9-alt2
- Updated to maint v1.41.9-14-g51e6459.
- Moved "make check" to %%check section.

* Thu Sep 03 2009 Dmitry V. Levin <ldv@altlinux.org> 1.41.9-alt1
- Updated to maint v1.41.9-4-g8bafedb.

* Thu Jul 16 2009 Dmitry V. Levin <ldv@altlinux.org> 1.41.8-alt1
- Updated to maint v1.41.8-6-g25c7e0c.

* Tue Jun 30 2009 Dmitry V. Levin <ldv@altlinux.org> 1.41.7-alt1
- Updated to maint v1.41.7.

* Sun May 31 2009 Dmitry V. Levin <ldv@altlinux.org> 1.41.6-alt1
- Updated to maint v1.41.6.

* Tue May 19 2009 Dmitry V. Levin <ldv@altlinux.org> 1.41.5-alt2
- libblkid-devel: Removed unneeded dependence on libuuid-devel.
- Removed obsolete %%install_info/%%uninstall_info calls.

* Tue May 19 2009 Dmitry V. Levin <ldv@altlinux.org> 1.41.5-alt1

* Tue May 12 2009 Dmitry V. Levin <ldv@altlinux.org> 1.41.5-alt1
- Updated to maint v1.41.5-10-g5fdb89e.

* Wed Jan 28 2009 Dmitry V. Levin <ldv@altlinux.org> 1.41.4-alt1
- Updated to maint v1.41.4.

* Wed Dec 03 2008 Dmitry V. Levin <ldv@altlinux.org> 1.41.3-alt1
- Updated to maint v1.41.3-13-g8680b4e.

* Mon Jan 28 2008 Dmitry V. Levin <ldv@altlinux.org> 1.40.5-alt1
- Updated to maint v1.40.5.

* Tue Jan 01 2008 Dmitry V. Levin <ldv@altlinux.org> 1.40.4-alt1
- Updated to maint v1.40.4.

* Wed Dec 19 2007 Dmitry V. Levin <ldv@altlinux.org> 1.40.3-alt1
- Updated to maint v1.40.3-12-g740837d.

* Thu Dec 06 2007 Dmitry V. Levin <ldv@altlinux.org> 1.40.2-alt2
- Updated to maint v1.40.2-33-g1113bf7.
- libext2fs: Added checks to prevent integer overflows
  (Rafal Wojtczuk, CVE-2007-5497).

* Thu Oct 18 2007 Dmitry V. Levin <ldv@altlinux.org> 1.40.2-alt1
- Updated to maint v1.40.2-26-gf305918.

* Mon Apr 09 2007 Dmitry V. Levin <ldv@altlinux.org> 1.39-alt4
- blkid library:
  + Updated to e2fsprogs-1.40-WIP-2007-04-11.
  + Fixed RAID support (vsu, #11419).

* Sun Apr 01 2007 Dmitry V. Levin <ldv@altlinux.org> 1.39-alt3
- Changed packaging scheme to use .gear-tags.
- Imported Owl patches (tmp.diff, blkid-env.diff).
- Moved blkid, com_err, ss and uuid libraries from libe2fs package
  to separate sibpackages; also move -devel counterparts.
- Set correct libuuid License tag (#6685)
- Dropped ChangeLog* files, RELEASE-NOTES should be enough.
- Updated blkid library to e2fsprogs-1.40-WIP-1114-2.
- Changed blkid library to skip hidden (.*) names (#11133).
- Built blkid library with devmapper support (#11133).

* Tue Jun 06 2006 Dmitry V. Levin <ldv@altlinux.org> 1.39-alt2
- Deal with compilation warnings generated by new gcc compiler.

* Tue May 30 2006 Dmitry V. Levin <ldv@altlinux.org> 1.39-alt1
- Updated to 1.39 release.

* Mon May 29 2006 Dmitry V. Levin <ldv@altlinux.org> 1.39-alt0.3
- Updated to 1.39 test snapshot 2006.04.09.

* Thu Mar 30 2006 Dmitry V. Levin <ldv@altlinux.org> 1.39-alt0.2
- Updated to 1.39 test snapshot 2006.03.30.

* Thu Feb 09 2006 Dmitry V. Levin <ldv@altlinux.org> 1.39-alt0.1
- Updated to 1.39 test snapshot 2005.12.31.
- Reviewed and updated patches.

* Thu Feb 02 2006 ALT QA Team Robot <qa-robot@altlinux.org> 1.37-alt2.1
- Rebuilt for new pkg-config dependencies.

* Sun Apr 03 2005 Dmitry V. Levin <ldv@altlinux.org> 1.37-alt2
- e2fsck:
  + allowed -p/-a options along with -y/-n again, see #6388.
  + preenhalt: do not stop when -y option is used.

* Wed Mar 30 2005 Dmitry V. Levin <ldv@altlinux.org> 1.37-alt1
- Updated to 1.37.
- Applied fixes from Owl package.
- Dropped the "notitle" patch.
- E2fsck will (again) print a warning (not an error this time)
  if more than one of the -p/-a, -n or -y options are specified.

* Wed Feb 09 2005 Dmitry V. Levin <ldv@altlinux.org> 1.36-alt1
- Updated to 1.36.
- Removed merged upstream patches:
  + alt-check_if_skip
- Updated patches:
  + alt-notitle
- Fixed multilib (closes #4879).
- Dropped evms-plugins-e2fsim subpackage.
- Dropped obsolete e2compr documentation.

* Mon Apr 12 2004 Dmitry V. Levin <ldv@altlinux.org> 1.35-alt2
- Fixed false "check after next mount" warning.

* Tue Mar 09 2004 Dmitry V. Levin <ldv@altlinux.org> 1.35-alt1
- Updated to 1.35.
- Removed obsolete pacthes:
  1.23-rh-autoconf
- Removed merged upstream patches:
  1.34-alt-fixes
- Updated patches:
  alt-notitle

* Thu Oct 30 2003 Dmitry V. Levin <ldv@altlinux.org> 1.34-alt2
- Reverted the following change to e2fsck-1.33:
  E2fsck will print an error if more than one of the -p/-a, -n
  or -y options are specified.

* Wed Oct 29 2003 Dmitry V. Levin <ldv@altlinux.org> 1.34-alt1
- Updated to 1.34.
- Removed obsolete pacthes:
  1.18-mdk-alt-fsck-loop
  1.18-rh-et
- Updated patches:
  alt-notitle
  alt-fixes
  alt-texinfo

* Thu Nov 21 2002 Dmitry V. Levin <ldv@altlinux.org> 1.32-alt1
- Updated to 1.32.

* Mon Nov 04 2002 Dmitry V. Levin <ldv@altlinux.org> 1.30-alt1
- Updated to 1.30.
- Following patches merged upstream:
  rh-mountlabel3
  alt-fixes (partial)
  owl-alt-lost+found-mode

* Wed Oct 09 2002 Dmitry V. Levin <ldv@altlinux.org> 1.29-alt2
- Fixed texinfo documentation.
- Added a patch for the permissions on lost+found (Owl).

* Fri Sep 27 2002 Dmitry V. Levin <ldv@altlinux.org> 1.29-alt1
- 1.29

* Mon Sep 09 2002 Dmitry V. Levin <ldv@altlinux.org> 1.28-alt1
- 1.28

* Tue Sep 03 2002 Dmitry V. Levin <ldv@altlinux.org> 1.27-alt2
- Use subst instead of perl for build.
- Updated %post/%postun scripts.
- Updated devel-static requirements.

* Fri Mar 22 2002 Dmitry V. Levin <ldv@alt-linux.org> 1.27-alt1
- 1.27

* Sat Mar 16 2002 Dmitry V. Levin <ldv@alt-linux.org> 1.26-alt2
- Resurrected notitle patch (lost somehow since 1.19-ipl3mdk release).
- Fixed dependencies, summaries and descriptions.
- Fixed various compilation warnings.
- Added necessary ext3 symlinks.
- Build e2fsck dynamically.
- Repackaged docs.

* Thu Feb 28 2002 Konstantin Volckov <goldhead@altlinux.ru> 1.26-alt1
- 1.26

* Tue Nov 28 2001 Konstantin Volckov <goldhead@altlinux.ru> 1.25-alt1
- 1.25
- Added some RH and MDK patches.
- Fixed %description's

* Thu Sep 20 2001 Konstantin Volckov <goldhead@altlinux.ru> 1.24a-alt1
- 1.24a

* Wed Jan 17 2001 Dmitry V. Levin <ldv@fandra.org> 1.19-ipl3mdk
- Create tmpfiles in more secure way.
- Added some "__progname" enhancements.
- Split into %name, libe2fs and libe2fs-devel subpackages.

* Fri Oct 13 2000 Dmitry V. Levin <ldv@fandra.org> 1.19-ipl2mdk
- Added mountlabel patch.

* Wed Aug  2 2000 Dmitry V. Levin <ldv@fandra.org> 1.19-ipl1mdk
- Updated:
  + new release 1.19
  + e2compr patch.
- Added: ext2 resize.

* Mon May 29 2000 Dmitry V. Levin <ldv@fandra.org> 1.18.9-ipl5mdk
- RE adaptions.

* Sat May 20 2000 Dmitry V. Levin <ldv@fandra.org> 1.18.9-5mdk.ldv
- Merged MDK changes.

* Sun Apr  2 2000 Dmitry V. Levin <ldv@fandra.org> 1.18.9-4mdk.mdk
- Merged RH patches.

* Tue Mar 28 2000 Dmitry V. Levin <ldv@fandra.org> 1.18.9-3mdk.ldv
- rpm-3.0.4

* Tue Mar 21 2000 Pixel <pixel@mandrakesoft.com> 1.18-3mdk
- patch for long device names and option -C (usefull for loopback)

* Sat Mar 11 2000 Pixel <pixel@mandrakesoft.com> 1.18-2mdk
- patch for adding ability to say "-t loop" or "-t noloop", looking in the fstab
  mount options

* Sun Feb  6 2000 Dmitry V. Levin <ldv@fandra.org>
- e2cfsprogs-9-patch-1.18

* Wed Nov 03 1999 Dmitry V. Levin <ldv@fandra.org>
- e2compr code and documentation
- optimal manpage compression
- Fandra adaptions

* Wed Oct 27 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- 1.17.

* Wed Oct 20 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- update mke2fs man page so that it reflects changes in mke2fs
  netweem 1.14 and 1.15.

* Fri Aug 13 1999 Thierry Vignaud <tvignaud@mandrakesoft.com>
- bzip2 info

* Wed Jul 21 1999 Thierry Vignaud <tvignaud@mandrakesoft.com>
- Updated to 1.15
- Added french description

* Wed Jun 23 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>

- Add e2fsprog-shared in the %files
 (proposed by H.J. Lu <hjl@varesearch.com>).

* Sat Apr 10 1999 Bernhard Rosenkraenzer <bero@linux-mandrake.com>
- Mandrake adaptions
- bzip2 man pages
- add de locale
- fix up description (you need %name in any case... Installing a
  system without e2fsck is definately stupid)
- add e2compression support

* Tue Mar 16 1999 Cristian Gafton <gafton@redhat.com>
- fix fsck segfault

* Tue Feb  2 1999 Jeff Johnson <jbj@redhat.com>
- update to 1.14
- use %configure to generate config.sub on arm

* Thu Jan 14 1999 Jeff Johnson <jbj@redhat.com>
- fix /usr/bin/compile_et and doco for com_err.h (#673)

* Thu Jan 07 1999 Cristian Gafton <gafton@redhat.com>
- build with prefix=/usr
- add arm patch

* Mon Dec 28 1998 Jeff Johnson  <jbj@redhat.com>
- update to 1.13.

* Fri Aug 28 1998 Jeff Johnson <jbj@redhat.com>
- recompile statically linked binary for 5.2/sparc

* Mon Jul 13 1998 Jeff Johnson <jbj@redhat.com>
- upgrade to 1.12.

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Apr 30 1998 Cristian Gafton <gafton@redhat.com>
- include <asm/types.h> to match kernel types in utils

* Tue Oct 14 1997 Donnie Barnes <djb@redhat.com>
- spec file cleanups

* Wed Oct 01 1997 Erik Troan <ewt@redhat.com>
- fixed broken llseek() prototype

* Wed Aug 20 1997 Erik Troan <ewt@redhat.com>
- added patch to prototype llseek

* Tue Jun 17 1997 Erik Troan <ewt@redhat.com>
- built against glibc
