# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Symbol.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-Test-Without-Module
Version:        0.17
Release:        alt2_11
Summary:        Test fallback behavior in absence of modules
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/Test-Without-Module/
Source0:        http://www.cpan.org/modules/by-module/Test/Test-Without-Module-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(File/Slurp.pm)
BuildRequires:  perl(File/Spec.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Test/Pod.pm)


Source44: import.info

%description
This module allows you to deliberately hide modules from a program even
though they are installed. This is mostly useful for testing modules that
have a fallback when a certain dependency module is not installed.

%prep
%setup -q -n Test-Without-Module-%{version}
find . -type f -exec chmod 644 {} \;
sed -i -e 's/\r//' README Changes

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;


%check
make test

%files
%doc Changes README
%{perl_vendor_privlib}/*

%changelog
* Fri Dec 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.17-alt2_11
- update to new release by fcimport

* Tue Nov 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.17-alt2_9
- sisyphus release

* Sat Nov 10 2012 Igor Vlasenko <viy@altlinux.ru> 0.17-alt1_9
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.17-alt1_8
- update to new release by fcimport

* Wed May 23 2012 Igor Vlasenko <viy@altlinux.ru> 0.17-alt1_6
- fc import

