# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Test/More.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
%define upstream_name    Iterator
%define upstream_version 0.03

Name:       perl-%{upstream_name}
Version:    %{upstream_version}
Release:    alt1_6

Summary:    A general-purpose iterator class
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module//%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Exception/Class.pm)
BuildRequires: perl(ExtUtils/MakeMaker.pm)
BuildRequires: perl(Test/Simple.pm)
BuildArch: noarch
Source44: import.info

%description
This module is meant to be the definitive implementation of iterators, as
popularized by Mark Jason Dominus's lectures and recent book (_Higher Order
Perl_, Morgan Kauffman, 2005).

An "iterator" is an object, represented as a code block that generates the
"next value" of a sequence, and generally implemented as a closure. When
you need a value to operate on, you pull it from the iterator. If it
depends on other iterators, it pulls values from them when it needs to.
Iterators can be chained together (see the Iterator::Util manpage for
functions that help you do just that), queueing up work to be done but _not
actually doing it_ until a value is needed at the front end of the chain.
At that time, one data value is pulled through the chain.

Contrast this with ordinary array processing, where you load or compute all
of the input values at once, then loop over them in memory. It's analogous
to the difference between looping over a file one line at a time, and
reading the entire file into an array of lines before operating on it.

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
* Wed Feb 17 2016 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1_6
- update by mgaimport

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1_5
- update by mgaimport

* Tue Oct 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1_4
- update by mgaimport

* Mon Oct 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1_3
- update by mgaimport

* Tue Aug 06 2013 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1_2
- update by mgaimport

* Mon Dec 10 2012 Igor Vlasenko <viy@altlinux.ru>  0.03-alt1_1
- mageia import by cas@ requiest

