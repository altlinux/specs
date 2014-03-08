%define dist IO-CaptureOutput
Name: perl-%dist
Version: 1.1103
Release: alt1

Summary: Capture STDOUT and STDERR from Perl code, subprocesses or XS
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/D/DA/DAGOLDEN/IO-CaptureOutput-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Fri Sep 28 2012
BuildRequires: perl-HTML-Parser perl-Inline perl-Inline-Files perl-Module-Build perl-Parse-RecDescent

%description
This module provides routines for capturing STDOUT and STDERR from perl
subroutines, forked system calls (e.g. "system()", "fork()") and from XS
or C modules.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/IO

%changelog
* Sat Mar 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.1103-alt1
- automated CPAN update

* Fri Sep 28 2012 Alexey Tourbin <at@altlinux.ru> 1.1102-alt1
- initial revision
