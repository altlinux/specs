%filter_from_requires /^perl.Paper.Specs.Axxxx.pm./d
%define module_version 0.10
%define module_name Paper-Specs
# BEGIN SourceDeps(oneline):
BuildRequires: perl-devel
# END SourceDeps(oneline)
Name:           perl-Paper-Specs
Version:        0.10
Release:        alt2
Summary:        Size and layout information for paper stock, forms, and labels
License:        perl
Group:          Development/Perl
URL:            http://search.cpan.org/dist/Paper-Specs/
Source0:        http://cpan.org.ua/authors/id/J/JO/JONALLEN/%module_name-%module_version.tar.gz
# https://rt.cpan.org/Public/Bug/Display.html?id=78027
Patch0:         %{name}-0.10-fix_Avery_5393.patch
BuildArch:      noarch
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(base.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Test/Pod.pm)
BuildRequires:  perl(Test/Pod/Coverage.pm)
Source44: import.info

%description
This package provides features such as:
- Layout PDF and PostScript documents
- Obtain page size information
- Support page sizes you didn't know about

%prep
%setup -n %module_name-%module_version
%patch0 -p1 

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

# %{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendor_privlib}/*

%changelog
* Wed Oct 16 2013 Igor Vlasenko <viy@altlinux.ru> 0.10-alt2
- build for Sisyphus (required for perl update)

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1_6
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1_5
- update to new release by fcimport

* Fri Apr 26 2013 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1_4
- initial fc import

