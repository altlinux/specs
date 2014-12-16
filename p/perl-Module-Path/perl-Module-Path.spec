%define _unpackaged_files_terminate_build 1
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Devel/FindPerl.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(File/Spec/Functions.pm) perl(FindBin.pm) perl(Test/More.pm)
# END SourceDeps(oneline)
%define module_version 0.16
%define module_name Module-Path
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.16
Release: alt1
Summary: get the full path to a locally installed module
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source: http://www.cpan.org/authors/id/N/NE/NEILB/Module-Path-%{version}.tar.gz
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
%setup -n %module_name-%module_version

%build
%perl_vendor_build INSTALLMAN1DIR=%_man1dir

%install
%perl_vendor_install

%files
%doc LICENSE Changes README
%perl_vendor_privlib/M*

%files scripts
%_bindir/*
%_man1dir/*

%changelog
* Tue Dec 16 2014 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1
- automated CPAN update

* Mon Oct 20 2014 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1
- automated CPAN update

* Tue Aug 19 2014 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1
- automated CPAN update

* Mon Feb 24 2014 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1
- automated CPAN update

* Thu Feb 20 2014 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1
- automated CPAN update

* Wed Feb 05 2014 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1
- automated CPAN update

* Tue Oct 01 2013 Igor Vlasenko <viy@altlinux.ru> 0.09-alt2
- regenerated from template by package builder

* Mon Sep 09 2013 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1
- initial import by package builder

