%define dist Math-Round
Name: perl-%dist
Version: 0.06
Release: alt2

Summary: Perl extension for rounding numbers
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sun Nov 13 2011
BuildRequires: perl-devel

%description
Math::Round supplies functions that will round numbers in different
ways.  The functions round and nearest are exported by
default; others are available as described below.  "use ... qw(:all)"
exports all functions.

%prep
%setup -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Math
%perl_vendor_privlib/auto/Math

%changelog
* Sun Nov 13 2011 Alexey Tourbin <at@altlinux.ru> 0.06-alt2
- rebuilt

* Thu Jul 08 2010 Vitaly Lipatov <lav@altlinux.ru> 0.06-alt1
- initial build for ALT Linux Sisyphus
