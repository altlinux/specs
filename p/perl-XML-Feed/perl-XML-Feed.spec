%define dist XML-Feed
Name: perl-%dist
Version: 0.46
Release: alt1

Summary: XML Syndication Feed Support
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# this dependency cannot be detected automatically
Requires: perl-XML-RSS

# Automatically added by buildreq on Fri Nov 11 2011
BuildRequires: perl-Feed-Find perl-Module-Build perl-Module-Pluggable perl-Test-Pod perl-Test-Pod-Coverage perl-URI-Fetch perl-XML-Atom perl-XML-RSS

%description
XML::Feed is a syndication feed parser for both RSS and Atom feeds.
It also implements feed auto-discovery for finding feeds, given a URI.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/XML

%changelog
* Fri Nov 11 2011 Alexey Tourbin <at@altlinux.ru> 0.46-alt1
- 0.43 -> 0.46

* Mon Nov 29 2010 Igor Vlasenko <viy@altlinux.ru> 0.43-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Tue Jul 21 2009 Alexey Tourbin <at@altlinux.ru> 0.43-alt1
- 0.42 -> 0.43

* Fri Apr 24 2009 Alexey Tourbin <at@altlinux.ru> 0.42-alt1
- 0.40 -> 0.42

* Wed Nov 26 2008 Alexey Tourbin <at@altlinux.ru> 0.40-alt1
- 0.12 -> 0.40

* Sun Jul 22 2007 Alexey Tourbin <at@altlinux.ru> 0.12-alt2
- eliminated build dependency on ExtUtils::AutoInstall

* Tue Sep 05 2006 Alexey Tourbin <at@altlinux.ru> 0.12-alt1
- 0.10 -> 0.12

* Wed Jul 19 2006 Alexey Tourbin <at@altlinux.ru> 0.10-alt1
- 0.08 -> 0.10

* Mon Apr 17 2006 Alexey Tourbin <at@altlinux.ru> 0.08-alt1
- 0.07 -> 0.08

* Sat Sep 10 2005 Alexey Tourbin <at@altlinux.ru> 0.07-alt1
- initial revision
