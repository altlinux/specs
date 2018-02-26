%define dist Unicode-String
Name: perl-%dist
Version: 2.09
Release: alt1.2

Summary: Perl module to represent strings of Unicode chars 
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

Provides: perl-Unicode-CharName = %version
Obsoletes: perl-Unicode-CharName <= %version

# Automatically added by buildreq on Sat Oct 08 2011
BuildRequires: perl-devel

%description
Perl module to represent strings of Unicode chars. They were made before
perl included native UTF8 support.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/Unicode
%perl_vendor_autolib/Unicode

%changelog
* Sat Oct 08 2011 Alexey Tourbin <at@altlinux.ru> 2.09-alt1.2
- rebuilt for perl-5.14
- merged perl-Unicode-CharName subpackage into perl-Unicode-String

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 2.09-alt1.1
- rebuilt with perl 5.12

* Sat Sep 06 2008 Vitaly Lipatov <lav@altlinux.ru> 2.09-alt1
- disable man packaging

* Tue Feb 21 2006 Vitaly Lipatov <lav@altlinux.ru> 2.09-alt0.1
- new version (2.09)
- change packager
- add Url, fix Source URL

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 2.07-alt1.1
- Rebuilt with rpm-build-perl-0.5.1.

* Thu Mar 20 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.07-alt1
- 2.07

* Mon Nov 04 2002 Stanislav Ievlev <inger@altlinux.ru> 2.06-alt2
- rebuild with new perl

* Thu Jan 10 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.06-alt1
- First build for Sisyphus.
