Name: perl-Wx-Scintilla
Version: 0.34
Release: alt1

Summary: Wx::Scintilla - Scintilla source code editing component for wxWidgets
Group: Development/Perl
License: Perl

Url: %CPAN Wx-Scintilla
Source: %name-%version.tar

BuildRequires: perl-devel perl-Module-Build perl-Alien-wxWidgets perl-Wx-devel gcc-c++ perl-ExtUtils-XSpp libpng-devel libgtk+2-devel libpango-devel libfreetype-devel fontconfig-devel glib2-devel zlib-devel libwxGTK-devel xvfb-run

Requires: perl-Alien-wxWidgets

%define _perl_req_method relaxed

%description
%summary

%prep
%setup -q

%build
%def_without test
%perl_vendor_build
xvfb-run -a ./Build test

%install
%perl_vendor_install

%files
%perl_vendor_archlib/Wx/Scintilla*
%perl_vendor_autolib/Wx/Scintilla*
%doc Changes README 

%changelog
* Mon Nov 14 2011 Vladimir Lettiev <crux@altlinux.ru> 0.34-alt1
- initial build
