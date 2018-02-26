%define dist Devel-Symdump
Name: perl-%dist
Version: 2.08
Release: alt2

Summary: Perl module for inspecting Perl's symbol table
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Tue Oct 04 2011
BuildRequires: perl-Test-Pod

%description
The perl module Devel::Symdump provides a convenient way to inspect
perl's symbol table and the class hierarchie within a running program.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc ChangeLog README
%perl_vendor_privlib/Devel

%changelog
* Tue Oct 04 2011 Alexey Tourbin <at@altlinux.ru> 2.08-alt2
- rebuilt

* Thu Apr 24 2008 Alexey Tourbin <at@altlinux.ru> 2.08-alt1
- 2.03 -> 2.08

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 2.03-alt2.1
- Rebuilt with rpm-build-perl-0.5.1.

* Tue Sep 23 2003 Alexey Tourbin <at@altlinux.ru> 2.03-alt2
- descriptions updated

* Fri Nov 01 2002 Stanislav Ievlev <inger@altlinux.ru> 2.03-alt1
- Inital Release for ALT
