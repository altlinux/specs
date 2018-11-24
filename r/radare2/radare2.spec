Summary: A reverse engineering framework
Name: radare2
Version: 2.8.0
Release: alt1
License: %lgpl3plus
Group: Development/Tools
Url: http://radare.org/
Source: %name-%version.tar
Packager: Nikita Ermakov <arei@altlinux.org>

BuildRequires: rpm-build-licenses libzip-devel zlib-devel libmagic-devel git-core libnss-mdns python3-module-yieldfrom java-devel-default jna python-devel capstone-devel

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
%configure --with-syscapstone --with-sysmagic --with-syszip
sed -i -- 's|-lm|-lm\ -L\.\./util -lr_util|g' libr/hash/Makefile
LDFLAGS="-lutil -ldl -lpthread -lm" DESTDIR=%buildroot CFLAGS="%optflags -fPIC -I../include" LIBDIR=%_libdir PREFIX=%prefix DATADIR=%_datadir %make_build

%install
NOSUDO=1 LIBDIR=%_libdir PREFIX=%prefix make install DESTDIR=%buildroot
rm -f %buildroot/%_libdir/libr_shlr.a
cp -r shlr/heap/include/r_jemalloc %buildroot/%_includedir/

%files devel
%_libdir/pkgconfig/*.pc
%_includedir/libr/
%_includedir/r_jemalloc/

%files
%doc AUTHORS.md DEVELOPERS.md COPYING COPYING.LESSER CONTRIBUTING.md README.md
%_docdir/%name
%_bindir/*
%_libdir/libr*.so*
%_datadir/%name/
%_mandir/man1/*
%_mandir/man7/*
%_libdir/%name/

%changelog
* Mon Nov 12 2018 Nikita Ermakov <arei@altlinux.org> 2.8.0-alt1
- Updated to 2.8.0.

* Fri Jun 29 2018 Nikita Ermakov <arei@altlinux.org> 2.7.0-alt1
- Initial build for ALT Linux Sisyphus
