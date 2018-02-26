%define dist Test-Tester
Name: perl-%dist
Version: 0.108
Release: alt1

Summary: Ease testing test modules built with Test::Builder
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Mon Feb 20 2012
BuildRequires: perl-devel perl-threads

%description
If you have written a test module based on Test::Builder then Test::Tester
allows you to test it with the minimum of effort.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Test

%changelog
* Mon Feb 20 2012 Alexey Tourbin <at@altlinux.ru> 0.108-alt1
- 0.107 -> 0.108

* Mon Dec 08 2008 Mikhail Pokidko <pma@altlinux.org> 0.107-alt1
- initial build for ALT Linux Sisyphus
