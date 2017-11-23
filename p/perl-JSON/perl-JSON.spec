%define _unpackaged_files_terminate_build 1
%define dist JSON
Name: perl-%dist
Version: 2.97000
Release: alt1

Summary: Parse and convert to JSON (JavaScript Object Notation)
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/I/IS/ISHIGAKI/%{dist}-%{version}.tar.gz

BuildArch: noarch

# Manually added by Alexey Tourbin!
Requires: perl-JSON-XS

# Automatically added by buildreq on Tue Nov 15 2011
BuildRequires: perl-JSON-PP perl-JSON-XS perl-Test-Pod perl-Tie-IxHash

%description
This module converts between JSON (JavaScript Object Notation)
and Perl data structure into each other.

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/JSON*

%changelog
* Thu Nov 23 2017 Igor Vlasenko <viy@altlinux.ru> 2.97000-alt1
- automated CPAN update

* Wed Aug 02 2017 Igor Vlasenko <viy@altlinux.ru> 2.94-alt1
- automated CPAN update

* Fri Nov 01 2013 Igor Vlasenko <viy@altlinux.ru> 2.90-alt1
- automated CPAN update

* Sat Oct 19 2013 Igor Vlasenko <viy@altlinux.ru> 2.61-alt1
- automated CPAN update

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 2.59-alt1
- automated CPAN update

* Tue Nov 15 2011 Alexey Tourbin <at@altlinux.ru> 2.53-alt1
- 2.50 -> 2.53

* Sat Feb 26 2011 Alexey Tourbin <at@altlinux.ru> 2.50-alt1
- 2.21 -> 2.50
- added dependency on perl-JSON-XS

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 2.21-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Fri Apr 09 2010 Alexey Tourbin <at@altlinux.ru> 2.21-alt1
- 2.12 -> 2.21

* Fri Sep 05 2008 Michael Bochkaryov <misha@altlinux.ru> 2.12-alt2
- fix directory ownership violation

* Thu Jul 17 2008 Michael Bochkaryov <misha@altlinux.ru> 2.12-alt1
- 2.09 -> 2.12 version update

* Sat May 24 2008 Michael Bochkaryov <misha@altlinux.ru> 2.09-alt1
- 2.09 version

* Fri Apr 18 2008 Michael Bochkaryov <misha@altlinux.ru> 2.06-alt1
- 1.07 => 2.06

* Thu Mar 22 2007 Sir Raorn <raorn@altlinux.ru> 1.07-alt1
- first build for ALT Linux Sisyphus

