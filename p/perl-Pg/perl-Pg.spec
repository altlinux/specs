Name: perl-Pg
Version: 2.1.1
Release: alt2.1

Summary: PostgreSQL database native Perl driver
License: GPL or Artistic
Group: Development/Perl

URL: http://gborg.postgresql.org/project/pgperl/
Source: Pg-%version.tar.bz2

# Automatically added by buildreq on Wed Oct 19 2011
BuildRequires: perl-devel postgresql-devel

%description
PostgreSQL database native Perl driver

%prep
%setup -q -n Pg-%version

# requires db connection
%def_without test

%build
POSTGRES_INCLUDE=`pg_config --includedir`
POSTGRES_LIB=`pg_config --libdir`
export POSTGRES_INCLUDE POSTGRES_LIB
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/Pg*
%perl_vendor_autolib/Pg

%changelog
* Wed Oct 19 2011 Alexey Tourbin <at@altlinux.ru> 2.1.1-alt2.1
- rebuilt for perl-5.14

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 2.1.1-alt2.0.1
- rebuilt with perl 5.12

* Fri Mar 30 2007 ALT QA Team Robot <qa-robot@altlinux.org> 2.1.1-alt2.0
- Fixed postgresql build dependencies.
- Rebuilt due to libpq.so.4 -> libpq.so.5 soname change.

* Thu Dec 08 2005 Konstantin Timoshenko <kt@altlinux.ru> 2.1.1-alt2
- fix build requires

* Fri Jun 24 2005 Konstantin Timoshenko <kt@altlinux.ru> 2.1.1-alt1
- 2.1.1

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 2.0.2-alt2.1
- Rebuilt with rpm-build-perl-0.5.1.

* Fri Sep 26 2003 Konstantin Timoshenko <kt@altlinux.ru> 2.0.2-alt2
- fix build requires.

* Wed Dec 18 2002 Konstantin Timoshenko <kt@altlinux.ru> 2.0.2-alt1
- First AltLinux release
