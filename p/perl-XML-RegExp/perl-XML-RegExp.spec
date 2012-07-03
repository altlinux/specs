%define dist XML-RegExp
Name: perl-%dist
Version: 0.03
Release: alt5

Summary: Regular expressions for XML tokens
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Mon Nov 14 2011
BuildRequires: perl-devel

%description
This package contains regular expressions for the following XML tokens:
BaseChar, Ideographic, Letter, Digit, Extender, CombiningChar, NameChar,
EntityRef, CharRef, Reference, Name, NmToken, and AttValue.

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
* Mon Nov 14 2011 Alexey Tourbin <at@altlinux.ru> 0.03-alt5
- rebuilt as plain src.rpm

* Mon Sep 28 2009 Alexey Tourbin <at@altlinux.ru> 0.03-alt4
- rebuild

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.03-alt3.1
- Rebuilt with rpm-build-perl-0.5.1.

* Mon Nov 24 2003 Andrey Brindeew <abr@altlinux.ru> 0.03-alt3
- Url and Summary was fixed.

* Wed Jul 30 2003 Andrey Brindeew <abr@altlinux.ru> 0.03-alt2
- Minor specfile fixes.

* Fri Jul 18 2003 Andrey Brindeew <abr@altlinux.ru> 0.03-alt1
- First build for ALTLinux.
