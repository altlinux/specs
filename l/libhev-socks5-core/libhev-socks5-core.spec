Name:           libhev-socks5-core
Version:        1.6.2
Release:        alt1
Source:         hev-socks5-core-%version.tar.gz

Summary:        Simple, lightweight socks5 library
License:        MIT
Group:          Development/C
URL:            https://hev.cc/
VCS:            https://github.com/heiher/hev-socks5-core

BuildRequires: libhev-task-system-devel

%description
HevSocks5Core is a simple, lightweight socks5 library.

Features

    IPv4/IPv6. (dual stack)
    Standard CONNECT command.
    Standard UDP ASSOCIATE command.
    Extended FWD UDP command. (UDP in TCP)
    Multiple username/password authentication.

%package devel
Summary:        Development version of %name
Group:          Development/C
%description devel
%summary

%prep
%setup -n hev-socks5-core-%version

%build
%__cc %optflags -fPIC -shared -Wl,-soname,%name.so.0 src/*.c -o %name.so -lhev-task-system

%install
install -D %name.so %buildroot%_libdir/%name.so.0
ln -sr %buildroot%_libdir/%name.so.0 %buildroot%_libdir/%name.so
mkdir -p %buildroot%_includedir
install -m644 include/* %buildroot%_includedir/

%files
%doc README*
%_libdir/%name.so.0

%files devel
%_libdir/%name.so
%_includedir/hev-*

%changelog
* Wed Jun 10 2026 Fr. Br. George <george@altlinux.ru> 1.6.2-alt1
- Initial build for ALT


