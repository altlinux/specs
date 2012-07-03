Name: nilfs-utils
Version: 2.0.23a
Release: alt1

Summary: Utilities for managing NILFS v2 filesystems
License: GPLv2+
Group: System/Kernel and hardware

Url: http://www.nilfs.org
Source: http://www.nilfs.org/download/%name-%version.tar
Packager: Michael Shigorin <mike@altlinux.org>

BuildRequires: libuuid-devel
Provides: nilfs2-utils = %version

%define libname libnilfs
%define _libdir /%_lib

%description
Utilities to work with NILFS v2 filesystems

%package -n %libname
Summary: NILFS2 library
Group: System/Libraries

%description -n %libname
This package contains shared code for %name and other
utilities dealing with NILFS2 filesystems.

%package -n %libname-devel
Summary: NILFS2 filesystem-specific headers
Group: Development/C
Requires: %libname = %version-%release

%description -n %libname-devel
This package contains the header files needed to develop
NILFS filesystem-specific programs.

You should install it if you want to develop NILFS
filesystem-specific programs. If you install this,
you'll also want to install %name.

%prep
%setup

%build
%autoreconf
%configure --libdir %_libdir --disable-static
%make_build

%install
%makeinstall_std

%files
%doc COPYING ChangeLog
%config(noreplace) %_sysconfdir/nilfs_cleanerd.conf
/sbin/*
%_bindir/*
%_mandir/*/*

%files -n %libname
%_libdir/*.so.*

%files -n %libname-devel
%_libdir/*.so
%_includedir/*.h

%changelog
* Thu Jun 23 2011 Michael Shigorin <mike@altlinux.org> 2.0.23a-alt1
- retrofitted upstream commit to fix m4/ nanoissue
  (thx Ryusuke Konishi)

* Mon Jun 20 2011 Michael Shigorin <mike@altlinux.org> 2.0.23-alt2
- fix build (thx led@)

* Thu May 19 2011 Michael Shigorin <mike@altlinux.org> 2.0.23-alt1
- 2.0.23

* Tue Apr 05 2011 Michael Shigorin <mike@altlinux.org> 2.0.21-alt1
- 2.0.21 (closes: #25389)

* Sun Feb 21 2010 Michael Shigorin <mike@altlinux.org> 2.0.15-alt1
- 2.0.15 (trivial fixes)
- dropped the (upstream) patch

* Fri Nov 27 2009 Michael Shigorin <mike@altlinux.org> 2.0.14-alt2
- fixed FTBFS (updated buildrequires)
- minor spec cleanup

* Wed Nov 04 2009 Michael Shigorin <mike@altlinux.org> 2.0.14-alt1
- built for ALT Linux (starting off a fedora proposed package)
- considerable spec cleanup
- replaced patch/hacks with two upstream git commits

* Thu Jul 30 2009 Eric Sandeen <sandeen@redhat.com> 2.0.14-2
- Fix libuuid-devel dep, fix odd chown in make install

* Wed Jul 29 2009 Eric Sandeen <sandeen@redhat.com> 2.0.14-1
- New upstream release

* Wed Jun 10 2009 Eric Sandeen <sandeen@redhat.com> 2.0.12-1
- Initial fedora package

