%define dist MooseX-Getopt
Name: perl-%dist
Version: 0.56
Release: alt1

Summary: A Moose role for processing command line options
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/E/ET/ETHER/MooseX-Getopt-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Oct 26 2011
BuildRequires: perl-Getopt-Long-Descriptive perl-MooseX-Role-Parameterized perl-Test-Deep perl-Test-Fatal perl-Test-Requires perl-Test-Warn perl-Test-Trap perl(Test/CheckDeps.pm) perl(Test/NoWarnings.pm) perl(Path/Tiny.pm) perl(Config/Any/YAML.pm)

%description
This is a role which provides an alternate constructor for creating
objects using parameters passed in from the command line.

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
