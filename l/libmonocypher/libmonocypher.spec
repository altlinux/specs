%def_with check

%define oname monocypher

Name: libmonocypher
Version: 4.0.2
Release: alt1

Summary: Monocypher is an easy to use auditable crypto library written in C
License: CC0-1.0 OR BSD-2-Clause
Group: System/Libraries
Url: https://monocypher.org/

Source: %name-%version.tar

%description
Monocypher is an easy-to-use crypto library.

* Small. Sloccount counts under 2000 lines of code, small enough to allow
audits. The binaries can be under 50KB, small enough for many embedded targets.
* Easy to deploy. Just add monocypher.c and monocypher.h to your project.
They compile as C99 or C++ and are dedicated to the public domain (CC0-1.0,
alternatively 2-clause BSD).
* Portable. There are no dependencies, not even on libc.
* Honest. The API is small, consistent, and cannot fail on correct input.
* Direct. The abstractions are minimal. A developer with experience in applied
cryptography can be productive in minutes.
* Fast. The primitives are fast to begin with and performance wasn`t needlessly
sacrificed. Monocypher holds up pretty well against libsodium, despite being
closer in size to TweetNaCl.

Features.

* Authenticated Encryption with XChaCha20 and Poly1305 (RFC 8439), with nonces
big enough to be random. Regular ChaCha20 is also implemented.
* Hashing with BLAKE2b, which is as secure as SHA-3 and as fast as MD5.
* Password Hashing with Argon2i, which won the Password Hashing competition.
* Public Key Cryptography with X25519 (Diffie-Hellman key exchange). X25519
uses public keys to compute a symmetric key that can be used for
authenticated encryption.
* Public Key Signatures with EdDSA (RFC 8032). By default, EdDSA uses BLAKE2b
and Edwards25519. Ed25519 (SHA-512 and Edwards25519) is available as an option.
* Steganography support with Elligator 2. Elligator can hide ephemeral public
keys as random noise, which is easier to hide from censors and other such
adversaries.
* Password Authenticated Key Exchange (PAKE) support with Elligator 2
(map to point) and scalar inversion (Oblivious Pseudo-Random Function).

%package devel
Summary: Development files for %oname
Group: Development/C
Requires: %name = %EVR

%description devel
Contains the library and header files needed to develop applications using
%oname.

%package doc
Summary: Documentation files for %oname
Group: Documentation
Requires: %name = %EVR

%description doc
Contains documentation for the %oname API in html format.

%prep
%setup

%build
%make_build CC='gcc -std=c99 -pedantic'

%install
%makeinstall_std \
	PREFIX=%prefix \
	LIBDIR=%_libdir \
	INCLUDEDIR=%_includedir \
	MANDIR=%_man3dir \
	PKGCONFIGDIR=%_pkgconfigdir
rm -v %buildroot%_libdir/%name.a

%check
%make_build CC='gcc -std=c99 -pedantic' test
%make_build CC='gcc -std=c99 -pedantic' tis-ci

%files
%_libdir/%name.so.*

%files devel
%_libdir/%name.so
%_includedir/%oname.h
%_includedir/%oname-ed25519.h
%_pkgconfigdir/%oname.pc
%_man3dir/*

%files doc
%doc doc/html/*.html doc/html/style.css

%changelog
* Fri Feb 21 2025 Ulysses Apokin <ulysses@altlinux.org> 4.0.2-alt1
- Initial build for Sisyphus.
