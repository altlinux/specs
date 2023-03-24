%def_disable check
%{!?_systemdgeneratordir: %global _systemdgeneratordir /lib/systemd/system-generators}
%define _libexecdir %_usr/libexec
%def_with tests
%def_with ed25519

Name: ostree
Version: 2023.2
Release: alt1

Summary: Linux-based operating system develop/build/deploy tool
License: LGPLv2+
Group: Development/Other
Url: https://github.com/ostreedev/ostree

Vcs: https://github.com/ostreedev/ostree.git
Source: %name-%version.tar
# Note! Always use HEAD!!
# Source1-url: https://github.com/GNOME/libglnx/archive/master.zip
Source1: libglnx.tar
# Source2-url: https://github.com/mendsley/bsdiff/archive/master.zip
Source2: bsdiff.tar

Patch1: %name-%version.patch

Requires: libostree = %EVR
Requires: %_bindir/gpg2

BuildRequires(pre): rpm-macros-systemd

# Core requirements
BuildRequires: pkgconfig(gio-unix-2.0) >= 2.66.0
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(libcurl) >= 7.29.0
BuildRequires: pkgconfig(libcrypto) >= 1.0.1
# The tests still require soup
BuildRequires: pkgconfig(libsoup-2.4) >= 2.39.1
BuildRequires: libattr-devel
# The tests require attr
BuildRequires: attr
# Extras
BuildRequires: pkgconfig(libarchive) >= 2.8.0
BuildRequires: pkgconfig(liblzma) >= 5.0.5
BuildRequires: pkgconfig(libselinux) >= 2.1.13
BuildRequires: pkgconfig(mount)
BuildRequires: pkgconfig(fuse)
BuildRequires: pkgconfig(e2p)
BuildRequires: libcap-devel
BuildRequires: pkgconfig(gpgme) >= 1.1.8 pkgconfig(gpg-error)
%{?_with_ed25519:BuildRequires: pkgconfig(libsodium) >= 1.0.14}
BuildRequires: pkgconfig(libsystemd) pkgconfig(systemd)
BuildRequires: /usr/bin/g-ir-scanner
BuildRequires: dracut
BuildRequires: bison

#BuildRequires: libavahi-glib-devel libgjs-devel

# For docs
BuildRequires: gtk-doc
BuildRequires: xsltproc docbook-style-xsl

%description
libostree is a shared library designed primarily for
use by higher level tools to manage host systems (e.g. rpm-ostree),
as well as container tools like flatpak and the atomic CLI.

%package grub2
Summary: GRUB2 integration for OSTree
Group: System/Configuration/Boot and Init
%ifnarch aarch64 %arm
Requires: grub2
%else
Requires: grub2-efi
%endif
Requires: %name

%description grub2
GRUB2 integration for OSTree

%package tests
Summary: Tests for the %name package
Group: Development/Other
Requires: %name = %EVR

%description tests
This package contains tests that can be used to verify
the functionality of the installed %name package.

%package -n lib%name
Summary: Library files of %name
Group: System/Libraries
License: LGPLv2

%description -n lib%name
Library files of %name.

%package -n lib%name-devel
Summary: Library and header files of %name
Group: Development/C
License: LGPLv2
Requires: lib%name = %version-%release

%description -n lib%name-devel
Development package containing library and header files of %name.

%package -n lib%name-devel-doc
Summary: Development documentation for lib%name
Group: Development/Documentation
BuildArch: noarch

%description -n lib%name-devel-doc
This package contains development documentation for lib%name.

%prep
%setup -a1 -a2
%patch1 -p1
%__subst 's|$(prefix)\(/lib/tmpfiles.d\)|\1|g' Makefile-boot.am

%build
NOCONFIGURE=1 sh -x ./autogen.sh

%configure --disable-silent-rules \
           --with-selinux \
           --with-curl \
           --with-openssl \
           %{?_with_ed25519:--with-ed25519-libsodium} \
           --enable-gtk-doc \
           --enable-trivial-httpd-cmdline \
           --with-builtin-grub2-mkconfig \
           --without-grub2-mkconfig-path \
           %{?with_tests:--enable-installed-tests=exclusive} \
           --with-dracut=yesbutnoconf

#           --with-dracut \

# hack to fix missed dirname declaration
#echo "#include <libgen.h>" >>config.h

%make_build

%install
%makeinstall_std

%check
%make check

# Needed to enable the service at compose time currently
%post
%systemd_post ostree-remount.service

%preun
%systemd_preun ostree-remount.service

%files
%doc COPYING README.md
#%_sysconfdir/grub.d/15_ostree
%_bindir/%name
%_bindir/rofiles-fuse
%_datadir/%name
%_datadir/bash-completion/completions/%name
#%_sysconfdir/dracut.conf.d/*
%prefix/lib/dracut/modules.d/*
%_systemdgeneratordir/ostree-system-generator
%_unitdir/ostree-*
%_tmpfilesdir/*.conf
%_libexecdir/lib%name
%_prefix/lib/%name
%_man1dir/*
%_man5dir/ostree*
#%exclude %_sysconfdir/grub.d/*ostree
#%exclude %_libexecdir/lib%name/grub2*
%exclude %_libexecdir/lib%name/ostree-trivial-httpd

#%files grub2
#%_sysconfdir/grub.d/*ostree
#%_libexecdir/lib%name/grub2*

%if_with tests
%files tests
#%_libexecdir/installed-tests
#%_datadir/installed-tests
%_libexecdir/libostree/ostree-trivial-httpd
%endif

%files -n lib%name
%_libdir/*.so.*
%_typelibdir/*.typelib

%files -n lib%name-devel
%_includedir/ostree-1
%_libdir/*.so
%_pkgconfigdir/*.pc
%_girdir/*.gir

%files -n lib%name-devel-doc
%_datadir/gtk-doc/html/%name

%changelog
* Fri Mar 24 2023 Alexey Shabalin <shaba@altlinux.org> 2023.2-alt1
- 2023.2

* Wed Jan 11 2023 Alexey Shabalin <shaba@altlinux.org> 2022.7-alt1
- 2022.7

* Sat Jul 30 2022 Alexey Shabalin <shaba@altlinux.org> 2022.5-alt1
- 2022.5

* Wed Jun 15 2022 Alexey Shabalin <shaba@altlinux.org> 2022.4-alt1
- 2022.4

* Mon Mar 28 2022 Alexey Shabalin <shaba@altlinux.org> 2022.2-alt2
- build with ed25519 sign support (ALT#42271)

* Wed Mar 23 2022 Alexey Shabalin <shaba@altlinux.org> 2022.2-alt1
- 2022.2

* Tue Jan 11 2022 Alexey Shabalin <shaba@altlinux.org> 2022.1-alt1
- 2022.1
- define /usr/libexec as %%_libexecdir
- update BR
- add tests package
- build --with-dracut=xyesbutnoconf
- build without avahi support

* Wed Nov 24 2021 Andrey Sokolov <keremet@altlinux.org> 2021.6-alt1
- 2021.6

* Tue Oct 05 2021 Andrey Sokolov <keremet@altlinux.org> 2021.3-alt3
- mount readonly /bin, /sbin, /lib, /lib64, /libx32

* Fri Jul 30 2021 Andrey Sokolov <keremet@altlinux.org> 2021.3-alt2
- add ignition support to grub.cfg generator

* Thu Jul 22 2021 Andrey Sokolov <keremet@altlinux.org> 2021.3-alt1
- GRUB2 configuration file generation using built-in script
- set GRUB timeout to 5

* Fri Jul 09 2021 Andrey Sokolov <keremet@altlinux.org> 2021.2-alt2
- add trivial-httpd command

* Tue Jul 06 2021 Andrey Sokolov <keremet@altlinux.org> 2021.2-alt1
- 2021.2
- remove unused file import.info

* Fri Jul 02 2021 Andrey Sokolov <keremet@altlinux.org> 2020.8-alt2
- add dracut module

* Sun Jan 17 2021 Yuri N. Sedunov <aris@altlinux.org> 2020.8-alt1
- 2020.8

* Thu Jun 25 2020 Yuri N. Sedunov <aris@altlinux.org> 2020.3-alt1
- 2020.3

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

