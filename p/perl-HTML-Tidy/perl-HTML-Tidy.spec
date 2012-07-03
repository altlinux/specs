%define dist HTML-Tidy
Name: perl-%dist
Version: 1.08
Release: alt1.2

Summary: HTML validation in a Perl object
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Sat Oct 08 2011
BuildRequires: libtidy-devel perl-Test-Pod perl-Test-Pod-Coverage perl-libwww

%description
HTML::Tidy is an HTML checker in a handy dandy object.  It's meant
as a replacement for HTML::Lint.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%_bindir/webtidy
%perl_vendor_autolib/HTML
%perl_vendor_archlib/HTML

%changelog
* Sat Oct 08 2011 Alexey Tourbin <at@altlinux.ru> 1.08-alt1.2
- rebuilt for perl-5.14

* Sat Nov 06 2010 Vladimir Lettiev <crux@altlinux.ru> 1.08-alt1.1
- rebuilt with perl 5.12

* Sun Mar 02 2008 Nikolay A. Fetisov <naf@altlinux.ru> 1.08-alt1
- New version 1.08

* Tue Aug 08 2006 Nikolay A. Fetisov <naf@altlinux.ru> 1.06-alt1
- Initial build for ALT Linux Sisyphus
