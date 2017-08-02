%define _unpackaged_files_terminate_build 1
%define dist XML-Atom
Name: perl-%dist
Version: 0.42
Release: alt1

Summary: Atom API and Feed Support
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/M/MI/MIYAGAWA/%{dist}-%{version}.tar.gz

BuildArch: noarch

# requires mod_perl
%add_findreq_skiplist */XML/Atom/Server.pm

# Automatically added by buildreq on Wed Nov 16 2011
BuildRequires: perl-Class-Data-Inheritable perl-DateTime perl-Digest-SHA1 perl-Pod-Escapes perl-XML-LibXML perl-XML-XPath perl-devel perl(Module/Build/Tiny.pm)

%description
Atom is a syndication, API, and archiving format for weblogs and other
data. XML::Atom implements the feed format as well as a client for the
API.

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/XML

%changelog
* Wed Aug 02 2017 Igor Vlasenko <viy@altlinux.ru> 0.42-alt1
- automated CPAN update

* Wed Nov 16 2011 Alexey Tourbin <at@altlinux.ru> 0.41-alt2
- disabled build dependency on perl-Module-Install

* Wed Oct 05 2011 Alexey Tourbin <at@altlinux.ru> 0.41-alt1
- 0.37 -> 0.41
- rebuilt as plain src.rpm

* Mon Mar 29 2010 Alexey Tourbin <at@altlinux.ru> 0.37-alt1
- 0.35 -> 0.37
- updated build dependencies for new Module::Install

* Mon May 04 2009 Alexey Tourbin <at@altlinux.ru> 0.35-alt1
- 0.33 -> 0.35

* Thu Apr 23 2009 Alexey Tourbin <at@altlinux.ru> 0.33-alt1
- 0.32 -> 0.33

* Tue Nov 25 2008 Alexey Tourbin <at@altlinux.ru> 0.32-alt1
- 0.31 -> 0.32

* Tue Nov 18 2008 Alexey Tourbin <at@altlinux.ru> 0.31-alt1
- 0.28 -> 0.31

* Sat Nov 10 2007 Alexey Tourbin <at@altlinux.ru> 0.28-alt1
- 0.25_02 -> 0.28

* Sun Jul 22 2007 Alexey Tourbin <at@altlinux.ru> 0.25_02-alt1
- 0.25 -> 0.25_02
- t/25-utf8-create.t: applied decode_utf8() fix from rt.cpan.org #28406

* Wed Mar 28 2007 Alexey Tourbin <at@altlinux.ru> 0.25-alt1
- 0.23 -> 0.25

* Sun Aug 27 2006 Alexey Tourbin <at@altlinux.ru> 0.23-alt1
- 0.21 -> 0.23

* Thu Jul 13 2006 Alexey Tourbin <at@altlinux.ru> 0.21-alt1
- 0.19 -> 0.21

* Mon Apr 17 2006 Alexey Tourbin <at@altlinux.ru> 0.19-alt1
- 0.13 -> 0.19

* Sun Aug 21 2005 Alexey Tourbin <at@altlinux.ru> 0.13-alt1
- initial revision
