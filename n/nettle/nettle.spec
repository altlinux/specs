Name: nettle
Version: 2.6
Release: alt1
Summary: A low-level cryptographic library

License: LGPLv2.1+
Group: System/Libraries
Url: http://www.lysator.liu.se/~nisse/nettle/

# git://git.altlinux.org/gears/n/nettle.git
Source: %name-%version-%release.tar

Requires: lib%name = %version-%release

BuildRequires: gcc-c++ libgmp-devel libssl-devel

%description
Nettle is a cryptographic library that is designed to fit easily in more
or less any context: in crypto toolkits for object-oriented languages
(C++, Python, Pike, ...), in applications like LSH or GNUPG, or even in
kernel space.

%package -n lib%name
Summary: A low-level cryptographic library
Group: System/Libraries

%description -n lib%name
Nettle is a cryptographic library that is designed to fit easily in more
or less any context: in crypto toolkits for object-oriented languages
(C++, Python, Pike, ...), in applications like LSH or GNUPG, or even in
kernel space.

%package -n lib%name-devel
Summary: Header files, libraries and development documentation for %name
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
Nettle is a cryptographic library that is designed to fit easily in more
or less any context: in crypto toolkits for object-oriented languages
(C++, Python, Pike, ...), in applications like LSH or GNUPG, or even in
kernel space.

This package contains header files, development libraries and
development documentation for %name.

%prep
%setup -n %name-%version-%release
sed -i 's/ -ggdb3//' configure.ac
sed -i -e 's/libnettle\.a/\$(LIBNETTLE_FORLINK)/' \
       -e 's/libhogweed\.a/\$(LIBHOGWEED_FORLINK)/' */Makefile.in

%build
%autoreconf
%configure
%make_build LIBTARGETS= DOCTARGETS=nettle.info

%install
%makeinstall_std install-shared LIBTARGETS= DOCTARGETS=nettle.info

%check
%make_build -k check

%files
%_bindir/*

%files -n lib%name
%_libdir/lib*.so.*
%doc AUTHORS NEWS README

%files -n lib%name-devel
%_pkgconfigdir/*.pc
%_libdir/lib*.so
%_includedir/*
%_infodir/*.*

%changelog
* Sat Sep 01 2012 Dmitry V. Levin <ldv@altlinux.org> 2.6-alt1
- Initial build for Sisyphus.
