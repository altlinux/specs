%define dist MooseX-Meta-TypeConstraint-ForceCoercion
Name: perl-%dist
Version: 0.01
Release: alt1

Summary: Force coercion when validating type constraints
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sun Nov 20 2011
BuildRequires: perl-Devel-PartialDump perl-devel perl-namespace-autoclean

%description
This class allows to wrap any Moose::Meta::TypeConstraint in a way that will
force coercion of the value when checking or validating a value against it.

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
* Sun Nov 20 2011 Alexey Tourbin <at@altlinux.ru> 0.01-alt1
- initial revision
