Name: libdrm
Version: 2.4.33
Release: alt1
Epoch: 1
Summary: Userspace interface to kernel DRM service
License: GPL
Group: System/Libraries
Url: http://dri.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: libudev-devel libpciaccess-devel

%description
This library implements the userspace interface to the kernel DRM
services. DRM stands for "Direct Rendering Manager", which is the
kernelspace portion of the "Direct Rendering Infrastructure" (DRI).
The DRI is currently used on Linux to provide hardware-accelerated
OpenGL drivers

%package devel
Summary: The drm Library and Header Files
Group: Development/C
Requires: %name = %epoch:%version-%release

%description devel
%name-devel contains the libraries and header files needed to
develop programs which make use of %name

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure \
	--enable-nouveau-experimental-api \
	--enable-omap-experimental-api \
	--enable-udev \
	--disable-libkms \
	--disable-static
%make_build

%install
%make DESTDIR=%buildroot install

%files
%_libdir/*.so.*

%files devel
%_includedir/%name
%_includedir/nouveau
%_includedir/omap
%_includedir/*.h
%_libdir/*.so
%_pkgconfigdir/*.pc

%changelog
* Thu Mar 29 2012 Valery Inozemtsev <shrek@altlinux.ru> 1:2.4.33-alt1
- 2.4.33

* Sat Mar 17 2012 Valery Inozemtsev <shrek@altlinux.ru> 1:2.4.32-alt1
- 2.4.32

* Tue Feb 07 2012 Valery Inozemtsev <shrek@altlinux.ru> 1:2.4.31-alt1
- 2.4.31

* Sat Jan 07 2012 Valery Inozemtsev <shrek@altlinux.ru> 1:2.4.30-alt1
- 2.4.30

* Tue Dec 13 2011 Valery Inozemtsev <shrek@altlinux.ru> 1:2.4.29-alt1
- 2.4.29

* Tue Dec 06 2011 Valery Inozemtsev <shrek@altlinux.ru> 1:2.4.28-alt1
- 2.4.28

* Sat Oct 29 2011 Valery Inozemtsev <shrek@altlinux.ru> 1:2.4.27-alt1
- 2.4.27

* Sat Jun 04 2011 Valery Inozemtsev <shrek@altlinux.ru> 1:2.4.26-alt1
- 2.4.26

* Mon Apr 11 2011 Valery Inozemtsev <shrek@altlinux.ru> 1:2.4.25-alt1
- 2.4.25

* Tue Mar 01 2011 Valery Inozemtsev <shrek@altlinux.ru> 1:2.4.24-alt1
- 2.4.24

* Thu Feb 10 2011 Alexey Tourbin <at@altlinux.ru> 1:2.4.23-alt3
- rebuilt for debuginfo
- disabled symbol versioning

* Sat Jan 08 2011 Valery Inozemtsev <shrek@altlinux.ru> 1:2.4.23-alt2
- updated to master git.bad5242

* Fri Dec 10 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:2.4.23-alt1
- 2.4.23

* Fri Nov 05 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:2.4.22-alt2
- intel:
  + Prepare for BLT ring split
  + enable relaxed fence allocation for i915

* Wed Sep 29 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:2.4.22-alt1
- 2.4.22

* Tue Sep 28 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:2.4.21-alt3
- nouveau: drop unused nouveau_class.h

* Fri Sep 24 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:2.4.21-alt2
- GIT snapshot 2010-09-21 (81fa7a9f56b1efb04658db921e5228c102548921)

* Thu Jun 10 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:2.4.21-alt1
- 2.4.21

* Sat Apr 03 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:2.4.20-alt1
- 2.4.20

* Wed Mar 03 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:2.4.19-alt1
- 2.4.19

* Mon Feb 22 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:2.4.18-alt2
- enabled nouveau

* Wed Feb 17 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:2.4.18-alt1
- 2.4.18

* Sat Feb 13 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:2.4.18-alt0.d1
- GIT snapshot 2010-02-10 (4a17be4a86cde1065908576e44f3710f6d9d68af)

* Wed Feb 10 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:2.4.17-alt4
- intel: Handle resetting of input params after EINTR during SET_TILING

* Tue Feb 09 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:2.4.17-alt3
- intel: account for potential pinned buffers hogging fences

* Tue Feb 02 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:2.4.17-alt2
- intel: check return value for calloc

* Mon Dec 21 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:2.4.17-alt1
- 2.6.17

* Thu Dec 03 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:2.4.16-alt1
- 2.4.16

* Tue Dec 01 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:2.4.15-alt2
- libdrm_radeon: added radeon_bo_is_referenced_by_cs function

* Fri Oct 09 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:2.4.15-alt1
- 2.4.15

* Tue Sep 29 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:2.4.14-alt1
- 2.4.14

* Sun Sep 06 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:2.4.13-alt1
- 2.4.13

* Wed Jul 15 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:2.4.12-alt1
- 2.4.12

* Wed Jun 17 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:2.4.11-alt2
- added initial libdrm_radeon

* Sat May 16 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:2.4.11-alt1
- 2.4.11

* Fri May 15 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:2.4.6-alt2
- 2.4.6

* Wed May 13 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.4.10-alt1
- 2.4.10

* Tue Apr 28 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.4.9-alt2
- fixed assertion failures on later use of the object

* Sat Apr 11 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.4.9-alt1
- 2.4.9

* Tue Apr 07 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.4.6-alt1
- 2.4.6

* Tue Mar 03 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.4.5-alt3
- reenabled udev

* Thu Feb 26 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.4.5-alt2
- disabled udev

* Tue Feb 24 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.4.5-alt1
- 2.4.5

* Wed Feb 04 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.4.4-alt0.M50.1
- build for branch 5.0

* Thu Jan 15 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.4.4-alt1
- 2.4.4

* Tue Dec 23 2008 Valery Inozemtsev <shrek@altlinux.ru> 2.4.3-alt1
- 2.4.3

* Sat Nov 22 2008 Valery Inozemtsev <shrek@altlinux.ru> 2.4.1-alt2
- removed obsolete %%post_ldconfig/%%postun_ldconfig calls

* Thu Oct 30 2008 Valery Inozemtsev <shrek@altlinux.ru> 2.4.1-alt1
- 2.4.1

* Sun Oct 19 2008 Valery Inozemtsev <shrek@altlinux.ru> 2.4.0-alt4
- enabled support for using udev instead of mknod

* Sun Oct 19 2008 Valery Inozemtsev <shrek@altlinux.ru> 2.4.0-alt3
- 2.4.0 release

* Tue Mar 25 2008 Valery Inozemtsev <shrek@altlinux.ru> 2.4.0-alt2
- GIT snapshot 2008-05-28

* Mon Nov 12 2007 Valery Inozemtsev <shrek@altlinux.ru> 2.4.0-alt1
- 2.4.0

* Mon Sep 10 2007 Valery Inozemtsev <shrek@altlinux.ru> 2.3.1-alt7
- revert 2.3.1 release
- added xgi_drm.h

* Sun Sep 09 2007 Valery Inozemtsev <shrek@altlinux.ru> 2.3.1-alt6
- GIT snapshot, drop upstream patches

* Tue Aug 07 2007 Valery Inozemtsev <shrek@altlinux.ru> 2.3.1-alt5
- updated nouveau_drm.h to patchlevel 10

* Sat Jul 21 2007 Valery Inozemtsev <shrek@altlinux.ru> 2.3.1-alt4
- updated nouveau_drm.h to patchlevel 9

* Tue May 08 2007 Valery Inozemtsev <shrek@altlinux.ru> 2.3.1-alt3
- fix typo on ttm fence interface master

* Sun Apr 08 2007 Valery Inozemtsev <shrek@altlinux.ru> 2.3.1-alt2
- updated nouveau_drm.h to patchlevel 6

* Fri Mar 16 2007 Valery Inozemtsev <shrek@altlinux.ru> 2.3.1-alt1
- 2.3.1

* Sun Jan 21 2007 Valery Inozemtsev <shrek@altlinux.ru> 2.3.0-alt2
- fixed libdrm-2.3.0-alt-version-script.patch

* Thu Nov 09 2006 Valery Inozemtsev <shrek@altlinux.ru> 2.3.0-alt1
- 2.3.0:
  + This adds support for server to user system libdrm, and also for
    drmOpenOnce and drmCloseOnce APIs.

* Sun Oct 29 2006 Valery Inozemtsev <shrek@altlinux.ru> 2.2.0-alt2
- added version script

* Sun Oct 29 2006 Valery Inozemtsev <shrek@altlinux.ru> 2.2.0-alt1
- 2.2.0

* Sun Oct 15 2006 Valery Inozemtsev <shrek@altlinux.ru> 2.0.2-alt2
- GIT snapshot 2006-08-30:
	+ drmUpdateDrawableInfo

* Thu Jun 29 2006 Valery Inozemtsev <shrek@altlinux.ru> 2.0.2-alt1
- 2.0.2

* Thu Apr 13 2006 Valery Inozemtsev <shrek@altlinux.ru> 2.0.1-alt1
- 2.0.1

* Sat Mar 18 2006 Valery Inozemtsev <shrek@altlinux.ru> 2.0-alt4
- CVS snapshot 20060314

* Mon Feb 20 2006 Valery Inozemtsev <shrek@altlinux.ru> 2.0-alt3
- CVS snapshot 20060220

* Tue Feb 14 2006 Valery Inozemtsev <shrek@altlinux.ru> 2.0-alt2
- added libdrm-2.0-cvs_changes patch

* Mon Dec 05 2005 Valery Inozemtsev <shrek@altlinux.ru> 2.0-alt1
- 2.0

* Wed Nov 23 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.0.5-alt0.1
- initial release

