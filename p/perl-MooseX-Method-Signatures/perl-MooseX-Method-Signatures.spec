%define _unpackaged_files_terminate_build 1
BuildRequires: perl(Module/Build/Tiny.pm) perl(Module/Build.pm)
%define dist MooseX-Method-Signatures
Name: perl-%dist
Version: 0.49
Release: alt1.1

Summary: Method declarations with type constraints and no source filter
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/E/ET/ETHER/MooseX-Method-Signatures-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Sep 26 2012
BuildRequires: perl-Context-Preserve perl-Devel-Declare perl-MooseX-LazyRequire perl-MooseX-Meta-TypeConstraint-ForceCoercion perl-Parse-Method-Signatures perl-Task-Weaken perl-Test-CheckDeps perl-Test-Deep perl-Test-Fatal perl-Test-Script perl-Text-Balanced

%description
Provides a proper method keyword, like "sub" but specifically for making
methods and validating their arguments against Moose type constraints.

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
* Sat Apr 09 2016 Igor Vlasenko <viy@altlinux.ru> 0.49-alt1.1
- rebuild to restore role requires

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 0.49-alt1
- automated CPAN update

* Tue Oct 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.48-alt1
- automated CPAN update

* Wed Mar 05 2014 Igor Vlasenko <viy@altlinux.ru> 0.47-alt1
- automated CPAN update

* Wed Oct 02 2013 Igor Vlasenko <viy@altlinux.ru> 0.46-alt1
- automated CPAN update

* Mon Sep 16 2013 Igor Vlasenko <viy@altlinux.ru> 0.45-alt1
- automated CPAN update

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 0.44-alt1
- automated CPAN update

* Wed Sep 26 2012 Alexey Tourbin <at@altlinux.ru> 0.43-alt1
- 0.37 -> 0.43

* Tue Sep 11 2012 Vladimir Lettiev <crux@altlinux.ru> 0.37-alt2
- fixed build

* Sun Nov 20 2011 Alexey Tourbin <at@altlinux.ru> 0.37-alt1
- initial revision
