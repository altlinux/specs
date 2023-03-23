%define _unpackaged_files_terminate_build 1
BuildRequires: perl(Module/Build/Tiny.pm) perl(Module/Build.pm)
%define dist YAML-Tiny
Name: perl-%dist
Version: 1.74
Release: alt1

Summary: Read/Write YAML files with as little code as possible
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/E/ET/ETHER/%{dist}-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sat Dec 18 2010
BuildRequires: perl-YAML perl-YAML-Syck perl-devel perl(Capture/Tiny.pm) perl(Test/CheckDeps.pm)

%description
YAML::Tiny is a perl class for reading and writing YAML-style files,
written with as little code as possible, reducing load time and
memory overhead.

%prep
%setup -q -n %{dist}-%{version}
# Test::More 0.99 - not in perl 5.18.2
[ %version = 1.62 ] && rm t/*t

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README CONTRIBUTING
%perl_vendor_privlib/YAML*

%changelog
* Thu Mar 23 2023 Igor Vlasenko <viy@altlinux.org> 1.74-alt1
- automated CPAN update

* Wed Mar 07 2018 Igor Vlasenko <viy@altlinux.ru> 1.73-alt1
- automated CPAN update

* Tue Feb 14 2017 Igor Vlasenko <viy@altlinux.ru> 1.70-alt1
- automated CPAN update

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 1.69-alt1
- automated CPAN update

* Fri May 22 2015 Igor Vlasenko <viy@altlinux.ru> 1.67-alt1
- automated CPAN update

* Wed Apr 01 2015 Igor Vlasenko <viy@altlinux.ru> 1.66-alt1
- automated CPAN update

* Tue Dec 16 2014 Igor Vlasenko <viy@altlinux.ru> 1.64-alt1
- automated CPAN update

* Mon Mar 24 2014 Igor Vlasenko <viy@altlinux.ru> 1.62-alt1
- automated CPAN update

* Thu Mar 06 2014 Igor Vlasenko <viy@altlinux.ru> 1.61-alt1
- automated CPAN update

* Wed Sep 25 2013 Igor Vlasenko <viy@altlinux.ru> 1.56-alt1
- automated CPAN update

* Mon Sep 23 2013 Igor Vlasenko <viy@altlinux.ru> 1.55-alt1
- automated CPAN update

* Mon Sep 16 2013 Igor Vlasenko <viy@altlinux.ru> 1.54-alt1
- automated CPAN update

* Wed Sep 26 2012 Igor Vlasenko <viy@altlinux.ru> 1.51-alt1
- automated CPAN update

* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 1.50-alt1
- automated CPAN update

* Sat Dec 18 2010 Alexey Tourbin <at@altlinux.ru> 1.46-alt1
- 1.41 -> 1.46

* Mon Mar 29 2010 Alexey Tourbin <at@altlinux.ru> 1.41-alt1
- 1.40 -> 1.41

* Thu Aug 06 2009 Alexey Tourbin <at@altlinux.ru> 1.40-alt1
- 1.32 -> 1.40

* Wed Sep 24 2008 Alexey Tourbin <at@altlinux.ru> 1.32-alt1
- initial revision (for new Module::Install)
