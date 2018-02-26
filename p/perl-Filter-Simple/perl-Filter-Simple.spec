%define dist Filter-Simple
Name: perl-%dist
Version: 0.88
Release: alt1

Summary: Simplified source filtering
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Mon Feb 20 2012
BuildRequires: perl-Filter perl-Text-Balanced perl-devel

%description
The Filter::Simple module provides a simplified interface to
Filter::Util::Call; one that is sufficient for most common cases.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Filter

%changelog
* Mon Feb 20 2012 Alexey Tourbin <at@altlinux.ru> 0.88-alt1
- 0.87 -> 0.88

* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.87-alt1
- automated CPAN update

* Sat Feb 26 2011 Alexey Tourbin <at@altlinux.ru> 0.85-alt1
- 0.84 -> 0.85

* Tue Mar 03 2009 Alexey Tourbin <at@altlinux.ru> 0.84-alt1
- 0.82 -> 0.84

* Tue Jun 28 2005 Alexey Tourbin <at@altlinux.ru> 0.82-alt1
- 0.79 -> 0.82

* Wed Dec 15 2004 Alexey Tourbin <at@altlinux.ru> 0.79-alt1
- initial revision (split from perl-base)
