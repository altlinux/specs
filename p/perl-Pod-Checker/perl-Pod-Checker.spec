# BEGIN SourceDeps(oneline):
BuildRequires: perl(Cwd.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(File/Basename.pm) perl(FileHandle.pm) perl(Pod/Simple.pm) perl(Pod/Simple/Methody.pm) perl(Test/More.pm) perl(base.pm)
# END SourceDeps(oneline)
%define module_name Pod-Checker
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.75
Release: alt1
Summary: Pod::Checker verifies POD documentation contents for compliance with the POD format specifications
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://www.cpan.org/authors/id/M/MA/MAREKR/%{module_name}-%{version}.tar.gz
BuildArch: noarch

%description
%summary

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build INSTALLMAN1DIR=%_man1dir

%install
%perl_vendor_install

%files
%doc README CHANGES
%perl_vendor_privlib/P*
%_bindir/*
%_man1dir/*

%changelog
* Mon May 23 2022 Igor Vlasenko <viy@altlinux.org> 1.75-alt1
- automated CPAN update

* Tue Oct 06 2020 Igor Vlasenko <viy@altlinux.ru> 1.74-alt1
- automated CPAN update

* Sun Jun 05 2016 Igor Vlasenko <viy@altlinux.ru> 1.73-alt1
- automated CPAN update

* Thu May 26 2016 Igor Vlasenko <viy@altlinux.ru> 1.72-alt1
- automated CPAN update

* Mon Jun 23 2014 Igor Vlasenko <viy@altlinux.ru> 1.71-alt1
- automated CPAN update

* Sun Oct 27 2013 Igor Vlasenko <viy@altlinux.ru> 1.70-alt1
- Sisyphus build

