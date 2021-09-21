# BEGIN SourceDeps(oneline):
BuildRequires: perl(UNIVERSAL/require.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
%define module Benchmark-Timer

Name: perl-%module
Version: 0.7112
Release: alt2

Packager: Victor Forsiuk <force@altlinux.org>

Summary: Benchmarking with statistical confidence
License: GPLv2
Group: Development/Perl

Url: %CPAN %module
Source0: http://www.cpan.org/authors/id/D/DC/DCOPPIT/%{module}-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Mon Nov 22 2010
BuildRequires: perl-Module-Install perl-Statistics-TTest perl(Test/Compile.pm)

%description
The Benchmark::Timer class allows you to time portions of code conveniently, as
well as benchmark code by allowing timings of repeated trials. It is perfect
for when you need more precise information about the running time of portions
of your code than the Benchmark module will give you, but don't want to go all
out and profile your code.

%prep
%setup -q -n %{module}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc TODO LICENSE CHANGES README
%perl_vendor_privlib/Benchmark

%changelog
* Tue Sep 21 2021 Igor Vlasenko <viy@altlinux.org> 0.7112-alt2
- NMU for unknown reason:
  the person above was too neglectant to add --changelog "- NMU: <reason>" option.

* Thu Jul 12 2018 Igor Vlasenko <viy@altlinux.ru> 0.7112-alt1
- automated CPAN update

* Sun Jul 08 2018 Igor Vlasenko <viy@altlinux.ru> 0.7110-alt1
- automated CPAN update

* Fri May 22 2015 Igor Vlasenko <viy@altlinux.ru> 0.7107-alt1
- automated CPAN update

* Wed Apr 01 2015 Igor Vlasenko <viy@altlinux.ru> 0.7103-alt1
- automated CPAN update

* Mon Nov 22 2010 Victor Forsiuk <force@altlinux.org> 0.7102-alt1
- Initial build.
