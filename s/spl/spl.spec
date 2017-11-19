Name: spl
Version: 0.7.3
Release: alt1
Summary: Solaris Porting Layer (SPL)
License: GPLv2+
Group: System/Kernel and hardware
URL: http://zfsonlinux.org
Source: %name-%version.tar
Patch: spl-0.7.0-conf-alt.patch

BuildRequires: rpm-build-kernel

%description
Solaris Porting Layer utilities for Linux

%package utils
Summary: Solaris Porting Layer (SPL)
Group: System/Kernel and hardware
Provides: splat = %version-%release

%description utils
Solaris Porting Layer utilities for Linux

%package -n kernel-source-%name
Summary: SPL modules sources for Linux kernel
Group: Development/Kernel
BuildArch: noarch
Provides: kernel-src-%name = %version-%release

%description -n kernel-source-%name
This package contains SPL modules sources for Linux kernel.

%prep
%setup -q
%patch -p1

tar -C .. \
	--exclude .gitignore \
	--exclude 'include/*Makefile.*' \
	-cJf %name-%version.tar.xz \
	%name-%version/module \
	%name-%version/config/{{install-,ltmain.}sh,config.{awk,guess,sub},missing} \
	%name-%version/include \
	%name-%version/{AUTHORS,COPYING,DISCLAIMER,META,configure,%name{.release,_config.h}.in}

%build
%autoreconf
%configure \
	--with-config=user \
	--with-gnu-ld
%make_build

%install
install -pD -m0644 %name-%version.tar.xz %kernel_srcdir/%name-%version.tar.xz
%make DESTDIR=%buildroot install


%files utils
%doc AUTHORS DISCLAIMER META
%_sbindir/*
%_man1dir/*.1*
%_man5dir/*.5*

%files -n kernel-source-%name
%_usrsrc/kernel

%changelog
* Sat Nov 18 2017 Anton Farygin <rider@altlinux.ru> 0.7.3-alt1
- 0.7.3 

* Thu Sep 14 2017 Valery Inozemtsev <shrek@altlinux.ru> 0.7.1-alt1
- 0.7.1

* Mon Aug 07 2017 Valery Inozemtsev <shrek@altlinux.ru> 0.7.0-alt1
- 0.7.0

* Thu Jul 20 2017 Valery Inozemtsev <shrek@altlinux.ru> 0.6.5.11-alt0.M80P.1
- backport to p8 branch

* Thu Jul 13 2017 Valery Inozemtsev <shrek@altlinux.ru> 0.6.5.11-alt1
- 0.6.5.11

* Thu Jun 15 2017 Valery Inozemtsev <shrek@altlinux.ru> 0.6.5.10-alt1
- 0.6.5.10

* Tue Feb 07 2017 Valery Inozemtsev <shrek@altlinux.ru> 0.6.5.9-alt0.M80P.1
- backport to p8 branch

* Mon Feb 06 2017 Valery Inozemtsev <shrek@altlinux.ru> 0.6.5.9-alt1
- 0.6.5.9

* Tue Oct 11 2016 Valery Inozemtsev <shrek@altlinux.ru> 0.6.5.8-alt0.M80P.1
- backport to p8 branch

* Mon Oct 10 2016 Valery Inozemtsev <shrek@altlinux.ru> 0.6.5.8-alt1
- 0.6.5.8

* Wed Aug 27 2014 Led <led@altlinux.ru> 0.6.3-alt9
- upstream fixes

* Sat Aug 16 2014 Led <led@altlinux.ru> 0.6.3-alt8
- upstream updates

* Thu Aug 14 2014 Led <led@altlinux.ru> 0.6.3-alt7
- upstream updates

* Sat Aug 09 2014 Led <led@altlinux.ru> 0.6.3-alt6
- upstream updates

* Wed Jul 30 2014 Led <led@altlinux.ru> 0.6.3-alt5
- upstream updates

* Sat Jul 26 2014 Led <led@altlinux.ru> 0.6.3-alt4
- upstream updates

* Thu Jul 03 2014 Led <led@altlinux.ru> 0.6.3-alt3
- upstream updates and fixes

* Mon Jun 16 2014 Led <led@altlinux.ru> 0.6.3-alt2
- removed stupidly defined 'hz'

* Sat Jun 14 2014 Led <led@altlinux.ru> 0.6.3-alt1
- 0.6.3

* Sun Jun 01 2014 Led <led@altlinux.ru> 0.6.2-alt16
- upstream updates

* Fri May 23 2014 Led <led@altlinux.ru> 0.6.2-alt15
- upstream updates

* Sat Apr 26 2014 Led <led@altlinux.ru> 0.6.2-alt14
- upstream updates and fixes

* Tue Apr 15 2014 Led <led@altlinux.ru> 0.6.2-alt13
- upstream updates

* Sat Apr 12 2014 Led <led@altlinux.ru> 0.6.2-alt12
- upstream fixes

* Thu Apr 10 2014 Led <led@altlinux.ru> 0.6.2-alt11
- De-inline spl_kthread_create()

* Wed Apr 09 2014 Led <led@altlinux.ru> 0.6.2-alt10
- upstream fixes

* Wed Jan 08 2014 Led <led@altlinux.ru> 0.6.2-alt9
- upstream fixes

* Mon Dec 09 2013 Led <led@altlinux.ru> 0.6.2-alt8
- upstream updates

* Tue Dec 03 2013 Led <led@altlinux.ru> 0.6.2-alt7
- upstream fixes

* Sun Nov 24 2013 Led <led@altlinux.ru> 0.6.2-alt6
- upstream updates:
  + document SPL module parameters

* Tue Nov 12 2013 Led <led@altlinux.ru> 0.6.2-alt5
- upstream updates:
  + kernel 3.12 compat

* Tue Nov 05 2013 Led <led@altlinux.ru> 0.6.2-alt4
- upstream updates

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
