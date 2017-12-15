%define _unpackaged_files_terminate_build 1
%define dist DBD-Sybase
Name: perl-%dist
Version: 1.16
Release: alt1.1

Summary: Sybase database driver (TDS protocol) for the DBI module
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/M/ME/MEWP/%{dist}-%{version}.tar.gz

# Automatically added by buildreq on Sat Oct 08 2011
BuildRequires: libfreetds-devel perl-DBI-devel perl-devel

%description
DBD::Sybase is a Perl module which works with the DBI module to provide
access to Sybase databases.

%prep
%setup -q -n %{dist}-%{version}

# need access to a Sybase server to run the tests
%def_without test

%build
export SYBASE=/usr
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc BUGS CHANGES README eg README.freetds README.vms
%perl_vendor_archlib/DBD
%perl_vendor_autolib/DBD

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.16-alt1.1
- rebuild with new perl 5.26.1

* Tue Sep 26 2017 Igor Vlasenko <viy@altlinux.ru> 1.16-alt1
- automated CPAN update

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.15-alt2.1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 1.15-alt2.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.15-alt2.1
- rebuild with new perl 5.20.1

* Wed Aug 28 2013 Vladimir Lettiev <crux@altlinux.ru> 1.15-alt2
- built for perl 5.18

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 1.15-alt1
- automated CPAN update

* Fri Aug 31 2012 Vladimir Lettiev <crux@altlinux.ru> 1.14-alt2
- rebuilt for perl-5.16

* Sat Oct 08 2011 Alexey Tourbin <at@altlinux.ru> 1.14-alt1
- 1.07 -> 1.14
- built for perl-5.14

* Sat Nov 06 2010 Vladimir Lettiev <crux@altlinux.ru> 1.07-alt3.1
- rebuilt with perl 5.12

* Tue Jul 01 2008 Dmitry Lebkov <dlebkov@altlinux.ru> 1.07-alt3
- rebuild with FreeTDS v0.82

* Thu Dec 20 2007 Dmitry Lebkov <dlebkov@altlinux.ru> 1.07-alt2
- Rebuild with new freetds.

* Fri Jan 12 2007 Dmitry Lebkov <dlebkov@altlinux.ru> 1.07-alt1
- 1.07

* Fri May 27 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.05-alt1.1
- Rebuild with new freetds.

* Tue Dec 21 2004 Dmitry Lebkov <dlebkov@altlinux.ru> 1.05-alt1
- new version

* Wed Sep 22 2004 Dmitry Lebkov <dlebkov@altlinux.ru> 1.04-alt1
- new version

* Mon May 31 2004 Dmitry Lebkov <dlebkov@altlinux.ru> 1.02-alt0.1
- new version

* Wed Mar 19 2003 Dmitry Lebkov <dlebkov@altlinux.ru> 0.95-alt0.3
- rebuild wirth FreeTDS-0.61

* Mon Feb 10 2003 Dmitry Lebkov <dlebkov@altlinux.ru> 0.95-alt0.2
- rebuild wirth FreeTDS-0.61rc1

* Tue Jan 28 2003 Dmitry Lebkov <dlebkov@altlinux.ru> 0.95-alt0.1
- inital build for ALT Linux
