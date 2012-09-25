%define realname aufs3-util

Name: aufs3-util
Version: 3.0
Release: alt0.1

Group: System/Base
Summary: Utilities for aufs3
License: %gpl2plus
Url: http://aufs.sourceforge.net
Packager: Andriy Stepanov <stanv@altlinux.ru>

Source: %realname-%version.tar
Source1: aufs_type.h

BuildRequires: rpm-build-licenses
BuildRequires: kernel-headers >= 3.0.0
BuildRequires: glibc-devel-static

Conflicts: aufs2-util-ng
Conflicts: aufs2-util

%description
These utilities are always necessary for aufs3
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
* Tue Sep 25 2012 Andriy Stepanov <stanv@altlinux.ru> 3.0-alt0.1
- Upstream cc453fadac git commit.

