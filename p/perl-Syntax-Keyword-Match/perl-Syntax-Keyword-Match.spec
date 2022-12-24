%define module_name Syntax-Keyword-Match
#BuildRequires: perl(Future/AsyncAwait.pm)
# BEGIN SourceDeps(oneline):
BuildRequires: perl(ExtUtils/CBuilder.pm) perl(Module/Build.pm) perl(Test/More.pm) perl(XS/Parse/Infix/Builder.pm) perl(XS/Parse/Keyword.pm) perl(XS/Parse/Keyword/Builder.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.09
Release: alt2
Summary: a C<match/case> syntax for perl
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://mirror.yandex.ru/mirrors/cpan/authors/id/P/PE/PEVANS/%{module_name}-%{version}.tar.gz

%description
This module provides a syntax plugin that implements a control-flow block
called `match/case', which executes at most one of a choice of different
blocks depending on the value of its controlling expression.

This is similar to C's `switch/case' syntax (copied into many other
languages), or syntax provided by the Switch::Plain manpage.

This is an initial, experimental implementation. Furthermore, it is built as
a non-trivial example use-case on top of the XS::Parse::Keyword manpage, which is also
experimental. No API or compatbility guarantees are made at this time.

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README LICENSE
%perl_vendor_archlib/S*
%perl_vendor_autolib/*

%changelog
* Fri Dec 23 2022 Igor Vlasenko <viy@altlinux.org> 0.09-alt2
- to Sisyphus as Future-AsyncAwait dependency

* Wed Feb 23 2022 Igor Vlasenko <viy@altlinux.org> 0.09-alt1
- updated by package builder

* Mon Sep 06 2021 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- updated by package builder

* Wed Jun 16 2021 Igor Vlasenko <viy@altlinux.org> 0.04-alt2
- rebuild with perl 5.34.0

* Fri May 28 2021 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- updated by package builder

* Mon Apr 26 2021 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- updated by package builder

* Wed Apr 21 2021 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- initial import by package builder

