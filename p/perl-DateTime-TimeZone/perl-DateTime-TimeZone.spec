%define _unpackaged_files_terminate_build 1
%define dist DateTime-TimeZone
%def_without bootstrap
Name: perl-%dist
Version: 2.15
Release: alt1

Summary: Time zone object base class and factory
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/D/DR/DROLSKY/%{dist}-%{version}.tar.gz

BuildArch: noarch

# avoid rpmdb bloat
%add_findprov_skiplist */DateTime/TimeZone/Africa/*
%add_findprov_skiplist */DateTime/TimeZone/America/*
%add_findprov_skiplist */DateTime/TimeZone/Antarctica/*
%add_findprov_skiplist */DateTime/TimeZone/Asia/*
%add_findprov_skiplist */DateTime/TimeZone/Atlantic/*
%add_findprov_skiplist */DateTime/TimeZone/Australia/*
%add_findprov_skiplist */DateTime/TimeZone/Europe/*
%add_findprov_skiplist */DateTime/TimeZone/Indian/*
%add_findprov_skiplist */DateTime/TimeZone/Pacific/*

%if_with bootstrap
# bootstrap: disable circular dependencies on DateTime
%add_findreq_skiplist */DateTime/TimeZone/*
# bootstrap: some dependencies have to be re-added manually
Requires: perl-Class-Load perl-Class-Singleton perl-Params-Validate perl-parent
%else
BuildRequires: perl-DateTime perl(Test/Requires.pm) perl(List/AllUtils.pm) perl(Test/Fatal.pm)
%endif

BuildRequires: perl-Class-Load perl-Class-Singleton perl-Test-Output perl-Params-Validate perl-parent

# perl -c fails; let us skip it as in debian
%add_findreq_skiplist */DateTime/TimeZone/OffsetOnly.pm
%add_findreq_skiplist */DateTime/TimeZone.pm
# and add requires manually
Requires: perl(Module/Runtime.pm) perl(Params/ValidationCompiler.pm) perl(Specio/Library/Builtins.pm) perl(Specio/Library/String.pm) perl(Try/Tiny.pm)


%description
The DateTime::TimeZone modules provide a Perl interface to the Olson
time zone database.  Rather than using the database directly, we parse
the database files and turn them into a set of modules, one for each
time zone defined.  This allows for various optimizations in doing
time zone calculations.  This conversion is done with the script in
tools/parse_olson.

The Olson time zone database is the best available source for world
wide time zone information.  It is available from
ftp://elsie.nci.nih.gov/pub/.  A good starting point for information
on the database, and time zones in general, is
http://www.twinsun.com/tz/tz-link.htm.

%prep
%setup -q -n %{dist}-%{version}

# avoid build dependency on perl-podlators
sed -i- '/Pod::Man/d' Makefile.PL

%if_with bootstrap
# bootstrap: avoid build dependency on DateTime
sed -i- 's/eval "use DateTime/eval "die/' t/check_datetime_version.pl
%endif

if [ %version != 2.15 ]; then
    echo update manual requires due to findreq_skiplist!
    exit 1
fi

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README.md CONTRIBUTING.md
%perl_vendor_privlib/DateTime

%changelog
* Tue Dec 19 2017 Igor Vlasenko <viy@altlinux.ru> 2.15-alt1
- automated CPAN update

* Mon Oct 02 2017 Igor Vlasenko <viy@altlinux.ru> 2.13-alt1
- automated CPAN update

* Tue May 09 2017 Igor Vlasenko <viy@altlinux.ru> 2.11-alt1
- automated CPAN update

* Tue Dec 20 2016 Igor Vlasenko <viy@altlinux.ru> 2.09-alt1
- automated CPAN update

* Mon Jul 25 2016 Igor Vlasenko <viy@altlinux.ru> 2.01-alt1
- automated CPAN update

* Mon Jun 13 2016 Igor Vlasenko <viy@altlinux.ru> 2.00-alt1
- automated CPAN update

* Wed Apr 20 2016 Igor Vlasenko <viy@altlinux.ru> 1.98-alt1
- automated CPAN update

* Mon Mar 28 2016 Igor Vlasenko <viy@altlinux.ru> 1.97-alt1
- automated CPAN update

* Sat Mar 19 2016 Igor Vlasenko <viy@altlinux.ru> 1.96-alt1
- automated CPAN update

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 1.95-alt1
- automated CPAN update

* Mon Oct 26 2015 Igor Vlasenko <viy@altlinux.ru> 1.94-alt1
- automated CPAN update

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 1.93-alt1
- automated CPAN update

* Fri May 22 2015 Igor Vlasenko <viy@altlinux.ru> 1.90-alt1
- automated CPAN update

* Tue Oct 07 2014 Igor Vlasenko <viy@altlinux.ru> 1.75-alt1
- automated CPAN update

* Mon Sep 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.74-alt1
- automated CPAN update

* Wed Aug 20 2014 Igor Vlasenko <viy@altlinux.ru> 1.73-alt1
- automated CPAN update

* Mon Jun 23 2014 Igor Vlasenko <viy@altlinux.ru> 1.71-alt1
- automated CPAN update

* Mon Jun 02 2014 Igor Vlasenko <viy@altlinux.ru> 1.70-alt1
- automated CPAN update

* Mon May 19 2014 Igor Vlasenko <viy@altlinux.ru> 1.69-alt1
- automated CPAN update

* Mon Mar 10 2014 Igor Vlasenko <viy@altlinux.ru> 1.65-alt1
- automated CPAN update

* Sat Feb 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.64-alt1
- automated CPAN update

* Tue Oct 29 2013 Igor Vlasenko <viy@altlinux.ru> 1.63-alt1
- automated CPAN update

* Fri Sep 27 2013 Igor Vlasenko <viy@altlinux.ru> 1.62-alt1
- automated CPAN update

* Mon Sep 23 2013 Igor Vlasenko <viy@altlinux.ru> 1.61-alt1
- automated CPAN update

* Thu Sep 12 2013 Vladimir Lettiev <crux@altlinux.ru> 1.60-alt4
- fixed failed unbootsrap

* Thu Sep 05 2013 Vladimir Lettiev <crux@altlinux.ru> 1.60-alt3
- re-enabled dependency on perl-DateTime

* Sun Aug 25 2013 Vladimir Lettiev <crux@altlinux.ru> 1.60-alt2
- bootstrap for perl-5.18

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 1.60-alt1
- automated CPAN update

* Tue Oct 23 2012 Igor Vlasenko <viy@altlinux.ru> 1.51-alt1
- automated CPAN update

* Tue Sep 25 2012 Igor Vlasenko <viy@altlinux.ru> 1.50-alt1
- automated CPAN update

* Sun Sep 09 2012 Vladimir Lettiev <crux@altlinux.ru> 1.48-alt2
- re-enabled dependency on perl-DateTime

* Tue Aug 28 2012 Vladimir Lettiev <crux@altlinux.ru> 1.48-alt1
- 1.41 -> 1.48
- bootstrap for perl-5.16

* Tue Oct 25 2011 Alexey Tourbin <at@altlinux.ru> 1.41-alt1
- 1.39 -> 1.41
- re-enabled dependency on perl-DateTime

* Thu Oct 06 2011 Alexey Tourbin <at@altlinux.ru> 1.39-alt2
- bootstrap for perl-5.14

* Wed Oct 05 2011 Alexey Tourbin <at@altlinux.ru> 1.39-alt1
- 1.27 -> 1.39
- rebuild as plain src.rpm

* Fri Feb 04 2011 Alexey Tourbin <at@altlinux.ru> 1.27-alt1
- 1.26 -> 1.27

* Sat Dec 18 2010 Alexey Tourbin <at@altlinux.ru> 1.26-alt1
- 1.21 -> 1.26
- re-enabled dependency on perl-DateTime

* Mon Sep 20 2010 Alexey Tourbin <at@altlinux.ru> 1.21-alt1
- 1.18 -> 1.21
- disabled dependency on perl-DateTime, for bootsrap

* Tue May 04 2010 Alexey Tourbin <at@altlinux.ru> 1.18-alt1
- 1.15 -> 1.18

* Mon Mar 29 2010 Alexey Tourbin <at@altlinux.ru> 1.15-alt1
- 1.10 -> 1.15

* Tue Feb 16 2010 Alexey Tourbin <at@altlinux.ru> 1.10-alt1
- 0.99 -> 1.10

* Mon Oct 19 2009 Alexey Tourbin <at@altlinux.ru> 0.99-alt1
- 0.91 -> 0.99

* Thu Jul 02 2009 Alexey Tourbin <at@altlinux.ru> 0.91-alt1
- 0.90 -> 0.91

* Mon May 11 2009 Alexey Tourbin <at@altlinux.ru> 0.90-alt1
- 0.89 -> 0.90

* Sun Apr 19 2009 Alexey Tourbin <at@altlinux.ru> 0.89-alt1
- 0.86 -> 0.89

* Tue Mar 24 2009 Alexey Tourbin <at@altlinux.ru> 0.86-alt1
- 0.83 -> 0.86

* Thu Nov 06 2008 Alexey Tourbin <at@altlinux.ru> 0.83-alt1
- 0.79 -> 0.83

* Mon Aug 04 2008 Alexey Tourbin <at@altlinux.ru> 0.79-alt1
- 0.7701 -> 0.79

* Thu Jun 19 2008 Alexey Tourbin <at@altlinux.ru> 0.77-alt1
- 0.72 -> 0.7701

* Wed Mar 05 2008 Alexey Tourbin <at@altlinux.ru> 0.72-alt1
- 0.64 -> 0.72

* Tue Apr 10 2007 Alexey Tourbin <at@altlinux.ru> 0.64-alt1
- 0.48 -> 0.64

* Mon Sep 04 2006 Alexey Tourbin <at@altlinux.ru> 0.48-alt1
- 0.46 -> 0.48

* Thu Aug 10 2006 Alexey Tourbin <at@altlinux.ru> 0.46-alt1
- 0.44 -> 0.46

* Wed Apr 19 2006 Alexey Tourbin <at@altlinux.ru> 0.44-alt1
- 0.36 -> 0.44

* Sun Aug 21 2005 Alexey Tourbin <at@altlinux.ru> 0.36-alt1
- initial revision
