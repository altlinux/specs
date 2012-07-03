%define dist Template-Extract
Name: perl-%dist
Version: 0.41
Release: alt3

Summary: Use TT2 syntax to extract data from documents
License: MIT
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Nov 16 2011
BuildRequires: perl-Template perl-devel

%description
This module adds template extraction functionality to the Template
toolkit.  It can take a rendered document and its template together,
and get the original data structure back, effectively reversing
the Template::process function.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Template

%changelog
* Wed Nov 16 2011 Alexey Tourbin <at@altlinux.ru> 0.41-alt3
- disabled build dependency on perl-Module-Install

* Tue Oct 04 2011 Alexey Tourbin <at@altlinux.ru> 0.41-alt2
- rebuilt

* Fri Apr 25 2008 Alexey Tourbin <at@altlinux.ru> 0.41-alt1
- 0.40 -> 0.41
- updated License tag to "MIT"

* Mon Jul 17 2006 Alexey Tourbin <at@altlinux.ru> 0.40-alt1
- initial revision
