%define module_name Data-Integer
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Carp.pm) perl(Exporter.pm) perl(Module/Build.pm) perl(Test/More.pm) perl(constant.pm) perl(integer.pm) perl(parent.pm) perl(strict.pm) perl(warnings.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.007
Release: alt1
Summary: details of the native integer data type
Group: Development/Perl
License: Perl
Url: %CPAN %module_name

Source0: http://www.cpan.org/authors/id/R/RR/RRWO/%{module_name}-%{version}.tar.gz
BuildArch: noarch

%description
%summary

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README SECURITY.md
%perl_vendor_privlib/D*

%changelog
* Thu Apr 17 2025 Igor Vlasenko <viy@altlinux.org> 0.007-alt1
- automated CPAN update

* Wed Aug 05 2020 Andrew A. Vasilyev <andy@altlinux.org> 0.006-alt2
- import for Sisyphus

* Thu Aug 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.006-alt1
- regenerated from template by package builder

* Thu Apr 02 2015 Igor Vlasenko <viy@altlinux.ru> 0.005-alt1
- regenerated from template by package builder

* Fri Sep 06 2013 Igor Vlasenko <viy@altlinux.ru> 0.004-alt1
- initial import by package builder

