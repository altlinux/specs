%define _unpackaged_files_terminate_build 1
BuildRequires: perl(Module/Build.pm) perl(namespace/autoclean.pm) perl(Sub/Exporter/ForMethods.pm) perl(Sub/Defer.pm)
BuildRequires: perl(Module/Build/Tiny.pm)
%define dist MooseX-Types
Name: perl-%dist
Version: 0.50
Release: alt2

Summary: Organise your Moose types in libraries
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/E/ET/ETHER/%{dist}-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Dec 22 2010
BuildRequires: perl-Carp-Clan perl-Moose perl-Test-Fatal perl-Test-Requires perl-namespace-clean perl(Test/NoWarnings.pm) perl(Test/CheckDeps.pm) perl(Sub/Name.pm)

%description
The types provided with Moose are by design global. This package helps
you to organise and selectively import your own and the built-in types in
libraries. As a nice side effect, it catches typos at compile-time too.

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/MooseX*

%changelog
* Thu Mar 23 2023 Igor Vlasenko <viy@altlinux.org> 0.50-alt2
- fixed build

* Wed Apr 22 2020 Igor Vlasenko <viy@altlinux.ru> 0.50-alt1.1
- dropped deprecated BR: perl-Module-Install

* Tue Feb 14 2017 Igor Vlasenko <viy@altlinux.ru> 0.50-alt1
- automated CPAN update

* Thu Dec 29 2016 Igor Vlasenko <viy@altlinux.ru> 0.49-alt1
- automated CPAN update

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
