# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-devel perl-podlators
# END SourceDeps(oneline)
BuildRequires: gcc-c++
Name:           perl-ExtUtils-CppGuess
Version:        0.11
Release:        alt1_2
Summary:        Guess C++ compiler and flags
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/ExtUtils-CppGuess/
Source0:        http://www.cpan.org/authors/id/D/DA/DAVIDO/ExtUtils-CppGuess-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(Capture/Tiny.pm)
BuildRequires:  perl(Cwd.pm)
BuildRequires:  perl(Exporter.pm)
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(ExtUtils/Manifest.pm)
BuildRequires:  perl(Fatal.pm)
BuildRequires:  perl(File/Path.pm)
BuildRequires:  perl(File/Spec/Functions.pm)
BuildRequires:  perl(Module/Build.pm)
BuildRequires:  perl(Test/More.pm)
Source44: import.info

%description
ExtUtils::CppGuess attempts to guess the system's C++ compiler that is
compatible with the C compiler that your perl was built with.

%prep
%setup -q -n ExtUtils-CppGuess-%{version}

%build
perl Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} \;

# %{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendor_privlib}/ExtUtils*

%changelog
* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1_2
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1_1
- update to new release by fcimport

* Tue Apr 07 2015 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1_1
- update to new release by fcimport

* Mon Jan 19 2015 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- automated CPAN update

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1_8
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1_7
- update to new release by fcimport

* Tue Feb 18 2014 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1_6
- moved to Sisyphus for Slic3r (by dd@ request)

* Thu Oct 03 2013 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- initial import by package builder

