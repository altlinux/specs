# IPv6 support seems broken
%def_disable ipv6

Name: libircclient
Version: 1.3
Release: alt1

Summary: Library that implements the client-server IRC protocol
License: %lgpl2plus
Group: System/Libraries

URL: http://libircclient.sourceforge.net/
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses
BuildRequires: gcc-c++

%description
libircclient is a small but powerful library that implements the
client-server IRC protocol. It has all features needed to create your
own IRC client or bot, including multi-threading support, sync and async
interfaces, CTCP/DCC support, colors and so on.

%package devel
Summary: Development files for %name
Group: Development/C++
Requires: %name = %version-%release

%description devel
This package contains libraries and header files for
developing applications that use %name.

%prep
%setup
%patch -p1

%build
sed -i 's;/usr/lib;%_libdir;g' src/Makefile.in
export CFLAGS="%optflags -fPIC -fno-strict-aliasing"
%autoreconf
%configure \
	%{subst_enable ipv6}
%make_build

%install
%makeinstall_std -C src

%files
%_libdir/*.so.*

%files devel
%_includedir/%name
%_libdir/*.so
%_datadir/doc/%name
%_man3dir/*

%exclude %_libdir/*.a

%changelog
* Sat Jan 07 2012 Mikhail Efremov <sem@altlinux.org> 1.3-alt1
- Initial build.
