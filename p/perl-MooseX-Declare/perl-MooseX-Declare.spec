%define dist MooseX-Declare
Name: perl-%dist
Version: 0.35
Release: alt1

Summary: Declarative syntax for Moose
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sun Nov 20 2011
BuildRequires: perl-MooseX-Method-Signatures perl-MooseX-Role-Parameterized perl-Test-Exception perl-Test-NoWarnings

%description
This module provides syntactic sugar for Moose, the postmodern object
system for Perl 5.  When used, it sets up the "class" and "role" keywords.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/MooseX

%changelog
* Sun Nov 20 2011 Alexey Tourbin <at@altlinux.ru> 0.35-alt1
- initial revision
