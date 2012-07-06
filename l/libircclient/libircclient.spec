%def_enable ipv6
%def_enable openssl

Name: libircclient
Version: 1.6
Release: alt1

Summary: Library that implements the client-server IRC protocol
License: %lgpl2plus
Group: System/Libraries

URL: http://www.ulduzsoft.com/libircclient/
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Patch1: libircclient-1.6-fedora-install.patch
Patch2: libircclient-1.6-fedora-rfc.patch
Patch3: libircclient-1.6-fedora-shared.patch

BuildRequires(pre): rpm-build-licenses
BuildRequires: gcc-c++
%{?_enable_openssl:BuildRequires: libssl-devel}

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
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
export CFLAGS="%optflags -fPIC"
%autoreconf
%configure \
	--enable-shared \
	%{subst_enable ipv6} \
	%{subst_enable openssl}
%make_build

%install
%makeinstall_std
mkdir -p %buildroot/%_datadir/doc/libircclient
mkdir -p %buildroot/%_man3dir
cp -a doc/{html,rfc1459.txt} %buildroot/%_datadir/doc/libircclient/
cp -a doc/man/man3/* %buildroot/%_man3dir/

%files
%_libdir/*.so.*

%files devel
%_includedir/*
%_libdir/*.so
%_datadir/doc/%name
%_man3dir/*

%changelog
* Fri Jul 06 2012 Mikhail Efremov <sem@altlinux.org> 1.6-alt1
- Updated to 1.6.
- Updated URL.
- Enabled IPv6 support.
- Build with OpenSSL support.
- Patches from Fedora:
    + Correct install target to use includedir and libdir.
    + Add rfc include to main header.
    + Create a dynamic library by default.

* Sat Jan 07 2012 Mikhail Efremov <sem@altlinux.org> 1.3-alt1
- Initial build.
