%def_enable shared
%def_enable static
%def_enable gcc_wrapper
%define libc_dir /%_lib

%{!?x86_64:%define x86_64 x86_64}
%define subst_enable_to() %{expand:%%{?_enable_%{1}:--enable-%{2}}} %{expand:%%{?_disable_%{1}:--disable-%{2}}}

Name: musl
Version: 0.9.6
Release: alt9
Group: System/Libraries
Summary: musl libc - new standard library
License: MIT
Url: http://www.etalabs.net/%name
Source: %url/releases/%name-%version.tar
Patch: %name-%version-%release.patch
ExclusiveOS: Linux
ExclusiveArch: %ix86 %x86_64 %arm
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
%makeinstall_std
rm -rf %buildroot%musl_dir/include/linux
for d in linux asm asm-generic; do
	ln -sf %_includedir/$d %buildroot%musl_dir/include/
done

install -d -m 0755 %buildroot%_docdir/%name-%version
install -m 0644 README WHATSNEW %buildroot%_docdir/%name-%version/

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
