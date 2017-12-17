%define dist Wx-Scintilla
Name: perl-%dist
Version: 0.39
Release: alt4.1.1

Summary: Wx::Scintilla - Scintilla source code editing component for wxWidgets
Group: Development/Perl
License: Perl

Url: %CPAN %dist
Source: %dist-%version.tar.gz
Patch1: 0001-fixed-linking.patch
Patch2: 0002-fix-compilation-with-gcc6.patch

BuildRequires: perl-devel perl-Module-Build perl-Alien-wxWidgets perl-Wx-devel gcc-c++ perl-ExtUtils-XSpp libpng-devel libgtk+2-devel libpango-devel libfreetype-devel fontconfig-devel glib2-devel zlib-devel libwxGTK-devel xvfb-run

Requires: perl-Alien-wxWidgets

%add_findreq_skiplist */Wx/Scintilla.pm

%description
%summary

%prep
%setup -q -n %dist-%version
%patch1 -p1
%patch2 -p1

%build
%def_without test
%perl_vendor_build

%install
%perl_vendor_install

%check
xvfb-run -a ./Build test

%files
%perl_vendor_archlib/Wx/Scintilla*
%perl_vendor_autolib/Wx/Scintilla*
%doc Changes README

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.39-alt4.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.39-alt4.1
- rebuild with new perl 5.24.1

* Sat Jan 28 2017 Vladimir Lettiev <crux@altlinux.ru> 0.39-alt4
- fixed build with gcc6

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.39-alt3.1
- rebuild with new perl 5.22.0

* Fri Oct 30 2015 Vladimir Lettiev <crux@altlinux.ru> 0.39-alt3
- rebuilt for perl 5.20
- fixed linking

* Thu Nov 14 2013 Vladimir Lettiev <crux@altlinux.ru> 0.39-alt2
- rebuilt for perl 5.18

* Tue Sep 11 2012 Vladimir Lettiev <crux@altlinux.ru> 0.39-alt1
- 0.34 -> 0.39

* Mon Nov 14 2011 Vladimir Lettiev <crux@altlinux.ru> 0.34-alt1
- initial build
