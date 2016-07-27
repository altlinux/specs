# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Pod/Coverage/TrustPod.pm) perl(Test/EOL.pm) perl(Test/NoTabs.pm) perl(Test/Pod.pm) perl(Test/Pod/Coverage.pm) perl-podlators
# END SourceDeps(oneline)
%define upstream_name    Data-DPath
%define upstream_version 0.55

%{?perl_default_filter}

Name:       perl-%{upstream_name}
Version:    %{upstream_version}
Release:    alt1_3

Summary:    Magic functions available inside filter conditions
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Data/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Class/XSAccessor.pm)
BuildRequires: perl(Class/XSAccessor/Array.pm)
BuildRequires: perl(Data/Dumper.pm)
BuildRequires: perl(ExtUtils/MakeMaker.pm)
BuildRequires: perl(Iterator/Util.pm)
BuildRequires: perl(List/MoreUtils.pm)
BuildRequires: perl(List/Util.pm)
BuildRequires: perl(POSIX.pm)
BuildRequires: perl(Safe.pm)
BuildRequires: perl(Scalar/Util.pm)
BuildRequires: perl(Sub/Exporter.pm)
BuildRequires: perl(Test/Deep.pm)
BuildRequires: perl(Test/More.pm)
BuildRequires: perl(Text/Balanced.pm)
BuildRequires: perl(aliased.pm)
BuildRequires: perl(constant.pm)
BuildRequires: perl(strict.pm)
BuildRequires: perl(warnings.pm)
BuildArch:  noarch
Source44: import.info

%description
no description found

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor

%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes LICENSE META.json META.yml  README
%{perl_vendor_privlib}/*


%changelog
* Wed Jul 27 2016 Igor Vlasenko <viy@altlinux.ru> 0.55-alt1_3
- update by mgaimport

* Tue Mar 29 2016 Igor Vlasenko <viy@altlinux.ru> 0.55-alt1_2
- update by mgaimport

* Fri Nov 27 2015 Igor Vlasenko <viy@altlinux.ru> 0.55-alt1_1
- update by mgaimport

* Thu Nov 12 2015 Igor Vlasenko <viy@altlinux.ru> 0.55-alt1
- automated CPAN update

* Mon Sep 28 2015 Igor Vlasenko <viy@altlinux.ru> 0.54-alt1_1
- update by mgaimport

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 0.50-alt1_3
- update by mgaimport

* Tue Apr 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.50-alt1_1
- update by mgaimport

* Mon Oct 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.49-alt1_3
- update by mgaimport

* Tue Aug 06 2013 Igor Vlasenko <viy@altlinux.ru> 0.49-alt1_2
- update by mgaimport

* Sat Jul 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.49-alt1
- automated CPAN update

* Mon Dec 10 2012 Igor Vlasenko <viy@altlinux.ru>  0.47-alt1_1
- mageia import by cas@ requiest

