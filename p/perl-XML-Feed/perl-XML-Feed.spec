%define _unpackaged_files_terminate_build 1
%define dist XML-Feed
Name: perl-%dist
Version: 0.61
Release: alt1

Summary: XML Syndication Feed Support
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/D/DA/DAVECROSS/%{dist}-%{version}.tar.gz

BuildArch: noarch

# this dependency cannot be detected automatically
Requires: perl-XML-RSS

# Automatically added by buildreq on Wed Sep 26 2012
BuildRequires: perl-Feed-Find perl-Module-Build perl-Module-Pluggable perl-Test-Pod perl-Test-Pod-Coverage perl-URI-Fetch perl-XML-Atom perl-XML-RSS perl(XML/XPath.pm) perl(DateTime/Format/Flexible.pm) perl(DateTime/Format/ISO8601.pm) perl(DateTime/Format/Natural.pm)

%description
XML::Feed is a syndication feed parser for both RSS and Atom feeds.
It also implements feed auto-discovery for finding feeds, given a URI.

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README ChangeLog.md
%perl_vendor_privlib/XML

%changelog
* Mon Feb 01 2021 Igor Vlasenko <viy@altlinux.ru> 0.61-alt1
- automated CPAN update

* Fri Jan 15 2021 Igor Vlasenko <viy@altlinux.ru> 0.60-alt1
- automated CPAN update

* Wed Feb 20 2019 Igor Vlasenko <viy@altlinux.ru> 0.59-alt1
- automated CPAN update

* Wed Oct 24 2018 Igor Vlasenko <viy@altlinux.ru> 0.55-alt1
- automated CPAN update

* Mon Oct 08 2018 Igor Vlasenko <viy@altlinux.ru> 0.54-alt1
- automated CPAN update

* Tue Dec 15 2015 Igor Vlasenko <viy@altlinux.ru> 0.53-alt1
- automated CPAN update

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 0.52-alt1
- automated CPAN update

* Wed Sep 26 2012 Alexey Tourbin <at@altlinux.ru> 0.50-alt1
- 0.46 -> 0.50

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
