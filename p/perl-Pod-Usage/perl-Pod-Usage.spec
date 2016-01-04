%define _unpackaged_files_terminate_build 1
%def_without bootstrap
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Config.pm) perl(Cwd.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(File/Basename.pm) perl(File/Spec.pm) perl(FileHandle.pm) perl(Pod/PlainText.pm) perl(Pod/Text.pm) perl(Test/More.pm)
# END SourceDeps(oneline)
%define module_version 1.68
%define module_name Pod-Usage
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.68
Release: alt1
Summary: Pod::Usage extracts POD documentation and shows usage information
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source: http://www.cpan.org/authors/id/M/MA/MAREKR/Pod-Usage-%{version}.tar.gz
BuildArch: noarch
Conflicts: perl-Pod-Parser < 1.60
%if_without bootstrap
# circular deps, see #31371
Requires: perl-podlators
%endif

%description
%summary

%prep
%setup -n %module_name-%module_version

%build
%perl_vendor_build INSTALLMAN1DIR=%_man1dir

%install
%perl_vendor_install

%files
%doc CHANGES README
%perl_vendor_privlib/P*
%_bindir/*
%_man1dir/*

%changelog
* Mon Jan 04 2016 Igor Vlasenko <viy@altlinux.ru> 1.68-alt1
- automated CPAN update

* Sat Oct 17 2015 Igor Vlasenko <viy@altlinux.ru> 1.67-alt2
- added circular dep (see #31371) on perl-podlators

* Wed Apr 01 2015 Igor Vlasenko <viy@altlinux.ru> 1.67-alt1
- automated CPAN update

* Fri Nov 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.64-alt2
- added explicit Conflict to perl-Pod-Parser < 1.60 (closes: #30470)

* Tue Jul 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.64-alt1
- automated CPAN update

* Sun Oct 27 2013 Igor Vlasenko <viy@altlinux.ru> 1.63-alt1
- Sisyphus build

