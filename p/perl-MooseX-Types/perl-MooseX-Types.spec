%define _unpackaged_files_terminate_build 1
BuildRequires: perl(Module/Build.pm) perl(namespace/autoclean.pm) perl(Sub/Exporter/ForMethods.pm)
BuildRequires: perl(Module/Build/Tiny.pm)
%define dist MooseX-Types
Name: perl-%dist
Version: 0.48
Release: alt1

Summary: Organise your Moose types in libraries
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/E/ET/ETHER/MooseX-Types-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Dec 22 2010
BuildRequires: perl-Carp-Clan perl-Module-Install perl-Moose perl-Test-Fatal perl-Test-Requires perl-namespace-clean perl(Test/NoWarnings.pm) perl(Test/CheckDeps.pm)

%description
The types provided with Moose are by design global. This package helps
you to organise and selectively import your own and the built-in types in
libraries. As a nice side effect, it catches typos at compile-time too.

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
* Sun Dec 18 2016 Igor Vlasenko <viy@altlinux.ru> 0.48-alt1
- automated CPAN update

* Sat Apr 09 2016 Igor Vlasenko <viy@altlinux.ru> 0.46-alt1.1
- rebuild to restore role requires

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 0.46-alt1
- automated CPAN update

* Tue Sep 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.45-alt1
- automated CPAN update

* Mon Mar 10 2014 Igor Vlasenko <viy@altlinux.ru> 0.44-alt1
- automated CPAN update

* Wed Mar 05 2014 Igor Vlasenko <viy@altlinux.ru> 0.41-alt1
- automated CPAN update

* Mon Sep 23 2013 Igor Vlasenko <viy@altlinux.ru> 0.38-alt1
- automated CPAN update

* Mon Sep 16 2013 Igor Vlasenko <viy@altlinux.ru> 0.37-alt1
- automated CPAN update

* Sat Jul 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.36-alt1
- automated CPAN update

* Mon Sep 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.35-alt1
- automated CPAN update

* Sun Sep 25 2011 Igor Vlasenko <viy@altlinux.ru> 0.30-alt1
- automated CPAN update

* Wed Dec 22 2010 Alexey Tourbin <at@altlinux.ru> 0.25-alt1
- 0.22 -> 0.25

* Thu Jun 10 2010 Alexey Tourbin <at@altlinux.ru> 0.22-alt1
- 0.21 -> 0.22

* Tue Apr 13 2010 Alexey Tourbin <at@altlinux.ru> 0.21-alt1
- initial revision
