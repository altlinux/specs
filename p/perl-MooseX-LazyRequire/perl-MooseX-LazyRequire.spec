%define _unpackaged_files_terminate_build 1
%define dist MooseX-LazyRequire
Name: perl-%dist
Version: 0.11
Release: alt1.1

Summary: Required attributes which fail only when trying to use them
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/E/ET/ETHER/MooseX-LazyRequire-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sun Nov 20 2011
BuildRequires: perl-MooseX-Types perl-Test-Exception perl-aliased perl-namespace-autoclean perl(Test/Fatal.pm) perl(Test/CheckDeps.pm) perl(Module/Build.pm)

%description
This module adds a lazy_required option to Moose attribute declarations.

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
* Sat Apr 09 2016 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1.1
- rebuild to restore role requires

* Tue Aug 19 2014 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1
- automated CPAN update

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1
- automated CPAN update

* Wed Sep 26 2012 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- automated CPAN update

* Sun Nov 20 2011 Alexey Tourbin <at@altlinux.ru> 0.07-alt1
- initial revision
