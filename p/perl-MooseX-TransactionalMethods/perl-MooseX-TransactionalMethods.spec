%define dist MooseX-TransactionalMethods
Name: perl-%dist
Version: 0.009
Release: alt2

Summary: Syntax sugar for transactional methods
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/M/MJ/MJG/MooseX-TransactionalMethods-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sun Nov 20 2011
BuildRequires: perl-Moose perl-Pod-Escapes perl-aliased perl-devel perl(Sub/Name.pm)

%description
This method exports the "transactional" declarator that will enclose
the method in a txn_do call.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README
%perl_vendor_privlib/MooseX

%changelog
* Thu Mar 23 2023 Igor Vlasenko <viy@altlinux.org> 0.009-alt2
- fixed build

* Sat Apr 09 2016 Igor Vlasenko <viy@altlinux.ru> 0.009-alt1.1
- rebuild to restore role requires

* Wed Apr 01 2015 Igor Vlasenko <viy@altlinux.ru> 0.009-alt1
- automated CPAN update

* Sun Nov 20 2011 Alexey Tourbin <at@altlinux.ru> 0.008-alt1
- initial revision
