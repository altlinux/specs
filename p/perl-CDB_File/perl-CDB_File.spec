%define _unpackaged_files_terminate_build 1
%define dist CDB_File
Name: perl-%dist
Version: 0.99
Release: alt1.1.1

Summary: Perl extension for access to cdb databases
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/T/TO/TODDR/CDB_File-%{version}.tar.gz

# Automatically added by buildreq on Fri Oct 07 2011
BuildRequires: perl-devel

%description
CDB_File is a module which provides a Perl interface to Dan
Berstein's cdb package.  cdb is a fast, reliable, lightweight
package for creating and reading constant databases.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install
rm -f %buildroot%perl_vendor_archlib/bun-x.pl

%files
%doc ACKNOWLEDGE CHANGES COPYRIGHT README
%perl_vendor_archlib/CDB_File*
%perl_vendor_autolib/CDB_File*

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.99-alt1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.99-alt1.1
- rebuild with new perl 5.24.1

* Mon Jul 25 2016 Igor Vlasenko <viy@altlinux.ru> 0.99-alt1
- automated CPAN update

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.98-alt1.1
- rebuild with new perl 5.22.0

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 0.98-alt1
- automated CPAN update

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.97-alt5.1
- rebuild with new perl 5.20.1

* Tue Aug 27 2013 Vladimir Lettiev <crux@altlinux.ru> 0.97-alt5
- built for perl 5.18

* Thu Aug 30 2012 Vladimir Lettiev <crux@altlinux.ru> 0.97-alt4
- rebuilt for perl-5.16

* Fri Oct 07 2011 Alexey Tourbin <at@altlinux.ru> 0.97-alt3
- rebuilt for perl-5.14

* Tue Oct 04 2011 Alexey Tourbin <at@altlinux.ru> 0.97-alt2
- rebuilt

* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.97-alt1
- automated CPAN update

* Fri Nov 05 2010 Vladimir Lettiev <crux@altlinux.ru> 0.96-alt1
- new version
- rebuilt with perl 5.12

* Wed Sep 12 2007 Alexey Tourbin <at@altlinux.ru> 0.95-alt1
- 0.94 -> 0.95

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.94-alt1.1
- Rebuilt with rpm-build-perl-0.5.1.

* Tue May 11 2004 Alexey Tourbin <at@altlinux.ru> 0.94-alt1
- 0.92 -> 0.94, resurrected

* Fri Mar 21 2003 Stanislav Ievlev <inger@altlinux.ru> 0.92-alt1
- 0.92

* Tue Nov 12 2002 Stanislav Ievlev <inger@altlinux.ru> 0.91-alt1
- Initial release
