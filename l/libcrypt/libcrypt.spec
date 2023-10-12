Name: libcrypt
Version: 4.4.35
Release: alt2

Summary: Modern password hashing library
License: LGPLv2.1+
Group: System/Libraries
Url: https://github.com/besser82/libxcrypt
Source: %name-%version-%release.tar

%ifnarch %e2k
%global ver_glibc_final 6:2.27-alt6
%global ver_glibc_pre   6:2.27-alt5
%else
%global ver_glibc_final 6:2.23-alt3.E2K.18
%global ver_glibc_pre   6:2.23-alt3.E2K.17
%endif

Provides: crypt-yescrypt = 1.0.3
Provides: glibc-crypt_blowfish = 1.3
Provides: libcrypt1 = %ver_glibc_final
Obsoletes: libcrypt1 < %ver_glibc_final
Conflicts: glibc-core < %ver_glibc_pre

%description
libcrypt is a modern library for one-way hashing of passwords.
It supports DES, MD5, SHA-2-256, SHA-2-512, bcrypt and yescrypt-based
password hashes, and provides the traditional Unix 'crypt' and
'crypt_r' interfaces, as well as a set of extended interfaces
pioneered by Openwall Linux, 'crypt_rn', 'crypt_ra',
'crypt_gensalt', 'crypt_gensalt_rn', and 'crypt_gensalt_ra'.

%package devel
Summary: Development files for libcrypt password hashing library
License: LGPLv2.1+
Group: Development/C
Requires: %name = %EVR
Conflicts: glibc-devel < %ver_glibc_final
Conflicts: man-pages < 4.16

%description -n libcrypt-devel
This package contains libraries and header files for developing
applications that use libcrypt.

%package devel-static
Summary: Development files (static) for libcrypt password hashing library
License: LGPLv2.1+
Group: Development/C
Requires: %name-devel = %EVR
Conflicts: glibc-devel-static < %ver_glibc_final

%description devel-static
This package contains static library for developing applications that use
libcrypt.

%prep
%setup -n %name-%version-%release

%build
%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}
%autoreconf
%configure \
	--enable-obsolete-api=alt \
	--enable-hashes=alt,glibc,strong \
	#
%make_build

%install
%makeinstall_std
%define docdir %_docdir/%name
install -Dpm0644 -t %buildroot%docdir AUTHORS LICENSING README NEWS

# Relocate shared library from %_libdir/ to /%_lib/.
mkdir -p %buildroot/%_lib
for f in %buildroot%_libdir/libcrypt.so; do
	t=$(readlink -v "$f")
	ln -rsnf %buildroot/%_lib/"$t" "$f"
done
mv %buildroot%_libdir/*.so.* %buildroot/%_lib/

%set_verify_elf_method strict
%define _unpackaged_files_terminate_build 1

%check
%make_build -k check VERBOSE=1

%files
%docdir/
/%_lib/libcrypt.so.1*
%_man5dir/*.5*

%files devel
%_libdir/lib*crypt.so
%_includedir/*crypt.h
%_pkgconfigdir/lib*crypt.pc
%_man3dir/*.3*

%files devel-static
%_libdir/lib*crypt.a

%changelog
* Wed Oct 11 2023 Vitaly Chikunov <vt@altlinux.org> 4.4.35-alt2
- Package libcrypt-devel-static.

* Tue Jun 06 2023 Dmitry V. Levin <ldv@altlinux.org> 4.4.35-alt1
- v4.4.23 -> v4.4.35.

* Sun Jun 20 2021 Dmitry V. Levin <ldv@altlinux.org> 4.4.23-alt1
- v4.4.17 -> v4.4.23.

* Sun Aug 23 2020 Dmitry V. Levin <ldv@altlinux.org> 4.4.17-alt1
- v4.4.16 -> v4.4.17.

* Thu Apr 09 2020 Andrew Savchenko <bircoph@altlinux.org> 4.4.16-alt2
- Fix glibc-related dependencies on e2k.

* Sat Apr 04 2020 Dmitry V. Levin <ldv@altlinux.org> 4.4.16-alt1
- v4.4.4 -> v4.4.16.

* Sat Apr 04 2020 Andrew Savchenko <bircoph@altlinux.org> 4.4.4-alt2
- Add e2k architecture support.

* Sun Mar 03 2019 Dmitry V. Levin <ldv@altlinux.org> 4.4.4-alt1
- v4.4.2 -> v4.4.4.

* Sat Dec 22 2018 Dmitry V. Levin <ldv@altlinux.org> 4.4.2-alt1
- v4.4.0 -> v4.4.2.

* Thu Nov 29 2018 Vitaly Chikunov <vt@altlinux.org> 4.4.0-alt1
- Merge upstream tag 'v4.4.0'.

* Wed Jul 04 2018 Dmitry V. Levin <ldv@altlinux.org> 4.0.1-alt2
- Added yescrypt and gost-yescrypt support (by vt@).

* Wed Jun 27 2018 Dmitry V. Levin <ldv@altlinux.org> 4.0.1-alt1
- Initial build for Sisyphus.
