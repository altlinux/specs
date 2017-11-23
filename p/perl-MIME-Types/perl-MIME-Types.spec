%define _unpackaged_files_terminate_build 1
%define dist MIME-Types
Name: perl-MIME-Types
Version: 2.14
Release: alt1

Summary: Definition of MIME types
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/M/MA/MARKOV/%{dist}-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Sep 26 2012
BuildRequires: perl-devel perl-Encode perl(Mojo/Base.pm)

%description
MIME types are used in MIME compliant lines, for instance as part
of e-mail and HTTP traffic, to indicate the type of content which is
transmitted.  Sometimes real knowledge about a mime-type is need.

This module maintains a set of MIME::Type|MIME::Type objects, which
each describe one known mime type.  There are many types defined
by RFCs and vendors, so the list is long but not complete.

%package -n perl-MojoX-MIME-Types
Group: Development/Perl
Summary: Definition of MIME types for Mojolicious
Requires: %name = %version-%release

%description -n perl-MojoX-MIME-Types
%summary

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc	ChangeLog README
%dir	%perl_vendor_privlib/MIME
	%perl_vendor_privlib/MIME/*.pm
	%perl_vendor_privlib/MIME/*.db
%doc	%perl_vendor_privlib/MIME/*.pod

%files -n perl-MojoX-MIME-Types
%dir	%perl_vendor_privlib/MojoX/MIME
	%perl_vendor_privlib/MojoX/MIME/*.pm
%doc	%perl_vendor_privlib/MojoX/MIME/*.pod

%changelog
* Thu Nov 23 2017 Igor Vlasenko <viy@altlinux.ru> 2.14-alt1
- automated CPAN update

* Sat Mar 19 2016 Igor Vlasenko <viy@altlinux.ru> 2.13-alt1
- automated CPAN update

* Tue Dec 15 2015 Vladimir Lettiev <crux@altlinux.ru> 2.12-alt2
- separated package for MojoX::MIME::Types (Closes: #31614)

* Thu Nov 12 2015 Igor Vlasenko <viy@altlinux.ru> 2.12-alt1
- automated CPAN update

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 2.11-alt1
- automated CPAN update

* Tue Dec 16 2014 Igor Vlasenko <viy@altlinux.ru> 2.09-alt1
- automated CPAN update

* Mon Sep 01 2014 Igor Vlasenko <viy@altlinux.ru> 2.06-alt1
- automated CPAN update

* Mon Sep 16 2013 Igor Vlasenko <viy@altlinux.ru> 2.04-alt1
- automated CPAN update

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 1.38-alt1
- automated CPAN update

* Wed Sep 26 2012 Alexey Tourbin <at@altlinux.ru> 1.35-alt1
- 1.32 -> 1.35

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
