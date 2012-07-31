# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-Devel-Hide
Version:        0.0008
Release:        alt2_13
Summary:        Forces the unavailability of specified Perl modules (for testing)
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/Devel-Hide/
Source0:        http://www.cpan.org/authors/id/F/FE/FERREIRA/Devel-Hide-%{version}.tar.gz
# 'defined(@array)' is deprecated - avoid warnings
# see https://rt.cpan.org/Public/Bug/Display.html?id=74225
Patch0:         rt74225.patch
BuildArch:      noarch
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Test/Pod.pm)
BuildRequires:  perl(Test/Pod/Coverage.pm)
Source44: import.info

%description
Given a list of Perl modules/filenames, this module makes require and
use statements fail (no matter the specified files/modules are
installed or not).

%prep
%setup -q -n Devel-Hide-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%install

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;


%check
make test

%files
%doc Changes README
%{perl_vendor_privlib}/*

%changelog
* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.0008-alt2_13
- update to new release by fcimport

* Fri May 25 2012 Igor Vlasenko <viy@altlinux.ru> 0.0008-alt2_9
- fc import

* Thu May 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.0008-alt1_9
- fc import

