%define dist String-CamelCase
Name: perl-%dist
Version: 0.02
Release: alt1

Summary: CamelCase, de-camelcase
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Tue Nov 15 2011
BuildRequires: perl-Test-Pod perl-Test-Pod-Coverage

%description
CamelCase, de-camelcase

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/String

%changelog
* Tue Nov 15 2011 Alexey Tourbin <at@altlinux.ru> 0.02-alt1
- initial revision
