%define _unpackaged_files_terminate_build 1
%define module_name Future-IO
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Future.pm) perl(Module/Build.pm) perl(Struct/Dumb.pm) perl(Test/Identity.pm) perl(Test/More.pm) perl(Time/HiRes.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.08
Release: alt1
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

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/F*

%changelog
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

