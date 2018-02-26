%define dist HTML-FormatText-WithLinks
Name: perl-%dist
Version: 0.14
Release: alt1

Summary: HTML to text conversion with links as footnotes
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Fri Nov 11 2011
BuildRequires: perl-HTML-Tree perl-Module-Build perl-Test-MockObject perl-Test-Pod perl-Test-Pod-Coverage

%description
HTML::FormatText::WithLinks takes HTML and turns it into plain text
but prints all the links in the HTML as footnotes. By default, it attempts
to mimic the format of the lynx text based web browser's --dump option.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/HTML

%changelog
* Fri Nov 11 2011 Alexey Tourbin <at@altlinux.ru> 0.14-alt1
- 0.07 -> 0.14

* Thu Feb 01 2007 Alexey Tourbin <at@altlinux.ru> 0.07-alt1
- 0.05 -> 0.07
- implemented link unique numbering (cpan #24713)

* Sat Sep 17 2005 Alexey Tourbin <at@altlinux.ru> 0.05-alt1
- 0.03 -> 0.05
- alt-href.patch mreged upstream (cpan #14288)

* Wed Aug 24 2005 Alexey Tourbin <at@altlinux.ru> 0.03-alt2
- skip <a> tags without href= attribute (cpan #14288)

* Sun Aug 21 2005 Alexey Tourbin <at@altlinux.ru> 0.03-alt1
- initial revision
