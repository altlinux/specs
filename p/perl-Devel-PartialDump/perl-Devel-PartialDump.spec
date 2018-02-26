%define dist Devel-PartialDump
Name: perl-%dist
Version: 0.15
Release: alt1

Summary: Partial dumping of data structures, optimized for argument printing
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sun Nov 20 2011
BuildRequires: perl-Moose perl-Test-Warn perl-Test-use-ok perl-namespace-clean

%description
This module is a data dumper optimized for logging of arbitrary parameters.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes
%perl_vendor_privlib/Devel

%changelog
* Sun Nov 20 2011 Alexey Tourbin <at@altlinux.ru> 0.15-alt1
- initial revision
