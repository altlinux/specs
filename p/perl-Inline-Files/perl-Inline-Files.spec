%define _unpackaged_files_terminate_build 1
%define dist Inline-Files
Name: perl-%dist
Version: 0.69
Release: alt1

Summary: Multiple virtual files at the end of your code
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/A/AM/AMBS/Inline-Files-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sun Apr 24 2011
BuildRequires: perl-Filter perl-devel

%description
Inline::Files generalizes the notion of the __DATA__ marker
and the associated DATA filehandle, to an arbitrary number
of markers and associated filehandles.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Inline

%changelog
* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 0.69-alt1
- automated CPAN update

* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.68-alt1
- automated CPAN update

* Sun Apr 24 2011 Alexey Tourbin <at@altlinux.ru> 0.64-alt1
- 0.62 -> 0.64

* Mon Jul 17 2006 Alexey Tourbin <at@altlinux.ru> 0.62-alt1
- initial revision
