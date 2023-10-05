%define _unpackaged_files_terminate_build 1
%define dist CryptX

Name: perl-%dist
Version: 0.080
Release: alt1

Summary: Crypto toolkit with multiple ciphers, hash functions and other
License: %perl_license
Group: Development/Perl

Url: %CPAN %dist
Source0: http://www.cpan.org/authors/id/M/MI/MIK/%{dist}-%{version}.tar.gz
# e2k
Patch3: CryptX-0.057-alt-uint128.patch

BuildRequires: rpm-build-licenses
BuildRequires: perl-HTML-Parser perl-JSON-XS perl-Module-Build

%description
CryptX - Crypto toolkit (self-contained no external libraries needed)
Cryptography in CryptX is based on https://github.com/libtom/libtomcrypt

    Currently available modules:

    *   Ciphers - see Crypt::Cipher and related modules

        Crypt::Cipher::AES, Crypt::Cipher::Anubis, Crypt::Cipher::Blowfish,
        Crypt::Cipher::Camellia, Crypt::Cipher::CAST5, Crypt::Cipher::DES,
        Crypt::Cipher::DES_EDE, Crypt::Cipher::KASUMI,
        Crypt::Cipher::Khazad, Crypt::Cipher::MULTI2,
        Crypt::Cipher::Noekeon, Crypt::Cipher::RC2, Crypt::Cipher::RC5,
        Crypt::Cipher::RC6, Crypt::Cipher::SAFERP,
        Crypt::Cipher::SAFER_K128, Crypt::Cipher::SAFER_K64,
        Crypt::Cipher::SAFER_SK128, Crypt::Cipher::SAFER_SK64,
        Crypt::Cipher::SEED, Crypt::Cipher::Skipjack,
        Crypt::Cipher::Twofish, Crypt::Cipher::XTEA

    *   Block cipher modes

        Crypt::Mode::CBC, Crypt::Mode::CFB, Crypt::Mode::CTR,
        Crypt::Mode::ECB, Crypt::Mode::OFB

    *   Authenticated encryption modes

        Crypt::AuthEnc::CCM, Crypt::AuthEnc::EAX, Crypt::AuthEnc::GCM,
        Crypt::AuthEnc::OCB

    *   Hash Functions - see Crypt::Digest and related modules

        Crypt::Digest::CHAES, Crypt::Digest::MD2, Crypt::Digest::MD4,
        Crypt::Digest::MD5, Crypt::Digest::RIPEMD128,
        Crypt::Digest::RIPEMD160, Crypt::Digest::RIPEMD256,
        Crypt::Digest::RIPEMD320, Crypt::Digest::SHA1,
        Crypt::Digest::SHA224, Crypt::Digest::SHA256, Crypt::Digest::SHA384,
        Crypt::Digest::SHA512, Crypt::Digest::SHA512_224,
        Crypt::Digest::SHA512_256, Crypt::Digest::Tiger192,
        Crypt::Digest::Whirlpool

    *   Message Authentication Codes

        Crypt::Mac::F9, Crypt::Mac::HMAC, Crypt::Mac::OMAC,
        Crypt::Mac::Pelican, Crypt::Mac::PMAC, Crypt::Mac::XCBC

    *   Public key cryptography

        Crypt::PK::RSA, Crypt::PK::DSA, Crypt::PK::ECC, Crypt::PK::DH

    *   Cryptographically secure random number generators

        Crypt::PRNG, Crypt::PRNG::Fortuna, Crypt::PRNG::Yarrow,
        Crypt::PRNG::RC4, Crypt::PRNG::Sober128

    *   Key derivation functions - PBKDF1, PBKFD2 and HKDF

        Crypt::KeyDerivation

%prep
%setup -q -n %{dist}-%{version}
%ifarch e2k
%patch3 -p1
%endif

#[ %version = 0.061 ] && rm -f t/mbi_ltm_bugs.t t/mbi_ltm_bigintpm.t

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README.md
%perl_vendor_archlib/Crypt
%perl_vendor_archlib/CryptX.pm
%perl_vendor_autolib/CryptX
%perl_vendor_archlib/Math

%changelog
* Thu Oct 05 2023 Igor Vlasenko <viy@altlinux.org> 0.080-alt1
- automated CPAN update

* Sat Apr 29 2023 Igor Vlasenko <viy@altlinux.org> 0.078-alt1
- automated CPAN update

* Fri Aug 26 2022 Igor Vlasenko <viy@altlinux.org> 0.077-alt1
- automated CPAN update

* Thu Jun 23 2022 Igor Vlasenko <viy@altlinux.org> 0.076-alt2
- fixed build

* Sat Jan 08 2022 Igor Vlasenko <viy@altlinux.org> 0.076-alt1
- automated CPAN update

* Wed Dec 29 2021 Igor Vlasenko <viy@altlinux.org> 0.075-alt1
- automated CPAN update

* Thu Nov 11 2021 Igor Vlasenko <viy@altlinux.org> 0.074-alt1
- automated CPAN update

* Sun Jul 18 2021 Igor Vlasenko <viy@altlinux.org> 0.073-alt1
- automated CPAN update

* Sun May 16 2021 Igor Vlasenko <viy@altlinux.org> 0.072-alt1
- automated CPAN update

* Wed Mar 31 2021 Igor Vlasenko <viy@altlinux.org> 0.071-alt1
- automated CPAN update

* Tue Feb 16 2021 Igor Vlasenko <viy@altlinux.ru> 0.070-alt1
- automated CPAN update

* Tue Sep 01 2020 Igor Vlasenko <viy@altlinux.ru> 0.069-alt1
- automated CPAN update

* Sat Mar 14 2020 Igor Vlasenko <viy@altlinux.ru> 0.068-alt1
- automated CPAN update

* Wed Feb 12 2020 Igor Vlasenko <viy@altlinux.ru> 0.067-alt1
- automated CPAN update

* Mon Oct 28 2019 Igor Vlasenko <viy@altlinux.ru> 0.066-alt1
- automated CPAN update

* Mon Jun 17 2019 Igor Vlasenko <viy@altlinux.ru> 0.064-alt1
- automated CPAN update

* Thu Jan 24 2019 Igor Vlasenko <viy@altlinux.ru> 0.063-alt1.1
- rebuild with new perl 5.28.1

* Fri Dec 07 2018 Igor Vlasenko <viy@altlinux.ru> 0.063-alt1
- automated CPAN update

* Tue Oct 30 2018 Igor Vlasenko <viy@altlinux.ru> 0.062-alt1
- automated CPAN update

* Sun Oct 28 2018 Igor Vlasenko <viy@altlinux.ru> 0.061-alt2
- fixed build

* Tue Jun 12 2018 Igor Vlasenko <viy@altlinux.ru> 0.061-alt1
- automated CPAN update

* Wed May 02 2018 Igor Vlasenko <viy@altlinux.ru> 0.060-alt1
- automated CPAN update

* Mon Mar 26 2018 Igor Vlasenko <viy@altlinux.ru> 0.059-alt1
- automated CPAN update

* Wed Mar 07 2018 Igor Vlasenko <viy@altlinux.ru> 0.058-alt1
- automated CPAN update

* Sat Feb 03 2018 Michael Shigorin <mike@altlinux.ru> 0.057-alt2
- E2K: uint128_t workaround

* Thu Feb 01 2018 Igor Vlasenko <viy@altlinux.ru> 0.057-alt1
- automated CPAN update

* Tue Dec 26 2017 Igor Vlasenko <viy@altlinux.ru> 0.056-alt1
- automated CPAN update

* Mon Dec 18 2017 Igor Vlasenko <viy@altlinux.ru> 0.055-alt1
- automated CPAN update

* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.054-alt1.1
- rebuild with new perl 5.26.1

* Wed Nov 01 2017 Igor Vlasenko <viy@altlinux.ru> 0.054-alt1
- automated CPAN update

* Tue Sep 26 2017 Igor Vlasenko <viy@altlinux.ru> 0.053-alt1
- automated CPAN update

* Wed Aug 30 2017 Igor Vlasenko <viy@altlinux.ru> 0.051-alt1
- automated CPAN update

* Wed Aug 02 2017 Igor Vlasenko <viy@altlinux.ru> 0.050-alt1
- automated CPAN update

* Tue May 09 2017 Igor Vlasenko <viy@altlinux.ru> 0.047-alt1
- automated CPAN update

* Mon Apr 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.045-alt1
- automated CPAN update

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.044-alt1.1
- rebuild with new perl 5.24.1

* Sun Dec 18 2016 Igor Vlasenko <viy@altlinux.ru> 0.044-alt1
- automated CPAN update

* Wed Oct 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.041-alt1
- automated CPAN update

* Tue Sep 20 2016 Igor Vlasenko <viy@altlinux.ru> 0.040-alt1
- automated CPAN update

* Mon Jul 25 2016 Igor Vlasenko <viy@altlinux.ru> 0.038-alt1
- automated CPAN update

* Sun Jul 03 2016 Igor Vlasenko <viy@altlinux.ru> 0.037-alt1
- automated CPAN update

* Mon Jun 13 2016 Igor Vlasenko <viy@altlinux.ru> 0.036-alt1
- automated CPAN update

* Sun Jun 05 2016 Igor Vlasenko <viy@altlinux.ru> 0.035-alt1
- automated CPAN update

* Thu May 26 2016 Igor Vlasenko <viy@altlinux.ru> 0.034-alt1
- automated CPAN update

* Tue May 03 2016 Igor Vlasenko <viy@altlinux.ru> 0.031-alt1
- automated CPAN update

* Wed Apr 20 2016 Igor Vlasenko <viy@altlinux.ru> 0.030-alt1
- automated CPAN update

* Mon Mar 28 2016 Igor Vlasenko <viy@altlinux.ru> 0.028-alt1
- automated CPAN update

* Mon Feb 22 2016 Sergey Y. Afonin <asy@altlinux.ru> 0.027-alt1
- initial build
