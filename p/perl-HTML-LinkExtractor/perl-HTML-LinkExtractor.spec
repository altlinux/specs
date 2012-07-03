%define dist HTML-LinkExtractor
Name: perl-%dist
Version: 0.13
Release: alt2

Summary: Extract links from an HTML document
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Oct 05 2011
BuildRequires: perl-HTML-Parser perl-devel

%description
HTML::LinkExtractor is used for extracting links from HTML.
It is very similar to HTML::LinkExtor, except that besides
getting the URL, you also get the link-text.

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
* Wed Oct 05 2011 Alexey Tourbin <at@altlinux.ru> 0.13-alt2
- rebuilt

* Mon Jul 17 2006 Alexey Tourbin <at@altlinux.ru> 0.13-alt1
- initial revision
