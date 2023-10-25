%define _unpackaged_files_terminate_build 1
%set_perl_req_method relaxed
%ifarch ppc64le
%define _without_test 1
%endif
%define module_name Future-IO
%define test_module_name Test-Future-IO-Impl
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Future.pm) perl(Module/Build.pm) perl(Struct/Dumb.pm) perl(Test/ExpectAndCheck.pm) perl(Test/Future/IO/Impl.pm) perl(Test/Identity.pm) perl(Test/More.pm) perl(Test2/V0.pm) perl(Time/HiRes.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.15
Release: alt2
Summary: Future-returning IO methods
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://www.cpan.org/authors/id/P/PE/PEVANS/%{module_name}-%{version}.tar.gz
BuildArch: noarch

%description
This package provides a few basic methods that behave similarly to the
same-named core perl functions relating to IO operations, but yield their
results asynchronously via the Future manpage instances.

This is provided primarily as a decoupling mechanism, to allow modules to be
written that perform IO in an asynchronous manner to depend directly on this,
while allowing asynchronous event systems to provide an implementation of
these operations.


%package -n perl-%{test_module_name}
Summary: acceptance tests for Future::IO implementations
Group: Development/Perl

%description -n perl-%{test_module_name}
This module contains a collection of acceptance tests for implementations of Future::IO

%prep
%setup -q -n %{module_name}-%{version}

# ifarch ppc64le define _without_test 1 does not work for noarch :(
case `uname -m` in
    ppc64*|loongarch*)
    # hangs
    #rm -f t/04syswrite.t ?
    rm -f t/0[4-9]*.t
    ;;
esac

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/F*

%if 0
%files -n perl-%{test_module_name}
%perl_vendor_privlib/Test*
%endif

%changelog
* Wed Oct 25 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 0.15-alt2
- NMU: disable 04syswrite test on LoongArch too. Fixes FTBFS on LoongArch.

* Mon Oct 23 2023 Igor Vlasenko <viy@altlinux.org> 0.15-alt1
- automated CPAN update

* Sat Apr 29 2023 Igor Vlasenko <viy@altlinux.org> 0.14-alt1
- automated CPAN update

* Sat Feb 25 2023 Igor Vlasenko <viy@altlinux.org> 0.13-alt1
- automated CPAN update

* Tue Jan 31 2023 Igor Vlasenko <viy@altlinux.org> 0.12-alt1
- automated CPAN update

* Sat Jan 08 2022 Igor Vlasenko <viy@altlinux.org> 0.11-alt1
- automated CPAN update

* Tue Oct 12 2021 Igor Vlasenko <viy@altlinux.org> 0.10-alt2
- set test module name to Test-Future-IO-Impl

* Mon Oct 11 2021 Igor Vlasenko <viy@altlinux.org> 0.10-alt1
- automated CPAN update
- added test subpackage
- disabled tests on ppc64le

* Wed Jan 06 2021 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- automated CPAN update

* Wed Mar 25 2020 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- automated CPAN update

* Fri Jun 28 2019 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- automated CPAN update

* Mon Jun 17 2019 Igor Vlasenko <viy@altlinux.ru> 0.05-alt2
- to Sisyphus as perl-IO-Async dep

* Tue May 07 2019 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- updated by package builder

* Mon Apr 29 2019 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- updated by package builder

* Fri Apr 26 2019 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- updated by package builder

* Thu Apr 11 2019 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- updated by package builder

* Wed Apr 10 2019 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- initial import by package builder

