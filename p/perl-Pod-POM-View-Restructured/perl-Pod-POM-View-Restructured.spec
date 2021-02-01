%define _unpackaged_files_terminate_build 1
%define module_name Pod-POM-View-Restructured
# BEGIN SourceDeps(oneline):
BuildRequires: perl(ExtUtils/MakeMaker.pm) perl(Pod/POM.pm) perl(base.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.000003
Release: alt1
Summary: View for Pod::POM that outputs reStructuredText
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://www.cpan.org/authors/id/A/AL/ALEXM/%{module_name}-%{version}.tar.gz
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
%doc ChangeLog README
%perl_vendor_privlib/P*

%files scripts
%_man1dir/*
%_bindir/*

%changelog
* Mon Feb 01 2021 Igor Vlasenko <viy@altlinux.ru> 1.000003-alt1
- automated CPAN update

* Fri Dec 07 2018 Igor Vlasenko <viy@altlinux.ru> 1.000002-alt1
- automated CPAN update

* Mon Apr 09 2018 Igor Vlasenko <viy@altlinux.ru> 1.000001-alt1
- automated CPAN update

* Fri May 12 2017 Igor Vlasenko <viy@altlinux.ru> 0.03-alt2
- to Sisyphus

* Tue Feb 14 2017 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- regenerated from template by package builder

* Wed Sep 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- initial import by package builder

