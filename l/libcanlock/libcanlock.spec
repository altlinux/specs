%define _unpackaged_files_terminate_build 1

Name: libcanlock
Version: 3.3.0
Release: alt1
%define abiversion 3

Summary: Library for creating and verifying Usenet cancel locks
License: MIT
Group: Development/C
Url: https://micha.freeshell.org/libcanlock/

Source0: %{name}-%{version}.tar.bz2

BuildRequires: bison flex chrpath

%description
Cancel locks are used by Usenet article posters to authenticate their
authorship of an article. It may then by used by servers to prevent
cancel and supersede abuse. The use of this feature remains the
newsmaster's decision.

This library may be used for both the generation and the verification
of cancel locks.

%package -n %{name}%{abiversion}
Summary: Library for creating and verifying Usenet cancel locks
Group: System/Libraries

%description -n %{name}%{abiversion}
libcanlock is a library for creating and verifying RFC 8315 Netnews
Cancel-Locks. This implementation uses the recommended algorithm from
Section 4 with HMAC based on the same hash function as <scheme>.

This subpackage contains shared library part of libcanlock.

%package devel
Summary: Development files for Usenet cancel lock library
Group: Development/C
Requires: %{name}%{abiversion} = %{version}

%description devel
libcanlock is a library for creating and verifying RFC 8315 Netnews
Cancel-Locks. This implementation uses the recommended algorithm from
Section 4 with HMAC based on the same hash function as <scheme>.

This subpackage contains libraries and header files for developing
applications that want to make use of libcanlock.

%package -n canlock
Summary: Utilities for creating and verifying Usenet cancel locks
Group: Networking/News

%description -n canlock
Cancel locks are used by Usenet article posters to authenticate their
authorship of an article. It may then by used by servers to prevent
cancel and supersede abuse. The use of this feature remains the
newsmaster's decision.

This package contains a simple utility wrapping the canlock library,
which may be used for both the generation and the verification of
cancel locks, along with a message header parser and a header field
parser.

%prep
%setup -q

%build
%configure --enable-pc-files
%make_build

%install
%make install DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT/%_libdir/libcanlock.a
rm -f $RPM_BUILD_ROOT/%_libdir/libcanlock-hp.a

find $RPM_BUILD_ROOT -type f | while read f; do
    COUNT=`file $f | grep ELF | wc -l`
    if [ $[ $COUNT > 0 ] == 1 ]; then
       chrpath -d $f
    fi
done

%files -n canlock
%_bindir/canlock
%_bindir/canlock-hfp
%_bindir/canlock-mhp
%_man1dir/*

%files -n %{name}%{abiversion}
%doc ChangeLog README COPYING
%_libdir/libcanlock.so.*
%_libdir/libcanlock-hp.so.*

%files devel
%dir %_includedir/libcanlock-%{abiversion}

%_includedir/libcanlock-%{abiversion}/canlock.h
%_includedir/libcanlock-%{abiversion}/canlock-hp.h
%_libdir/libcanlock.so
%_libdir/libcanlock-hp.so
%_libdir/pkgconfig/libcanlock-3.pc
%_libdir/pkgconfig/libcanlock-hp-3.pc

%_man3dir/*

%changelog
* Tue Nov 28 2023 Sergey Y. Afonin <asy@altlinux.org> 3.3.0-alt1
- initial build for ALT Linux (ALT #44168)
