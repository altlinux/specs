%define _unpackaged_files_terminate_build 1
%define dist Compress-LZO
Name: perl-%dist
Version: 1.09
Release: alt1.1.1

Summary: Perl interface to the LZO compression library
License: GPL
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/P/PE/PEPL/Compress-LZO-%{version}.tar.gz

# Automatically added by buildreq on Fri Oct 07 2011
BuildRequires: liblzo2-devel perl-devel perl(Devel/CheckLib.pm)

%description
This module provides a Perl interface to LZO compression library.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README*
%perl_vendor_archlib/Compress
%perl_vendor_autolib/Compress

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.09-alt1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.09-alt1.1
- rebuild with new perl 5.24.1

* Tue Sep 20 2016 Igor Vlasenko <viy@altlinux.ru> 1.09-alt1
- automated CPAN update

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 1.08-alt7.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.08-alt7.1
- rebuild with new perl 5.20.1

* Tue Aug 27 2013 Vladimir Lettiev <crux@altlinux.ru> 1.08-alt7
- built for perl 5.18

* Thu Aug 30 2012 Vladimir Lettiev <crux@altlinux.ru> 1.08-alt6
- rebuilt for perl-5.16

* Fri Oct 07 2011 Alexey Tourbin <at@altlinux.ru> 1.08-alt5
- rebuilt for perl-5.14

* Tue Oct 04 2011 Alexey Tourbin <at@altlinux.ru> 1.08-alt4
- rebuilt

* Sat Nov 06 2010 Vladimir Lettiev <crux@altlinux.ru> 1.08-alt3.1
- rebuilt with perl 5.12

* Sun Aug 10 2008 Alexey Tourbin <at@altlinux.ru> 1.08-alt3
- built with liblzo2

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.08-alt2.1
- Rebuilt with rpm-build-perl-0.5.1.

* Tue Nov 25 2003 Andrey Brindeew <abr@altlinux.ru> 1.08-alt2
- Url tag was fixed

* Tue Nov 05 2002 Stanislav Ievlev <inger@altlinux.ru> 1.08-alt1
- rebuild with new perl

* Sun Aug 25 2002 Andrey Brindeew <abr@altlinux.ru> 1.00-alt1
- Initial release
