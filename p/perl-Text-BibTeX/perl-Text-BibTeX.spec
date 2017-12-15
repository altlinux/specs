%define _unpackaged_files_terminate_build 1
%define dist Text-BibTeX
Name: perl-%dist
Version: 0.85
Release: alt1.1

Summary: Interface to read and parse BibTeX files
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/A/AM/AMBS/%{dist}-%{version}.tar.gz
Patch0: perl-Text-BibTeX-0.61-alt-rpath.patch
Patch1:	perl-Text-BibTeX-0.61-alt-gcc47.patch

# Automatically added by buildreq on Wed Oct 19 2011
BuildRequires: perl-Capture-Tiny perl-Config-AutoConf perl-ExtUtils-LibBuilder perl-Module-Build perl-Pod-Parser perl(Unicode/Normalize.pm)

%description
Text::BibTeX is a Perl library for reading, parsing, and processing
BibTeX files.  It is the Perl half of btOOL, a pair of libraries for
dealing with BibTeX data.

%prep
%setup -q -n %{dist}-%{version}
%patch0 -p1 
%patch1 -p1 
# Sub::Util 
[ %version = 0.77 ] && sed -i -e s,1.42,0.00, META.json Build.PL META.yml


%build
%perl_vendor_build

%install
%perl_vendor_install

mkdir -p %buildroot%_man1dir
install -p -m644 blib/bindoc/*.1 %buildroot%_man1dir/

%files
%doc Changes README THANKS examples README.OLD
%_bindir/*
%_man1dir/*
%_libdir/libbtparse.so
%perl_vendor_autolib/Text
%perl_vendor_archlib/Text

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.85-alt1.1
- rebuild with new perl 5.26.1

* Tue Sep 26 2017 Igor Vlasenko <viy@altlinux.ru> 0.85-alt1
- automated CPAN update

* Wed Aug 30 2017 Igor Vlasenko <viy@altlinux.ru> 0.83-alt1
- automated CPAN update

* Wed Aug 02 2017 Igor Vlasenko <viy@altlinux.ru> 0.81-alt1
- automated CPAN update

* Mon Apr 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.80-alt1
- automated CPAN update

* Wed Mar 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.79-alt1
- automated CPAN update

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.78-alt1.1
- rebuild with new perl 5.24.1

* Sat Jan 14 2017 Igor Vlasenko <viy@altlinux.ru> 0.78-alt1
- automated CPAN update

* Sun Sep 25 2016 Igor Vlasenko <viy@altlinux.ru> 0.77-alt1
- automated CPAN update

* Mon Jul 25 2016 Igor Vlasenko <viy@altlinux.ru> 0.76-alt1
- automated CPAN update

* Tue May 03 2016 Igor Vlasenko <viy@altlinux.ru> 0.72-alt1
- automated CPAN update

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.71-alt1.1
- rebuild with new perl 5.22.0

* Sat Nov 21 2015 Igor Vlasenko <viy@altlinux.ru> 0.71-alt1
- automated CPAN update

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.70-alt1.1
- rebuild with new perl 5.20.1

* Tue Sep 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.70-alt1
- automated CPAN update

* Wed Mar 05 2014 Igor Vlasenko <viy@altlinux.ru> 0.69-alt1
- automated CPAN update

* Thu Aug 29 2013 Vladimir Lettiev <crux@altlinux.ru> 0.66-alt2
- built for perl 5.18

* Thu Jan 24 2013 Kirill Maslinsky <kirill@altlinux.org> 0.66-alt1
- 0.65 -> 0.66

* Wed Oct 17 2012 Igor Vlasenko <viy@altlinux.ru> 0.65-alt1
- automated CPAN update
- added gcc47 patch

* Sun Sep 02 2012 Vladimir Lettiev <crux@altlinux.ru> 0.64-alt1
- 0.61 -> 0.64
- built for perl-5.16

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
