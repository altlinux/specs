%def_disable check

Name: ostree
Version: 2019.6
Release: alt1

Summary: Linux-based operating system develop/build/deploy tool
License: LGPLv2+
Group: Development/Other
Url: https://github.com/ostreedev/ostree

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/ostreedev/ostree/releases/download/v%version/lib%name-%version.tar.gz
Source: %name-%version.tar
# Note! Always use HEAD!!
# Source1-url: https://github.com/GNOME/libglnx/archive/master.zip
Source1: libglnx.tar
# Source2-url: https://github.com/mendsley/bsdiff/archive/master.zip
Source2: bsdiff.tar

Source44: import.info

Requires: libostree = %version-%release
Requires: %_bindir/gpg2

BuildRequires: db2latex-xsl libarchive-devel libe2fs-devel
BuildRequires: libfuse-devel libgpgme-devel liblzma-devel libsystemd-devel
BuildRequires: zlib-devel libselinux-devel libcurl-devel libssl-devel
BuildRequires: libgpgme-devel liblzma-devel libmount-devel
BuildRequires: gobject-introspection-devel
BuildRequires: libsoup-devel libattr-devel
BuildRequires: libavahi-glib-devel libgjs-devel
# For docs
BuildRequires: gtk-doc

%description
See https://ostree.readthedocs.io/en/latest/

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

%package -n libostree-devel-doc
Summary: Development documentation for lib%name
Group: Development/Documentation
BuildArch: noarch

%description -n libostree-devel-doc
This package contains development documentation for lib%name.

%prep
%setup -a1 -a2
%__subst 's|$(prefix)\(/lib/tmpfiles.d\)|\1|g' Makefile-boot.am

%build
NOCONFIGURE=1 sh -x ./autogen.sh

%configure --disable-silent-rules \
	   --without-dracut \
           --with-selinux \
           --with-curl \
           --with-openssl \
           --enable-gtk-doc \
	   --without-grub2-mkconfig-path

# hack to fix missed dirname declaration
echo "#include <libgen.h>" >>config.h

%make_build

%install
%makeinstall_std
rm -rf %buildroot/etc/dracut.conf.d/ %buildroot/usr/lib/dracut/
rm -rf %buildroot%_sysconfdir/grub.d/15_ostree
rm -rf %buildroot/lib/systemd/system-generators/ostree-system-generator

%check
%make check

%files
%doc COPYING README.md
#%_sysconfdir/grub.d/15_ostree
%_bindir/ostree
%_bindir/rofiles-fuse
%_libexecdir/lib%name/
%_libexecdir/%name/
%exclude /usr/lib/libostree/grub2-15_ostree
%_datadir/%name/
%_unitdir/ostree-prepare-root.service
%_unitdir/ostree-remount.service
%_tmpfilesdir/ostree-tmpfiles.conf
%_datadir/bash-completion/completions/ostree
%_unitdir/ostree-finalize-staged.service
%_unitdir/ostree-finalize-staged.path
%_typelibdir/*.typelib
%_man1dir/*
%_man5dir/ostree*

%files -n libostree
%_libdir/libostree*.so.*

%files -n libostree-devel
%_includedir/ostree-1/
%_libdir/libostree*.so
%_pkgconfigdir/*.pc
%_girdir/*.gir

%files -n libostree-devel-doc
%_datadir/gtk-doc/html/ostree/

%changelog
* Mon Dec 16 2019 Yuri N. Sedunov <aris@altlinux.org> 2019.6-alt1
- 2019.6

* Sun Nov 03 2019 Yuri N. Sedunov <aris@altlinux.org> 2019.5-alt1
- 2019.5

* Tue Apr 30 2019 Yuri N. Sedunov <aris@altlinux.org> 2019.2-alt1
- 2019.2

* Mon Jan 14 2019 Yuri N. Sedunov <aris@altlinux.org> 2019.1-alt1
- 2019.1

* Thu Nov 29 2018 Yuri N. Sedunov <aris@altlinux.org> 2018.9-alt1
- updated to v2018.9-10-g05e8c7ef

* Fri Sep 14 2018 Yuri N. Sedunov <aris@altlinux.org> 2018.8-alt1
- updated to v2018.8-7-ge4e6d85e

* Wed Aug 29 2018 Yuri N. Sedunov <aris@altlinux.org> 2018.7-alt2
- rebuilt with openssl-1.1

* Mon Jul 23 2018 Yuri N. Sedunov <aris@altlinux.org> 2018.7-alt1
- updated to v2018.7-2-g93da568
- some spec cleanup

* Fri Jun 08 2018 Vitaly Lipatov <lav@altlinux.ru> 2018.5-alt2
- enable gtk-doc build
- enable build with libcurl, openssl, selinux

* Fri Jun 08 2018 Vitaly Lipatov <lav@altlinux.ru> 2018.5-alt1
- new version (2018.5) with rpmgs script

* Sat Feb 24 2018 Vitaly Lipatov <lav@altlinux.ru> 2018.2-alt1
- new version 2018.2 (with rpmrb script)

* Wed Feb 07 2018 Vitaly Lipatov <lav@altlinux.ru> 2018.1-alt1
- new version 2018.1 (with rpmrb script)

* Sun Dec 24 2017 Vitaly Lipatov <lav@altlinux.ru> 2017.14-alt1
- new version 2017.14 (with rpmrb script)

* Sat Dec 09 2017 Vitaly Lipatov <lav@altlinux.ru> 2017.13-alt1
- new version 2017.13 (with rpmrb script)

* Sun Oct 08 2017 Vitaly Lipatov <lav@altlinux.ru> 2017.12-alt1
- new version 2017.12 (with rpmrb script)

* Sat Oct 07 2017 Vitaly Lipatov <lav@altlinux.ru> 2017.11-alt1
- new version 2017.11 (with rpmrb script)

* Sat Jul 22 2017 Vitaly Lipatov <lav@altlinux.ru> 2017.8-alt1
- new version 2017.8 (with rpmrb script)

* Tue May 09 2017 Vitaly Lipatov <lav@altlinux.ru> 2017.5-alt1
- new version 2017.5 (with rpmrb script)

* Wed Mar 15 2017 Vitaly Lipatov <lav@altlinux.ru> 2017.3-alt1
- new version 2017.3 (with rpmrb script)

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

