%define _unpackaged_files_terminate_build 1
%define module_name Metrics-Any
# BEGIN SourceDeps(oneline):
BuildRequires: perl(List/Util.pm) perl(Module/Build.pm) perl(Test/Fatal.pm) perl(Test/More.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.09
Release: alt1.1
Summary: abstract collection of monitoring metrics
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://www.cpan.org/authors/id/P/PE/PEVANS/%{module_name}-%{version}.tar.gz
BuildArch: noarch

%description
Provides a central location for modules to report monitoring metrics, such as
counters of the number of times interesting events have happened, and programs
to collect up and send those metrics to monitoring services.

Inspired by the Log::Any manpage, this module splits the overall problem into two
sides. Modules wishing to provide metrics for monitoring purposes can use the
`use Metrics::Any' statement to obtain a *collector* into which they can
report metric events. By default this collector doesn't actually do anything,
so modules can easily use it without adding extra specific dependencies for
specific reporting.

A program using one or more such modules can apply a different policy and
request a particular *adapter* implementation in order to actually report
these metrics to some external system, by using the
`use Metrics::Any::Adapter' statement.

This separation of concerns allows module authors to write code which will
report metrics without needing to care about the exact mechanism of that
reporting (as well as to write code which does not itself depend on the code
required to perform that reporting).

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/M*

%changelog
* Sat Dec 24 2022 Igor Vlasenko <viy@altlinux.org> 0.09-alt1.1
- automated CPAN update

* Wed Dec 14 2022 Igor Vlasenko <viy@altlinux.org> 0.09-alt1
- automated CPAN update

* Wed Oct 12 2022 Igor Vlasenko <viy@altlinux.org> 0.08-alt1
- automated CPAN update

* Sat Jul 24 2021 Igor Vlasenko <viy@altlinux.org> 0.07-alt1
- automated CPAN update

* Thu Oct 01 2020 Igor Vlasenko <viy@altlinux.ru> 0.06-alt2
- to Sisyphus as IO-Async dep

* Sat Jul 04 2020 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- updated by package builder

* Thu May 14 2020 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- updated by package builder

* Mon May 04 2020 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- updated by package builder

* Wed Apr 29 2020 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- initial import by package builder

