Name: libu2f-server
Version: 1.0.1
Release: alt1
Summary: Yubico Universal 2nd Factor (U2F) Server C Library

Group: System/Libraries
License: BSD
Url: https://developers.yubico.com/%name
# repacked https://developers.yubico.com/%name/Releases/%name-%version.tar.xz
Source0: %name-%version.tar

BuildRequires: libjson-c-devel openssl-devel libcheck-devel

%description
This is a C library that implements the server-side of the U2F protocol.
More precisely, it provides an API for generating the JSON blobs
required by U2F devices to perform the U2F Registration and U2F
Authentication operations, and functionality for verifying the
cryptographic operations.

%package -n u2f-server
Group: Security/Networking
Summary: Server-side command-line tool for U2F devices
Requires: %name = %EVR

%description -n u2f-server
u2f-server provides a command line tool that implements the server-side
of the U2F protocol.

%package devel
Group: Development/C
Summary: Development files for %name
Requires: %name = %EVR

%description devel
This package contains the header files needed to develop applications
that use libu2f-server.

%prep
%setup

%build
%configure --disable-rpath --disable-static

# --disable-rpath doesn't work.
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%make_build CFLAGS="%optflags"

%check
LD_LIBRARY_PATH="$PWD/u2f-server/.libs" make check

%install
%makeinstall_std
find %buildroot -name '*.la' -delete

%files
%doc COPYING README AUTHORS NEWS THANKS
%_libdir/*.so.*

%files -n u2f-server
%_bindir/u2f-server
%_man1dir/u2f-server.1*

%files devel
%doc %_datadir/gtk-doc/html/u2f-server
%_libdir/pkgconfig/*.pc
%_libdir/*.so
%_includedir/*

%changelog
* Tue Nov 01 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.0.1-alt1
- Initial build.
