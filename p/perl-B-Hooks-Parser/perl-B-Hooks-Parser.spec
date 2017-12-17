%define _unpackaged_files_terminate_build 1
%define module_name B-Hooks-Parser
# BEGIN SourceDeps(oneline):
BuildRequires: libsowing-devel perl(B/Hooks/EndOfScope.pm) perl(B/Hooks/OP/Check.pm) perl(DynaLoader.pm) perl(ExtUtils/Depends.pm) perl(ExtUtils/MakeMaker.pm) perl(File/Spec.pm) perl(Test/Exception.pm) perl(Test/More.pm) perl(parent.pm) perl(strict.pm) perl(warnings.pm) perl(Module/Metadata.pm) perl(Test/Fatal.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.19
Release: alt1.1
Summary: Interface to perl's parser variables
Group: Development/Perl
License: perl
URL: https://github.com/karenetheridge/B-Hooks-Parser

Source0: http://www.cpan.org/authors/id/E/ET/ETHER/%{module_name}-%{version}.tar.gz

%description
This module provides an API for parts of the perl parser. It can be used to
modify code while it's being parsed.


%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes LICENCE README
%perl_vendor_archlib/B*
%perl_vendor_autolib/*

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.19-alt1.1
- rebuild with new perl 5.26.1

* Tue May 09 2017 Igor Vlasenko <viy@altlinux.ru> 0.19-alt1
- automated CPAN update

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.17-alt1.1
- rebuild with new perl 5.24.1

* Tue Sep 20 2016 Igor Vlasenko <viy@altlinux.ru> 0.17-alt1
- automated CPAN update

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1.1
- rebuild with new perl 5.22.0

* Wed Oct 14 2015 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1
- regenerated from template by package builder

* Sat Dec 13 2014 Cronbuild Service <cronbuild@altlinux.org> 0.12-alt2
- rebuild to get rid of unmets

* Mon Sep 30 2013 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1
- initial import by package builder

