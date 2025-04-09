%define dist Crypt-DSA
Name: perl-%dist
Version: 1.19
Release: alt1

Summary: %dist - DSA signatures and key generation

License: Artistic
Group: Development/Perl
Url: %CPAN %dist

BuildArch: noarch
Source0: http://www.cpan.org/authors/id/T/TI/TIMLEGGE/%{dist}-%{version}.tar.gz

# Automatically added by buildreq on Tue Jun 17 2008
BuildRequires: openssl perl-Convert-PEM perl-Crypt-DES_EDE3 perl-Data-Buffer perl-Digest-SHA1 perl-Module-Install perl-File-Which perl(Crypt/URandom.pm)

%description
Crypt::DSA is an implementation of the DSA (Digital Signature Algorithm)
signature verification system. The implementation itself is pure Perl,
although the heavy-duty mathematics underneath are provided by the
Math::Pari library.  This package provides DSA signing, signature
verification, and key generation.

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc LICENSE Changes README
%perl_vendor_privlib/Crypt/DSA*

%changelog
* Fri Apr 04 2025 Igor Vlasenko <viy@altlinux.org> 1.19-alt1
- automated CPAN update

* Thu Sep 29 2011 Igor Vlasenko <viy@altlinux.ru> 1.17-alt1
- automated CPAN update

* Tue Dec 07 2010 Vladimir Lettiev <crux@altlinux.ru> 1.16-alt2
- fixed build with openssl 1.0.0b
  (patch from https://rt.cpan.org/Public/Bug/Display.html?id=49668)
- spec cleanup

* Fri Jul 16 2010 Igor Vlasenko <viy@altlinux.ru> 1.16-alt1
- automated CPAN update

* Sat Sep 06 2008 Vitaly Lipatov <lav@altlinux.ru> 0.14-alt2
- fix directory ownership violation

* Tue Jun 17 2008 Vitaly Lipatov <lav@altlinux.ru> 0.14-alt1
- new version 0.14 (with rpmrb script)

* Sat Aug 27 2005 Vitaly Lipatov <lav@altlinux.ru> 0.13-alt1
- first build for ALT Linux Sisyphus
