%define dist Text-BibTeX
Name: perl-%dist
Version: 0.61
Release: alt2

Summary: Interface to read and parse BibTeX files
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz
Patch0: perl-Text-BibTeX-0.61-alt-rpath.patch

# Automatically added by buildreq on Wed Oct 19 2011
BuildRequires: perl-Capture-Tiny perl-Config-AutoConf perl-ExtUtils-LibBuilder perl-Module-Build perl-Pod-Parser

%description
Text::BibTeX is a Perl library for reading, parsing, and processing
BibTeX files.  It is the Perl half of btOOL, a pair of libraries for
dealing with BibTeX data.

%prep
%setup -q -n %dist-%version
%patch0 -p1 

%build
%perl_vendor_build

%install
%perl_vendor_install

mkdir -p %buildroot%_man1dir
install -p -m644 blib/bindoc/*.1 %buildroot%_man1dir/

%files
%doc CHANGES README THANKS examples
%_bindir/*
%_man1dir/*
%_libdir/libbtparse.so
%perl_vendor_autolib/Text
%perl_vendor_archlib/Text

%changelog
* Tue Dec 27 2011 Kirill Maslinsky <kirill@altlinux.org> 0.61-alt2
- remove standard libdir from Rpath

* Tue Dec 06 2011 Kirill Maslinsky <kirill@altlinux.org> 0.61-alt1
- 0.61

* Wed Oct 19 2011 Alexey Tourbin <at@altlinux.ru> 0.60-alt1
- 0.43 -> 0.60
- built for perl-5.14

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 0.43-alt1.1
- rebuilt with perl 5.12
- fixed manpages installation

* Mon Mar 22 2010 Kirill Maslinsky <kirill@altlinux.org> 0.43-alt1
- 0.43

* Fri Mar 12 2010 Kirill Maslinsky <kirill@altlinux.org> 0.40-alt1
- 0.40

* Mon Sep 14 2009 Kirill Maslinsky <kirill@altlinux.org> 0.38-alt1
- initial build for ALT Linux Sisyphus
