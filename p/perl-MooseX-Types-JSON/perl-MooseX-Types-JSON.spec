%define dist MooseX-Types-JSON
Name: perl-%dist
Version: 0.02
Release: alt1

Summary: JSON datatype for Moose
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Tue Apr 13 2010
BuildRequires: perl-Class-C3-XS perl-JSON-XS perl-MooseX-Types perl-Test-Pod

%description
%summary.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/MooseX*

%changelog
* Tue Apr 13 2010 Alexey Tourbin <at@altlinux.ru> 0.02-alt1
- initial revision
