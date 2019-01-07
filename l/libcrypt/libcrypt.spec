Name: libcrypt
Version: 4.4.2
Release: alt1

Summary: Modern password hashing library
License: LGPLv2.1+
Group: System/Libraries
Url: https://github.com/besser82/libxcrypt
Source: %name-%version-%release.tar

Provides: crypt-yescrypt = 1.0.3
Provides: glibc-crypt_blowfish = 1.3
Provides: libcrypt1 = 6:2.27-alt6
Obsoletes: libcrypt1 < 6:2.27-alt6
Conflicts: glibc-core < 6:2.27-alt5

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
Conflicts: glibc-devel < 6:2.27-alt6
Conflicts: man-pages < 4.16

%description -n libcrypt-devel
This package contains libraries and header files for developing
applications that use libcrypt.

%prep
%setup -n %name-%version-%release

%build
%autoreconf
%configure \
	--disable-static \
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

%changelog
* Sat Dec 22 2018 Dmitry V. Levin <ldv@altlinux.org> 4.4.2-alt1
- v4.4.0 -> v4.4.2.

* Thu Nov 29 2018 Vitaly Chikunov <vt@altlinux.org> 4.4.0-alt1
- Merge upstream tag 'v4.4.0'.

* Wed Jul 04 2018 Dmitry V. Levin <ldv@altlinux.org> 4.0.1-alt2
- Added yescrypt and gost-yescrypt support (by vt@).

* Wed Jun 27 2018 Dmitry V. Levin <ldv@altlinux.org> 4.0.1-alt1
- Initial build for Sisyphus.
