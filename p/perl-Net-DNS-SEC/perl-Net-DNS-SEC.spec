%define _unpackaged_files_terminate_build 1
%define module_name Net-DNS-SEC
# unsupported in libcrypto
%add_findreq_skiplist */perl5/Net/DNS/SEC/DSA.pm
%add_findreq_skiplist */perl5/Net/DNS/SEC/ECCGOST.pm
%add_findreq_skiplist */perl5/Net/DNS/SEC/EdDSA.pm

Name: perl-%module_name
Version: 1.22
Release: alt1

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
%doc demo Changes README WARNING
%perl_vendor_archlib/Net/DNS
%perl_vendor_autolib/Net/DNS

%changelog
* Wed Sep 13 2023 Igor Vlasenko <viy@altlinux.org> 1.22-alt1
- automated CPAN update

* Tue Jun 13 2023 Igor Vlasenko <viy@altlinux.org> 1.21-alt1
- automated CPAN update

* Thu Oct 06 2022 Igor Vlasenko <viy@altlinux.org> 1.20-alt1
- automated CPAN update

* Tue Oct 12 2021 Igor Vlasenko <viy@altlinux.org> 1.19-alt1
- automated CPAN update

* Tue Oct 06 2020 Igor Vlasenko <viy@altlinux.ru> 1.18-alt1
- automated CPAN update

* Sat Jul 04 2020 Igor Vlasenko <viy@altlinux.ru> 1.17-alt1
- automated CPAN update

* Fri Jun 05 2020 Igor Vlasenko <viy@altlinux.ru> 1.16-alt1
- automated CPAN update

* Wed Feb 12 2020 Igor Vlasenko <viy@altlinux.ru> 1.15-alt1
- automated CPAN update

* Tue Oct 15 2019 Igor Vlasenko <viy@altlinux.ru> 1.14-alt1
- automated CPAN update

* Sun May 12 2019 Igor Vlasenko <viy@altlinux.ru> 1.13-alt1
- automated CPAN update

* Thu Mar 21 2019 Igor Vlasenko <viy@altlinux.ru> 1.12-alt1
- automated CPAN update

* Thu Jan 24 2019 Igor Vlasenko <viy@altlinux.ru> 1.11-alt1.1
- rebuild with new perl 5.28.1

* Thu Dec 13 2018 Igor Vlasenko <viy@altlinux.ru> 1.11-alt1
- automated CPAN update

* Mon Oct 08 2018 Igor Vlasenko <viy@altlinux.ru> 1.10-alt1
- automated CPAN update

* Wed Aug 29 2018 Grigory Ustinov <grenka@altlinux.org> 1.09-alt1.1
- NMU: Rebuild with new openssl 1.1.0.

* Wed Jun 06 2018 Igor Vlasenko <viy@altlinux.ru> 1.09-alt1
- automated CPAN update

* Thu May 17 2018 Igor Vlasenko <viy@altlinux.ru> 1.08-alt1
- automated CPAN update

* Thu Apr 05 2018 Igor Vlasenko <viy@altlinux.ru> 1.07-alt1
- automated CPAN update

* Sat Mar 24 2018 Igor Vlasenko <viy@altlinux.ru> 1.06-alt1
- automated CPAN update

* Tue Mar 20 2018 Igor Vlasenko <viy@altlinux.ru> 1.05-alt1
- automated CPAN update

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
