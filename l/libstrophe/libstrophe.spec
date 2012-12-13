Name:		libstrophe
# configure.ac:AC_INIT([libstrophe], [0.8-snapshot], [jack@metajack.im])
Version:	0.8
Release:	alt1
Summary:	A lightweight XMPP client library written in C
Group:		System/Libraries
License:	GPLv3
# TODO update from git
Source:		%name-%version.tar

# Automatically added by buildreq on Thu Dec 13 2012
# optimized out: libcom_err-devel libkrb5-devel pkg-config
BuildRequires: doxygen libssl-devel libxml2-devel zlib-devel libcheck-devel

%description
libstrophe is a lightweight XMPP client library written in C. It has
minimal dependencies and is configurable for various environments. It
runs well on both Linux, Unix, and Windows based platforms.

Its goals are:

- usable quickly
- well documented
- reliable

%package devel
Group:		Development/C
Summary:	Development environment for %name
Requires: %name = %version-%release
%description devel
Development environment for %name

%prep
%setup
sed -i 's/^CFLAGS/AM_CFLAGS/' Makefile.am

%build
%autoreconf
%make_build
# TODO: CFLAGS=-fPIC + .so, pkgconfig -lxml2 -lssl -lcrypto -lz -lresolv
doxygen

%install
%makeinstall

%check
make check

%files
%_libdir/*.a

%files devel
%doc README.markdown docs
%_includedir/*

%changelog
* Thu Dec 13 2012 Fr. Br. George <george@altlinux.ru> 0.8-alt1
Initial build

