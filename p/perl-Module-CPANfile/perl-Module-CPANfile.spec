%define _unpackaged_files_terminate_build 1
# BEGIN SourceDeps(oneline):
BuildRequires: perl(CPAN/Meta.pm) perl(CPAN/Meta/Prereqs.pm) perl(ExtUtils/MakeMaker.pm) perl(Test/More.pm) perl(File/pushd.pm)
# END SourceDeps(oneline)
%define module_name Module-CPANfile
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.1004
Release: alt1
Summary: Parse cpanfile
Group: Development/Perl
License: perl
URL: https://github.com/miyagawa/cpanfile

Source0: http://www.cpan.org/authors/id/M/MI/MIYAGAWA/%{module_name}-%{version}.tar.gz
BuildArch: noarch

%description
%summary

%package scripts
Summary: %module_name scripts
Group: Development/Perl
Requires: %{?epoch:%epoch:}%name = %version-%release

%description scripts
scripts for %module_name

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build INSTALLMAN1DIR=%_man1dir

%install
%perl_vendor_install

%files
%doc Changes LICENSE README
%perl_vendor_privlib/M*
%perl_vendor_privlib/c*

%files scripts
%_bindir/*
%_man1dir/*

%changelog
* Wed May 02 2018 Igor Vlasenko <viy@altlinux.ru> 1.1004-alt1
- automated CPAN update

* Wed Apr 25 2018 Igor Vlasenko <viy@altlinux.ru> 1.1003-alt1
- automated CPAN update

* Thu Mar 03 2016 Igor Vlasenko <viy@altlinux.ru> 1.1002-alt1
- automated CPAN update

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 1.1001-alt1
- automated CPAN update

* Mon Sep 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.1000-alt1
- automated CPAN update

* Thu Oct 17 2013 Igor Vlasenko <viy@altlinux.ru> 1.0002-alt1
- initial import by package builder

