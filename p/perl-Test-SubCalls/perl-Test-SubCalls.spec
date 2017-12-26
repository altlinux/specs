%define _unpackaged_files_terminate_build 1
%define dist Test-SubCalls
Name: perl-%dist
Version: 1.10
Release: alt1

Summary: Track the number of times subs are called
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/E/ET/ETHER/%{dist}-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Nov 16 2011
BuildRequires: perl-Hook-LexWrap perl-devel

%description
There are a number of different situations (like testing cacheing
code) where you want to want to do a number of tests, and then verify
that some underlying subroutine deep within the code was called a
specific number of times.

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
* Tue Dec 26 2017 Igor Vlasenko <viy@altlinux.ru> 1.10-alt1
- automated CPAN update

* Wed Nov 16 2011 Alexey Tourbin <at@altlinux.ru> 1.09-alt2
- disabled build dependency on perl-Module-Install

* Sat Dec 18 2010 Alexey Tourbin <at@altlinux.ru> 1.09-alt1
- 1.06 -> 1.09

* Sun Jun 17 2007 Alexey Tourbin <at@altlinux.ru> 1.06-alt1
- initial revision (for PPI)
