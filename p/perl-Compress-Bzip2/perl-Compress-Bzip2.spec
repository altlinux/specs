%define _unpackaged_files_terminate_build 1
%define dist Compress-Bzip2
Name: perl-%dist
Version: 2.26
Release: alt1.1

Summary: Interface to Bzip2 compression library
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/R/RU/RURBAN/%{dist}-%{version}.tar.gz

# Automatically added by buildreq on Fri Oct 07 2011
BuildRequires: bzlib-devel perl-devel

%description
The Compress::Bzip2 module provides a Perl interface to the Bzip2
compression library.

%prep
%setup -q -n %{dist}-%{version}

%build
export BUILD_BZLIB=0
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README*
%perl_vendor_archlib/Compress
%perl_vendor_autolib/Compress

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 2.26-alt1.1
- rebuild with new perl 5.26.1

* Tue May 09 2017 Igor Vlasenko <viy@altlinux.ru> 2.26-alt1
- automated CPAN update

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 2.25-alt1.1
- rebuild with new perl 5.24.1

* Thu Nov 17 2016 Igor Vlasenko <viy@altlinux.ru> 2.25-alt1
- automated CPAN update

* Tue Dec 15 2015 Igor Vlasenko <viy@altlinux.ru> 2.24-alt1
- automated CPAN update

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 2.22-alt1.1
- rebuild with new perl 5.22.0

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 2.22-alt1
- automated CPAN update

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 2.19-alt1.1
- rebuild with new perl 5.20.1

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 2.19-alt1
- automated CPAN update

* Tue Aug 19 2014 Igor Vlasenko <viy@altlinux.ru> 2.18-alt1
- automated CPAN update

* Thu Sep 12 2013 Igor Vlasenko <viy@altlinux.ru> 2.17-alt1
- automated CPAN update

* Tue Aug 27 2013 Vladimir Lettiev <crux@altlinux.ru> 2.16-alt2
- built for perl 5.18

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 2.16-alt1
- automated CPAN update

* Thu Aug 30 2012 Vladimir Lettiev <crux@altlinux.ru> 2.09-alt5
- rebuilt for perl-5.16

* Fri Oct 07 2011 Alexey Tourbin <at@altlinux.ru> 2.09-alt4
- rebuilt for perl-5.14

* Tue Oct 04 2011 Alexey Tourbin <at@altlinux.ru> 2.09-alt3
- rebuilt

* Sat Nov 06 2010 Vladimir Lettiev <crux@altlinux.ru> 2.09-alt2.1
- rebuilt with perl 5.12

* Mon Oct 13 2008 Alexey Tourbin <at@altlinux.ru> 2.09-alt2
- Compress/Bzip2.pm: removed AutoLoader
- fixed directory packaging

* Sat Aug 27 2005 Andrey Brindeew <abr@altlinux.org> 2.09-alt1
- 2.09

* Mon Nov 24 2003 Andrey Brindeew <abr@altlinux.ru> 1.02-alt2
- Url and Summary tag was fixed

* Wed Jul 30 2003 Andrey Brindeew <abr@altlinux.ru> 1.02-alt1
- First build for ALT Linux

