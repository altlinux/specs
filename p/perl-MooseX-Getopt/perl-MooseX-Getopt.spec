%define dist MooseX-Getopt
Name: perl-%dist
Version: 0.37
Release: alt1

Summary: A Moose role for processing command line options
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Oct 26 2011
BuildRequires: perl-Getopt-Long-Descriptive perl-MooseX-Role-Parameterized perl-Test-Deep perl-Test-Fatal perl-Test-Requires perl-Test-Warn

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
%doc ChangeLog README
%perl_vendor_privlib/MooseX

%changelog
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
