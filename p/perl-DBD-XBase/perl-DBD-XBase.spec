%define _unpackaged_files_terminate_build 1
%define dist DBD-XBase
Name: perl-%dist
Version: 1.08
Release: alt1

Summary: XBase driver for DBI interface in Perl
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/J/JA/JANPAZ/%{dist}-%{version}.tar.gz

# Automatically added by buildreq on Wed Mar 05 2008
BuildRequires: perl-DBI perl-DBM perl-devel

# automatically added during perl 5.8 -> 5.12 upgrade.
# perl-podlators is required for pod2man conversion.
BuildRequires: perl-podlators

%description
Module XBase provides access to XBase (dBase, Fox*) dbf files.
It also handles memo files (dbt, fpt) and to certain extend
index files (ndx, ntx, mdx, idx and cdx). The DBD::XBase is
a database driver for DBI and provides simple SQL interface for
reading and writing the database files. So this package offers
two ways of accessing your beloved data in dbf files: XBase.pm
and DBD::XBase. I recommend using DBD::XBase and only resort
to XBase.pm if you need something special which is not
supported by the DBI interface.

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build INSTALLMAN1DIR=%_man1dir

%install
%perl_vendor_install

%files
%doc	Changes MANIFEST README ToDo
%dir	%perl_vendor_privlib/DBD
	%perl_vendor_privlib/DBD/XBase.pm
	%perl_vendor_privlib/XBase.pm
%dir	%perl_vendor_privlib/XBase
	%perl_vendor_privlib/XBase/*
%dir	%perl_vendor_autolib/XBase
	%_man1dir/*
	%_bindir/*

%changelog
* Thu Jan 19 2017 Igor Vlasenko <viy@altlinux.ru> 1.08-alt1
- automated CPAN update

* Thu May 26 2016 Igor Vlasenko <viy@altlinux.ru> 1.07-alt1
- automated CPAN update

* Sat Mar 19 2016 Igor Vlasenko <viy@altlinux.ru> 1.06-alt1
- automated CPAN update

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 1.05-alt1
- automated CPAN update

* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 1.03-alt1
- automated CPAN update

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.241-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Wed Mar 05 2008 Serhii Hlodin <hlodin@altlinux.ru> 0.241-alt1
- Initial build module from CPAN
