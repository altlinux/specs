# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(List/Util.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-Convert-Color
Version:        0.08
Release:        alt1_5
Summary:        Color space conversions and named lookups
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/Convert-Color/
Source0:        http://www.cpan.org/authors/id/P/PE/PEVANS/Convert-Color-%{version}.tar.gz
Patch0:         Convert-Color-0.07.diff
BuildArch:      noarch

BuildRequires:  perl(List/UtilsBy.pm)
BuildRequires:  perl(Module/Build.pm)
BuildRequires:  perl(Module/Pluggable.pm)
BuildRequires:  perl(Test/More.pm)
# For improved testing
BuildRequires:  perl(Test/Pod.pm)
BuildRequires:  xorg-rgb

Source44: import.info

%description
This module provides conversions between commonly used ways to express
colors. It provides conversions between color spaces such as RGB and HSV,
and it provides ways to look up colors by a name.

%prep
%setup -q -n Convert-Color-%{version}
%patch0 -p1

%build
%{__perl} Build.PL --install_path bindoc=%_man1dir installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;


%check
./Build test

%files
%doc Changes examples LICENSE README
%{perl_vendor_privlib}/*

%changelog
* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1_5
- update to new release by fcimport

* Sun May 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1_3
- fc import

