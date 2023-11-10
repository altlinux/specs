%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict,lint=relaxed

Name: musl
Version: 1.2.4
Release: alt2
Group: System/Libraries
Summary: Implementation of the C standard library
License: MIT
Url: https://musl.libc.org/
Vcs: https://git.musl-libc.org/git/musl

Source: %name-%version.tar
Patch3500: musl-20231008-loongarch.patch

%description
%summary.

%package libc
Summary: Shared library and dynamic linker for musl
Group: System/Libraries

%description libc
%summary.

%package devel
Summary: Development files for musl
Group: Development/C
Provides: musl-gcc = %EVR
AutoReq: nocpp
Requires: musl-libc = %EVR
Requires: kernel-headers-common

%description devel
musl is an implementation of the C standard library built on top of
the Linux system call API, including interfaces defined in the base
language standard, POSIX, and widely agreed-upon extensions. musl is
lightweight, fast, simple, free, and strives to be correct in the sense
of standards-conformance and safety.

%package devel-static
Summary: Static libraries for musl
Group: Development/C
Requires: musl-devel = %EVR

%description devel-static
%summary.

%package -n rpm-macros-musl
Summary: RPM macros to find musl libraries
Group: Development/Other

%description -n rpm-macros-musl
%summary. This should be rarely needed,
and is not required for normal builds.

%package checkinstall
Summary: CI tests for musl
Group: Development/Other
BuildArch: noarch
Requires(post): musl-devel-static = %EVR
Requires(post): clang
Requires(post): gcc
Requires(post): toilet

%description checkinstall
%summary.

%prep
%setup
%patch3500 -p1

# Use musl-fts from Debian.
mkdir -p src/fts
cp debian/musl-fts/fts.c debian/musl-fts/config.h src/fts/
cp debian/musl-fts/fts.h include/

%define _muslarch %_arch
%ifarch armh
%define _muslarch armhf
%endif
%ifarch ppc64le
%define _muslarch powerpc64le
%endif
%ifarch %ix86
%define _muslarch i386
%endif
%define ldname ld-musl-%_muslarch.so.1
%define ldpath ld-musl-%_muslarch.path
%define soname libc.so
%define _musldir %_prefix/%_lib/musl

%build
%define optflags_lto %nil
%global _libdir %_musldir/lib
%global _includedir %_musldir/include
%ifarch ppc64le
# [ppc64le] checking whether compiler's long double definition matches float.h... no
# [ppc64le] ./configure: error: unsupported long double type
# We set this via CC (and not CFLAGS) so it also pass into musl-gcc by default.
export CC='gcc -mlong-double-64'
%endif
%configure \
	--enable-debug \
	--enable-wrapper=all
%make_build

%install
%make_install DESTDIR=%buildroot install

# https://wiki.musl-libc.org/guidelines-for-distributions
#   "Most importantly [...] distributions should not change the dynamic
#   linker location to /lib64 or anything else, since this breaks ABI."
mkdir -p %buildroot/lib
ln -rs %buildroot%_libdir/%soname %buildroot/lib/%ldname
mkdir %buildroot%_sysconfdir
cat <<-EOF > %buildroot%_sysconfdir/%ldpath
	%_libdir
EOF

# UAPI headers.
rpm -ql kernel-headers-common | grep ^/usr/include/ |
	xargs -t ln -s -t %buildroot%_includedir

mkdir -p %buildroot%_rpmmacrosdir
cat > %buildroot%_rpmmacrosdir/musl <<-EOF
	%%_musl_libdir %_libdir
	%%_musl_includedir %_includedir
EOF

# Cannot be in %%pre.
install -Dp .gear/checkinstall %buildroot%_datadir/%name-checkinstall/_post

%check
grep 'ldso=' %buildroot%_bindir/ld.musl-clang
grep -Ex 'ldso="/lib/%ldname"' %buildroot%_bindir/ld.musl-clang

%post checkinstall -p %_datadir/%name-checkinstall/_post

%files libc
%doc COPYRIGHT
%_sysconfdir/%ldpath
/lib/%ldname
%dir %_musldir
%dir %_libdir
%_libdir/%soname

%files devel
%doc README WHATSNEW
%_bindir/*
%_musldir/*
%exclude %_musldir/lib/*.a
%exclude %_musldir/lib/%soname

%files devel-static
%_musldir/lib/*.a

%files -n rpm-macros-musl
%_rpmmacrosdir/musl

%files checkinstall
%_datadir/%name-checkinstall

%changelog
* Fri Nov 10 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 1.2.4-alt2
- NMU: support LoongArch architecture (added patch from
  https://www.openwall.com/lists/musl/2023/10/08/1)

* Thu Aug 10 2023 Vitaly Chikunov <vt@altlinux.org> 1.2.4-alt1
- Package re-created after deletion by ALT beekeeper (due to FTBFS).
- Update to v1.2.4 (2023-05-01), sync with upstream sources.
- Add checkinstall package with basic tests.
- (Fixes: CVE-2015-1817, CVE-2017-15650, CVE-2019-14697, CVE-2020-28928).
- Note: this is an experimental build and known to fail on some
  architecture/compiler cases. Basically, musl-gcc is most expected
  to work and especially for static linking.

* Tue Jul 01 2014 Led <led@altlinux.ru> 1.1.3-alt2
- fixes from upstream's SCM

* Thu Jun 26 2014 Led <led@altlinux.ru> 1.1.3-alt1
- 1.1.3

* Sun Jun 22 2014 Led <led@altlinux.ru> 1.1.2-alt8
- updates from upstream's SCM

* Sun Jun 22 2014 Led <led@altlinux.ru> 1.1.2-alt7
- fixes and updates from upstream's SCM

* Fri Jun 20 2014 Led <led@altlinux.ru> 1.1.2-alt6
- updates from upstream's SCM

* Thu Jun 19 2014 Led <led@altlinux.ru> 1.1.2-alt5
- fixes and updates from upstream's SCM

* Wed Jun 18 2014 Led <led@altlinux.ru> 1.1.2-alt4
- updates from upstream's SCM

* Sun Jun 15 2014 Led <led@altlinux.ru> 1.1.2-alt3
- fix missing argument to syscall in fanotify_mark

* Thu Jun 12 2014 Led <led@altlinux.ru> 1.1.2-alt2
- updates from upstream's SCM

* Sat Jun 07 2014 Led <led@altlinux.ru> 1.1.2-alt1
- 1.1.2

* Fri Jun 06 2014 Led <led@altlinux.ru> 1.1.1-alt3
- fixes from upstream's SCM

* Thu Jun 05 2014 Led <led@altlinux.ru> 1.1.1-alt2
- updates from upstream's SCM

* Wed May 21 2014 Led <led@altlinux.ru> 1.1.1-alt1
- 1.1.1

* Tue May 20 2014 Led <led@altlinux.ru> 1.1.0-alt10
- fix unhandled cases in strptime

* Tue May 20 2014 Led <led@altlinux.ru> 1.1.0-alt9
- fixes from upstream's SCM

* Fri May 09 2014 Led <led@altlinux.ru> 1.1.0-alt8
- fixed strftime %%s not to zero pad with default width=2

* Mon May 05 2014 Led <led@altlinux.ru> 1.1.0-alt7
- fixes from upstream's SCM
- reverted adding '-Wa,-mimplicit-it=thumb'

* Thu Apr 24 2014 Led <led@altlinux.ru> 1.1.0-alt6
- added '-Wa,-mimplicit-it=thumb' for arm* when ASMSUBARCH == hf (by sbolshakov@)

* Tue Apr 22 2014 Led <led@altlinux.ru> 1.1.0-alt5
- optimization from upstream's SCM

* Sun Apr 20 2014 Led <led@altlinux.ru> 1.1.0-alt4
- expose public execvpe interface

* Sat Apr 19 2014 Led <led@altlinux.ru> 1.1.0-alt3
- fixed false negatives with periodic needles in strstr, wcsstr, and memmem

* Fri Apr 18 2014 Led <led@altlinux.ru> 1.1.0-alt2
- updates from upstream's SCM
- added dummy '--verify' option when explicitly invoking dynamic loader

* Wed Apr 16 2014 Led <led@altlinux.ru> 1.1.0-alt1
- 1.1.0

* Tue Apr 15 2014 Led <led@altlinux.ru> 1.0.0-alt8
- fixes from upstream's SCM

* Thu Apr 10 2014 Led <led@altlinux.ru> 1.0.0-alt7
- fixed search past the end of haystack in memmem

* Wed Apr 09 2014 Led <led@altlinux.ru> 1.0.0-alt6
- fixes and updates from upstream's SCM

* Fri Apr 04 2014 Led <led@altlinux.ru> 1.0.0-alt5
- fixes and updates from upstream's SCM

* Tue Mar 25 2014 Led <led@altlinux.ru> 1.0.0-alt4
- fixes from upstream's SCM:
  + fix confstr return value

* Mon Mar 24 2014 Led <led@altlinux.ru> 1.0.0-alt3
- fixes and updates from upstream's SCM

* Sun Mar 23 2014 Led <led@altlinux.ru> 1.0.0-alt2
- removed GNU qsort_r

* Thu Mar 20 2014 Led <led@altlinux.ru> 1.0.0-alt1
- 1.0.0

* Wed Mar 19 2014 Led <led@altlinux.ru> 0.9.15-alt17
- fixes from upstream's SCM

* Mon Mar 17 2014 Led <led@altlinux.ru> 0.9.15-alt16
- fixes from upstream's SCM

* Mon Mar 10 2014 Led <led@altlinux.ru> 0.9.15-alt15
- fixes from upstream's SCM

* Wed Feb 26 2014 Led <led@altlinux.ru> 0.9.15-alt14
- fixes and updates from upstream's SCM

* Mon Feb 24 2014 Led <led@altlinux.ru> 0.9.15-alt13
- reverted for fix build on ARM

* Sun Feb 23 2014 Led <led@altlinux.ru> 0.9.15-alt12
- fixes and updates from upstream's SCM

* Tue Feb 18 2014 Led <led@altlinux.ru> 0.9.15-alt11
- fixes from upstream's SCM

* Fri Feb 14 2014 Led <led@altlinux.ru> 0.9.15-alt10
- fixes from upstream's SCM

* Wed Feb 12 2014 Led <led@altlinux.ru> 0.9.15-alt9
- fixes from upstream's SCM

* Tue Feb 11 2014 Led <led@altlinux.ru> 0.9.15-alt8
- fixes from upstream's SCM

* Mon Feb 10 2014 Led <led@altlinux.ru> 0.9.15-alt7
- fixes from upstream's SCM

* Fri Feb 07 2014 Led <led@altlinux.ru> 0.9.15-alt6
- fixes from upstream's SCM

* Thu Feb 06 2014 Led <led@altlinux.ru> 0.9.15-alt5
- fixes from upstream's SCM

* Sun Feb 02 2014 Led <led@altlinux.ru> 0.9.15-alt4
- fixes from upstream's SCM

* Tue Jan 21 2014 Led <led@altlinux.ru> 0.9.15-alt3
- fixes from upstream's SCM

* Thu Jan 09 2014 Led <led@altlinux.ru> 0.9.15-alt2
- fixes from upstream's SCM

* Wed Jan 08 2014 Led <led@altlinux.ru> 0.9.15-alt1
- 0.9.15

* Fri Dec 20 2013 Led <led@altlinux.ru> 0.9.14-alt33
- updated from upstream's SCM

* Thu Dec 19 2013 Led <led@altlinux.ru> 0.9.14-alt32
- fixes from upstream's SCM

* Fri Dec 13 2013 Led <led@altlinux.ru> 0.9.14-alt31
- updated from upstream's SCM

* Thu Dec 05 2013 Led <led@altlinux.ru> 0.9.14-alt30
- fixes from upstream's SCM

* Mon Dec 02 2013 Led <led@altlinux.ru> 0.9.14-alt29
- updated from upstream's SCM

* Sun Dec 01 2013 Led <led@altlinux.ru> 0.9.14-alt28
- updated from upstream's SCM

* Thu Nov 28 2013 Led <led@altlinux.ru> 0.9.14-alt27
- fixes from upstream's SCM

* Wed Nov 27 2013 Led <led@altlinux.ru> 0.9.14-alt26
- fixes from upstream's SCM

* Tue Nov 26 2013 Led <led@altlinux.ru> 0.9.14-alt25
- updated from upstream's SCM

* Sun Nov 24 2013 Led <led@altlinux.ru> 0.9.14-alt24
- updated from upstream's SCM

* Sun Nov 17 2013 Led <led@altlinux.ru> 0.9.14-alt23
- fixed getgrnam_r() and getgrgid_r()

* Thu Nov 14 2013 Led <led@altlinux.ru> 0.9.14-alt22
- fixed soname

* Wed Nov 13 2013 Led <led@altlinux.ru> 0.9.14-alt21
- init '__environ' (ALT#29579)

* Tue Nov 12 2013 Led <led@altlinux.ru> 0.9.14-alt20
- fixes from upstream's SCM

* Mon Nov 11 2013 Led <led@altlinux.ru> 0.9.14-alt19
- fixes and updates from upstream's SCM

* Tue Nov 05 2013 Led <led@altlinux.ru> 0.9.14-alt18
- fixes from upstream's SCM

* Sun Nov 03 2013 Led <led@altlinux.ru> 0.9.14-alt17
- netinet/if_ether.h: removed definitions defined in linux/if_ether.h

* Sun Nov 03 2013 Led <led@altlinux.ru> 0.9.14-alt16
- fixes from upstream's SCM

* Sat Nov 02 2013 Led <led@altlinux.ru> 0.9.14-alt15
- fixes from upstream's SCM

* Wed Oct 30 2013 Led <led@altlinux.ru> 0.9.14-alt14
- fixes from upstream's SCM

* Tue Oct 29 2013 Led <led@altlinux.ru> 0.9.14-alt13
- updated from upstream's SCM

* Sat Oct 26 2013 Led <led@altlinux.ru> 0.9.14-alt12
- updated from upstream's SCM

* Tue Oct 22 2013 Led <led@altlinux.ru> 0.9.14-alt11
- fixes from upstream's SCM

* Sun Oct 20 2013 Led <led@altlinux.ru> 0.9.14-alt10
- fixes from upstream's SCM

* Mon Oct 14 2013 Led <led@altlinux.ru> 0.9.14-alt9
- fixes from upstream's SCM

* Fri Oct 11 2013 Led <led@altlinux.ru> 0.9.14-alt8
- updated from upstream's SCM

* Sun Oct 06 2013 Led <led@altlinux.ru> 0.9.14-alt7
- fixes from upstream's SCM

* Thu Oct 03 2013 Led <led@altlinux.ru> 0.9.14-alt6
- fixes from upstream's SCM

* Mon Sep 30 2013 Led <led@altlinux.ru> 0.9.14-alt5
- added symlink to kernel mtd includes

* Sun Sep 29 2013 Led <led@altlinux.ru> 0.9.14-alt4
- added GNU qsort_r(3)

* Sun Sep 29 2013 Led <led@altlinux.ru> 0.9.14-alt3
- fixes from upstream's SCM

* Sun Sep 29 2013 Led <led@altlinux.ru> 0.9.14-alt2
- fixes from upstream's SCM

* Fri Sep 27 2013 Led <led@altlinux.ru> 0.9.14-alt1
- 0.9.14

* Fri Sep 20 2013 Led <led@altlinux.ru> 0.9.13-alt7
- fixes from upstream's SCM

* Wed Sep 18 2013 Led <led@altlinux.ru> 0.9.13-alt6
- fixes from upstream's SCM

* Sat Sep 14 2013 Led <led@altlinux.ru> 0.9.13-alt5
- fixes from upstream's SCM

* Tue Sep 10 2013 Led <led@altlinux.ru> 0.9.13-alt4
- fixes from upstream's SCM

* Sat Sep 07 2013 Led <led@altlinux.ru> 0.9.13-alt3
- updated from upstream's SCM

* Tue Sep 03 2013 Led <led@altlinux.ru> 0.9.13-alt2
- fixes from upstream's SCM

* Sun Sep 01 2013 Led <led@altlinux.ru> 0.9.13-alt1
- 0.9.13

* Thu Aug 29 2013 Led <led@altlinux.ru> 0.9.12-alt14
- updated from upstream's SCM

* Wed Aug 28 2013 Led <led@altlinux.ru> 0.9.12-alt13
- updated from upstream's SCM

* Tue Aug 27 2013 Led <led@altlinux.ru> 0.9.12-alt12
- updated from upstream's SCM

* Wed Aug 21 2013 Led <led@altlinux.ru> 0.9.12-alt11
- fixes from upstream's SCM

* Sun Aug 18 2013 Led <led@altlinux.ru> 0.9.12-alt10
- updated from upstream's SCM

* Wed Aug 14 2013 Led <led@altlinux.ru> 0.9.12-alt9
- updated from upstream's SCM

* Sun Aug 11 2013 Led <led@altlinux.ru> 0.9.12-alt8
- fixes and updates from upstream's SCM

* Thu Aug 08 2013 Led <led@altlinux.ru> 0.9.12-alt7
- fixes and updates from upstream's SCM

* Sun Aug 04 2013 Led <led@altlinux.ru> 0.9.12-alt6
- fixes and updates from upstream's SCM

* Thu Aug 01 2013 Led <led@altlinux.ru> 0.9.12-alt5
- fixes from upstream's SCM

* Wed Jul 31 2013 Led <led@altlinux.ru> 0.9.12-alt4
- updated from upstream's SCM

* Tue Jul 30 2013 Led <led@altlinux.ru> 0.9.12-alt3
- fixes from upstream's SCM

* Mon Jul 29 2013 Led <led@altlinux.ru> 0.9.12-alt2
- Revert "remove soname from libc.so/ld-musl"

* Mon Jul 29 2013 Led <led@altlinux.ru> 0.9.12-alt1
- 0.9.12

* Mon Jul 22 2013 Led <led@altlinux.ru> 0.9.11-alt10
- updated from upstream's SCM

* Thu Jul 18 2013 Led <led@altlinux.ru> 0.9.11-alt9
- updated from upstream's SCM

* Mon Jul 15 2013 Led <led@altlinux.ru> 0.9.11-alt8
- fixes from upstream's SCM

* Thu Jul 11 2013 Led <led@altlinux.ru> 0.9.11-alt7
- fix invalid library phdr pointers passed to callback from dl_iterate_phdr

* Tue Jul 09 2013 Led <led@altlinux.ru> 0.9.11-alt6
- updated from upstream's SCM

* Sun Jul 07 2013 Led <led@altlinux.ru> 0.9.11-alt5
- updated from upstream's SCM

* Sat Jul 06 2013 Led <led@altlinux.ru> 0.9.11-alt4
- updated from upstream's SCM

* Thu Jul 04 2013 Led <led@altlinux.ru> 0.9.11-alt3
- updated from upstream's SCM

* Tue Jul 02 2013 Led <led@altlinux.ru> 0.9.11-alt2
- updated from upstream's SCM

* Mon Jul 01 2013 Led <led@altlinux.ru> 0.9.11-alt1
- 0.9.11

* Tue Jun 25 2013 Led <led@altlinux.ru> 0.9.10-alt20
- fixes from upstream's SCM

* Sun Jun 16 2013 Led <led@altlinux.ru> 0.9.10-alt19
- fixes from upstream's SCM

* Mon Jun 10 2013 Led <led@altlinux.ru> 0.9.10-alt18
- updated from upstream's SCM

* Sat Jun 08 2013 Led <led@altlinux.ru> 0.9.10-alt17
- updated from upstream's SCM

* Fri Jun 07 2013 Led <led@altlinux.ru> 0.9.10-alt16
- updated from upstream's SCM

* Wed Jun 05 2013 Led <led@altlinux.ru> 0.9.10-alt15
- updated from upstream's SCM

* Tue Jun 04 2013 Led <led@altlinux.ru> 0.9.10-alt14
- fixes from upstream's SCM

* Tue May 28 2013 Led <led@altlinux.ru> 0.9.10-alt13
- fixes from upstream's SCM

* Sat May 25 2013 Led <led@altlinux.ru> 0.9.10-alt12
- fixes from upstream's SCM

* Thu May 23 2013 Led <led@altlinux.ru> 0.9.10-alt11
- fixes from upstream's SCM

* Mon May 20 2013 Led <led@altlinux.ru> 0.9.10-alt10
- updated from upstream's SCM

* Fri May 17 2013 Led <led@altlinux.ru> 0.9.10-alt9
- updated from upstream's SCM

* Thu May 16 2013 Led <led@altlinux.ru> 0.9.10-alt8
- updated from upstream's SCM

* Tue May 07 2013 Led <led@altlinux.ru> 0.9.10-alt7
- updated from upstream's SCM

* Sun Apr 28 2013 Led <led@altlinux.ru> 0.9.10-alt6
- updated from upstream's SCM

* Sat Apr 27 2013 Led <led@altlinux.ru> 0.9.10-alt5
- updated from upstream's SCM

* Tue Apr 23 2013 Led <led@altlinux.ru> 0.9.10-alt4
- fixes from upstream's SCM

* Mon Apr 22 2013 Led <led@altlinux.ru> 0.9.10-alt3
- fixes from upstream's SCM

* Mon Apr 22 2013 Led <led@altlinux.ru> 0.9.10-alt2
- updated from upstream's SCM

* Mon Apr 15 2013 Led <led@altlinux.ru> 0.9.10-alt1
- 0.9.10

* Tue Apr 09 2013 Led <led@altlinux.ru> 0.9.9-alt18
- updated from upstream's SCM

* Sun Apr 07 2013 Led <led@altlinux.ru> 0.9.9-alt17
- updated from upstream's SCM

* Fri Apr 05 2013 Led <led@altlinux.ru> 0.9.9-alt16
- updated from upstream's SCM

* Wed Apr 03 2013 Led <led@altlinux.ru> 0.9.9-alt15
- updated from upstream's SCM

* Fri Mar 29 2013 Led <led@altlinux.ru> 0.9.9-alt14
- updated from upstream's SCM

* Mon Mar 25 2013 Led <led@altlinux.ru> 0.9.9-alt13
- updated from upstream's SCM

* Mon Mar 25 2013 Led <led@altlinux.ru> 0.9.9-alt12
- updated from upstream's SCM

* Sun Mar 24 2013 Led <led@altlinux.ru> 0.9.9-alt11
- updated from upstream's SCM:
  + fix multiple bugs in syslog interfaces

* Mon Mar 11 2013 Led <led@altlinux.ru> 0.9.9-alt10
- updated from upstream's SCM

* Wed Mar 06 2013 Led <led@altlinux.ru> 0.9.9-alt9
- updated from upstream's SCM:
  + fix missing type error in grp.h from adding fgetgrent

* Tue Mar 05 2013 Led <led@altlinux.ru> 0.9.9-alt8
- fixes from upstream's SCM

* Wed Feb 27 2013 Led <led@altlinux.ru> 0.9.9-alt7
- updated from upstream's SCM

* Sat Feb 23 2013 Led <led@altlinux.ru> 0.9.9-alt6
- updated from upstream's SCM

* Thu Feb 21 2013 Led <led@altlinux.ru> 0.9.9-alt5
- updated from upstream's SCM:
  + added mkostemp, mkstemps, and mkostemps functions
  + added arpa/ftp.h

* Mon Feb 18 2013 Led <led@altlinux.ru> 0.9.9-alt4
- updated from upstream's SCM

* Fri Feb 08 2013 Led <led@altlinux.ru> 0.9.9-alt3
- updated from upstream's SCM

* Mon Feb 04 2013 Led <led@altlinux.ru> 0.9.9-alt2
- added ether_aton(), ether_aton_r(), ether_ntoa(), ether_ntoa_r()
- added dummy ether_hostton() stub
- updated from upstream's SCM

* Sun Feb 03 2013 Led <led@altlinux.ru> 0.9.9-alt1
- 0.9.9 with updates from upstream's SCM

* Wed Jan 30 2013 Led <led@altlinux.ru> 0.9.8-alt22
- netinet/if_ether.h: remove struct ethhdr definition
- sys/personality.h: add include linux/personality.h

* Sun Jan 27 2013 Led <led@altlinux.ru> 0.9.8-alt21
- fix tm_to_time logic for number of days in november

* Sat Jan 26 2013 Led <led@altlinux.ru> 0.9.8-alt20
- updated from upstream's SCM

* Sat Jan 19 2013 Led <led@altlinux.ru> 0.9.8-alt19
- updated from upstream's SCM

* Thu Jan 17 2013 Led <led@altlinux.ru> 0.9.8-alt18
- updated from upstream's SCM

* Tue Jan 15 2013 Led <led@altlinux.ru> 0.9.8-alt17
- updated from upstream's SCM

* Fri Jan 11 2013 Led <led@altlinux.ru> 0.9.8-alt16
- updated from upstream's SCM

* Sat Jan 05 2013 Led <led@altlinux.ru> 0.9.8-alt15
- updated from upstream's SCM

* Thu Jan 03 2013 Led <led@altlinux.ru> 0.9.8-alt14
- updated from upstream's SCM

* Fri Dec 28 2012 Led <led@altlinux.ru> 0.9.8-alt13
- updated from upstream's SCM

* Fri Dec 28 2012 Led <led@altlinux.ru> 0.9.8-alt12
- updated from upstream's SCM

* Fri Dec 21 2012 Led <led@altlinux.ru> 0.9.8-alt11
- updated from upstream's SCM:
  + clean up and fix logic for making mmap fail on invalid/unsupported offsets

* Thu Dec 20 2012 Led <led@altlinux.ru> 0.9.8-alt10
- updated from upstream's SCM

* Tue Dec 18 2012 Led <led@altlinux.ru> 0.9.8-alt9
- updated from upstream's SCM

* Sun Dec 16 2012 Led <led@altlinux.ru> 0.9.8-alt8
- updated from upstream's SCM

* Fri Dec 14 2012 Led <led@altlinux.ru> 0.9.8-alt7
- fixes from upstream's SCM

* Thu Dec 13 2012 Led <led@altlinux.ru> 0.9.8-alt6
- updated from upstream's SCM

* Sat Dec 08 2012 Led <led@altlinux.ru> 0.9.8-alt5
- updated from upstream's SCM

* Wed Dec 05 2012 Led <led@altlinux.ru> 0.9.8-alt4
- updated from upstream's SCM

* Mon Dec 03 2012 Led <led@altlinux.ru> 0.9.8-alt3
- fix a couple issues in the inttypes.h PRI/SCN macros (from upstream's SCM)

* Sat Dec 01 2012 Led <led@altlinux.ru> 0.9.8-alt2
- fixes from upstream's SCM

* Fri Nov 30 2012 Led <led@altlinux.ru> 0.9.8-alt1
- 0.9.8

* Tue Nov 27 2012 Led <led@altlinux.ru> 0.9.7-alt11
- updated from upstream's SCM

* Sat Nov 24 2012 Led <led@altlinux.ru> 0.9.7-alt10
- updated from upstream's SCM

* Wed Nov 21 2012 Led <led@altlinux.ru> 0.9.7-alt9
- updated from upstream's SCM

* Sat Nov 17 2012 Led <led@altlinux.ru> 0.9.7-alt8
- updated from upstream's SCM

* Wed Nov 14 2012 Led <led@altlinux.ru> 0.9.7-alt7
- updated from upstream's SCM

* Sat Nov 10 2012 Led <led@altlinux.ru> 0.9.7-alt6
- added defines to sched.h, termios.h
- updated from upstream's SCM

* Fri Nov 09 2012 Led <led@altlinux.ru> 0.9.7-alt5
- updated from upstream's SCM

* Mon Nov 05 2012 Led <led@altlinux.ru> 0.9.7-alt4
- updated from upstream's SCM

* Mon Nov 05 2012 Led <led@altlinux.ru> 0.9.7-alt3
- updated from upstream's SCM

* Fri Nov 02 2012 Led <led@altlinux.ru> 0.9.7-alt2
- updated from upstream's SCM

* Mon Oct 29 2012 Led <led@altlinux.ru> 0.9.7-alt1
- 0.9.7

* Wed Oct 24 2012 Led <led@altlinux.ru> 0.9.6-alt10
- updated from upstream's SCM

* Sun Oct 21 2012 Led <led@altlinux.ru> 0.9.6-alt9
- updated from upstream's SCM
- fixed unowned dirs

* Sat Oct 20 2012 Led <led@altlinux.ru> 0.9.6-alt8
- updated from upstream's SCM

* Fri Oct 12 2012 Led <led@altlinux.ru> 0.9.6-alt7
- updated from upstream's SCM

* Mon Oct 01 2012 Led <led@altlinux.ru> 0.9.6-alt6
- updated from upstream's SCM

* Wed Sep 26 2012 Led <led@altlinux.ru> 0.9.6-alt5
- updated from upstream's SCM

* Tue Sep 25 2012 Led <led@altlinux.ru> 0.9.6-alt4
- updated from upstream's SCM:
  + fix handling of EINTR during close()

* Mon Sep 24 2012 Led <led@altlinux.ru> 0.9.6-alt3
- updated from upstream's SCM

* Fri Sep 21 2012 Led <led@altlinux.ru> 0.9.6-alt2
- updated from upstream's SCM
- updated Summary

* Mon Sep 17 2012 Led <led@altlinux.ru> 0.9.6-alt1
- 0.9.6

* Tue Sep 11 2012 Led <led@altlinux.ru> 0.9.4-alt1
- updated from upstream's SCM

* Tue Sep 04 2012 Led <led@massivesolutions.co.uk> 0.9.4-cx6
- updated from upstream's SCM

* Fri Aug 31 2012 Led <led@massivesolutions.co.uk> 0.9.4-cx5
- updated from upstream's SCM

* Sun Aug 26 2012 Led <led@massivesolutions.co.uk> 0.9.4-cx4
- configure: removed --hash-style=both linker flag

* Sun Aug 26 2012 Led <led@massivesolutions.co.uk> 0.9.4-cx3
- updated from upstream's SCM:
  + add gnu hash support in the dynamic linker

* Thu Aug 23 2012 Led <led@massivesolutions.co.uk> 0.9.4-cx2
- upstream: fix bug whereby most atexit-registered functions got skipped

* Sun Aug 19 2012 Led <led@massivesolutions.co.uk> 0.9.4-cx1
- 0.9.4

* Mon Aug 13 2012 Led <led@massivesolutions.co.uk> 0.9.3-cx6
- updated from upstream's SCM

* Sun Aug 12 2012 Led <led@massivesolutions.co.uk> 0.9.3-cx5
- updated from upstream's SCM

* Wed Aug 08 2012 Led <led@massivesolutions.co.uk> 0.9.3-cx4
- updated from upstream's SCM
- added acct syscall wrapper

* Tue Aug 07 2012 Led <led@massivesolutions.co.uk> 0.9.3-cx3
- updated from upstream's SCM

* Sun Aug 05 2012 Led <led@massivesolutions.co.uk> 0.9.3-cx2
- changed soname

* Fri Aug 03 2012 Led <led@massivesolutions.co.uk> 0.9.3-cx1
- 0.9.3

* Fri Aug 03 2012 Led <led@massivesolutions.co.uk> 0.9.2-cx7
- moved shared library to /%%_lib/

* Fri Jul 27 2012 Led <led@massivesolutions.co.uk> 0.9.2-cx6
- fixed License
- cleaned up spec
- added config into %%_sysconfig/ld.so.conf.d/

* Fri Jul 27 2012 Led <led@massivesolutions.co.uk> 0.9.2-cx5
- added upstream fixes
- added extended attributes syscall wrappers
- added splice and vmsplice syscall wrappers

* Thu Jul 26 2012 Led <led@massivesolutions.co.uk> 0.9.2-cx4
- added ppoll syscall wrapper

* Sat Jul 21 2012 Led <led@massivesolutions.co.uk> 0.9.2-cx3
- added ioperm syscall wrapper
- added iopl syscall wrapper

* Mon Jul 16 2012 Led <led@massivesolutions.co.uk> 0.9.2-cx2
- removed -O3 from CFLAGS_ALL_SHARED

* Sun Jul 15 2012 Led <led@massivesolutions.co.uk> 0.9.2-cx1
- 0.9.2 with postrelease upstream fixes

* Mon Jul 02 2012 Led <led@massivesolutions.co.uk> 0.8.10-cx6
- added accept4 syscall wrapper

* Mon Jul 02 2012 Led <led@massivesolutions.co.uk> 0.8.10-cx5
- added pipe2 syscall wrapper
- added %%musl_dir/include/asm* symlinks

* Sun Jul 01 2012 Led <led@massivesolutions.co.uk> 0.8.10-cx4
- added %%musl_dir/include/linux symlink

* Fri Jun 29 2012 Led <led@massivesolutions.co.uk> 0.8.10-cx3
- added readahead syscall wrapper

* Fri Jun 29 2012 Led <led@massivesolutions.co.uk> 0.8.10-cx2
- added personality syscall wrapper
- implemented stub versions of sched_*
- added init_module/delete_module syscall wrappers
- fixed sys/param.h

* Thu Jun 28 2012 Led <led@massivesolutions.co.uk> 0.8.10-cx1
- initial build
