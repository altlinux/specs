Name: libstrophe
# configure.ac:AC_INIT([libstrophe], [0.8-snapshot], [jack@metajack.im])
Version: 0.9.3
Release: alt1
Summary: A lightweight XMPP client library written in C
Group: System/Libraries
License: GPLv3
Url: http://strophe.im/libstrophe
# https://github.com/strophe/libstrophe
Source: %name-%version.tar

# Automatically added by buildreq on Sun Jul 22 2018
# optimized out: glibc-kernheaders-generic glibc-kernheaders-x86 libcom_err-devel libkrb5-devel perl pkg-config python-base
BuildRequires: doxygen libexpat-devel libssl-devel

%description
libstrophe is a lightweight XMPP client library written in C. It has
minimal dependencies and is configurable for various environments. It
runs well on both Linux, Unix, and Windows based platforms.

Its goals are:

- usable quickly
- well documented
- reliable

%package devel
Group: Development/C
Summary: Development environment for %name
Requires: %name = %version-%release
%description devel
Development environment for %name

%package static
Group: System/Libraries
Summary: A lightweight XMPP client library written in C
%description static
Static version of %name

%prep
%setup

%build
%autoreconf
%configure
%make_build
doxygen

%install
%makeinstall

%check
make check

%files
%_libdir/*.so.*

%files devel
%doc README.markdown docs
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*

%files static
%_libdir/*.a

%changelog
* Tue Dec 17 2019 Grigory Ustinov <grenka@altlinux.org> 0.9.3-alt1
- Build new version.
- Build from git.

* Wed Aug 29 2018 Grigory Ustinov <grenka@altlinux.org> 0.9.2-alt1.1
- NMU: Rebuild with new openssl 1.1.0.

* Sun Jul 22 2018 Fr. Br. George <george@altlinux.ru> 0.9.2-alt1
- Autobuild version bump to 0.9.2
- Introduce .so

* Thu Dec 13 2012 Fr. Br. George <george@altlinux.ru> 0.8-alt1
Initial build

