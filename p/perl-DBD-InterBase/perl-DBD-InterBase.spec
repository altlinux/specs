%define dist DBD-InterBase
Name: perl-%dist
Version: 0.48
Release: alt3

Summary: DBI driver for Firebird and InterBase RDBMS server
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

Patch0: perl-DBD-InterBase-0.48-alt-test.patch
Patch1: perl-DBD-InterBase-0.48-alt-dbdimp.patch

# Automatically added by buildreq on Tue Oct 18 2011
BuildRequires: firebird-devel firebird-utils-classic perl-DBI-devel perl-devel

%description
DBD::InterBase is a Perl module which works with the DBI module to provide
access to Firebird and InterBase databases.

%prep
%setup -n %dist-%version
%patch0
%patch1 -p1
sed -i- 's@/usr/lib\>@%_libdir@' Makefile.PL

# do not override default CCFLAGS
sed -i '/CCFLAGS/d' Makefile.PL

# requires interbase installation
%def_without test

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_archlib/DBD
%perl_vendor_autolib/DBD

%changelog
* Tue Oct 18 2011 Alexey Tourbin <at@altlinux.ru> 0.48-alt3
- rebuilt for perl-5.14

* Wed Aug 10 2011 Andrey V. Stroganov <dja@altlinux.org> 0.48-alt2
- fixed x86_64 build; patch by Vladimir Lettiev <crux@altlinux.ru>

* Fri Jul 22 2011 Andrey V. Stroganov <dja@altlinux.org> 0.48-alt1
- initial build for ALT Linux Sisyphus
