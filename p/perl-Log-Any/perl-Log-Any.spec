Name: perl-Log-Any
Version: 0.14
Release: alt1

Summary: Log::Any - bringing loggers and listeners together

License: Artistic
Group: Development/Perl
Url: %CPAN Log-Any

BuildArch: noarch
Source: http://www.cpan.org/authors/id/J/JS/JSWARTZ/Log-Any-0.14.tar.gz

# Automatically added by buildreq on Thu Nov 19 2009
BuildRequires: perl-Module-Install
Provides: perl(Log/Any/Adapter.pm)

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
* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1
- automated CPAN update

* Fri Jul 29 2011 Vladimir Lettiev <crux@altlinux.ru> 0.12-alt1
- 0.12
- spec cleanup

* Thu Nov 19 2009 Vitaly Lipatov <lav@altlinux.ru> 0.06-alt1
- initial build for ALT Linux Sisyphus

