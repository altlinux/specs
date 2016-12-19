# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(CPAN.pm) perl-Module-Build perl-podlators
# END SourceDeps(oneline)
Name:           perl-accessors
Version:        1.01
Release:        alt1_20
Summary:        Create accessor methods in caller's package
License:        GPL+ or Artistic
Group:          Development/Other
URL:            http://search.cpan.org/dist/accessors/
Source0:        http://www.cpan.org/authors/id/S/SP/SPURKIS/accessors-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl(Module/Build.pm)
BuildRequires:  perl(Test/More.pm)
Source44: import.info

%description
The accessors pragma lets you create simple accessors at compile-time.

%prep
%setup -q -n accessors-%{version}

%build
%{__perl} Build.PL --install_path bindoc=%_man1dir installdirs=vendor
./Build

%install

./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

# %{_fixperms} $RPM_BUILD_ROOT/*

# A few of the .pm modules have bogus execute permission
find $RPM_BUILD_ROOT%{perl_vendor_privlib} -name *.pm | xargs chmod a-x

%check
./Build test

%files
%doc Changes README TODO
%{perl_vendor_privlib}/*

%changelog
* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 1.01-alt1_20
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 1.01-alt1_19
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.01-alt1_18
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.01-alt1_16
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.01-alt1_15
- update to new release by fcimport

* Wed Aug 07 2013 Igor Vlasenko <viy@altlinux.ru> 1.01-alt1_14
- Sisyphus build

* Mon Mar 04 2013 Igor Vlasenko <viy@altlinux.ru> 1.01-alt1_12
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 1.01-alt1_11
- update to new release by fcimport

* Thu May 24 2012 Igor Vlasenko <viy@altlinux.ru> 1.01-alt1_9
- fc import

