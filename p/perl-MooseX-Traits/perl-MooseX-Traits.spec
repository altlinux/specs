%define dist MooseX-Traits
Name: perl-%dist
Version: 0.11
Release: alt1

Summary: Automatically apply roles at object creation time
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sun Nov 20 2011
BuildRequires: perl-MooseX-Role-Parameterized perl-Pod-Escapes perl-Test-Exception perl-Test-use-ok perl-namespace-autoclean

%description
Often you want to create components that can be added to a class
arbitrarily. This module makes it easy for the end user to use these
components. Instead of requiring the user to create a named class with
the desired roles applied, or apply roles to the instance one-by-one,
he can just create a new class from yours with "with_traits", and then
instantiate that.

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
* Sun Nov 20 2011 Alexey Tourbin <at@altlinux.ru> 0.11-alt1
- initial revision
