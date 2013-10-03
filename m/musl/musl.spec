%def_enable shared
%def_enable static
%def_enable gcc_wrapper
%define libc_dir /%_lib

%{!?x86_64:%define x86_64 x86_64}
%define subst_enable_to() %{expand:%%{?_enable_%{1}:--enable-%{2}}} %{expand:%%{?_disable_%{1}:--disable-%{2}}}

Name: musl
Version: 0.9.14
Release: alt6
Group: System/Libraries
Summary: musl libc - new standard library
License: MIT
Url: http://www.etalabs.net/%name
Source: %url/releases/%name-%version.tar
Patch: %name-%version-%release.patch
ExclusiveOS: Linux
%define musl_dir %_libdir/%name
%define soname libc-%name.so.1
%define libname libc-%name-%version.so

%{!?libc_dir:%define libc_dir %musl_dir/lib}

%description
%name libc is a new standard library to power a new generation of Linux-based
devices. %name is lightweight, fast, simple, free, and strives to be correct in
the sense of standards-conformance and safety.
%name is an alternative to glibc, eglibc, uClibc, dietlibc, and klibc.


%package devel
Summary: Development files for %name
Group: Development/C
AutoReq: yes, nosymlinks, nocpp
Requires: %name = %version-%release
Requires: kernel-headers-common
Provides: %name-gcc = %version-%release

%description devel
Development files and headers for %name.


%prep
%setup -q
%patch -p1
[ -x tools/install.sh ] || chmod a+x tools/install.sh
sed -i '/--hash-style=both/d' configure
sed -i 's/\(-soname=\)libc\.so/\1%soname/' Makefile
sed -i 's/libc\.so/%libname/' Makefile
%if "%_lib" != "lib"
sed -i 's|"/lib\(:/usr/local/lib:\)/usr/lib"|"/%_lib\1%_libdir"|' src/ldso/dynlink.c
%endif


%build
%define _optlevel s
%add_optflags -U_FORTIFY_SOURCE
./configure \
	CFLAGS="%optflags" \
	--prefix=%musl_dir \
	--exec-prefix=%prefix \
	--syslibdir=/%_lib \
	%{subst_enable shared} \
	%{subst_enable static} \
	%{subst_enable_to gcc_wrapper gcc-wrapper} \
	--enable-warnings
%make_build


%install
# Used custom INSTALL - install.sh
%__make DESTDIR=%buildroot install
rm -rf %buildroot%musl_dir/include/linux
for d in linux asm asm-generic mtd; do
	ln -sf %_includedir/$d %buildroot%musl_dir/include/
done

install -d -m 0755 %buildroot%_docdir/%name-%version
install -p -m 0644 README WHATSNEW %buildroot%_docdir/%name-%version/

%if "%libc_dir" != "%musl_dir/lib"
mv %buildroot%musl_dir/lib/%libname %buildroot/%_lib/
ln -sf /%_lib/%soname %buildroot%musl_dir/lib/libc.so
%if "%libc_dir" == "/%_lib"
ln -sf %libname %buildroot/%_lib/ld-*
%else
ln -sf %libc_dir/%libname %buildroot/%_lib/ld-*
%endif
%endif

install -d -m 0755 %buildroot%_sysconfdir/ld.so.conf.d
echo "%musl_dir/lib" > %buildroot%_sysconfdir/ld.so.conf.d/%name-%_lib.conf


%files
%if "%libc_dir" != "%musl_dir/lib"
%dir %musl_dir
%dir %musl_dir/lib
%endif
%if "%libc_dir" != "/%_lib"
%libc_dir/*.so
%endif
/%_lib/*
%config %_sysconfdir/ld.so.conf.d/*


%files devel
%doc %_docdir/%name-%version
%_bindir/*
%musl_dir/include
%musl_dir/lib/*
%if "%libc_dir" == "%musl_dir/lib"
%exclude %musl_dir/lib/*.so
%endif


%changelog
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
