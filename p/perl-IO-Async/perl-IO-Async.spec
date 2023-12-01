%define _unpackaged_files_terminate_build 1
%global oname IO-Async

Name: perl-%oname
Version: 0.802
Release: alt2

Summary: Asynchronous event-driven programming
Group: Development/Perl
License: perl

Url: %CPAN %oname
# https://cpan.metacpan.org/authors/id/P/PE/PEVANS/%oname-%version.tar.gz
Source: %oname-%version.tar

BuildArch: noarch
BuildRequires: /proc perl(IO/Socket/IP.pm) perl(Module/Build.pm) perl(Future.pm) perl(Future/Utils.pm) perl-devel perl(Struct/Dumb.pm) perl(Future/IO.pm)
# tests
BuildRequires: perl(Test/Refcount.pm) perl(Test/Fatal.pm) perl(Test/Future/IO/Impl.pm) perl(Test/Identity.pm) perl(Test/Metrics/Any.pm) perl(experimental.pm)

%add_findreq_skiplist */IO/Async/MergePoint.pm

%description
%summary

%package -n perl-Future-IO-Impl-IOAsync
Summary: Future::IO Implementation using IO::Async
Group: Development/Perl
Requires: %name = %EVR

%description -n perl-Future-IO-Impl-IOAsync
Future::IO Implementation using IO::Async

%package tests
Summary: Test modules for IO::Async
Group: Development/Perl
Requires: %name = %EVR

%description tests

This package contains tests for %name.

%prep
%setup -q -n %oname-%version

# on ppc64le, but ifarch did not expand here :(
[ `uname -m` = "ppc64le" ] && rm -f t/70future-io.t

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README examples
%perl_vendor_privlib/IO/Async*
%exclude %perl_vendor_privlib/IO/Async/LoopTests.pm
%exclude %perl_vendor_privlib/IO/Async/Test.pm

%files -n perl-Future-IO-Impl-IOAsync
%perl_vendor_privlib/Future/IO/Impl/IOAsync.pm

%files tests
%perl_vendor_privlib/IO/Async/LoopTests.pm
%perl_vendor_privlib/IO/Async/Test.pm

%changelog
* Fri Dec 01 2023 Igor Vlasenko <viy@altlinux.org> 0.802-alt2
- fixed build with perl 5.38

* Thu Aug 18 2022 Igor Vlasenko <viy@altlinux.org> 0.802-alt1
- new version

* Tue Dec 21 2021 Igor Vlasenko <viy@altlinux.org> 0.801-alt1
- new version

* Wed Nov 17 2021 Igor Vlasenko <viy@altlinux.org> 0.800-alt1
- new version

* Sat Aug 21 2021 Vitaly Lipatov <lav@altlinux.ru> 0.79-alt2
- pack tests to the submodule

* Fri Aug 20 2021 Igor Vlasenko <viy@altlinux.org> 0.79-alt1
- new version

* Wed Aug 18 2021 Vitaly Lipatov <lav@altlinux.ru> 0.78-alt2
- don't pack IO/Async/LoopTests.pm IO/Async/Test.pm

* Mon Jan 25 2021 Igor Vlasenko <viy@altlinux.ru> 0.78-alt1
- new version

* Thu Oct 01 2020 Igor Vlasenko <viy@altlinux.ru> 0.77-alt1
- new version

* Mon Feb 24 2020 Igor Vlasenko <viy@altlinux.ru> 0.75-alt1
- new version

* Sun Jul 07 2019 Igor Vlasenko <viy@altlinux.ru> 0.74-alt1
- new version

* Mon Jun 17 2019 Igor Vlasenko <viy@altlinux.ru> 0.73-alt2
- added perl-Future-IO-Impl-IOAsync subpackage

* Mon Jun 17 2019 Igor Vlasenko <viy@altlinux.ru> 0.73-alt1
- new version

* Thu Apr 05 2018 Igor Vlasenko <viy@altlinux.ru> 0.72-alt1
- automated CPAN update

* Fri Aug 18 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.71-alt1
- Updated to upstream version 0.71.

* Wed Nov 11 2015 Igor Vlasenko <viy@altlinux.ru> 0.69-alt1
- automated CPAN update

* Thu Oct 15 2015 Igor Vlasenko <viy@altlinux.ru> 0.68-alt1
- automated CPAN update

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 0.64-alt1
- automated CPAN update

* Fri Jul 25 2014 Igor Vlasenko <viy@altlinux.ru> 0.63-alt1
- automated CPAN update

* Tue Jun 24 2014 Igor Vlasenko <viy@altlinux.ru> 0.62-alt1
- automated CPAN update

* Sat Dec 14 2013 Vladimir Lettiev <crux@altlinux.ru> 0.61-alt1
- initial build for ALTLinux

