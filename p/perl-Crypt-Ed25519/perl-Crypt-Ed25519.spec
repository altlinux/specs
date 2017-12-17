%define _unpackaged_files_terminate_build 1
%define dist Crypt-Ed25519


Name: perl-%dist
Version: 1.04
Release: alt1.1

Summary: bare-bones Ed25519 public key signing/verification system
License: %perl_license
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/M/ML/MLEHMANN/%{dist}-%{version}.tar.gz

BuildRequires: rpm-build-licenses

BuildRequires: perl-devel perl-Canary-Stability perl-Encode

%description
This module implements Ed25519 public key generation, message signing and
verification. It is a pretty bare-bones implementation that implements
the standard Ed25519 variant with SHA512 hash, as well as a slower API
compatible with the upcoming EdDSA RFC.

The security target for Ed25519 is to be equivalent to 3000 bit RSA or
AES-128.

The advantages of Ed25519 over most other signing algorithms are:
small public/private key and signature sizes (<= 64 octets), good key
generation, signing and verification performance, no reliance on random
number generators for signing and by-design immunity against branch or
memory access pattern side-channel attacks.

More detailed praise and other info can be found at
http://ed25519.cr.yp.to/index.html.

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/Crypt
%perl_vendor_autolib/Crypt

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.04-alt1.1
- rebuild with new perl 5.26.1

* Wed Mar 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.04-alt1
- automated CPAN update

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.03-alt2.1
- rebuild with new perl 5.24.1

* Thu Apr 07 2016 Sergey Y. Afonin <asy@altlinux.ru> 1.03-alt2
- merged spec with package from autoimports

* Thu Feb 18 2016 Sergey Y. Afonin <asy@altlinux.ru> 1.03-alt1
- initial build for Sisyphus

* Wed Oct 14 2015 Igor Vlasenko <viy@altlinux.ru> 1.03-alt1
- regenerated from template by package builder

* Wed Apr 01 2015 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1
- initial import by package builder
