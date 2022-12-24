%define module_name Future-AsyncAwait
#BuildRequires: perl(Devel/MAT.pm) perl(Devel/MAT/Dumper.pm)
# BEGIN SourceDeps(oneline):
BuildRequires: perl(ExtUtils/CBuilder.pm) perl(Future.pm) perl(IO/Async/Loop.pm) perl(Module/Build.pm) perl(Object/Pad.pm) perl(Role/Tiny.pm) perl(Role/Tiny/With.pm) perl(Syntax/Keyword/Defer.pm) perl(Syntax/Keyword/Dynamically.pm) perl(Syntax/Keyword/Match.pm) perl(Syntax/Keyword/MultiSub.pm) perl(Syntax/Keyword/Try.pm) perl(Test/Fatal.pm) perl(Test/Future/Deferred.pm) perl(Test/MemoryGrowth.pm) perl(Test/More.pm) perl(Test/Refcount.pm) perl(XS/Parse/Keyword.pm) perl(XS/Parse/Keyword/Builder.pm) perl(XS/Parse/Sublike.pm) perl(XS/Parse/Sublike/Builder.pm) perl(experimental.pm)
# END SourceDeps(oneline)
# exclude for bootstrap:
# perl(Devel/MAT.pm) perl(Devel/MAT/Dumper.pm) perl(Object/Pad.pm) perl(Syntax/Keyword/Defer.pm) perl(Syntax/Keyword/Dynamically.pm) perl(Syntax/Keyword/Try.pm) 
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

# bootstrap loop with Syntax/Keyword* and Future-AsyncAwait
%define _without_test 1
#BuildRequires: perl(Devel/MAT.pm) perl(Devel/MAT/Dumper.pm) perl(Syntax/Keyword/Dynamically.pm) perl(Syntax/Keyword/Try.pm) perl(Object/Pad.pm)

Name: perl-%module_name
Version: 0.59
Release: alt1.1
Summary: deferred subroutine syntax for futures
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://mirror.yandex.ru/mirrors/cpan/authors/id/P/PE/PEVANS/%{module_name}-%{version}.tar.gz

%description
use Future::AsyncAwait;

 async sub do_a_thing
 {
    my $first = await do_first_thing();

    my $second = await do_second_thing();

    return combine_things( $first, $second );
 }

 do_a_thing()->get;

This module provides syntax for deferring and resuming subroutines while
waiting for the Future manpages to complete.

WARNING: The actual semantics in this module are not yet implemented. This
is released purely to demonstrate the syntax parts of its operation, to
reserve the name on CPAN, and to provide something that actually exists in
order to look at it. Don't expect to be able to use this module in any real
code yet.

That said, the only part that isn't actually implemented currently is the part
that suspends and resumes subroutines while waiting for a future to complete.
The syntax parsing, as well as semantics for immediate futures, are already
defined and working now. So it is already very slightly useful for writing
simple functions that return immediate futures.

Instead of writing

 sub foo
 {
    ...
    return Future->done( @result );
 }

you can now simply write

 async sub
 {
    ...
    return @result;
 }

with the added side-benefit that any exceptions thrown by the elided code will
be turned into an immediate-failed `Future' rather than making the call
itself propagate the exception, which is usually what you wanted when dealing
with futures.
%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes LICENSE README
%perl_vendor_archlib/F*
%perl_vendor_archlib/Test/Future/AsyncAwait/Awaitable.pm
%perl_vendor_autolib/*

%changelog
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

