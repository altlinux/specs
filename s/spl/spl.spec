Name: spl
Version: 0.6.2
Release: alt3
Summary: Solaris Porting Layer (SPL)
License: GPLv2+
Group: System/Kernel and hardware
URL: http://zfsonlinux.org
Source: http://archive.zfsonlinux.org/downloads/zfsonlinux/%name/%name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: rpm-build-kernel

%description
The Solaris Porting Layer (SPL) is a Linux kernel module which provides many of
the Solaris kernel APIs. This shim layer makes it possible to run Solaris kernel
code in the Linux kernel with relatively minimal modification. This can be
particularly useful when you want to track upstream Solaris development closely
and don't want the overhead of maintaining a large patch which converts Solaris
primitives to Linux primitives.


%package utils
Summary: SPL modules sources for Linux kernel
Group: System/Kernel and hardware
Provides: splat = %version-%release

%description utils
The Solaris Porting Layer (SPL) is a Linux kernel module which provides many of
the Solaris kernel APIs. This shim layer makes it possible to run Solaris kernel
code in the Linux kernel with relatively minimal modification. This can be
particularly useful when you want to track upstream Solaris development closely
and don't want the overhead of maintaining a large patch which converts Solaris
primitives to Linux primitives.
This package contains splat - Solaris Porting LAyer Tests. This utility uses the
splat.ko kernel module to test the spl.ko kernel module.


%package -n kernel-source-%name
Summary: SPL modules sources for Linux kernel
Group: Development/Kernel
BuildArch: noarch
Provides: kernel-src-%name = %version-%release

%description -n kernel-source-%name
The Solaris Porting Layer (SPL) is a Linux kernel module which provides many of
the Solaris kernel APIs. This shim layer makes it possible to run Solaris kernel
code in the Linux kernel with relatively minimal modification. This can be
particularly useful when you want to track upstream Solaris development closely
and don't want the overhead of maintaining a large patch which converts Solaris
primitives to Linux primitives.
This package contains SPL modules sources for Linux kernel.


%prep
%setup -q
%patch -p1
sed -i '/^AC_OUTPUT/itest "x$SPL_CONFIG" != "xkernel" || ac_config_files="module/Makefile module/spl/Makefile module/splat/Makefile"\n' configure.ac


%build
./autogen.sh

tar -C .. \
	--exclude .gitignore \
	--exclude 'include/*Makefile.*' \
	-cJf %name-%version.tar.xz \
	%name-%version/module \
	%name-%version/config/{{install-,ltmain.}sh,config.{awk,guess,sub},missing} \
	%name-%version/include \
	%name-%version/{AUTHORS,COPYING,DISCLAIMER,META,configure,%name{.release,_config.h}.in}

%configure --with-config=user --with-gnu-ld
%make_build


%install
install -pD -m 0644 {,%kernel_srcdir/}%name-%version.tar.xz
%makeinstall_std


%files utils
%doc AUTHORS DISCLAIMER META README*
%_sbindir/*
%_man1dir/*


%files -n kernel-source-%name
%_usrsrc/kernel


%changelog
* Tue Oct 29 2013 Led <led@altlinux.ru> 0.6.2-alt3
- upstream updates and fixes

* Mon Oct 14 2013 Led <led@altlinux.ru> 0.6.2-alt2
- upstream fixes

* Tue Aug 27 2013 Led <led@altlinux.ru> 0.6.2-alt1
- 0.6.2

* Sun Aug 11 2013 Led <led@altlinux.ru> 0.6.1-alt7
- upstream fixes

* Fri Aug 02 2013 Led <led@altlinux.ru> 0.6.1-alt6
- upstream fixes

* Wed Jul 17 2013 Led <led@altlinux.ru> 0.6.1-alt5
- upstream updates

* Fri Jul 12 2013 Led <led@altlinux.ru> 0.6.1-alt4
- upstream updates

* Sat Jul 06 2013 Led <led@altlinux.ru> 0.6.1-alt3
- kernel-source-%name: add config/missing

* Tue Jul 02 2013 Led <led@altlinux.ru> 0.6.1-alt2
- upstream fixes

* Mon Jun 17 2013 Led <led@altlinux.ru> 0.6.1-alt1
- initial build
