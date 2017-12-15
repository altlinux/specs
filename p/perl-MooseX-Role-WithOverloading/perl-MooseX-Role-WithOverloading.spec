%define _unpackaged_files_terminate_build 1
%define dist MooseX-Role-WithOverloading
Name: perl-%dist
Version: 0.17
Release: alt1.1.1.1.1

Summary: Roles which support overloading
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/E/ET/ETHER/MooseX-Role-WithOverloading-%{version}.tar.gz

# Automatically added by buildreq on Sat Nov 19 2011
BuildRequires: perl-MooseX-Types perl-aliased perl-devel perl-namespace-autoclean perl(Test/CheckDeps.pm) perl(Test/NoWarnings.pm) perl(Test/Warnings.pm)

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
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.17-alt1.1.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.17-alt1.1.1.1
- rebuild with new perl 5.24.1

* Sat Apr 09 2016 Igor Vlasenko <viy@altlinux.ru> 0.17-alt1.1.1
- rebuild to restore role requires

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.17-alt1.1
- rebuild with new perl 5.22.0

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 0.17-alt1
- automated CPAN update

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1.1
- rebuild with new perl 5.20.1

* Tue Nov 25 2014 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1
- automated CPAN update

* Tue Aug 19 2014 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1
- automated CPAN update

* Mon Aug 04 2014 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1
- automated CPAN update

* Thu Aug 29 2013 Vladimir Lettiev <crux@altlinux.ru> 0.13-alt2
- built for perl 5.18

* Sat Jul 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1
- automated CPAN update

* Sun Sep 02 2012 Vladimir Lettiev <crux@altlinux.ru> 0.09-alt4
- rebuilt for perl-5.16

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
