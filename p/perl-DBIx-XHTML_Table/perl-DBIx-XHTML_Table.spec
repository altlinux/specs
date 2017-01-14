%define _unpackaged_files_terminate_build 1
%define module_name DBIx-XHTML_Table
# BEGIN SourceDeps(oneline):
BuildRequires: perl(DBD/CSV.pm) perl(DBI.pm) perl(ExtUtils/MakeMaker.pm) perl(FindBin.pm) perl(Test/More.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.49
Release: alt1
Summary: perl module %module_name
Group: Development/Perl
License: artistic_2
URL: https://github.com/jeffa/DBIx-XHTML_Table

Source0: http://www.cpan.org/authors/id/J/JE/JEFFA/%{module_name}-%{version}.tar.gz
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
%doc readme.md Changes
%perl_vendor_privlib/D*

%changelog
* Sat Jan 14 2017 Igor Vlasenko <viy@altlinux.ru> 1.49-alt1
- automated CPAN update

* Thu Mar 03 2016 Igor Vlasenko <viy@altlinux.ru> 1.48-alt1
- automated CPAN update

* Mon Jan 04 2016 Igor Vlasenko <viy@altlinux.ru> 1.47-alt1
- automated CPAN update

* Wed Oct 14 2015 Igor Vlasenko <viy@altlinux.ru> 1.46-alt1
- regenerated from template by package builder

* Tue Feb 18 2014 Igor Vlasenko <viy@altlinux.ru> 1.36-alt2
- moved to Sisyphus for Slic3r (by dd@ request)

* Fri Sep 06 2013 Igor Vlasenko <viy@altlinux.ru> 1.36-alt1
- initial import by package builder

