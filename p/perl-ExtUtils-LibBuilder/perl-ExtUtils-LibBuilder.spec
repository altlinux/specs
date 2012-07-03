%define dist ExtUtils-LibBuilder
Name: perl-%dist
Version: 0.04
Release: alt1

Summary: A tool to build C libraries
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Oct 19 2011
BuildRequires: perl-Module-Build perl-Test-Pod perl-Test-Pod-Coverage

%description
Some Perl modules need to ship C libraries together with their Perl
code. Although there are mechanisms to compile and link (or glue) C
code in your Perl programs, there isn't a clear method to compile
standard, self-contained C libraries.

This module main goal is to help in that task.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/ExtUtils

%changelog
* Wed Oct 19 2011 Alexey Tourbin <at@altlinux.ru> 0.04-alt1
- initial revision
