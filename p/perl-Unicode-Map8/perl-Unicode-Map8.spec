%define dist Unicode-Map8
Name: perl-%dist
Version: 0.13
Release: alt4.1.1.1.1

Summary: Perl module to represent mapping tables between 8-bit chars and Unicode
License: GPL
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

Patch0: Unicode-Map8-0.12-type.diff
Patch1: Unicode-Map8-0.12-declaration.diff

# Automatically added by buildreq on Sun Oct 09 2011
BuildRequires: perl-Unicode-String perl-devel perl-podlators

%description
The Unicode::Map8 class implement efficient mapping tables between
8-bit character sets and 16 bit character sets like Unicode.  The
tables are efficient both in terms of space allocated and translation
speed.  The 16-bit strings is assumed to use network byte order.

%prep
%setup -q -n %dist-%version
%patch0
%patch1

%build
%perl_vendor_build INSTALLMAN1DIR=%_man1dir

%install
%perl_vendor_install

%files 
%doc Changes README
%_bindir/umap
%_man1dir/umap.1*
%perl_vendor_archlib/Unicode*
%perl_vendor_autolib/Unicode*

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.13-alt4.1.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.13-alt4.1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.13-alt4.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.13-alt4.1
- rebuild with new perl 5.20.1

* Wed Aug 28 2013 Vladimir Lettiev <crux@altlinux.ru> 0.13-alt4
- built for perl 5.18

* Sat Sep 01 2012 Vladimir Lettiev <crux@altlinux.ru> 0.13-alt3
- rebuilt for perl-5.16

* Sun Oct 09 2011 Alexey Tourbin <at@altlinux.ru> 0.13-alt2
- rebuilt for perl-5.14

* Sun Sep 25 2011 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1
- automated CPAN update

* Mon Nov 08 2010 Vladimir Lettiev <crux@altlinux.ru> 0.12-alt3.1
- rebuilt with perl 5.12

* Fri Nov 24 2006 Slava Dubrovskiy <dubrsl@altlinux.ru> 0.12-alt3
- NMU: Fix x86_64 build (#10311)
- Add patch Unicode-Map8-%version-type.diff and Unicode-Map8-%version-declaration.diff
  from OpenSUSE
- Add /usr/bin/umap, /usr/share/man/man1/umap.1.gz
- Add rfc1345.txt in doc

* Tue Feb 21 2006 Vitaly Lipatov <lav@altlinux.ru> 0.12-alt2
- NMU: fix Source Url

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.12-alt1.1
- Rebuilt with rpm-build-perl-0.5.1.

* Thu Mar 20 2003 Alexey Dyachenko <alexd@altlinux.ru> 0.12-alt1
- 0.12

* Mon Nov 04 2002 Stanislav Ievlev <inger@altlinux.ru> 0.11-alt2
- rebuild with new perl

* Mon Sep 16 2002 Alexey Dyachenko <alexd@altlinux.ru> 0.11-alt1
- Initial build for Sisyphus.
