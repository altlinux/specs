%define _unpackaged_files_terminate_build 1
%define dist Test-Pod
Name: perl-%dist
Version: 1.52
Release: alt1

Summary: Check for POD errors in files
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/E/ET/ETHER/%{dist}-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Mon Nov 14 2011
BuildRequires: perl-devel perl(Pod/Simple.pm)

%description
Test::Pod allows to check the validity of a POD file, and report
its results in standard Test::Simple fashion.

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Test

%changelog
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.52-alt1
- automated CPAN update

* Wed Oct 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.51-alt2
- updated BuildRequires.

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 1.51-alt1
- automated CPAN update

* Fri May 22 2015 Igor Vlasenko <viy@altlinux.ru> 1.49-alt1
- automated CPAN update

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 1.48-alt1
- automated CPAN update

* Mon Nov 14 2011 Alexey Tourbin <at@altlinux.ru> 1.45-alt1
- 1.44 -> 1.45

* Sun May 16 2010 Alexey Tourbin <at@altlinux.ru> 1.44-alt1
- 1.42 -> 1.44

* Tue Mar 23 2010 Alexey Tourbin <at@altlinux.ru> 1.42-alt1
- 1.41 -> 1.42

* Wed Feb 17 2010 Alexey Tourbin <at@altlinux.ru> 1.41-alt1
- 1.26 -> 1.41

* Wed Apr 04 2007 Alexey Tourbin <at@altlinux.ru> 1.26-alt1
- 1.24 -> 1.26

* Mon May 22 2006 Alexey Tourbin <at@altlinux.ru> 1.24-alt1
- 1.20 -> 1.24

* Tue Dec 28 2004 Alexey Tourbin <at@altlinux.ru> 1.20-alt1
- initial revision (required for Curses::UI tests)
