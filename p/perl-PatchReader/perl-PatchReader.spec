%define dist PatchReader
Name: perl-%dist
Version: 0.9.6
Release: alt1

Summary: Utilities to read and manipulate patches and CVS
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/T/TM/TMANNERM/PatchReader-0.9.6.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Tue Sep 07 2004
BuildRequires: perl-devel

%description
PatchReader is a set of utilities for reading in, transforming, and doing
various other things with a patch.  It basically allows you to create a chain of
readers that can read a patch, remove files from a patch, add CVS context, fix
up the patch root according to CVS, and output the patch as raw unified or
through a template processor (used in some places to output a patch as HTML).

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/PatchReader*

%changelog
* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.9.6-alt1
- automated CPAN update

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.9.5-alt1.1.1
- repair after perl 5.12 upgrade using girar-nmu

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.9.5-alt1.1
- Rebuilt with rpm-build-perl-0.5.1.

* Tue Sep 07 2004 Alexey Tourbin <at@altlinux.ru> 0.9.5-alt1
- initial revision (this module is needed for bugzilla)
