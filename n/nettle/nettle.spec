%define libnettle_soname 8
%define libhogweed_soname 6

%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: nettle
Version: 3.9.1
Release: alt1
Summary: A low-level cryptographic library

License: GPL-2.0-or-later or LGPL-3.0-or-later
Group: System/Libraries
Url: https://www.lysator.liu.se/~nisse/nettle/

Vcs: https://git.lysator.liu.se/nettle/nettle.git
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
%add_optflags %(getconf LFS_CFLAGS)
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
%_libdir/libnettle.so.%{libnettle_soname}
%_libdir/libnettle.so.%{libnettle_soname}.*
%doc AUTHORS NEWS README COPYING*

%files -n %libhogweed
%_libdir/libhogweed.so.%{libhogweed_soname}
%_libdir/libhogweed.so.%{libhogweed_soname}.*

%files -n lib%name-devel
%_pkgconfigdir/*.pc
%_libdir/lib*.so
%_includedir/*
%_infodir/*.*

%changelog
* Tue Jun 06 2023 Mikhail Efremov <sem@altlinux.org> 3.9.1-alt1
- Updated to 3.9.1.

* Thu May 25 2023 Mikhail Efremov <sem@altlinux.org> 3.9.0-alt1
- Updated to 3.9.0.

* Tue Oct 11 2022 Vitaly Chikunov <vt@altlinux.org> 3.8.1-alt2
- Enabled LFS on 32-bit systems.
- Updated License tag.

* Tue Aug 02 2022 Mikhail Efremov <sem@altlinux.org> 3.8.1-alt1
- Updated to 3.8.1.

* Tue Jun 28 2022 Mikhail Efremov <sem@altlinux.org> 3.8.0-alt1
- Updated to 3.8.0.
- Updated Vcs tag.
- Updated Url tag.

* Fri Jul 02 2021 Mikhail Efremov <sem@altlinux.org> 3.7.3-alt1
- Updated to 3.7.3.

* Mon Mar 22 2021 Mikhail Efremov <sem@altlinux.org> 3.7.2-alt1
- Updated to 3.7.2.

* Fri Jan 22 2021 Mikhail Efremov <sem@altlinux.org> 3.7-alt1
- Updated to 3.7.

* Wed May 13 2020 Mikhail Efremov <sem@altlinux.org> 3.6-alt1
- Add Vcs tag.
- Updated to 3.6.

* Wed Jul 31 2019 Mikhail Efremov <sem@altlinux.org> 3.5.1-alt1
- Updated patches.
- Updated to 3.5.1.

* Thu Dec 06 2018 Mikhail Efremov <sem@altlinux.org> 3.4.1-alt1
- Updated to 3.4.1 (fixes: CVE-2018-16869).

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
