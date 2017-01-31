# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(base.pm) perl-podlators
# END SourceDeps(oneline)
Name:           perl-Test-Email
Version:        0.07
Release:        alt2_8
Summary:        Test Email Contents
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/Test-Email/
Source0:        http://www.cpan.org/authors/id/J/JA/JAMES/Test-Email-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(Mail/POP3Client.pm)
BuildRequires:  perl(Mail/Sendmail.pm)
BuildRequires:  perl(MIME/Entity.pm)
BuildRequires:  perl(MIME/Parser.pm)
BuildRequires:  perl(Test/Builder.pm)
Source44: import.info

%description
Test::Email is a subclass of MIME::Entity, with the above methods.
If you want the messages fetched from a POP3 account, use Test::POP3.

%prep
%setup -q -n Test-Email-%{version}

# Fix permissions
find -type f -exec chmod -x {} \;

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
# %{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendor_privlib}/*

%changelog
* Tue Jan 31 2017 Igor Vlasenko <viy@altlinux.ru> 0.07-alt2_8
- to Sisyphus

* Sun May 29 2016 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1_8
- update to new release by fcimport

* Wed Mar 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1_7
- update to new release by fcimport

* Mon Sep 21 2015 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1_5
- update to new release by fcimport

* Tue Sep 16 2014 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1_3
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1_2
- update to new release by fcimport

* Sat Jan 04 2014 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1_1
- update to new release by fcimport

* Mon Sep 02 2013 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1_14
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1_13
- update to new release by fcimport

* Mon Mar 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1_12
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1_11
- update to new release by fcimport

* Wed May 23 2012 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1_9
- fc import

