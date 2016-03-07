# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(APR/Table.pm) perl(Apache.pm) perl(Apache/Constants.pm) perl(Apache2/Const.pm) perl(Apache2/RequestIO.pm) perl(Apache2/RequestRec.pm) perl(Apache2/RequestUtil.pm) perl(Exporter.pm) perl(FindBin.pm) perl(SOAP/Lite.pm) perl(SOAP/Transport/HTTP.pm) perl(base.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
%global perlname Apache2-SOAP

Name:      perl-Apache2-SOAP
Version:   0.73
Release:   alt1_20
Summary:   A replacement for Apache::SOAP designed to work with mod_perl 2

Group:     Development/Perl
License:   GPL+ or Artistic
URL:       http://search.cpan.org/dist/Apache2-SOAP/
Source:    http://search.cpan.org/CPAN/authors/id/R/RK/RKOBES/%{perlname}-%{version}.tar.gz

BuildArch: noarch

BuildRequires: perl(ExtUtils/MakeMaker.pm)
BuildRequires: apache2-mod_perl-devel
# perl(ModPerl::MM) is provided by mod_perl on EL5, by mod_perl-devel on Fedora
#BuildRequires: perl(ModPerl::MM)
# BR for test (disabled)
#BuildRequires: httpd, perl(SOAP::Lite), perl(LWP::UserAgent)
#BuildRequires: perl(Test::More)



Source44: import.info


%description
This Apache Perl module provides the ability to add support for SOAP
(Simple Object Access Protocol) protocol with easy configuration
(either in .conf or in .htaccess file). This functionality should
give you lightweight option for hosting SOAP services and greatly
simplify configuration aspects. This module inherites functionality
from SOAP::Transport::HTTP2::Apache component of SOAP::Lite module.


%prep
%setup -q -n %{perlname}-%{version}


%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}


%install
make pure_install PERL_INSTALL_ROOT=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';' -print
find %{buildroot} -type d -depth -exec rmdir {} 2>/dev/null ';' -print
chmod -R u+rwX,go+rX,go-w %{buildroot}/*


%files
%doc Changes README
%{perl_vendor_privlib}/Apache2
%{perl_vendor_privlib}/SOAP/Transport/HTTP2.pm


%changelog
* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.73-alt1_20
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.73-alt1_19
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.73-alt1_17
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.73-alt1_16
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.73-alt1_15
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.73-alt1_14
- update to new release by fcimport

* Sun Apr 14 2013 Igor Vlasenko <viy@altlinux.ru> 0.73-alt1_13
- fixed build

* Sun Sep 25 2011 Igor Vlasenko <viy@altlinux.ru> 0.73-alt1
- automated CPAN update

* Mon Dec 15 2008 Lebedev Sergey <barabashka@altlinux.org> 0.72-alt3.1
- moved back noarch, removed empty dir perl_vendor_autolib/Apache2*

* Mon Dec 15 2008 Lebedev Sergey <barabashka@altlinux.org> 0.72-alt3
- removed noarch from package due to perl_vendor_autolib/Apache2

* Mon Dec 15 2008 Lebedev Sergey <barabashka@altlinux.org> 0.72-alt2
- fixed ownership viloation 

* Sun Apr 06 2008 Sir Raorn <raorn@altlinux.ru> 0.72-alt1
- first build for ALT Linux Sisyphus

