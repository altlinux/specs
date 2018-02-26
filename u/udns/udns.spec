Name: udns
Version: 0.2
Release: alt1
Summary: A collection of useful DNS resolver utilities
License: LGPLv2+
Group: System/Libraries
URL: http://www.corpit.ru/mjt/udns.html
# http://www.corpit.ru/mjt/udns/%name-%version.tar.gz
Source: %name-%version.tar
Requires: lib%name = %version-%release

%description
UDNS is a stub DNS resolver library with ability to perform both
synchronous and asynchronous DNS queries.

This package provides a collection of useful DNS resolver utilities.

%package -n lib%name
Summary: DNS resolver library for both synchronous and asynchronous DNS queries
Group: System/Libraries

%description -n lib%name
UDNS is a stub DNS resolver library with ability to perform both
synchronous and asynchronous DNS queries.

This package provides libudns shared library.

%package -n lib%name-devel
Summary: Development files for lib%name
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
UDNS is a stub DNS resolver library with ability to perform both
synchronous and asynchronous DNS queries.

This package provides libudns development library and header files.

%prep
%setup

%build
CFLAGS='%optflags' ./configure --enable-ipv6
%make_build shared
mv dnsget{_s,}
mv rblcheck{_s,}

%install
mkdir -p %buildroot{%_libdir,%_bindir,%_includedir,%_man1dir,%_man3dir}
install -pm644 libudns.so.0 %buildroot%_libdir/
ln -s libudns.so.0 %buildroot%_libdir/libudns.so
install -pm755 dnsget rblcheck %buildroot%_bindir/
install -pm644 dnsget.1 rblcheck.1 %buildroot%_man1dir/
install -pm644 udns.3 %buildroot%_man3dir/
install -pm644 udns.h %buildroot%_includedir/

%files
%_bindir/*
%_man1dir/*

%files -n lib%name
%_libdir/libudns.so.*
%doc NEWS NOTES TODO

%files -n lib%name-devel
%_libdir/libudns.so
%_includedir/*
%_man3dir/*

%changelog
* Mon Jan 16 2012 Dmitry V. Levin <ldv@altlinux.org> 0.2-alt1
- Updated to 0.2.
- Rewrote specfile.

* Fri Dec 05 2008 Alexey Sidorov <alexsid@altlinux.ru> 0.0.9-alt2
- Fixed repocop warnings

* Mon May 26 2008 Alexey Sidorov <alexsid@altlinux.ru> 0.0.9-alt1
- Initial build for ALT Linux Sisyphus
