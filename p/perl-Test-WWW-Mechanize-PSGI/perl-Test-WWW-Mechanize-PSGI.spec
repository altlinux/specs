%define _unpackaged_files_terminate_build 1
Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Pod/Coverage/TrustPod.pm) perl(Pod/Wordlist.pm) perl(Test/CPAN/Changes.pm) perl(Test/Pod/Coverage.pm) perl(Test/Spelling.pm) perl(Test/Synopsis.pm) perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           perl-Test-WWW-Mechanize-PSGI
Version:        0.38
Release:        alt1
Summary:        Test PSGI programs using WWW::Mechanize
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/Test-WWW-Mechanize-PSGI/
Source0:        http://www.cpan.org/authors/id/O/OA/OALDERS/Test-WWW-Mechanize-PSGI-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{__perl}

BuildRequires:  rpm-build-perl
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(CGI/Cookie.pm)
BuildRequires:  perl(File/Spec.pm)
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(HTTP/Message/PSGI.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Test/WWW/Mechanize.pm)
BuildRequires:  perl(Try/Tiny.pm)

BuildRequires:  perl(base.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(warnings.pm)
Source44: import.info


%description
PSGI is a specification to decouple web server environments from web
application framework code. Test::WWW::Mechanize is a subclass of
WWW::Mechanize that incorporates features for web application testing. The
Test::WWW::Mechanize::PSGI module meshes the two to allow easy testing of
PSGI applications.

%prep
%setup -q -n Test-WWW-Mechanize-PSGI-%{version}

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor NO_PACKLIST=1
%{__make} %{?_smp_mflags}

%install
%{__make} pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

# %{_fixperms} $RPM_BUILD_ROOT/*

%check
%{__make} test

%files
%doc Changes CONTRIBUTORS README.md
%doc LICENSE
%{perl_vendor_privlib}/*

%changelog
* Sat Nov 25 2017 Igor Vlasenko <viy@altlinux.ru> 0.38-alt1
- automated CPAN update

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.37-alt1_2
- update to new release by fcimport

* Wed Aug 02 2017 Igor Vlasenko <viy@altlinux.ru> 0.37-alt1
- automated CPAN update

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.36-alt2_2
- update to new release by fcimport

* Tue Jan 31 2017 Igor Vlasenko <viy@altlinux.ru> 0.36-alt2_1
- to Sisyphus

* Fri Sep 30 2016 Igor Vlasenko <viy@altlinux.ru> 0.36-alt1_1
- update to new release by fcimport

* Sun May 29 2016 Igor Vlasenko <viy@altlinux.ru> 0.35-alt2_16
- update to new release by fcimport

* Wed Mar 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.35-alt2_15
- update to new release by fcimport

* Mon Sep 21 2015 Igor Vlasenko <viy@altlinux.ru> 0.35-alt2_13
- update to new release by fcimport

* Tue Sep 16 2014 Igor Vlasenko <viy@altlinux.ru> 0.35-alt2_11
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.35-alt2_10
- update to new release by fcimport

* Mon Sep 02 2013 Igor Vlasenko <viy@altlinux.ru> 0.35-alt2_9
- update to new release by fcimport

* Mon Mar 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.35-alt2_7
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.35-alt2_6
- update to new release by fcimport

* Fri May 25 2012 Igor Vlasenko <viy@altlinux.ru> 0.35-alt2_4
- fc import

* Thu May 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.35-alt1_4
- fc import

