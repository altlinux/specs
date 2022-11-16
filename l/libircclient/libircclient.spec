%def_enable ipv6
%def_enable openssl

Name: libircclient
Version: 1.10
Release: alt2

Summary: Library that implements the client-server IRC protocol
License: LGPLv2+
Group: System/Libraries

URL: https://www.ulduzsoft.com/linux/libircclient/
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Patch2: libircclient-1.6-fedora-rfc.patch
# https://sourceforge.net/p/libircclient/bugs/24/
Patch3: debian-fix-ipv6-socaddr.patch

# Patch from upstream
Patch4: openssl-1.1-compatibility.patch

BuildRequires: gcc-c++
%{?_enable_openssl:BuildRequires: libssl-devel}

%define _unpackaged_files_terminate_build 1

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
%patch2 -p1
%patch3 -p1
%patch4 -p3

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

%files
%_libdir/*.so.*

%files devel
%_includedir/*
%_libdir/*.so

%changelog
* Wed Nov 16 2022 Mikhail Efremov <sem@altlinux.org> 1.10-alt2
- Updated Url tag.
- Don't use rpm-build-licenses.
- Patch from upstream:
  + Fix SSL 1.1 compatibility.

* Wed Aug 29 2018 Mikhail Efremov <sem@altlinux.org> 1.10-alt1
- Use _unpackaged_files_terminate_build.
- Fix ipv6.
- Updated to 1.10.

* Mon May 16 2016 Mikhail Efremov <sem@altlinux.org> 1.9-alt1
- Updated to 1.9.

* Tue May 27 2014 Mikhail Efremov <sem@altlinux.org> 1.8-alt1
- Fix Url.
- Updated to 1.8.

* Wed Jul 10 2013 Mikhail Efremov <sem@altlinux.org> 1.7-alt1
- Don't strip shared object.
- Don't build and package devel documentation.
- Drop obsoleted patches.
- Updated to 1.7.

* Thu Jul 12 2012 Mikhail Efremov <sem@altlinux.org> 1.6-alt2
- Install headers in %%_includedir/libircclient/ again.

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
