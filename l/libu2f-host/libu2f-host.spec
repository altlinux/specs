Name: libu2f-host
Version: 1.1.3
Release: alt1
Summary: Yubico Universal 2nd Factor (U2F) Host C Library
Group: System/Libraries

License: LGPLv2+
Url: http://developers.yubico.com/%name
# repacked http://developers.yubico.com/%name/releases/%name-%version.tar.xz
Source0: %name-%version.tar

# Automatically added by buildreq on Tue Nov 01 2016
# optimized out: gnu-config libjson-c pkg-config python-base
BuildRequires: libhidapi-devel libjson-c-devel

Requires: u2f-hidraw-policy

%description
libu2f-host provides a C library that implements the host-side of the
U2F protocol. There are APIs to talk to a U2F device and perform the U2F
Register and U2F Authenticate operations.

%package -n u2f-host
License: GPLv3+
Group: Security/Networking
Summary: Command-line tool for U2F devices
Requires: %name = %EVR

%description -n u2f-host
u2f-host provides a command line tool that implements the host-side of
the U2F protocol.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %EVR

%description devel
This package contains the header files needed to develop applications
that use libu2f-host.

%prep
%setup

%build
%configure --disable-rpath --disable-static

# --disable-rpath doesn't work.
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%make_build

%check
LD_LIBRARY_PATH="$PWD/u2f-host/.libs" make check

%install
%makeinstall_std
find %buildroot -name '*.la' -delete

%files
%doc COPYING.LGPLv2 README AUTHORS NEWS THANKS ChangeLog doc/*
%_libdir/*.so.*

%files -n u2f-host
%doc COPYING
%_bindir/u2f-host
%_mandir/man1/u2f-host.1*

%files devel
%doc %_datadir/gtk-doc
%_libdir/pkgconfig/*.pc
%_libdir/*.so
%_includedir/*

%changelog
* Tue Nov 01 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.1.3-alt1
- Initial build.
