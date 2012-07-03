%define dist File-Slurp
Name: perl-%dist
Version: 9999.19
Release: alt1

Summary: Efficient Reading/Writing of Complete Files
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/U/UR/URI/File-Slurp-9999.19.tar.gz
Patch: perl-File-Slurp-9999.15-alt-deps.patch

BuildArch: noarch

# Automatically added by buildreq on Tue Apr 05 2011
BuildRequires: perl-Test-Pod

%description
This module provides subroutines to read or write entire files with a
simple call.  It also has a subroutine for reading the list of filenames
in a directory.

%prep
%setup -q -n %dist-%version
%patch -p1

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%dir %perl_vendor_privlib/File
%perl_vendor_privlib/File/Slurp.pm

%changelog
* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 9999.19-alt1
- automated CPAN update

* Tue Apr 05 2011 Alexey Tourbin <at@altlinux.ru> 9999.15-alt1
- 9999.13 -> 9999.15

* Mon Apr 28 2008 Alexey Tourbin <at@altlinux.ru> 9999.13-alt1
- 9999.08 -> 9999.13

* Thu Apr 21 2005 Alexey Tourbin <at@altlinux.ru> 9999.08-alt1
- 9999.07 -> 9999.08

* Wed Feb 02 2005 Alexey Tourbin <at@altlinux.ru> 9999.07-alt1
- 9999.06 -> 9999.07
- manual pages not packaged (use perldoc)

* Thu Nov 04 2004 Alexey Tourbin <at@altlinux.ru> 9999.06-alt1
- 9999.04 -> 9999.06

* Wed Jun 09 2004 Alexey Tourbin <at@altlinux.ru> 9999.04-alt1
- initial revision (required by gimp-perl)
