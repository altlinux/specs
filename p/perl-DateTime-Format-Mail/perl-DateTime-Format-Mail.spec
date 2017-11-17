%define _unpackaged_files_terminate_build 1
%define dist DateTime-Format-Mail
Name: perl-%dist
Version: 0.403
Release: alt2
Serial:  1

Summary: Convert between DateTime and RFC2822/822 formats
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/B/BO/BOOK/DateTime-Format-Mail-%{version}.tar.gz

BuildArch: noarch

# Added by buildreq2 on Thu Aug 10 2006
BuildRequires: perl-DateTime perl-File-Find-Rule perl-Module-Build perl-Test-Pod perl-Params-Validate

%description
RFCs 2822 and 822 specify date formats to be used by email.
This module parses and emits such dates.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes CREDITS README
%perl_vendor_privlib/DateTime*

%changelog
* Fri Nov 17 2017 Oleg Solovyov <mcpain@altlinux.org> 1:0.403-alt2
- fix missing buildreq

* Sun Jul 03 2016 Igor Vlasenko <viy@altlinux.ru> 1:0.403-alt1
- automated CPAN update

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 1:0.402-alt1
- automated CPAN update

* Mon Jun 23 2014 Igor Vlasenko <viy@altlinux.ru> 1:0.401-alt1
- automated CPAN update

* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.3001-alt1
- automated CPAN update

* Thu Aug 10 2006 Alexey Tourbin <at@altlinux.ru> 0.30-alt1
- 0.2901 -> 0.30
- noarch

* Sun Aug 21 2005 Alexey Tourbin <at@altlinux.ru> 0.29.01-alt1
- initial revision (for XML::Feed)
