%define dist MooseX-Role-WithOverloading
Name: perl-%dist
Version: 0.09
Release: alt3

Summary: Roles which support overloading
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Sat Nov 19 2011
BuildRequires: perl-MooseX-Types perl-aliased perl-devel perl-namespace-autoclean

%description
MooseX::Role::WithOverloading allows you to write a "Moose::Role" which
defines overloaded operators and allows those operator overloadings to be
composed into the classes/roles/instances it's compiled to, while plain
"Moose::Role"s would lose the overloading.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/MooseX
%perl_vendor_autolib/MooseX

%changelog
* Sat Nov 19 2011 Alexey Tourbin <at@altlinux.ru> 0.09-alt3
- updated build dependencies

* Tue Oct 11 2011 Alexey Tourbin <at@altlinux.ru> 0.09-alt2
- rebuilt for perl-5.14

* Mon Jan 24 2011 Alexey Tourbin <at@altlinux.ru> 0.09-alt1
- 0.06 -> 0.09

* Tue Nov 09 2010 Vladimir Lettiev <crux@altlinux.ru> 0.06-alt1.1
- rebuilt with perl 5.12

* Tue Jul 13 2010 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- automated CPAN update

* Tue Apr 13 2010 Alexey Tourbin <at@altlinux.ru> 0.05-alt1
- initial revision
