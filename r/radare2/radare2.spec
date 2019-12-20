Summary: A reverse engineering framework
Name: radare2
Version: 4.1.1
Release: alt1
License: %lgpl3plus
Group: Development/Tools
Url: http://radare.org/
Source: %name-%version.tar
Packager: Nikita Ermakov <arei@altlinux.org>

BuildRequires: rpm-build-licenses libzip-devel zlib-devel libmagic-devel git-core libnss-mdns python3-module-yieldfrom java-devel-default jna python-devel capstone-devel libxxhash-devel liblz4-devel meson openssl-devel libuv-devel

# bundled sdb ./shlr/sdb/README.md
# bundled js0n ./shlr/sdb/src/json/README
# bundled openbsdregex libr/util/regex/README
# bundled tcc ./shlr/tcc/README.md
# bundled binutils 2.13  ./libr/asm/arch/tricore/README.md
#                        ./libr/asm/arch/ppc/gnu/
#                        ./libr/asm/arch/arm/gnu/
# bundled vavrdisasm 1.6 ./libr/asm/arch/avr/README

%description
A reverse engineering framework and command line tools.

%package devel
Summary: Development files for %name
License: %lgpl3plus
Group: Development/Tools
Requires: %name = %version-%release
%description devel
Development files for %name package.

%prep
%setup

%build
%meson                    \
  -Duse_sys_magic=true    \
  -Duse_sys_zip=true      \
  -Duse_sys_zlib=true     \
  -Duse_sys_lz4=true      \
  -Duse_sys_xxhash=true   \
  -Duse_sys_openssl=true  \
  -Duse_libuv=true        \
  -Duse_sys_capstone=true
%meson_build

%install
%meson_install
# Remove static library
rm -f %buildroot/%_libdir/libr_shlr.a
# Remove package manager
rm %buildroot/%_bindir/r2pm
# Copy r_jemalloc to the include directory
cp -r shlr/heap/include/r_jemalloc %buildroot/%_includedir/
# Create symbolic link to the radare2.
# Some programs (e.g. rahash2) looking for r2 instead of radare2.
ln -s radare2 %buildroot/usr/bin/r2

%files devel
%_libdir/pkgconfig/*.pc
%_includedir/libr/
%_includedir/r_jemalloc/

%files
%doc AUTHORS.md DEVELOPERS.md COPYING COPYING.LESSER CONTRIBUTING.md README.md
%doc %_docdir/%{name}
%_bindir/*
%_libdir/libr*.so*
%_datadir/%name/
%_mandir/man1/*
%_mandir/man7/*
%_datadir/zsh

%changelog
* Fri Dec 20 2019 Nikita Ermakov <arei@altlinux.org> 4.1.1-alt1
- Update to 4.1.1.

* Thu Dec 19 2019 Nikita Ermakov <arei@altlinux.org> 4.1.0-alt1
- Update to 4.1.0.

* Tue Sep 17 2019 Nikita Ermakov <arei@altlinux.org> 3.9.0-alt1
- Update to 3.9.0.

* Tue Sep  3 2019 Nikita Ermakov <arei@altlinux.org> 3.8.0-alt1
- Update to 3.8.0.

* Thu Aug 29 2019 Nikita Ermakov <arei@altlinux.org> 3.7.0-alt2
- Create symbolic link to the radare2.

* Thu Aug 01 2019 Nikita Ermakov <arei@altlinux.org> 3.7.0-alt1
- Update to 3.7.0.

* Thu Jun 27 2019 Nikita Ermakov <arei@altlinux.org> 3.6.0-alt1
- Update to 3.6.0.

* Thu May 16 2019 Nikita Ermakov <arei@altlinux.org> 3.5.1-alt1
- Updated to 3.5.1.

* Mon May 13 2019 Nikita Ermakov <arei@altlinux.org> 3.5.0-alt1
- Updated to 3.5.0.

* Mon Apr 15 2019 Nikita Ermakov <arei@altlinux.org> 3.4.1-alt1
- Updated to 3.4.1.
- Moved from "make" to "meson".
- Use system wide lz4 library (ALT bug #36395).

* Mon Feb 20 2019 Nikita Ermakov <arei@altlinux.org> 3.3.0-alt1
- Updated to 3.3.0.

* Mon Feb 04 2019 Nikita Ermakov <arei@altlinux.org> 3.2.1-alt1
- Updated to 3.2.1.

* Mon Dec 17 2018 Nikita Ermakov <arei@altlinux.org> 3.1.3-alt1
- Updated to 3.1.3.

* Mon Nov 12 2018 Nikita Ermakov <arei@altlinux.org> 2.8.0-alt1
- Updated to 2.8.0.

* Fri Jun 29 2018 Nikita Ermakov <arei@altlinux.org> 2.7.0-alt1
- Initial build for ALT Linux Sisyphus
