%define module_name Syntax-Keyword-Try
#BuildRequires: perl(Future/AsyncAwait.pm) perl(Syntax/Keyword/Defer.pm)
# BEGIN SourceDeps(oneline):
BuildRequires: perl(ExtUtils/CBuilder.pm) perl(Module/Build.pm) perl(Test/More.pm) perl(XS/Parse/Keyword.pm) perl(XS/Parse/Keyword/Builder.pm) perl(threads.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

# bootstrap loop with Syntax/Keyword* and Future-AsyncAwait
%define _without_test 1
#BuildRequires: perl(Future/AsyncAwait.pm)

Name: perl-%module_name
Version: 0.27
Release: alt1.1
Summary: a C<try/catch/finally> syntax for perl
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://mirror.yandex.ru/mirrors/cpan/authors/id/P/PE/PEVANS/%{module_name}-%{version}.tar.gz

%description
This module provides a syntax plugin that implements exception-handling
semantics in a form familiar to users of other languages, being built on a
block labeled with the `try' keyword, followed by at least one of a `catch'
or `finally' block.

As well as providing a handy syntax for this useful behaviour, this module
also serves to contain a number of code examples for how to implement parser
plugins and manipulate optrees to provide new syntax and behaviours for perl
code.
%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README LICENSE Changes
%perl_vendor_archlib/S*
%perl_vendor_autolib/*

%changelog
* Fri Dec 02 2022 Igor Vlasenko <viy@altlinux.org> 0.27-alt1.1
- to Sisyphus as perl-Sub-HandlesVia dep

* Wed Feb 23 2022 Igor Vlasenko <viy@altlinux.org> 0.27-alt1
- updated by package builder

* Wed Oct 13 2021 Igor Vlasenko <viy@altlinux.ru> 0.26-alt1
- updated by package builder

* Thu Jul 01 2021 Igor Vlasenko <viy@altlinux.ru> 0.25-alt1
- updated by package builder

* Wed Jun 16 2021 Igor Vlasenko <viy@altlinux.org> 0.24-alt2
- rebuild with perl 5.34.0

* Fri May 14 2021 Igor Vlasenko <viy@altlinux.ru> 0.24-alt1
- updated by package builder

* Tue Mar 30 2021 Igor Vlasenko <viy@altlinux.ru> 0.23-alt1
- updated by package builder

* Sun Jan 24 2021 Igor Vlasenko <viy@altlinux.ru> 0.21-alt1
- updated by package builder

* Thu Nov 26 2020 Igor Vlasenko <viy@altlinux.ru> 0.20-alt1
- updated by package builder

* Wed Oct 07 2020 Cronbuild Service <cronbuild@altlinux.org> 0.18-alt2
- rebuild to get rid of unmets

* Fri Aug 28 2020 Igor Vlasenko <viy@altlinux.ru> 0.18-alt1
- updated by package builder

* Fri Jul 24 2020 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1
- updated by package builder

* Tue Jul 21 2020 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1
- updated by package builder

* Wed Jul 15 2020 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1
- updated by package builder

* Wed Jul 01 2020 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1
- updated by package builder

* Sat Sep 07 2019 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1
- updated by package builder

* Fri Jun 14 2019 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1
- updated by package builder

* Fri Feb 01 2019 Cronbuild Service <cronbuild@altlinux.org> 0.09-alt2.1
- rebuild with perl 5.28.1

* Mon Dec 18 2017 Igor Vlasenko <viy@altlinux.ru> 0.09-alt2
- rebuild with perl 5.26

* Sat Nov 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1
- regenerated from template by package builder

* Thu Oct 26 2017 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- regenerated from template by package builder

* Wed Aug 02 2017 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- regenerated from template by package builder

* Sun Feb 12 2017 Cronbuild Service <cronbuild@altlinux.org> 0.04-alt2
- rebuild to get rid of unmets

* Wed Nov 30 2016 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- regenerated from template by package builder

* Mon Sep 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- initial import by package builder

