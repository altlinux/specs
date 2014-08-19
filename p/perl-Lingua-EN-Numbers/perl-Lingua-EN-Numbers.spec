%define _unpackaged_files_terminate_build 1
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Exporter.pm) perl(Test.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-Lingua-EN-Numbers
Version:        2.00
Release:        alt1
Summary:        Turn "407" into "four hundred and seven", etc
License:        GPLv2
Group:          Development/Perl
URL:            http://search.cpan.org/dist/Lingua-EN-Numbers/
Source:        http://www.cpan.org/authors/id/N/NE/NEILB/Lingua-EN-Numbers-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(Test/More.pm)
Source44: import.info

%description
Lingua::EN::Numbers turns numbers into English text. It exports (upon
request) two functions, num2en and num2en_ordinal. Each takes a scalar
value and returns a scalar value. The return value is the English text
expressing that number; or if what you provided wasn't a number, then they
return undefined.

%prep
%setup -q -n Lingua-EN-Numbers-%{version}

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

# %{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes META.json README
%{perl_vendor_privlib}/*

%changelog
* Tue Aug 19 2014 Igor Vlasenko <viy@altlinux.ru> 2.00-alt1
- automated CPAN update

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.07-alt1_2
- update to new release by fcimport

* Thu Jun 05 2014 Igor Vlasenko <viy@altlinux.ru> 1.07-alt1_1
- converted for ALT Linux by srpmconvert tools

* Mon Jun 02 2014 Igor Vlasenko <viy@altlinux.ru> 1.07-alt1
- automated CPAN update

* Thu Feb 20 2014 Igor Vlasenko <viy@altlinux.ru> 1.06-alt2_1
- moved to Sisyphus for Slic3r (by dd@ request)

* Thu Jan 23 2014 Igor Vlasenko <viy@altlinux.ru> 1.06-alt1_1
- update to new release by fcimport

* Sat Dec 07 2013 Igor Vlasenko <viy@altlinux.ru> 1.05-alt1_1
- update to new release by fcimport

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 1.04-alt1_5
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 1.04-alt1_4
- update to new release by fcimport

* Fri Apr 26 2013 Igor Vlasenko <viy@altlinux.ru> 1.04-alt1_3
- initial fc import

