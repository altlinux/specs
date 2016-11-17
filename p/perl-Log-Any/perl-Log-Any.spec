%define _unpackaged_files_terminate_build 1
Name: perl-Log-Any
Version: 1.045
Release: alt1

Summary: Log::Any - bringing loggers and listeners together

License: Artistic
Group: Development/Perl
Url: %CPAN Log-Any

BuildArch: noarch
Source: http://www.cpan.org/authors/id/P/PR/PREACTION/Log-Any-%{version}.tar.gz

# Automatically added by buildreq on Thu Nov 19 2009
BuildRequires: perl-Module-Install

%description
`Log::Any' allows CPAN modules to safely and efficiently log messages,
while letting the application choose (or decline to choose) a logging
mechanism such as `Log::Dispatch' or `Log::Log4perl'.

`Log::Any' has a very tiny footprint and no dependencies beyond Perl 5.6,
which makes it appropriate for even small CPAN modules to use.
It defaults to 'null' logging activity, so a module can safely log
without worrying about whether the application has chosen (or will ever choose)
a logging mechanism.

The application, in turn, may choose one or more logging mechanisms via Log::Any::Adapter.

%prep
%setup -q -n Log-Any-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Log/Any*

%changelog
* Thu Nov 17 2016 Igor Vlasenko <viy@altlinux.ru> 1.045-alt1
- automated CPAN update

* Tue Sep 20 2016 Igor Vlasenko <viy@altlinux.ru> 1.042-alt1
- automated CPAN update

* Thu Mar 03 2016 Igor Vlasenko <viy@altlinux.ru> 1.040-alt1
- automated CPAN update

* Fri Oct 16 2015 Igor Vlasenko <viy@altlinux.ru> 1.032-alt1
- automated CPAN update

* Mon Sep 16 2013 Igor Vlasenko <viy@altlinux.ru> 0.15-alt2
- Log::Any::Adapter is in separate package

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1
- automated CPAN update

* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1
- automated CPAN update

* Fri Jul 29 2011 Vladimir Lettiev <crux@altlinux.ru> 0.12-alt1
- 0.12
- spec cleanup

* Thu Nov 19 2009 Vitaly Lipatov <lav@altlinux.ru> 0.06-alt1
- initial build for ALT Linux Sisyphus

