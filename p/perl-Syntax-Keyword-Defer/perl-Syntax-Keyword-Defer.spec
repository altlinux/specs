%define module_name Syntax-Keyword-Defer
#BuildRequires: perl(Future/AsyncAwait.pm)
# BEGIN SourceDeps(oneline):
BuildRequires: perl(ExtUtils/CBuilder.pm) perl(Module/Build.pm) perl(Syntax/Keyword/Try.pm) perl(Test/More.pm) perl(XS/Parse/Keyword.pm) perl(XS/Parse/Keyword/Builder.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.07
Release: alt1.1
Summary: add C<defer> block syntax to perl
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://mirror.yandex.ru/mirrors/cpan/authors/id/P/PE/PEVANS/%{module_name}-%{version}.tar.gz

%description
This module provides a syntax plugin that implements a block which executes
when the containing scope has finished.

It similar to features provided by other languages; Swift, Zig, Jai, Nim and
Odin all provide this. Note that while Go also provides a `defer' keyword,
the semantics here are not the same. Go's version defers until the end of the
entire function, rather than the closest enclosing scope as is common to most
other languages, and this module.

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc LICENSE README Changes
%perl_vendor_archlib/S*
%perl_vendor_autolib/*

%changelog
* Fri Dec 02 2022 Igor Vlasenko <viy@altlinux.org> 0.07-alt1.1
- to Sisyphus as perl-Sub-HandlesVia dep

* Wed Feb 23 2022 Igor Vlasenko <viy@altlinux.org> 0.07-alt1
- updated by package builder

* Mon Sep 06 2021 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- updated by package builder

* Wed Jun 16 2021 Igor Vlasenko <viy@altlinux.org> 0.05-alt2
- rebuild with perl 5.34.0

* Mon Apr 26 2021 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- updated by package builder

* Tue Mar 30 2021 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- initial import by package builder

