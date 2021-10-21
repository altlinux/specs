Name: libsixel
Version: 1.8.5
Release: alt2

Summary: A SIXEL encoder/decoder implementation
License: MIT
Group: System/Libraries
URL: https://github.com/saitoha/libsixel

Source0: %name-%version.tar


# Automatically added by buildreq on Fri Nov 23 2018 (-bb)
# optimized out: elfutils fontconfig glib2-devel glibc-kernheaders-generic glibc-kernheaders-x86 gnu-config libgdk-pixbuf libgio-devel libsasl2-3 perl pkg-config python-base python-modules python-modules-encodings python3 python3-base rpm-build-python3 sh3 tzdata xz zlib-devel
BuildRequires: libcurl-devel libgd3-devel libgdk-pixbuf-devel libjpeg-devel libnss-myhostname libpng-devel libpython3 python-modules-distutils

%description
This package provides encoder/decoder implementation for DEC SIXEL graphics,
and some converter programs.

%package -n libsixel1
Summary: %summary
Group: System/Libraries

%description -n  libsixel1
%summary

%package -n sixel-utils
Summary: %summary
Group: Graphics

%description -n sixel-utils
%summary

%package -n libsixel-devel
Summary: %summary
Group: Development/C

%description -n libsixel-devel
%summary

%prep
%setup -q

%build
%autoreconf -fisv
%configure \
    --disable-rpath \
    --with-gdk-pixbuf2 \
    --with-gd \
    --with-libcurl \
    --with-jpeg \
    --with-png
%make_build


%install
%makeinstall_std

rm -fv %buildroot%_libdir/*.a

%files -n sixel-utils
%_bindir/img2sixel
%_bindir/sixel2png
%_man1dir/*
%_man5dir/*
/usr/share/zsh/site-functions/*
/usr/share/bash-completion/completions/*


%files -n libsixel1
%_libdir/%name.so.*
%files devel
%_libdir/%name.so
%_pkgconfigdir/%name.pc
%_includedir/sixel.h
%_bindir/%name-config

%changelog
* Thu Oct 21 2021 Grigory Ustinov <grenka@altlinux.org> 1.8.5-alt2
- fixed FTBFS.

* Wed Sep 30 2020 Fr. Br. George <george@altlinux.ru> 1.8.5-alt1
- update to 1.8.5

* Mon Nov 26 2018 Denis Smirnov <mithraen@altlinux.ru> 1.8.2-alt2
- remove static library

* Fri Nov 23 2018 Denis Smirnov <mithraen@altlinux.ru> 1.8.2-alt1
- first build for Sisyphus


