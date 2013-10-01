Serial: 1
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Test/More.pm) perl-Module-Build perl-base perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-Modern-Perl
Version:        1.03
Release:        alt1_7
Summary:        Enable all of the features of Modern Perl with one command
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/Modern-Perl/
Source0:        http://www.cpan.org/authors/id/C/CH/CHROMATIC/Modern-Perl-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl(Module/Build.pm)
BuildRequires:  perl(Test/Simple.pm)
Source44: import.info
Provides: perl(Modern/Perl.pm) = 2012.0

%description
Modern Perl often relies on the presence of several core and CPAN pragmas
and modules.  Wouldn't it be nice to use them all with a single command?

%prep
%setup -q -n Modern-Perl-%{version}

%build
%{__perl} Build.PL --install_path bindoc=%_man1dir installdirs=vendor
./Build

%install

./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

# %{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes README
%{perl_vendor_privlib}/*

%changelog
* Tue Oct 01 2013 Igor Vlasenko <viy@altlinux.ru> 1:1.03-alt1_7
- added provides

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 1.20121103-alt1
- automated CPAN update

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.03-alt2_5
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 1.03-alt2_4
- update to new release by fcimport

* Fri May 25 2012 Igor Vlasenko <viy@altlinux.ru> 1.03-alt2_2
- fc import

* Thu May 24 2012 Igor Vlasenko <viy@altlinux.ru> 1.03-alt1_2
- fc import

