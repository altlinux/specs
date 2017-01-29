Name: ostree
Version: 2017.1
Release: alt1

Summary: Linux-based operating system develop/build/deploy tool

# Source-url: https://github.com/ostreedev/ostree/archive/v%version.tar.gz
Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %name-%version.tar

# Source1-url: https://git.gnome.org/browse/libglnx/snapshot/libglnx-master.tar.xz
Source1: libglnx.tar

# Source2-url: https://github.com/mendsley/bsdiff/archive/master.zip
Source2: bsdiff.tar

# The libostree.so (currently private) shared library, and almost all
# of the utilities are licensed under the LGPLv2+.  Only at present
# one utility program (ostree-switch-root) is forked from util-linux under
# the GPL.
# The BSD is there basically just for some random scripts, nothing
# important.
# As always, consult the upstream COPYING file, and individual source
# files for the canonical license status.

License: LGPLv2+ and GPLv2+ and BSD
Group: Other
Url: https://github.com/ostreedev/ostree


# manually removed: db2latex-xsl glibc-devel-static gobject-introspection-devel python-module-mwlib python3-dev python3-module-yieldfrom python3-module-zope ruby ruby-stdlibs 

# We always run autogen.sh
# Automatically added by buildreq on Sun Sep 25 2016
# optimized out: dconf docbook-dtds docbook-style-xsl glib-networking glib2-devel gnu-config gobject-introspection libgio-devel libgpg-error libgpg-error-devel perl pkg-config python-base python-devel python-module-google python-modules python-modules-compiler python-modules-encodings python-modules-xml python3 python3-base xml-common xsltproc
BuildRequires: gtk-doc gvfs libGConf libarchive-devel libe2fs-devel libfuse-devel libgpgme-devel liblzma-devel libsoup-devel time zlib-devel

BuildRequires: autoconf automake libtool
# Too bad there isn't a pkg-config file =(
BuildRequires: libattr-devel
# For docs
BuildRequires: gtk-doc

# BEGIN SourceDeps(oneline):
BuildRequires: %_bindir/xsltproc pkgconfig(libarchive)

# TODO
#Requires: linux-user-chroot

BuildRequires: pkgconfig(gio-unix-2.0)
BuildRequires: pkgconfig(libsoup-2.4)

BuildPreReq: libgpgme-devel liblzma-devel

Source44: import.info

Requires: libostree = %version-%release

%description
See http://live.gnome.org/OSTree

%package -n libostree
Summary: Library files of %name
Group: Development/C
License: LGPLv2

%description -n libostree
Library files of %name.


%package -n libostree-devel
Summary: Library and header files of %name
Group: Development/C
License: LGPLv2
Requires: libostree = %version-%release

%description -n libostree-devel
Development package containing library and header files of %name.


%prep
%setup -a1 -a2

%build
NOCONFIGURE=1 sh -x ./autogen.sh

%configure --disable-silent-rules \
	   --enable-documentation \
	   --disable-grub2-hook \
	   --without-dracut --without-grub2 \
	   --without-grub2-mkconfig-path
%make_build

%install
%makeinstall_std

rm -rf %buildroot/etc/dracut.conf.d/ %buildroot/usr/lib/dracut/
rm -rf %buildroot%_sysconfdir/grub.d/15_ostree
%files
%doc COPYING README.md
#%_sysconfdir/grub.d/15_ostree
%_bindir/ostree
%_bindir/rofiles-fuse
%_libexecdir/%name/
%exclude /usr/lib/ostree/grub2-15_ostree
%_datadir/%name/

# due missed buildreqs
#%_typelibdir/*.typelib
#%_girdir/*.gir

%_man1dir/*
%_man5dir/ostree*

%files -n libostree
%_libdir/libostree*.so.*

%files -n libostree-devel
%_includedir/ostree-1/
%_libdir/libostree*.so
%_pkgconfigdir/*.pc

%changelog
* Sun Jan 29 2017 Vitaly Lipatov <lav@altlinux.ru> 2017.1-alt1
- new version 2017.1 (with rpmrb script)

* Tue Jan 03 2017 Vitaly Lipatov <lav@altlinux.ru> 2016.15-alt1
- new version 2016.15 (with rpmrb script)

* Mon Dec 05 2016 Vitaly Lipatov <lav@altlinux.ru> 2016.12-alt1
- new version 2016.12 (with rpmrb script)

* Sat Sep 24 2016 Vitaly Lipatov <lav@altlinux.ru> 2016.10-alt1
- new version 2016.10 (with rpmrb script)

* Sat Sep 24 2016 Vitaly Lipatov <lav@altlinux.ru> 2016.8-alt1
- new version (2016.8) with rpmgs script

* Fri Apr 26 2013 Igor Vlasenko <viy@altlinux.ru> 2013.2-alt1_1
- initial fc import

