%define _unpackaged_files_terminate_build 1
%define module_name SQL-Interp
# BEGIN SourceDeps(oneline):
BuildRequires: perl(DBI.pm) perl(Module/Build.pm) perl(Scalar/Util.pm) perl(Sub/Exporter.pm) perl(Test/More.pm) perl(overload.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.27
Release: alt1
Summary: perl module %module_name
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://www.cpan.org/authors/id/Y/YO/YORHEL/%{module_name}-%{version}.tar.gz
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
%doc Changes README.md
%perl_vendor_privlib/S*
%perl_vendor_privlib/D*

%changelog
* Tue Feb 16 2021 Igor Vlasenko <viy@altlinux.ru> 1.27-alt1
- automated CPAN update

* Wed Apr 22 2020 Igor Vlasenko <viy@altlinux.ru> 1.26-alt1
- automated CPAN update

* Mon Oct 28 2019 Igor Vlasenko <viy@altlinux.ru> 1.25-alt1
- automated CPAN update

* Thu Mar 03 2016 Igor Vlasenko <viy@altlinux.ru> 1.24-alt1
- automated CPAN update

* Wed Feb 19 2014 Igor Vlasenko <viy@altlinux.ru> 1.22-alt2
- moved to Sisyphus for Slic3r (by dd@ request)

* Thu Sep 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.22-alt1
- regenerated from template by package builder

* Tue Sep 03 2013 Igor Vlasenko <viy@altlinux.ru> 1.02-alt1
- initial import by package builder

