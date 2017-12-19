%define dist Class-MakeMethods
Name: perl-%dist
Version: 1.01
Release: alt3

Summary: Generate common types of methods
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz
Patch0:         Class-MakeMethods-1.009-Fix-building-on-Perl-without-dot-in-INC.patch

BuildArch: noarch

# Automatically added by buildreq on Mon Sep 26 2011
BuildRequires: perl-Attribute-Handlers perl-Tie-RefHash perl-devel

# XXX syntax check failure
%add_findreq_skiplist */Class/MakeMethods/Composite/Array.pm
%add_findreq_skiplist */Class/MakeMethods/Composite/Global.pm

%description
The Class::MakeMethods framework allows Perl class developers to quickly
define common types of methods.  When a module uses Class::MakeMethods or
one of its subclasses, it can select from a variety of supported method
types, and specify a name for each method desired.  The methods are
dynamically generated and installed in the calling package.

%prep
%setup -q -n %dist-%version
%patch0 -p1

%build
%perl_vendor_build

%install
%perl_vendor_install

# requires ExtUtils::testlib, should not be packaged
rm %buildroot%perl_vendor_privlib/Class/benchmark.pl

%files
%doc README CHANGES
%perl_vendor_privlib/Class

%changelog
* Tue Dec 19 2017 Igor Vlasenko <viy@altlinux.ru> 1.01-alt3
- fixed build with new perl 5.26

* Mon Sep 26 2011 Alexey Tourbin <at@altlinux.ru> 1.01-alt2
- do not package Class/benchmark.pl

* Wed Nov 24 2010 Igor Vlasenko <viy@altlinux.ru> 1.01-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Thu Aug 25 2005 Alexey Morozov <morozov@altlinux.org> 1.01-alt1
- Initial build for ALT Linux
