%define module_version 1.22
%define module_name SQL-Interp
# BEGIN SourceDeps(oneline):
BuildRequires: perl(DBI.pm) perl(Module/Build.pm) perl(Scalar/Util.pm) perl(Sub/Exporter.pm) perl(Test/More.pm) perl(overload.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.22
Release: alt2
Summary: perl module %module_name
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/M/MA/MARKSTOS/%module_name-%module_version.tar.gz
BuildArch: noarch

%description
%summary

%prep
%setup -n %module_name-%module_version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/S*
%perl_vendor_privlib/D*

%changelog
* Wed Feb 19 2014 Igor Vlasenko <viy@altlinux.ru> 1.22-alt2
- moved to Sisyphus for Slic3r (by dd@ request)

* Thu Sep 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.22-alt1
- regenerated from template by package builder

* Tue Sep 03 2013 Igor Vlasenko <viy@altlinux.ru> 1.02-alt1
- initial import by package builder

