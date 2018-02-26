%define dist POE-Component-Logger
Name: perl-%dist
Version: 1.10
Release: alt1

Summary: A POE logging class
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sun Nov 20 2011
BuildRequires: perl-Log-Dispatch-Config perl-POE perl-Test-NoWarnings perl-Test-Pod perl-Time-Piece

%description
POE::Component::Logger provides a simple logging component that uses
Log::Dispatch::Config to drive it, allowing you to log to multiple places
at once (e.g. to STDERR and Syslog at the same time) and also to flexibly
define your logger's output.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/POE

%changelog
* Sun Nov 20 2011 Alexey Tourbin <at@altlinux.ru> 1.10-alt1
- 1.00 -> 1.10

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.00-alt1.1.1
- repair after perl 5.12 upgrade using girar-nmu

* Mon Oct 06 2008 Igor Vlasenko <viy@altlinux.ru> 1.00-alt1.1
- NMU for unknown reason

* Tue Jul 29 2008 Michael Bochkaryov <misha@altlinux.ru> 1.00-alt1
- first build for ALT Linux Sisyphus
