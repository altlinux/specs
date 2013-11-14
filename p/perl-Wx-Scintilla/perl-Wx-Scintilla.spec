%define dist Wx-Scintilla
Name: perl-%dist
Version: 0.39
Release: alt2

Summary: Wx::Scintilla - Scintilla source code editing component for wxWidgets
Group: Development/Perl
License: Perl

Url: %CPAN %dist
Source: %dist-%version.tar.gz

BuildRequires: perl-devel perl-Module-Build perl-Alien-wxWidgets perl-Wx-devel gcc-c++ perl-ExtUtils-XSpp libpng-devel libgtk+2-devel libpango-devel libfreetype-devel fontconfig-devel glib2-devel zlib-devel libwxGTK-devel xvfb-run

Requires: perl-Alien-wxWidgets

%add_findreq_skiplist */Wx/Scintilla.pm

%description
%summary

%prep
%setup -q -n %dist-%version

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
* Thu Nov 14 2013 Vladimir Lettiev <crux@altlinux.ru> 0.39-alt2
- rebuilt for perl 5.18

* Tue Sep 11 2012 Vladimir Lettiev <crux@altlinux.ru> 0.39-alt1
- 0.34 -> 0.39

* Mon Nov 14 2011 Vladimir Lettiev <crux@altlinux.ru> 0.34-alt1
- initial build
