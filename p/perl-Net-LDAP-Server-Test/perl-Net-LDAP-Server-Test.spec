# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Convert/ASN1.pm) perl-podlators
# END SourceDeps(oneline)
%define upstream_name    Net-LDAP-Server-Test
%define upstream_version 0.19

Name:       perl-%{upstream_name}
Version:    %{upstream_version}
Release:    alt4_6

Summary:    Test Net::LDAP code
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Net/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Data/Dump.pm)
BuildRequires: perl(ExtUtils/MakeMaker.pm)
BuildRequires: perl(IO/Select.pm)
BuildRequires: perl(IO/Socket.pm)
BuildRequires: perl(Net/LDAP.pm)
BuildRequires: perl(Net/LDAP/Server.pm)
BuildRequires: perl(Test/More.pm)
BuildArch:  noarch
Source44: import.info

%description
Now you can test your Net::LDAP code without having a real LDAP server
available.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes META.json META.yml  README
%perl_vendor_privlib/*

%changelog
* Tue Jan 31 2017 Igor Vlasenko <viy@altlinux.ru> 0.19-alt4_6
- to Sisyphus

* Wed Jul 27 2016 Igor Vlasenko <viy@altlinux.ru> 0.19-alt3_6
- update by mgaimport

* Sun Feb 21 2016 Igor Vlasenko <viy@altlinux.ru> 0.19-alt3_5
- update by mgaimport

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 0.19-alt3_4
- update by mgaimport

* Tue Oct 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.19-alt3_3
- update by mgaimport

* Tue Sep 02 2014 Cronbuild Service <cronbuild@altlinux.org> 0.19-alt3_2
- rebuild to get rid of unmets

* Tue Oct 29 2013 Igor Vlasenko <viy@altlinux.ru> 0.19-alt2_2
- mga update

* Fri Sep 13 2013 Cronbuild Service <cronbuild@altlinux.org> 0.19-alt2_1
- rebuild to get rid of unmets

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.19-alt1_1
- mgaimport update

* Thu Jul 25 2013 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1_1
- converted for ALT Linux by srpmconvert tools

