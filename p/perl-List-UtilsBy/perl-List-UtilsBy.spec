Group: Development/Perl
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           perl-List-UtilsBy
Version:        0.11
Release:        alt1_7
Summary:        Higher-order list utility functions
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/List-UtilsBy
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/List-UtilsBy-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  rpm-build-perl
BuildRequires:  perl(Module/Build.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Exporter.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(warnings.pm)

# for improved testing
BuildRequires:  perl(Test/Pod.pm)
Source44: import.info


%description
This module provides a number of list utility functions, all of which take
an initial code block to control their behaviour. They are variations on
similar core perl or List::Util functions of similar names, but which use
the block to control their behaviour. For example, the core Perl function
sort takes a list of values and returns them, sorted into order by their
string value. The sort_by function sorts them according to the string value
returned by the extra function, when given each value.

%prep
%setup -q -n List-UtilsBy-%{version}

%build
/usr/bin/perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

# %{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes README
%%doc --no-dereference LICENSE
%{perl_vendor_privlib}/*

%changelog
* Wed Nov 20 2019 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1_7
- update to new release by fcimport

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1_5
- update to new release by fcimport

* Thu Feb 01 2018 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1
- automated CPAN update

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1
- automated CPAN update

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.09-alt2_8
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.09-alt2_7
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.09-alt2_6
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.09-alt2_5
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.09-alt2_4
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.09-alt2_3
- update to new release by fcimport

* Fri May 25 2012 Igor Vlasenko <viy@altlinux.ru> 0.09-alt2_1
- fc import

* Thu May 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1_1
- fc import

