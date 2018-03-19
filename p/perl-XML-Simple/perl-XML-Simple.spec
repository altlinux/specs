%define _unpackaged_files_terminate_build 1
%define dist XML-Simple
Name: perl-%dist
Version: 2.25
Release: alt1

Summary: Easy API to read/write XML
Group: Development/Perl
License: GPL or Artistic

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/G/GR/GRANTM/%{dist}-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Sep 26 2012
BuildRequires: perl-Tie-IxHash perl-XML-Parser perl-XML-SAX perl-devel

%description
The XML::Simple module provides a simple API layer on top of an underlying
XML parsing module (either XML::Parser or one of the SAX2 parser modules).

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc	Changes README
%dir	%perl_vendor_privlib/XML
	%perl_vendor_privlib/XML/Simple.pm
%dir	%perl_vendor_privlib/XML/Simple
%doc	%perl_vendor_privlib/XML/Simple/*.pod

%changelog
* Mon Mar 19 2018 Igor Vlasenko <viy@altlinux.ru> 2.25-alt1
- automated CPAN update

* Tue May 09 2017 Igor Vlasenko <viy@altlinux.ru> 2.24-alt1
- automated CPAN update

* Mon Dec 07 2015 Igor Vlasenko <viy@altlinux.ru> 2.22-alt1
- automated CPAN update

* Wed Sep 26 2012 Alexey Tourbin <at@altlinux.ru> 2.20-alt1
- 2.18 -> 2.20

* Tue Oct 04 2011 Alexey Tourbin <at@altlinux.ru> 2.18-alt2
- rebuilt

* Fri Aug 17 2007 Alexey Tourbin <at@altlinux.ru> 2.18-alt1
- 2.14 -> 2.18

* Sat Aug 27 2005 Andrey Brindeew <abr@altlinux.org> 2.14-alt1
- 2.14

* Sun Nov 28 2004 Andrey Brindeew <abr@altlinux.org> 2.13-alt1
- 2.13

* Sun Oct 03 2004 Andrey Brindeew <abr@altlinux.org> 2.12-alt1
- 2.12

* Sat Mar 06 2004 Andrey Brindeew <abr@altlinux.ru> 2.11-alt1
- 2.11

* Mon Nov 24 2003 Andrey Brindeew <abr@altlinux.ru> 2.09-alt2
- Url and Summary was fixed

* Tue Sep 16 2003 Andrey Brindeew <abr@altlinux.ru> 2.09-alt1
- 2.09

* Tue Jul 29 2003 Andrey Brindeew <abr@altlinux.ru> 2.08-alt2
- Minor specfile fixes.
- Added `Changes' file to docs.

* Sat Jun 28 2003 Andrey Brindeew <abr@altlinux.ru> 2.08-alt1
- First build for ALTLinux.
- new version 2.08

