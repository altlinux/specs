Name:           hev-socks5-server
Version:        2.12.0
Release:        alt1
Source:         hev-socks5-server-%version.tar.gz
Source1:        %name.service

Summary:        Simple, lightweight socks5 server.
License:        MIT
Group:          Development/C
URL:            https://hev.cc/
VCS:            https://github.com/heiher/hev-socks5-server

# Automatically added by buildreq on Wed Jun 10 2026
# optimized out: bash5 glibc-kernheaders-generic glibc-kernheaders-x86 libgcc15-devel libgpg-error libhev-socks5-core libhev-task-system libhev-task-system-devel python3 python3-base sh5
BuildRequires: libhev-socks5-core-devel libyaml-devel

%description
HevSocks5Server is a simple, lightweight socks5 server.

Features

    IPv4/IPv6. (dual stack)
    Standard CONNECT command.
    Standard UDP ASSOCIATE command. 1
    Extended FWD UDP command. (UDP in TCP) 2
    Multiple username/password authentication.

%package -n lib%name
Summary:        Library version of %name, a simple, lightweight socks5 server
Group:          Development/C
%description -n lib%name
%summary

%package -n lib%name-devel
Summary:        Development version of lib%name
Group:          Development/C
%description -n lib%name-devel
%summary

%prep
%setup -n hev-socks5-server-%version
sed -i 's/ tp-/ # tp-/g' Makefile
sed -i '/@printf/d' Makefile

%build
%make_build     CFLAGS+=-g \
                V=1 \
                STRIP=/bin/touch \
                LFLAGS="-lhev-socks5-core -Wl,-soname,lib%name.so.0" \
                bin/%name
mv bin/%name %name
make clean
%make_build     CFLAGS+=-g \
                V=1 \
                STRIP=/bin/touch \
                LFLAGS="-lhev-socks5-core -Wl,-soname,lib%name.so.0" \
                bin/lib%name.so

%install
install -D %name %buildroot/%_bindir/%name
install -D bin/lib%name.so %buildroot/%_libdir/lib%name.so.0
ln -sr %buildroot/%_libdir/lib%name.so.0 %buildroot/%_libdir/lib%name.so
mkdir -p %buildroot%_includedir
install -m644 src/*.h %buildroot%_includedir/
install -m644 src/misc/*.h %buildroot%_includedir/
install -m644 -D %SOURCE1 %buildroot%systemd_unitdir/%name.service

%files
%doc README* conf
%_bindir/*
%systemd_unitdir/%name.service

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so

%changelog
* Wed Jun 10 2026 Fr. Br. George <george@altlinux.org> 2.12.0-alt1
- Initial build for ALT
