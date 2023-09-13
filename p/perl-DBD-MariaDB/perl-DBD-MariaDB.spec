%define _unpackaged_files_terminate_build 1
%define dist DBD-MariaDB
Name: perl-%dist
Version: 1.23
Release: alt1

Summary: MariaDB driver for DBI interface in Perl
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/P/PA/PALI/%{dist}-%{version}.tar.gz

BuildRequires: libmariadb-devel perl-DBI-devel perl-devel
BuildRequires: perl(Devel/CheckLib.pm) perl(Pod/Man.pm)
BuildRequires: perl(ExtUtils/MakeMaker.pm)

# Tests
#BuildRequires:  mariadb-server mariadb-client

# Required to process t/testrules.yml
#BuildRequires:  perl(CPAN/Meta/YAML.pm)
#BuildRequires:  perl(DBI/Const/GetInfoType.pm)
#BuildRequires:  perl(Encode.pm)
#BuildRequires:  perl(File/Path.pm)
#BuildRequires:  perl(File/Temp.pm)
#BuildRequires:  perl(FindBin.pm)
#BuildRequires:  perl(Test/Deep.pm)
#BuildRequires:  perl(Test/More.pm)
#BuildRequires:  perl(Time/HiRes.pm)
#BuildRequires:  perl(Net/SSLeay.pm)
#BuildRequires:  perl(Proc/ProcessTable.pm)
#BuildRequires:  perl(Storable.pm)

%description
DBD::mysql is an interface driver for connecting the DBMS independent
Perl-API DBI to the mysql DBMS.

%prep
%setup -q -n %{dist}-%{version}
bzip2 -k Changes
bzip2 -k Changes.historic

%build
%def_without test
%perl_vendor_build

%install
%perl_vendor_install

find %buildroot -type f -name '*.bs' -size 0 -delete
# should not be packaged
rm %buildroot%perl_vendor_archlib/DBD/MariaDB/INSTALL.pod

%files
%doc README* Changes Changes.historic
%perl_vendor_archlib/DBD/*
%perl_vendor_autolib/DBD/*

%changelog
* Wed Sep 13 2023 Igor Vlasenko <viy@altlinux.org> 1.23-alt1
- automated CPAN update

* Thu Aug 11 2022 Alexey Shabalin <shaba@altlinux.org> 1.22-alt1
- Initial package.
