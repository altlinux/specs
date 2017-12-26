%define _unpackaged_files_terminate_build 1
%define dist CryptX

Name: perl-%dist
Version: 0.056
Release: alt1

Summary: Crypto toolkit with multiple ciphers, hash functions and other
License: %perl_license
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/M/MI/MIK/%{dist}-%{version}.tar.gz

# Automatically added by buildreq on Mon Feb 22 2016
# optimized out: perl-CPAN-Meta perl-CPAN-Meta-Requirements perl-CPAN-Meta-YAML perl-Encode perl-ExtUtils-CBuilder perl-IPC-Cmd perl-JSON-PP perl-Locale-Maketext-Simple perl-Module-Load perl-Module-Load-Conditional perl-Module-Metadata perl-Params-Check perl-Parse-CPAN-Meta perl-Perl-OSType perl-Pod-Escapes perl-Pod-Simple perl-Types-Serialiser perl-common-sense perl-devel perl-parent perl-podlators
BuildRequires: perl-HTML-Parser perl-JSON-XS perl-Module-Build

BuildRequires: rpm-build-licenses libcxx-devel

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
