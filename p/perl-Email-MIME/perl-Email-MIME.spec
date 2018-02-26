%define dist Email-MIME
Name: perl-%dist
Version: 1.910
Release: alt1

Summary: Easy MIME message parsing
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/R/RJ/RJBS/Email-MIME-1.910.tar.gz

BuildArch: noarch

Provides: perl-Email-MIME-Modifier = 1.499 perl-Email-MIME-Creator = 1.499
Obsoletes: perl-Email-MIME-Modifier < 1.499 perl-Email-MIME-Creator < 1.499

# Automatically added by buildreq on Sat Dec 18 2010
BuildRequires: perl-Email-MIME-ContentType perl-Email-MIME-Encodings perl-Email-MessageID perl-Email-Simple perl-MIME-Types perl-Test-Pod perl-Test-Pod-Coverage

%description
This is an extension of the Email::Simple module, to handle MIME
encoded messages. It takes a message as a string, splits it up into
its constituent parts, and allows you access to various parts of
the message. Headers are decoded from MIME encoding.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Email*

%changelog
* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 1.910-alt1
- automated CPAN update

* Sat Dec 18 2010 Alexey Tourbin <at@altlinux.ru> 1.906-alt1
- 1.903 -> 1.906

* Wed Apr 28 2010 Alexey Tourbin <at@altlinux.ru> 1.903-alt1
- 1.863 -> 1.903
- provides and obsoletes perl-Email-MIME-Modifier perl-Email-MIME-Creator

* Sun Apr 12 2009 Alexey Tourbin <at@altlinux.ru> 1.863-alt1
- 1.861 -> 1.863

* Mon Sep 01 2008 Alexey Tourbin <at@altlinux.ru> 1.861-alt1
- 1.85 -> 1.861

* Mon Jul 17 2006 Alexey Tourbin <at@altlinux.ru> 1.85-alt1
- initial revision
