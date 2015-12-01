%define _name nettle

Name: nettle2
Version: 2.7.1
Release: alt2
Summary: A low-level cryptographic library

License: LGPLv2.1+
Group: System/Legacy libraries
Url: http://www.lysator.liu.se/~nisse/nettle/

# git://git.altlinux.org/gears/n/nettle.git
Source: %name-%version-%release.tar

Requires: lib%_name = %version-%release

BuildRequires: gcc-c++ libgmp-devel libssl-devel

%description
Nettle is a cryptographic library that is designed to fit easily in more
or less any context: in crypto toolkits for object-oriented languages
(C++, Python, Pike, ...), in applications like LSH or GNUPG, or even in
kernel space.

%package -n lib%_name
Summary: A low-level cryptographic library
Group: System/Libraries

%description -n lib%_name
Nettle is a cryptographic library that is designed to fit easily in more
or less any context: in crypto toolkits for object-oriented languages
(C++, Python, Pike, ...), in applications like LSH or GNUPG, or even in
kernel space.

%prep
%setup -n %name-%version-%release
sed -i 's/ -ggdb3//' configure.ac
sed -i -e 's/libnettle\.a/\$(LIBNETTLE_FORLINK)/' \
       -e 's/libhogweed\.a/\$(LIBHOGWEED_FORLINK)/' */Makefile.in

%build
%autoreconf
%configure \
	--disable-static \
	--disable-documentation
%make_build LIBTARGETS=

%install
%makeinstall_std install-shared LIBTARGETS=

%check
%make_build -k check

%files -n lib%_name
%_libdir/lib*.so.*
%doc AUTHORS NEWS README

%exclude %_bindir/*
%exclude %_pkgconfigdir/*.pc
%exclude %_libdir/lib*.so
%exclude %_includedir/*

%changelog
* Wed Dec 02 2015 Mikhail Efremov <sem@altlinux.org> 2.7.1-alt2
- Build as legacy library.

* Mon Jun 03 2013 Dmitry V. Levin <ldv@altlinux.org> 2.7.1-alt1
- Updated to nettle_2.7.1_release_20130528.

* Wed Apr 24 2013 Dmitry V. Levin <ldv@altlinux.org> 2.7-alt1
- Updated to nettle_2.7_release_20130424.

* Tue Apr 09 2013 Dmitry V. Levin <ldv@altlinux.org> 2.6-alt2
- Updated to nettle_2.6_release_20130116.

* Sat Sep 01 2012 Dmitry V. Levin <ldv@altlinux.org> 2.6-alt1
- Initial build for Sisyphus.
