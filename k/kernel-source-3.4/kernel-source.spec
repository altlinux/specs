%define original_kernel_version	3.4
%define kernel_version		3.4
%define patch_level		%nil

%define testing			0

%if %testing
%define kernel_fullversion	%kernel_version%patch_level
%else
%define kernel_fullversion	%kernel_version
%endif

# Numeric extra version scheme developed by Alexander Bokovoy:
# 0.0.X -- preX
# 0.X.0 -- rcX, testX
# 1.0.0 -- release
%define patch_level_numeric     1.0.0

Name: kernel-source-%kernel_version
Version: %patch_level_numeric
Release: alt1

Summary: Linux kernel %kernel_fullversion sources
License: GPL
Group: Development/Kernel
Packager: Kernel Maintainers Team <kernel@packages.altlinux.org>

Source0: linux-%original_kernel_version.tar.bz2

BuildArch: noarch
BuildPreReq: kernel-build-tools

%description
Kernel sources for Linux kernel %kernel_fullversion

%prep
%setup -qc
mv linux-%original_kernel_version kernel-source-%kernel_version
%if %testing
pushd kernel-source-%kernel_version
popd
%endif

%install
mkdir -p %kernel_srcdir
tar --owner=root --group=root --mode=u+w,go-w,go+rX -cjf \
	%kernel_srcdir/kernel-source-%kernel_version.tar.bz2 \
	kernel-source-%kernel_version

%files
%kernel_src/kernel-source-%kernel_version.tar.bz2

%changelog
* Mon May 21 2012 Valery Inozemtsev <shrek@altlinux.ru> 1.0.0-alt1
- 3.4

* Mon Mar 19 2012 Valery Inozemtsev <shrek@altlinux.ru> 1.0.0-alt1
- 3.3

* Thu Jan 05 2012 Valery Inozemtsev <shrek@altlinux.ru> 1.0.0-alt1
- 3.2

* Mon Oct 24 2011 Valery Inozemtsev <shrek@altlinux.ru> 1.0.0-alt1
- 3.1

* Fri Jul 22 2011 Valery Inozemtsev <shrek@altlinux.ru> 1.0.0-alt1
- 3.0

* Thu May 19 2011 Valery Inozemtsev <shrek@altlinux.ru> 1.0.0-alt1
- 2.6.39

* Tue Mar 15 2011 Valery Inozemtsev <shrek@altlinux.ru> 1.0.0-alt1
- 2.6.38

* Wed Jan 05 2011 Valery Inozemtsev <shrek@altlinux.ru> 1.0.0-alt1
- 2.6.37

* Thu Oct 21 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.0.0-alt1
- 2.6.36

* Mon May 17 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.0.0-alt1
- 2.6.34

* Wed Feb 24 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.0.0-alt1
- 2.6.33

* Thu Dec 03 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.0.0-alt1
- 2.6.32

* Thu Sep 10 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.0.0-alt1
- 2.6.31

* Mon Sep 07 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.9.0-alt1
- 2.6.31-rc9

* Wed Jun 10 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.0.0-alt1
- 2.6.30

* Wed Jun 03 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.8.0-alt1
- 2.6.30-rc8

* Mon May 25 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.7.0-alt1
- 2.6.30-rc7

* Sat May 16 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.6.0-alt1
- 2.6.30-rc6

* Tue Mar 24 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.0.0-alt1
- 2.6.29

* Fri Mar 13 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.8.0-alt1
- 2.6.29-rc8

* Wed Mar 04 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.7.0-alt1
- 2.6.29-rc7

* Wed Feb 25 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.6.0-alt1
- 2.6.29-rc6

* Thu Dec 25 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.0.0-alt1
- 2.6.28

* Fri Oct 10 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.0.0-alt1
- 2.6.27

* Mon Jul 14 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.0.0-alt1
- 2.6.26

* Sun Apr 20 2008 Michail Yakushin <silicium@altlinux.ru> 1.0.0-alt1
- 2.6.25

* Fri Jan 25 2008 Sergey Vlasov <vsu@altlinux.ru> 1.0.0-alt1
- 2.6.24

* Sun Oct 29 2006 Sergey Vlasov <vsu@altlinux.ru> 1.0.0-alt1
- 2.6.18

* Sun Jun 18 2006 Sergey Vlasov <vsu@altlinux.ru> 1.0.0-alt1
- 2.6.17

* Sun Apr 23 2006 Dmitry V. Levin <ldv@altlinux.org> 1.0.0-alt2
- Specfile cleanup.

* Mon Mar 20 2006 Sergey Vlasov <vsu@altlinux.ru> 1.0.0-alt1
- 2.6.16

* Fri Oct 28 2005 Sergey Vlasov <vsu@altlinux.ru> 1.0.0-alt1
- 2.6.14

* Sat Jun 18 2005 Sergey Vlasov <vsu@altlinux.ru> 1.0.0-alt1
- 2.6.12
- Removed kernel-doc package (documentation generation is performed when
  building kernel-image-%%flavour packages).

* Thu Mar 03 2005 Sergey Vlasov <vsu@altlinux.ru> 1.0.0-alt1
- 2.6.11

* Mon Dec 27 2004 Sergey Vlasov <vsu@altlinux.ru> 1.0.0-alt1
- 2.6.10

* Wed Oct 20 2004 Anton Farygin <rider@altlinux.ru> 1.0.0-alt1
- 2.6.9
