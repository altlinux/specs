Name: perl-X11-Xlib
Version: 0.02
Release: alt1.1

Summary: Low-level access to the X11 library
Group: Development/Perl
License: Perl

Url: %CPAN X11-Xlib
Source: %name-%version.tar

BuildRequires: perl-devel perl-Devel-CheckLib libX11-devel libXtst-devel xvfb-run

%description
%summary

%prep
%setup -q
rm -r inc

%build
%def_without test
%perl_vendor_build
xvfb-run -a make test

%install
%perl_vendor_install

%files
%perl_vendor_autolib/X11/Xlib*
%perl_vendor_archlib/X11/Xlib*
%doc Changes README

%changelog
* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1.1
- rebuild with new perl 5.20.1

* Mon Oct 07 2013 Vladimir Lettiev <crux@altlinux.ru> 0.02-alt1
- initial build for ALTLinux

