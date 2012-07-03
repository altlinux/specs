%define dist HTML-Encoding
Name: perl-%dist
Version: 0.61
Release: alt1

Summary: Determine the encoding of HTML/XML/XHTML documents
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sat Jan 22 2011
BuildRequires: perl-Test-Pod perl-Test-Pod-Coverage perl-libwww

%description
HTML::Encoding helps to determine the encoding of HTML and XML/XHTML
documents.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/HTML*

%changelog
* Sat Jan 22 2011 Alexey Tourbin <at@altlinux.ru> 0.61-alt1
- 0.52 -> 0.61

* Mon Jul 17 2006 Alexey Tourbin <at@altlinux.ru> 0.52-alt1
- initial revision
