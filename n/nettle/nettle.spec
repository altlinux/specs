%define libnettle_soname 6
%define libhogweed_soname 4

%define _unpackaged_files_terminate_build 1

Name: nettle
Version: 3.4
Release: alt1
Summary: A low-level cryptographic library

License: LGPLv2.1+
Group: System/Libraries
Url: http://www.lysator.liu.se/~nisse/nettle/

# git://git.altlinux.org/gears/n/nettle.git
Source: %name-%version-%release.tar

BuildRequires: gcc-c++ libgmp-devel libssl-devel makeinfo

%define libnettle libnettle%libnettle_soname
%define libhogweed libhogweed%libhogweed_soname

%description
Nettle is a cryptographic library that is designed to fit easily in more
or less any context: in crypto toolkits for object-oriented languages
(C++, Python, Pike, ...), in applications like LSH or GNUPG, or even in
kernel space.

%package -n %libnettle
Summary: A low-level cryptographic library (symmetric and one-way cryptos)
Group: System/Libraries

%description -n %libnettle
Nettle is a cryptographic library that is designed to fit easily in more
or less any context: in crypto toolkits for object-oriented languages
(C++, Python, Pike, ...), in applications like LSH or GNUPG, or even in
kernel space.

This package contains the symmetric and one-way cryptographic
algorithms. To avoid having this package depend on libgmp, the
asymmetric cryptos reside in a separate library, libhogweed.

%package -n %libhogweed
Summary: A low-level cryptographic library (asymmetric cryptos)
Group: System/Libraries

%description -n %libhogweed
Nettle is a cryptographic library that is designed to fit easily in more
or less any context: in crypto toolkits for object-oriented languages
(C++, Python, Pike, ...), in applications like LSH or GNUPG, or even in
kernel space.

This package contains the asymmetric cryptographic algorithms, which,
require the GNU multiple precision arithmetic library (libgmp) for
their large integer computations.

%package -n lib%name-devel
Summary: Header files, libraries and development documentation for %name
Group: Development/C
Requires: %libnettle = %version-%release
Requires: %libhogweed = %version-%release

%description -n lib%name-devel
Nettle is a cryptographic library that is designed to fit easily in more
or less any context: in crypto toolkits for object-oriented languages
(C++, Python, Pike, ...), in applications like LSH or GNUPG, or even in
kernel space.

This package contains header files, development libraries and
development documentation for %name and libhogweed.

%prep
%setup -n %name-%version-%release
sed -i 's/ -ggdb3//' configure.ac
sed -i -e 's/libnettle\.a/\$(LIBNETTLE_FORLINK)/' \
       -e 's/libhogweed\.a/\$(LIBHOGWEED_FORLINK)/' */Makefile.in

%build
%autoreconf
%configure \
	--disable-static
%make_build LIBTARGETS= DOCTARGETS=nettle.info

%install
%makeinstall_std install-shared LIBTARGETS= DOCTARGETS=nettle.info

%check
%make_build -k check

%files
%_bindir/*

%files -n %libnettle
%_libdir/libnettle.so.*
%doc AUTHORS NEWS README

%files -n %libhogweed
%_libdir/libhogweed.so.*

%files -n lib%name-devel
%_pkgconfigdir/*.pc
%_libdir/lib*.so
%_includedir/*
%_infodir/*.*

%changelog
* Fri Nov 24 2017 Mikhail Efremov <sem@altlinux.org> 3.4-alt1
- Updated to 3.4.

* Mon Oct 03 2016 Mikhail Efremov <sem@altlinux.org> 3.3-alt1
- Updated to 3.3.

* Tue Feb 02 2016 Mikhail Efremov <sem@altlinux.org> 3.2-alt1
- Updated to 3.2.

* Tue Dec 01 2015 Mikhail Efremov <sem@altlinux.org> 3.1.1-alt1
- Use soname in the names.
- Package libnettle and libhogweed as separate subpackages.
- Updated patches.
- Updated to nettle_3.1.1_release_20150424.

* Mon Jun 03 2013 Dmitry V. Levin <ldv@altlinux.org> 2.7.1-alt1
- Updated to nettle_2.7.1_release_20130528.

* Wed Apr 24 2013 Dmitry V. Levin <ldv@altlinux.org> 2.7-alt1
- Updated to nettle_2.7_release_20130424.

* Tue Apr 09 2013 Dmitry V. Levin <ldv@altlinux.org> 2.6-alt2
- Updated to nettle_2.6_release_20130116.

* Sat Sep 01 2012 Dmitry V. Levin <ldv@altlinux.org> 2.6-alt1
- Initial build for Sisyphus.
