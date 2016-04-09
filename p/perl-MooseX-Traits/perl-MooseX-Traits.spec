%define _unpackaged_files_terminate_build 1
%define dist MooseX-Traits
Name: perl-%dist
Version: 0.13
Release: alt1.1

Summary: Automatically apply roles at object creation time
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/E/ET/ETHER/MooseX-Traits-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sun Nov 20 2011
BuildRequires: perl-MooseX-Role-Parameterized perl-Pod-Escapes perl-Test-Exception perl-Test-use-ok perl-namespace-autoclean perl(Module/Build/Tiny.pm) perl(Test/Fatal.pm) perl(Test/Requires.pm)

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
* Sat Apr 09 2016 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1.1
- rebuild to restore role requires

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1
- automated CPAN update

* Wed Mar 05 2014 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1
- automated CPAN update

* Sun Nov 20 2011 Alexey Tourbin <at@altlinux.ru> 0.11-alt1
- initial revision
