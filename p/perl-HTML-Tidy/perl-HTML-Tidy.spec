%define dist HTML-Tidy
Name: perl-%dist
Version: 1.60
Release: alt1.1

Summary: HTML validation in a Perl object

License: %perl_license
Group: Development/Perl
URL: %CPAN %dist

Source: http://www.cpan.org/authors/id/P/PE/PETDANCE/HTML-Tidy-%{version}.tar.gz

BuildRequires(pre): rpm-build-licenses

# Automatically added by buildreq on Sun Jun 04 2017
# optimized out: perl perl-Devel-Symdump perl-Encode perl-Encode-Locale perl-HTTP-Date perl-HTTP-Message perl-Pod-Coverage perl-Pod-Escapes perl-Pod-Parser perl-Pod-Simple perl-Sub-Uplevel perl-Try-Tiny perl-URI perl-devel perl-libwww python-base python-modules python3 python3-base
BuildRequires: libtidyp-devel perl-Test-Exception perl-Test-Pod perl-Test-Pod-Coverage perl-libwww

BuildRequires: tidyp


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
%doc Changes README.markdown
%_bindir/webtidy
%perl_vendor_autolib/HTML
%perl_vendor_archlib/HTML

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.60-alt1.1
- rebuild with new perl 5.26.1

* Tue Sep 26 2017 Nikolay A. Fetisov <naf@altlinux.org> 1.60-alt1
- New version

* Sat Jun 10 2017 Nikolay A. Fetisov <naf@altlinux.org> 1.58-alt1
- New version

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.56-alt1.1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 1.56-alt1.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.56-alt1.1
- rebuild with new perl 5.20.1

* Tue Mar 11 2014 Igor Vlasenko <viy@altlinux.ru> 1.56-alt1
- automated CPAN update

* Wed Aug 28 2013 Vladimir Lettiev <crux@altlinux.ru> 1.54-alt2
- built for perl 5.18

* Fri Aug 31 2012 Vladimir Lettiev <crux@altlinux.ru> 1.54-alt1
- 1.08 -> 1.54
- built for perl-5.16
- libtidy -> libtidyp

* Sat Oct 08 2011 Alexey Tourbin <at@altlinux.ru> 1.08-alt1.2
- rebuilt for perl-5.14

* Sat Nov 06 2010 Vladimir Lettiev <crux@altlinux.ru> 1.08-alt1.1
- rebuilt with perl 5.12

* Sun Mar 02 2008 Nikolay A. Fetisov <naf@altlinux.ru> 1.08-alt1
- New version 1.08

* Tue Aug 08 2006 Nikolay A. Fetisov <naf@altlinux.ru> 1.06-alt1
- Initial build for ALT Linux Sisyphus
