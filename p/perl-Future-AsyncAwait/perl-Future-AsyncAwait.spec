%define _unpackaged_files_terminate_build 1
#set_perl_req_method relaxed
%define module_name Future-AsyncAwait
%def_with bootstrap

#BuildRequires: perl(Devel/MAT.pm) perl(Devel/MAT/Dumper.pm)
# BEGIN SourceDeps(oneline):
BuildRequires: perl(ExtUtils/CBuilder.pm) perl(Future.pm) perl(IO/Async/Loop.pm) perl(Module/Build.pm) perl(Role/Tiny.pm) perl(Role/Tiny/With.pm) perl(Test/Fatal.pm) perl(Test/Future/Deferred.pm) perl(Test/MemoryGrowth.pm) perl(Test/More.pm) perl(Test/Refcount.pm) perl(Test2/V0.pm) perl(XS/Parse/Keyword.pm) perl(XS/Parse/Keyword/Builder.pm) perl(XS/Parse/Sublike.pm) perl(XS/Parse/Sublike/Builder.pm) perl(experimental.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators

%if_with bootstrap
# bootstrap loop with Syntax/Keyword* and Future-AsyncAwait
%define _without_test 1
%else
BuildRequires: /proc
#BuildRequires: perl(Devel/MAT.pm) perl(Devel/MAT/Dumper.pm)
BuildRequires: perl(Object/Pad.pm)
BuildRequires: perl(Syntax/Keyword/Defer.pm) perl(Syntax/Keyword/Dynamically.pm) perl(Syntax/Keyword/Match.pm) perl(Syntax/Keyword/MultiSub.pm) perl(Syntax/Keyword/Try.pm)
%endif

Name: perl-%module_name
Version: 0.66
Release: alt2.1
Summary: deferred subroutine syntax for futures
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://www.cpan.org/authors/id/P/PE/PEVANS/%{module_name}-%{version}.tar.gz

%description
This module provides syntax for deferring and resuming subroutines
while waiting for Futures to complete. This syntax aims to make code
that performs asynchronous operations using futures look neater and
more expressive than simply using then chaining and other techniques on
the futures themselves. It is also a similar syntax used by a number of
other languages; notably C# 5, EcmaScript 6, Python 3, Dart, Rust, C++20.

This module is still under active development. While it now seems
relatively stable enough for most use-cases and has received a lot of
"battle-testing" in a wide variety of scenarios, there may still be the
occasional case of memory leak left in it, especially if still-pending
futures are abandoned.

The new syntax takes the form of two new keywords, async and await.

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/F*
%perl_vendor_archlib/Test/Future/AsyncAwait/Awaitable.pm
%perl_vendor_autolib/*

%changelog
* Fri Nov 24 2023 Igor Vlasenko <viy@altlinux.org> 0.66-alt2.1
- rebuild with new perl 5.38.0 (bootstrapped)

* Mon Oct 23 2023 Igor Vlasenko <viy@altlinux.org> 0.66-alt2
- proper bootstrap support

* Wed Sep 13 2023 Igor Vlasenko <viy@altlinux.org> 0.66-alt1
- automated CPAN update

* Mon Mar 20 2023 Igor Vlasenko <viy@altlinux.org> 0.65-alt1
- automated CPAN update

* Wed Feb 15 2023 Igor Vlasenko <viy@altlinux.org> 0.64-alt1
- automated CPAN update

* Sun Feb 12 2023 Igor Vlasenko <viy@altlinux.org> 0.63-alt1
- automated CPAN update

* Sun Dec 25 2022 Igor Vlasenko <viy@altlinux.org> 0.62-alt1
- automated CPAN update

* Fri Dec 02 2022 Igor Vlasenko <viy@altlinux.org> 0.59-alt1.1
- bootstrap build (w/o Devel/MAT)
- to Sisyphus as perl-Sub-HandlesVia dep

* Tue Sep 27 2022 Igor Vlasenko <viy@altlinux.org> 0.59-alt1
- updated by package builder

* Sun May 01 2022 Igor Vlasenko <viy@altlinux.org> 0.58-alt1
- updated by package builder

* Fri Mar 25 2022 Igor Vlasenko <viy@altlinux.org> 0.57-alt1
- updated by package builder

* Fri Jan 28 2022 Igor Vlasenko <viy@altlinux.org> 0.56-alt1
- updated by package builder

* Sat Dec 18 2021 Igor Vlasenko <viy@altlinux.org> 0.55-alt1
- updated by package builder

* Fri Oct 29 2021 Igor Vlasenko <viy@altlinux.ru> 0.54-alt1
- updated by package builder

* Wed Sep 01 2021 Igor Vlasenko <viy@altlinux.ru> 0.53-alt1
- updated by package builder

* Sun Jul 18 2021 Igor Vlasenko <viy@altlinux.ru> 0.52-alt1
- updated by package builder

* Thu Jul 01 2021 Igor Vlasenko <viy@altlinux.ru> 0.51-alt1
- updated by package builder

* Wed Jun 16 2021 Igor Vlasenko <viy@altlinux.org> 0.50-alt2
- rebuild with perl 5.34.0

* Tue May 04 2021 Igor Vlasenko <viy@altlinux.ru> 0.50-alt1
- updated by package builder

* Thu Feb 25 2021 Igor Vlasenko <viy@altlinux.ru> 0.49-alt1
- updated by package builder

* Fri Feb 05 2021 Igor Vlasenko <viy@altlinux.ru> 0.48-alt1
- updated by package builder

* Mon Nov 30 2020 Igor Vlasenko <viy@altlinux.ru> 0.47-alt1
- updated by package builder

* Tue Nov 10 2020 Igor Vlasenko <viy@altlinux.ru> 0.46-alt1
- updated by package builder

* Sun Nov 01 2020 Igor Vlasenko <viy@altlinux.ru> 0.45-alt1
- updated by package builder

* Thu Oct 01 2020 Igor Vlasenko <viy@altlinux.ru> 0.43-alt1
- updated by package builder

* Fri Feb 01 2019 Cronbuild Service <cronbuild@altlinux.org> 0.20-alt1.1
- rebuild with perl 5.28.1

* Thu Jan 17 2019 Igor Vlasenko <viy@altlinux.ru> 0.20-alt1
- regenerated from template by package builder

* Sat Jan 12 2019 Igor Vlasenko <viy@altlinux.ru> 0.19-alt1
- regenerated from template by package builder

* Sat Jan 05 2019 Igor Vlasenko <viy@altlinux.ru> 0.17-alt1
- regenerated from template by package builder

* Fri Jan 04 2019 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1
- regenerated from template by package builder

* Wed Apr 04 2018 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1
- regenerated from template by package builder

* Mon Dec 18 2017 Igor Vlasenko <viy@altlinux.ru> 0.10-alt2
- rebuild with perl 5.26

* Wed Oct 25 2017 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1
- regenerated from template by package builder

* Wed May 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- initial import by package builder

