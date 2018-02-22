%define _unpackaged_files_terminate_build 1
%define module_name Net-DNS-SEC

Name: perl-%module_name
Version: 1.04
Release: alt1

Packager: Victor Forsiuk <force@altlinux.org>

Summary: %module_name module for perl
License: Perl
Group: Development/Perl

Url: %CPAN %module_name
Source0: http://www.cpan.org/authors/id/N/NL/NLNETLABS/%{module_name}-%{version}.tar.gz

#BuildArch: noarch

BuildRequires: perl-Net-DNS > 0.63 perl(Crypt/OpenSSL/EC.pm) perl(Crypt/OpenSSL/ECDSA.pm) perl(Digest/GOST.pm) libssl-devel
# Automatically added by buildreq on Thu Apr 08 2010
BuildRequires: perl-Crypt-OpenSSL-DSA perl-Crypt-OpenSSL-RSA perl-Digest-SHA perl-Digest-SHA1 perl-MIME-Base32 perl-Math-BigInt perl-Test-Pod

%description
DNSSEC extensions to Net::DNS.

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc demo Changes README
%perl_vendor_archlib/Net/DNS
%perl_vendor_autolib/Net/DNS

%changelog
* Thu Feb 22 2018 Igor Vlasenko <viy@altlinux.ru> 1.04-alt1
- automated CPAN update

* Tue Sep 20 2016 Igor Vlasenko <viy@altlinux.ru> 1.03-alt1
- automated CPAN update

* Mon Nov 02 2015 Igor Vlasenko <viy@altlinux.ru> 1.02-alt1
- automated CPAN update

* Tue Aug 19 2014 Igor Vlasenko <viy@altlinux.ru> 0.20-alt1
- automated CPAN update

* Tue Jun 10 2014 Igor Vlasenko <viy@altlinux.ru> 0.19-alt1
- automated CPAN update

* Tue May 13 2014 Igor Vlasenko <viy@altlinux.ru> 0.18-alt1
- automated CPAN update

* Mon Dec 02 2013 Igor Vlasenko <viy@altlinux.ru> 0.17-alt1
- automated CPAN update

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Thu Apr 08 2010 Victor Forsiuk <force@altlinux.org> 0.16-alt1
- 0.16

* Mon Oct 05 2009 Victor Forsyuk <force@altlinux.org> 0.15-alt1
- Initial build.
