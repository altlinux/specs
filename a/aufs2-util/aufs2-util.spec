%define realname aufs2-util

Name: aufs2-util
Version: 2.1
Release: alt3.git0f0cf3f

Group: System/Base
Summary: Utilities for aufs2.1
License: %gpl2plus
Url: http://aufs.sourceforge.net
Packager: Andriy Stepanov <stanv@altlinux.ru>

Source: %realname-%version.tar
Source1: aufs_type.h

BuildRequires: rpm-build-licenses
BuildRequires: kernel-headers >= 2.6.35
BuildRequires: glibc-devel-static

Conflicts: aufs2-util-ng

%description
These utilities are always necessary for aufs2.1
If you forget to install them, your aufs may not work correctly.

%prep
%setup -q -n %realname-%version
install -d %_builddir/%realname-%version/include/linux
install -m0644 -p %{S:1} %_builddir/%realname-%version/include/linux
sed -i 's,-o root -g root,,' Makefile
make clean
find -name \*.a -or -name \*.so -exec rm -f '{}' \;
sed -i '/install_ulib: Tgt/ s,/usr/lib,%_libdir,' libau/Makefile

%build
%add_optflags -I%_builddir/%realname-%version/include
export CFLAGS="%optflags"
%make_build KDIR=%_includedir/linux

%install
%make install DESTDIR=%buildroot

%files
%config(noreplace) %_sysconfdir/default/aufs
%_bindir/*
%_libdir/*so*
/sbin/*
%_man5dir/*.*


%changelog
* Tue Apr 26 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 2.1-alt3.git0f0cf3f
- conflicts fixed

* Tue Feb 22 2011 Mykola Grechukh <gns@altlinux.ru> 2.1-alt2.git0f0cf3f
- 2011-02-14 snapshot

* Thu Nov 18 2010 Mykola Grechukh <gns@altlinux.ru> 2.1-alt1
- new version. Incompatible with sisyphus kernels

* Mon Jun 22 2009 Andriy Stepanov <stanv@altlinux.ru> 0.0-alt1
- Initial build for ALT Linux.

