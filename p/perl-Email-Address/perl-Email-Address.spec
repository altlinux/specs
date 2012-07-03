%define dist Email-Address
Name: perl-%dist
Version: 1.892
Release: alt1

Summary: RFC 2822 Address Parsing
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sat Dec 18 2010
BuildRequires: perl-Test-Pod perl-Test-Pod-Coverage

%description
This class implements a complete RFC 2822 parser that locates email
addresses in strings and returns a list of Email::Address objects
found. Alternatley you may construct objects manually. The goal
of this software is to be correct, and very very fast.

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
* Sat Dec 18 2010 Alexey Tourbin <at@altlinux.ru> 1.892-alt1
- 1.889 -> 1.892

* Wed Apr 28 2010 Alexey Tourbin <at@altlinux.ru> 1.889-alt1
- 1.887 -> 1.889

* Wed Apr 18 2007 Alexey Tourbin <at@altlinux.ru> 1.887-alt1
- 1.884 -> 1.887

* Thu Feb 22 2007 Alexey Tourbin <at@altlinux.ru> 1.884-alt1
- 1.85 -> 1.884 (closes #10404)

* Mon Jul 17 2006 Alexey Tourbin <at@altlinux.ru> 1.85-alt1
- initial revision
