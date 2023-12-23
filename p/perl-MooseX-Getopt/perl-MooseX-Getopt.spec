%define _unpackaged_files_terminate_build 1
BuildRequires: perl(Module/Build/Tiny.pm) perl(Module/Build.pm) perl(Module/Build.pm) perl(Test/Needs.pm)
%define dist MooseX-Getopt
Name: perl-%dist
Version: 0.76
Release: alt1

Summary: A Moose role for processing command line options
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/E/ET/ETHER/%{dist}-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Oct 26 2011
BuildRequires: perl-Getopt-Long-Descriptive perl-MooseX-Role-Parameterized perl-Test-Deep perl-Test-Fatal perl-Test-Requires perl-Test-Warn perl-Test-Trap perl(Test/CheckDeps.pm) perl(Test/NoWarnings.pm) perl(Path/Tiny.pm) perl(Config/Any/YAML.pm) perl(Test/Fatal.pm) perl(Test/Warnings.pm)

%description
This is a role which provides an alternate constructor for creating
objects using parameters passed in from the command line.

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README CONTRIBUTING Changes
%perl_vendor_privlib/MooseX

%changelog
* Sat Dec 23 2023 Igor Vlasenko <viy@altlinux.org> 0.76-alt1
- automated CPAN update

* Wed Mar 24 2021 Igor Vlasenko <viy@altlinux.org> 0.75-alt1
- automated CPAN update

* Mon Oct 08 2018 Igor Vlasenko <viy@altlinux.ru> 0.74-alt1
- automated CPAN update

* Sun Sep 02 2018 Igor Vlasenko <viy@altlinux.ru> 0.73-alt1
- automated CPAN update

* Wed Aug 08 2018 Igor Vlasenko <viy@altlinux.ru> 0.72-alt1
- automated CPAN update

* Sun Jul 03 2016 Igor Vlasenko <viy@altlinux.ru> 0.71-alt1
- automated CPAN update

* Thu May 26 2016 Igor Vlasenko <viy@altlinux.ru> 0.70-alt1
- automated CPAN update

* Tue May 03 2016 Igor Vlasenko <viy@altlinux.ru> 0.69-alt1
- automated CPAN update

* Sat Apr 09 2016 Igor Vlasenko <viy@altlinux.ru> 0.68-alt1.1
- rebuild to restore role requires

* Wed Apr 01 2015 Igor Vlasenko <viy@altlinux.ru> 0.68-alt1
- automated CPAN update

* Mon Feb 02 2015 Igor Vlasenko <viy@altlinux.ru> 0.66-alt1
- automated CPAN update

* Wed Aug 20 2014 Igor Vlasenko <viy@altlinux.ru> 0.65-alt1
- automated CPAN update

* Mon Aug 04 2014 Igor Vlasenko <viy@altlinux.ru> 0.64-alt1
- automated CPAN update

* Sat Mar 29 2014 Igor Vlasenko <viy@altlinux.ru> 0.63-alt1
- automated CPAN update

* Mon Mar 10 2014 Igor Vlasenko <viy@altlinux.ru> 0.62-alt1
- automated CPAN update

* Wed Mar 05 2014 Igor Vlasenko <viy@altlinux.ru> 0.61-alt1
- automated CPAN update

* Mon Sep 16 2013 Igor Vlasenko <viy@altlinux.ru> 0.58-alt1
- automated CPAN update

* Thu Sep 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.56-alt1
- automated CPAN update

* Wed Sep 26 2012 Igor Vlasenko <viy@altlinux.ru> 0.47-alt1
- automated CPAN update

* Wed Oct 26 2011 Alexey Tourbin <at@altlinux.ru> 0.37-alt1
- 0.33 -> 0.37

* Tue Dec 28 2010 Alexey Tourbin <at@altlinux.ru> 0.33-alt1
- 0.31 -> 0.33

* Tue Jul 13 2010 Igor Vlasenko <viy@altlinux.ru> 0.31-alt1
- automated CPAN update

* Thu Jun 10 2010 Alexey Tourbin <at@altlinux.ru> 0.28-alt1
- 0.27 -> 0.28

* Wed Apr 14 2010 Alexey Tourbin <at@altlinux.ru> 0.27-alt1
- initial revision
