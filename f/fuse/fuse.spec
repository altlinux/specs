%define _unpackaged_files_terminate_build 1

Name: fuse
Version: 2.9.9
Release: alt3

Summary: a tool for creating virtual filesystems
License: GPLv2
Group: System/Kernel and hardware

Url: https://github.com/libfuse/

Source: %name-%version.tar
Source1: fuserumount

Patch: %name-%version.patch

Requires: mount >= 2.11
Provides: avfs-fuse = %version
Obsoletes: avfs-fuse < %version
Requires(pre): fuse-common >= 1.1.0

%description
FUSE (Filesystem in USErspace), an excellent tool
for creating custom filesystems with minimal effort
as well as for using them.

%package -n lib%name
License: LGPLv2
Group: System/Kernel and hardware
Summary: tool for creating virtual filesystems
Provides: FUSE = %version avfs-fuse = %version libavfs-fuse = %version
Obsoletes: FUSE < %version avfs-fuse < %version libavfs-fuse < %version

%description -n lib%name
FUSE (Filesystem in USErspace), an excellent tool
for creating custom filesystems with minimal effort.

This package contains shared libraries.

%package -n lib%name-devel
License: LGPLv2
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
%patch -p1

%build
mkdir -p m4
cp /usr/share/gettext/config.rpath ./config.rpath
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

rm -f %buildroot%_sysconfdir/udev/rules.d/*

install -pD %SOURCE1 %buildroot%_bindir/fuserumount
rm -f %buildroot/etc/init.d/fuse

%pre
if [ $1 -ge 2 -o -e %_bindir/fusermount3 ]; then
    %_sbindir/control-dump fusermount
fi

%post
if [ $1 -ge 2 -o -e %_bindir/fusermount3 ]; then
    %_sbindir/control-restore fusermount
else
    %_sbindir/control fusermount fuseonly
fi

%files
%doc AUTHORS NEWS README.md README.NFS doc/how-fuse-works doc/kernel.txt
/sbin/mount.fuse
%attr(4710,root,fuse) %_bindir/fusermount
%_bindir/ulockmgr_server
%attr(0755,root,root) %_bindir/fuserumount
%_man1dir/*
%_man8dir/*

%files -n lib%name
/%_lib/lib%name.so.*
%_libdir/lib*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/lib*.so
%_pkgconfigdir/*.pc

%changelog
* Tue Apr 12 2022 Alexey Shabalin <shaba@altlinux.org> 2.9.9-alt3
- build from upstream upstream/fuse_2_9_bugfix branch
- deleted depends on fuse in libfuse (ALT#38714)
- make buffer size match kernel max transfer size

* Tue Jan 11 2022 Evgeny Sinelnikov <sin@altlinux.org> 2.9.9-alt2
- Fix build with closefrom() from newest unistd.h
- Adjust license to GPLv2 and LGPLv2 for library

* Mon Feb 04 2019 Rustem Bapin <rbapin@altlinux.org> 2.9.9-alt1
- 2.9.9
- fuserumount move back from fuse-common
- pre- and postinstall scriptlets are modified to take account mode of already installed fuse3 package

* Wed Apr 11 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.9.7-alt3
- pick mainline 914871b, fixes build on aarch64

* Tue Jul 25 2017 Denis Smirnov <mithraen@altlinux.ru> 2.9.7-alt2
- split fuse-common to separate package (for fuse3 compatibility)

* Sat Aug 13 2016 Denis Smirnov <mithraen@altlinux.ru> 2.9.7-alt1
- 2.9.7

* Sun Sep 06 2015 Denis Smirnov <mithraen@altlinux.ru> 2.9.4-alt3
- fix fuserumount script access (ALT#31225)

* Mon Aug 24 2015 Denis Smirnov <mithraen@altlinux.ru> 2.9.4-alt2
- add fuserumount script (ALT#31225)

* Wed May 27 2015 Denis Smirnov <mithraen@altlinux.ru> 2.9.4-alt1
- 2.9.4

* Sun Feb 09 2014 Denis Smirnov <mithraen@altlinux.ru> 2.9.3-alt4
- fix wheelonly mode, thanks legion@ (ALT#29814)

* Wed Jan 29 2014 Michael Shigorin <mike@altlinux.org> 2.9.3-alt3
- drop cuse.conf: conflicts with another one, see #29444 (ALT#29777)

* Thu Oct 10 2013 Denis Smirnov <mithraen@altlinux.ru> 2.9.3-alt2
- not use /lib/udev/devices (ALT#29444)

* Mon Aug 05 2013 Denis Smirnov <mithraen@altlinux.ru> 2.9.3-alt1
- 2.9.3

* Wed Apr 24 2013 Denis Smirnov <mithraen@altlinux.ru> 2.9.2-alt2
- repocop fixes

* Mon Nov 19 2012 Pavel Shilovsky <piastry@altlinux.org> 2.9.2-alt1
- 2.9.2
- remove mmap patch

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
