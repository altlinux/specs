%global pkgname cryptokit
%define ocamlsitelib %_libdir/ocaml
%define pkgsitelib %ocamlsitelib/%pkgname
%define ocamlstublib %_libdir/ocaml/stublibs/

Name: ocaml-%pkgname
Version: 1.20.1
Release: alt1
Group: Development/ML
Summary: OCaml library of cryptographic and hash functions
License: LGPLv2 with OCaml-LGPL-linking-exception
Url: http://forge.ocamlcore.org/projects/cryptokit/
Source0: %name-%version.tar
BuildRequires: ocaml ocaml-ocamldoc ocaml-zarith-devel ocaml-findlib zlib-devel
BuildRequires: dune ocaml-dune-configurator-devel
Provides: ocaml-cryptokit-runtime = %version-%release
Obsoletes: ocaml-cryptokit-runtime

%description
The Cryptokit library for Objective Caml provides a variety of
cryptographic primitives that can be used to implement cryptographic
protocols in security-sensitive applications. The primitives provided
include:

* Symmetric-key cryptography: AES, DES, Triple-DES, ARCfour, in ECB,
  CBC, CFB and OFB modes.
* Public-key cryptography: RSA encryption and signature; Diffie-Hellman
  key agreement.
* Hash functions and MACs: SHA-1, SHA-256, RIPEMD-160, MD5, and MACs
  based on AES and DES.
* Random number generation.
* Encodings and compression: base 64, hexadecimal, Zlib compression.

Additional ciphers and hashes can easily be used in conjunction with
the library. In particular, basic mechanisms such as chaining modes,
output buffering, and padding are provided by generic classes that can
easily be composed with user-provided ciphers. More generally, the
library promotes a "Lego"-like style of constructing and composing
transformations over character streams.

%package devel
Summary: Development files for %name
Requires: %name = %version-%release
Group: Development/ML

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup
%ifarch %e2k
sed -i '1i #undef __AES__' src/aesni.c
%ifarch e2k e2kv4 e2kv5
sed -i '1i #undef __PCLMUL__' src/pclmul.c
%else
sed -i 's/#include <cpuid.h>/#define __get_cpuid(x,a,b,c,d) (*(c)=-1,1)/' \
	src/pclmul.c
%endif
%endif

%build
%dune_build -p %pkgname @install

%install
%dune_install

%check
%dune_check

%files -f ocaml-files.runtime
%doc LICENSE

%files devel -f ocaml-files.devel
%doc README.md Changes

%changelog
* Mon Sep 16 2024 Anton Farygin <rider@altlinux.ru> 1.20.1-alt1
- 1.18 -> 1.20.1

* Thu Dec 07 2023 Michael Shigorin <mike@altlinux.org> 1.18-alt2
- E2K: fix build (ilyakurdyukov@)

* Fri Nov 10 2023 Anton Farygin <rider@altlinux.ru> 1.18-alt1
- 1.18

* Tue Mar 16 2021 Anton Farygin <rider@altlinux.org> 1.16.1-alt2
- spec BR: ocaml-dune-devel changed to ocaml-dune-configurator-devel
- spec: SPDX the ocaml linking exception in license tag

* Mon Jan 11 2021 Anton Farygin <rider@altlinux.ru> 1.16.1-alt1
- 1.16.1

* Tue Feb 25 2020 Anton Farygin <rider@altlinux.ru> 1.15-alt1
- 1.15

* Wed Jul 31 2019 Anton Farygin <rider@altlinux.ru> 1.13-alt4
- rebuilt with ocaml-4.08

* Thu Oct 18 2018 Anton Farygin <rider@altlinux.ru> 1.13-alt3
- rebuilt with ocaml-4.07.1

* Wed Sep 05 2018 Anton Farygin <rider@altlinux.ru> 1.13-alt2
- rebuilt with ocaml 4.07

* Fri May 18 2018 Anton Farygin <rider@altlinux.ru> 1.13-alt1
- 1.13

* Tue Jul 11 2017 Anton Farygin <rider@altlinux.ru> 1.11-alt3
- rebuild with ocaml 4.04.2

* Wed May 03 2017 Anton Farygin <rider@altlinux.ru> 1.11-alt2
- rebuild with ocaml 4.04.1

* Tue Feb 14 2017 Anton Farygin <rider@altlinux.ru> 1.11-alt1
- updated to new version

* Wed Jan 11 2012 Alexey Shabalin <shaba@altlinux.ru> 1.5-alt1
- 1.5

* Thu Oct 02 2008 Boris Savelev <boris@altlinux.org> 1.3-alt5
- remove "directory" from META

* Tue Sep 30 2008 Boris Savelev <boris@altlinux.org> 1.3-alt4
- add requires to META (fix #170011)

* Thu Sep 04 2008 Boris Savelev <boris@altlinux.org> 1.3-alt3
- rename to ocaml-cryptokit
- move files to site-lib/cryptokit
- add META
- split runtime and devel package

* Tue Aug 26 2008 Boris Savelev <boris@altlinux.org> 1.3-alt2
- add make allopt (to build cryptokit.cmxa)

* Sat Aug 23 2008 Boris Savelev <boris@altlinux.org> 1.3-alt1
- initial build

