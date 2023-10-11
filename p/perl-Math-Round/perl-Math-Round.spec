%define _unpackaged_files_terminate_build 1
%define dist Math-Round
Name: perl-%dist
Version: 0.08
Release: alt1

Summary: Perl extension for rounding numbers
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/N/NE/NEILB/%{dist}-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sun Nov 13 2011
BuildRequires: perl-devel

%description
Math::Round supplies functions that will round numbers in different
ways.  The functions round and nearest are exported by
default; others are available as described below.  "use ... qw(:all)"
exports all functions.

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes LICENSE README
%perl_vendor_privlib/Math

%changelog
* Wed Oct 11 2023 Igor Vlasenko <viy@altlinux.org> 0.08-alt1
- automated CPAN update

* Sat Jan 03 2015 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- automated CPAN update

* Sun Nov 13 2011 Alexey Tourbin <at@altlinux.ru> 0.06-alt2
- rebuilt

* Thu Jul 08 2010 Vitaly Lipatov <lav@altlinux.ru> 0.06-alt1
- initial build for ALT Linux Sisyphus
