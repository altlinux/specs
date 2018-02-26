%define dist MIME-Types
Name: perl-MIME-Types
Version: 1.32
Release: alt1

Summary: Definition of MIME types
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/M/MA/MARKOV/MIME-Types-1.32.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sat Dec 18 2010
BuildRequires: perl-devel

%description
MIME types are used in MIME compliant lines, for instance as part
of e-mail and HTTP traffic, to indicate the type of content which is
transmitted.  Sometimes real knowledge about a mime-type is need.

This module maintains a set of MIME::Type|MIME::Type objects, which
each describe one known mime type.  There are many types defined
by RFCs and vendors, so the list is long but not complete.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc	ChangeLog README
%dir	%perl_vendor_privlib/MIME
	%perl_vendor_privlib/MIME/Type.pm
%doc	%perl_vendor_privlib/MIME/Type.pod
	%perl_vendor_privlib/MIME/Types.pm
%doc	%perl_vendor_privlib/MIME/Types.pod

%changelog
* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 1.32-alt1
- automated CPAN update

* Sat Dec 18 2010 Alexey Tourbin <at@altlinux.ru> 1.31-alt1
- 1.29 -> 1.31

* Tue Mar 23 2010 Alexey Tourbin <at@altlinux.ru> 1.29-alt1
- 1.28 -> 1.29

* Tue Feb 16 2010 Alexey Tourbin <at@altlinux.ru> 1.28-alt1
- 1.27 -> 1.28

* Sat Jun 13 2009 Alexey Tourbin <at@altlinux.ru> 1.27-alt1
- 1.24 -> 1.27

* Sun Aug 10 2008 Alexey Tourbin <at@altlinux.ru> 1.24-alt1
- 1.16 -> 1.24

* Sat Feb 04 2006 Vitaly Lipatov <lav@altlinux.ru> 1.16-alt1
- first build for ALT Linux Sisyphus
