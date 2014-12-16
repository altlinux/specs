# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Test/Kwalitee.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-Lingua-EN-Numbers-Easy
Version:        2014120401
Release:        alt1
Summary:        Hash access to Lingua::EN::Numbers objects
License:        MIT
Group:          Development/Perl
URL:            http://search.cpan.org/dist/Lingua-EN-Numbers-Easy/
Source:        http://www.cpan.org/authors/id/A/AB/ABIGAIL/Lingua-EN-Numbers-Easy-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Lingua/EN/Numbers.pm)

 # Filters (not)shared c libs
Source44: import.info

%description
Lingua::EN::Numbers is a module that translates numbers to English words.
Unfortunately, it has an object oriented interface, which makes it hard to
interpolate them in strings. Lingua::EN::Numbers::Easy translates numbers
to words using a tied hash, which can be interpolated.

%prep
%setup -q -n Lingua-EN-Numbers-Easy-%{version}

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;

# %{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes
%{perl_vendor_privlib}/*

%changelog
* Tue Dec 16 2014 Igor Vlasenko <viy@altlinux.ru> 2014120401-alt1
- automated CPAN update

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 2009110701-alt2_7
- update to new release by fcimport

* Thu Feb 20 2014 Igor Vlasenko <viy@altlinux.ru> 2009110701-alt2_6
- moved to Sisyphus for Slic3r (by dd@ request)

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 2009110701-alt1_6
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 2009110701-alt1_5
- update to new release by fcimport

* Fri Apr 26 2013 Igor Vlasenko <viy@altlinux.ru> 2009110701-alt1_4
- initial fc import

