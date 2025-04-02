%define _libexecdir %_usr/libexec/
%def_disable doc
# Some algorithms needed by tools disabled for now
%def_disable tools
%def_enable static

Name: leancrypto
Version: 1.3.0
Release: alt1

Summary: Cryptographic library with stack-only support and PQC-safe algorithms
License: BSD-2-Clause and MIT and CC0-1.0 and ISC and BSD-3-Clause and Apache-2.0 and GPL-2.0-only and GPL-2.0-or-later
Group: System/Libraries
URL: https://leancrypto.org
Vcs: https://github.com/smuellerDD/leancrypto.git
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): meson rpm-macros-meson >= 1.3.1-alt1
%{?_enable_doc:BuildRequires: doxygen}

%define _unpackaged_files_terminate_build 1
%define soname 1

%description
Leancrypto provides a general-purpose cryptographic library with PQC-safe
algorithms. Further it only has POSIX dependencies, and allows all algorithms
to be used on stack as well as on heap. Accelerated algorithms are transparently
enabled if possible.

%package -n lib%name%soname
Summary: %summary
Group: System/Libraries

%description -n lib%name%soname
Leancrypto provides a general-purpose cryptographic library with PQC-safe
algorithms. Further it only has POSIX dependencies, and allows all algorithms
to be used on stack as well as on heap. Accelerated algorithms are transparently
enabled if possible.

%package -n lib%name-devel
Summary: Development files for lib%name%soname
Group: Development/C
Requires: lib%name%soname = %EVR

%description -n lib%name-devel
Leancrypto provides a general-purpose cryptographic library with PQC-safe
algorithms. Further it only has POSIX dependencies, and allows all algorithms
to be used on stack as well as on heap. Accelerated algorithms are transparently
enabled if possible.

This package contains libraries and header files for
developing applications that use lib%name%soname.

%if_enabled static
%package -n lib%name-devel-static
Summary: Static lib%name library
Group: Development/C
Requires: lib%name-devel = %EVR

%description -n lib%name-devel-static
Leancrypto provides a general-purpose cryptographic library with PQC-safe
algorithms. Further it only has POSIX dependencies, and allows all algorithms
to be used on stack as well as on heap. Accelerated algorithms are transparently
enabled if possible.

This package contains static library for developing applications that use
lib%name.
%endif

%if_enabled doc
%package -n lib%name-devel-doc
Summary: This package contains development documentation for lib%name
Group: Development/Documentation
BuildArch: noarch
Requires: lib%name-devel = %EVR

%description -n lib%name-devel-doc
Leancrypto provides a general-purpose cryptographic library with PQC-safe
algorithms. Further it only has POSIX dependencies, and allows all algorithms
to be used on stack as well as on heap. Accelerated algorithms are transparently
enabled if possible.

This package contains development documentation for lib%name
%endif

%if_enabled tools
%package tools
Summary: Applications provided by leancrypto
Group: System/Libraries

%description tools
Leancrypto provides a general-purpose cryptographic library with PQC-safe
algorithms. Further it only has POSIX dependencies, and allows all algorithms
to be used on stack as well as on heap. Accelerated algorithms are transparently
enabled if possible.

This subpackage holds the tools provided by the library, such as sha*sum.
%endif

%prep
%setup
%patch -p1

%build
# Algorithms not supported by GNUTLS are disabled for now.
%meson \
	-Ddefault_library=shared \
	-Dascon=disabled -Dascon_keccak=disabled \
	-Dbike_5=disabled -Dbike_3=disabled -Dbike_1=disabled \
	-Dkyber_x25519=disabled -Ddilithium_ed25519=disabled \
	-Dx509_parser=disabled -Dx509_generator=disabled \
	-Dpkcs7_parser=disabled -Dpkcs7_generator=disabled \
	-Dsha2-256=disabled \
	-Dchacha20=disabled -Dchacha20_drng=disabled \
	-Ddrbg_hash=disabled -Ddrbg_hmac=disabled \
	-Dhash_crypt=disabled \
	-Dhmac=disabled -Dhkdf=disabled \
	-Dkdf_ctr=disabled -Dkdf_fb=disabled -Dkdf_dpi=disabled \
	-Dpbkdf2=disabled \
	-Dkmac_drng=disabled -Dcshake_drng=disabled \
	-Dhotp=disabled -Dtotp=disabled \
	-Daes_block=disabled -Daes_cbc=disabled -Daes_ctr=disabled \
	-Daes_kw=disabled \
	%{subst_enable_meson_feature tools apps} \
	-Dstrip=false

%meson_build -v

%install
%meson_install

%check
#We can't use meson_test macro here: only regression suite is needed
%__meson test -C %__builddir --suite regression

%files -n lib%name%soname
%doc LICENSE README.md CHANGES.md SECURITY.md
%_libdir/lib%name.so.%soname
%exclude %_libdir/lib%name-fips.so.%soname

%files -n lib%name-devel
%_includedir/*
%_libdir/lib%name.so
%_libdir/pkgconfig/%name.pc

%exclude %_libdir/lib%name-fips.so
%exclude %_libdir/pkgconfig/%name-fips.pc

%if_enabled static
%files -n lib%name-devel-static
%_libdir/lib%name.a
%exclude %_libdir/lib%name-fips.a
%endif

%if_enabled doc
%files -n lib%name-devel-doc
%_defaultdocdir/%name
%endif

%if_enabled tools
%files tools
%_libexecdir/%name
%endif

%changelog
* Wed Apr 02 2025 Mikhail Efremov <sem@altlinux.org> 1.3.0-alt1
- Don't package fips variant.
- Updated to 1.3.0.

* Fri Feb 21 2025 Mikhail Efremov <sem@altlinux.org> 1.2.0-alt2
- Added devel-static subpackage.
- Disabled tools subpackage.
- Disabled algorithms not supported by gnutls.

* Tue Feb 18 2025 Mikhail Efremov <sem@altlinux.org> 1.2.0-alt1
- Initial build.

