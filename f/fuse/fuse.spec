Name: fuse
Version: 2.8.7
Release: alt4

Summary: a tool for creating virtual filesystems
License: GPL
Group: System/Kernel and hardware

Url: http://sourceforge.net/projects/fuse

Source: %name-%version.tar
Source1: fusermount-control

Patch0: %name.Makefile.patch
Patch1: %name.udev.patch
Patch2: %name.link.patch
Patch3: %name-2.8.0-alt-mmap.patch

Packager: Denis Smirnov <mithraen@altlinux.ru>

Requires: mount >= 2.11
Provides: avfs-fuse = %version
Obsoletes: avfs-fuse < %version

%description
FUSE (Filesystem in USErspace), an excellent tool
for creating custom filesystems with minimal effort
as well as for using them.

%package -n lib%name
Group: System/Kernel and hardware
Summary: tool for creating virtual filesystems
Requires: %name = %version-%release
Provides: FUSE = %version avfs-fuse = %version libavfs-fuse = %version
Obsoletes: FUSE < %version avfs-fuse < %version libavfs-fuse < %version

%description -n lib%name
FUSE (Filesystem in USErspace), an excellent tool
for creating custom filesystems with minimal effort.

This package contains shared libraries.

%package -n lib%name-devel
Group: System/Kernel and hardware
Summary: tool for creating virtual filesystems
Requires: lib%name = %version-%release
Provides: libavfs-fuse-devel = %version
Obsoletes: libavfs-fuse-devel < %version

%description -n lib%name-devel
FUSE (Filesystem in USErspace), an excellent tool
for creating custom filesystems with minimal effort.

This package contains development headers.

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p0
%patch3 -p1

%build
%autoreconf
%configure \
	--enable-lib \
	--enable-util \
	--disable-static
%make_build

%install
%makeinstall_std

mkdir -p %buildroot/%_lib
mv %buildroot%_libdir/lib%name.so.* %buildroot/%_lib/
ln -sf ../../%_lib/lib%name.so.%version %buildroot%_libdir/lib%name.so

install -pD %SOURCE1 %buildroot%_sysconfdir/control.d/facilities/fusermount
rm -fr %buildroot%_sysconfdir/init.d

mkdir -p %buildroot/lib/udev/devices
touch %buildroot/lib/udev/devices/{f,c}use

%pre
%_sbindir/groupadd -r -f fuse
%_sbindir/groupadd -r -f cuse
%pre_control fusermount

%post
%post_control -s fuseonly fusermount

%files
%doc AUTHORS NEWS README Filesystems README.NFS
%_sysconfdir/control.d/facilities/fusermount
%_sysconfdir/udev/rules.d/*
/sbin/mount.fuse
%attr(4710,root,fuse) %_bindir/fusermount
%_bindir/ulockmgr_server
%attr(0660,root,fuse) %dev(c,10,229) /lib/udev/devices/fuse
%attr(0660,root,cuse) %dev(c,10,59) /lib/udev/devices/cuse

%files -n lib%name
/%_lib/lib%name.so.*
%_libdir/lib*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/lib*.so
%_pkgconfigdir/*.pc

%changelog
* Thu May 10 2012 Michael Shigorin <mike@altlinux.org> 2.8.7-alt4
- relaxed /lib/udev/devices/{c,f}use permissions somewhat
  so that at least the default configuration is coherent

* Sat May 05 2012 Michael Shigorin <mike@altlinux.org> 2.8.7-alt3
- enabled "fuseonly" mode by default (closes: #27117)
- tightened up /lib/udev/devices/{c,f}use permissions
- use control macros in package scripts
- enhanced descriptions a bit

* Sun Mar 25 2012 Michael Shigorin <mike@altlinux.org> 2.8.7-alt2
- added "fuseonly" mode, thanks iv@ (see also #27117)

* Sun Mar 25 2012 Michael Shigorin <mike@altlinux.org> 2.8.7-alt1
- 2.8.7
- spec cleanup

* Tue Oct 04 2011 Evgeny Sinelnikov <sin@altlinux.ru> 2.8.6-alt1
- update to new release

* Fri Apr 29 2011 Denis Smirnov <mithraen@altlinux.ru> 2.8.5-alt3
- add 'cuse' group and grant access to /dev/cuse for 'cuse' group

* Fri Apr 01 2011 Denis Smirnov <mithraen@altlinux.ru> 2.8.5-alt2
- fix compatibility with new udev (thanks to shrek@)

* Fri Mar 25 2011 Alexey Tourbin <at@altlinux.ru> 2.8.5-alt1
- 2.8.5

* Sun Oct 24 2010 Denis Smirnov <mithraen@altlinux.ru> 2.8.3-alt3
- auto rebuild

* Sun Oct 10 2010 Denis Smirnov <mithraen@altlinux.ru> 2.8.3-alt2
- auto rebuild

* Thu Mar 11 2010 Denis Smirnov <mithraen@altlinux.ru> 2.8.3-alt1
- 2.8.3

* Wed Jan 27 2010 Denis Smirnov <mithraen@altlinux.ru> 2.8.2-alt1
- 2.8.2
- CVE-2009-3297 (ALT #22834)

* Thu Nov 12 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.8.1-alt3
- removed requires udev-extras

* Fri Nov 06 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.8.1-alt2
- used ACL

* Thu Sep 17 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.8.1-alt1
- 2.8.1

* Thu Sep 10 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.8.0-alt1
- 2.8.0 release

* Sun Aug 09 2009 L.A. Kostis <lakostis@altlinux.ru> 2.8.0-alt0.1.pre3
- NMU:
  + updated to 2.8.0pre3.
  + remove obsoleted patches.
  + disable -static build by default.
  + disable KM sources (removed by upstream).

* Sun Dec 07 2008 Denis Smirnov <mithraen@altlinux.ru> 2.7.3-alt3
- fix building

* Mon Dec 01 2008 Denis Smirnov <mithraen@altlinux.ru> 2.7.3-alt2
- cleanup spec

* Fri Feb 22 2008 Denis Smirnov <mithraen@altlinux.ru> 2.7.3-alt1
- upstream update to 2.7.3

* Sun Feb 03 2008 Denis Smirnov <mithraen@altlinux.ru> 2.7.1-alt1
- upstream update to 2.7.1
- remove charset conversion patch (upstream add different solution for this)
- remove kernel-source-fuse subpackage

* Sat Mar 17 2007 Denis Smirnov <mithraen@altlinux.ru> 2.6.3-alt2
- add charset conversion patch from Andy Schevchenko (bug 10658)
- add FUSE_ICONV symbol version

* Sun Feb 18 2007 Denis Smirnov <mithraen@altlinux.ru> 2.6.3-alt1
- upstream update

* Fri Dec 15 2006 Denis Smirnov <mithraen@altlinux.ru> 2.6.1-alt1
- upstream update

* Wed Oct 18 2006 Denis Smirnov <mithraen@altlinux.ru> 2.5.3-alt2
- create 'fuse' group
- fix typo in udev rule (9874)

* Mon Jun 19 2006 Denis Smirnov <mithraen@altlinux.ru> 2.5.3-alt1
- version update

* Sat Mar 25 2006 Denis Smirnov <mithraen@altlinux.ru> 2.5.2-alt1
- upstream update

* Sun Nov 27 2005 Denis Smirnov <mithraen@altlinux.ru> 2.4.2-alt1
- version update

* Tue Oct 11 2005 Denis Smirnov <mithraen@altlinux.ru> 2.4-alt1
- version update

* Sat Jun 04 2005 Denis Smirnov <mithraen@altlinux.ru> 2.3-alt1
- version update

* Fri Apr 22 2005 Denis Smirnov <mithraen@altlinux.ru> 2.2-alt6
- fixed req from libfuse to fuse

* Sun Apr 17 2005 Denis Smirnov <mithraen@altlinux.ru> 2.2-alt5
- cleanup
- headers moved to %_includedir/fuse
- static libraries moved to libfuse-devel-static

* Tue Feb 15 2005 Denis Smirnov <mithraen@altlinux.ru> 2.2-alt4
- rename avfs-fuse to fuse

* Thu Feb 10 2005 Denis Smirnov <mithraen@altlinux.ru> 2.2-alt3
- requires fixed

* Sun Feb 06 2005 Denis Smirnov <mithraen@altlinux.ru> 2.2-alt2
- fix

* Sat Feb 05 2005 Denis Smirnov <mithraen@altlinux.ru> 2.2-alt1
- some cleanups from lav@
- version update

* Wed Dec 22 2004 Denis Smirnov <mithraen@altlinux.ru> 2.1-alt2
- control support added (users now can user fusermount without sudo)

* Mon Dec 06 2004 Denis Smirnov <mithraen@altlinux.ru> 2.1-alt1
- version update

* Sat Oct 30 2004 Denis Smirnov <mithraen@altlinux.ru> 1.9-alt1
- version update
- support I/O in deleted files (upstream)
- some spec cleanups

* Tue May 18 2004 Anton Farygin <rider@altlinux.ru> 1.1-alt1
- new version, renamed to avfs-fuse (reselve packagename conflict with Spectrum Emulator fuse)

* Fri Nov 07 2003 Alexander Nekrasov <canis@altlinux.ru> 1.0-alt2
- now FUSE and kernel-source-FUSE build from one spec file

* Thu Nov 06 2003 Alexander Nekrasov <canis@altlinux.ru> 1.0-alt1
- first build
