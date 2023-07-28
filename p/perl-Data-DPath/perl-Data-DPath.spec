%define _unpackaged_files_terminate_build 1
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Pod/Coverage/TrustPod.pm) perl(Test/EOL.pm) perl(Test/NoTabs.pm) perl(Test/Pod.pm) perl(Test/Pod/Coverage.pm) perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define upstream_name    Data-DPath
%define upstream_version 0.58

%{?perl_default_filter}

Name:       perl-%{upstream_name}
Version:    0.59
Release:    alt1

Summary:    Magic functions available inside filter conditions
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/authors/id/S/SC/SCHWIGON/%{upstream_name}-%{version}.tar.gz

BuildRequires: perl(Class/XSAccessor.pm)
BuildRequires: perl(Class/XSAccessor/Array.pm)
BuildRequires: perl(Data/Dumper.pm)
BuildRequires: perl(ExtUtils/MakeMaker.pm)
BuildRequires: perl(File/Spec.pm)
BuildRequires: perl(IO/Handle.pm)
BuildRequires: perl(IPC/Open3.pm)
BuildRequires: perl(Iterator/Util.pm)
BuildRequires: perl(List/Util.pm)
BuildRequires: perl(POSIX.pm)
BuildRequires: perl(Safe.pm)
BuildRequires: perl(Scalar/Util.pm)
BuildRequires: perl(Sub/Exporter.pm)
BuildRequires: perl(Test/Deep.pm)
BuildRequires: perl(Test/More.pm)
BuildRequires: perl(Text/Balanced.pm)
BuildRequires: perl(aliased.pm)
BuildRequires: perl(blib.pm)
BuildRequires: perl(constant.pm)
BuildRequires: perl(if.pm)
BuildRequires: perl(strict.pm)
BuildRequires: perl(utf8.pm)
BuildRequires: perl(warnings.pm)
BuildArch:  noarch
Source44: import.info

%description
no description found

%prep
%setup -q -n %{upstream_name}-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.json META.yml README todo.org
%{perl_vendor_privlib}/*

%changelog
* Fri Jul 28 2023 Igor Vlasenko <viy@altlinux.org> 0.59-alt1
- automated CPAN update

* Wed Sep 18 2019 Igor Vlasenko <viy@altlinux.ru> 0.58-alt1_1
- update by mgaimport

* Thu Aug 29 2019 Igor Vlasenko <viy@altlinux.ru> 0.58-alt1
- automated CPAN update

* Fri Mar 01 2019 Igor Vlasenko <viy@altlinux.ru> 0.57-alt1_3
- update by mgaimport

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

