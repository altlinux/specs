%define dist Devel-Autoflush
Name: perl-%dist
Version: 0.06
Release: alt1

Summary: Set autoflush from the command line
License: Apache
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/D/DA/DAGOLDEN/Devel-Autoflush-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Fri Sep 28 2012
BuildRequires: perl-IO-CaptureOutput perl-Module-Build

%description
This module is a hack to set autoflush for STDOUT and STDERR from the
command line or from PERL5OPT for code that needs it but doesn't have it.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Devel

%changelog
* Sat Mar 08 2014 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- automated CPAN update

* Fri Sep 28 2012 Alexey Tourbin <at@altlinux.ru> 0.05-alt1
- initial revision
