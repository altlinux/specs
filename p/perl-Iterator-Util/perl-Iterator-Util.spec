# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Exporter.pm) perl(Test/More.pm) perl(base.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
%define upstream_name    Iterator-Util
%define upstream_version 0.02

Name:       perl-%{upstream_name}
Version:    %{upstream_version}
Release:    alt1_6

Summary:    Essential utilities for the Iterator class
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Iterator/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Exception/Class.pm)
BuildRequires: perl(ExtUtils/MakeMaker.pm)
BuildRequires: perl(Iterator.pm)
BuildRequires: perl(Test/Simple.pm)
BuildArch: noarch
Source44: import.info

%description
This module implements many useful functions for creating and manipulating
iterator objects.

An "iterator" is an object, represented as a code block that generates the
"next value" of a sequence, and generally implemented as a closure. For
further information, including a tutorial on using iterator objects, see
the the Iterator manpage documentation.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor

%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml README
%perl_vendor_privlib/*




%changelog
* Wed Feb 17 2016 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1_6
- update by mgaimport

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1_5
- update by mgaimport

* Tue Oct 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1_4
- update by mgaimport

* Mon Oct 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1_3
- update by mgaimport

* Tue Aug 06 2013 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1_2
- update by mgaimport

* Mon Dec 10 2012 Igor Vlasenko <viy@altlinux.ru>  0.02-alt1_1
- mageia import by cas@ requiest

