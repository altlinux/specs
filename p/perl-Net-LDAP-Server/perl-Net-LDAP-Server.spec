# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(IO/Select.pm) perl(IO/Socket.pm) perl(Net/Daemon.pm) perl(base.pm) perl(fields.pm) perl-podlators
# END SourceDeps(oneline)
%define upstream_name    Net-LDAP-Server
%define upstream_version 0.43

Name:       perl-%{upstream_name}
Version:    %{upstream_version}
Release:    alt4_7

Summary:    LDAP server side protocol handling
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Net/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Convert/ASN1.pm)
BuildRequires: perl(ExtUtils/MakeMaker.pm)
BuildRequires: perl(Net/LDAP.pm)
BuildArch:  noarch
Source44: import.info

%description
no description found

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
%doc Changelog META.yml README examples
%perl_vendor_privlib/*

%changelog
* Tue Jan 31 2017 Igor Vlasenko <viy@altlinux.ru> 0.43-alt4_7
- to Sisyphus

* Wed Jul 27 2016 Igor Vlasenko <viy@altlinux.ru> 0.43-alt3_7
- update by mgaimport

* Sun Feb 21 2016 Igor Vlasenko <viy@altlinux.ru> 0.43-alt3_6
- update by mgaimport

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 0.43-alt3_5
- update by mgaimport

* Tue Oct 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.43-alt3_4
- update by mgaimport

* Tue Sep 02 2014 Cronbuild Service <cronbuild@altlinux.org> 0.43-alt3_3
- rebuild to get rid of unmets

* Tue Oct 29 2013 Igor Vlasenko <viy@altlinux.ru> 0.43-alt2_3
- mga update

* Fri Sep 13 2013 Cronbuild Service <cronbuild@altlinux.org> 0.43-alt2_2
- rebuild to get rid of unmets

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.43-alt1_2
- mgaimport update

* Thu Jul 25 2013 Igor Vlasenko <viy@altlinux.ru> 0.43-alt1_1
- converted for ALT Linux by srpmconvert tools

