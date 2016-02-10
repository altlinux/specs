%define _unpackaged_files_terminate_build 1
%define module_version 0.14
%define module_name Dancer-Plugin-Database-Core
# BEGIN SourceDeps(oneline):
BuildRequires: perl(DBD/Sponge.pm) perl(DBI.pm) perl(ExtUtils/MakeMaker.pm) perl(Test/More.pm) perl(base.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.14
Release: alt1
Summary: Shared core for D1 and D2 Database plugins
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source: http://www.cpan.org/authors/id/A/AM/AMBS/Dancer-Plugin-Database-Core-%{version}.tar.gz
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
%doc Changes README
%perl_vendor_privlib/D*

%changelog
* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1
- automated CPAN update

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1
- automated CPAN update

* Fri May 22 2015 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1
- automated CPAN update

* Mon Oct 20 2014 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- automated CPAN update

* Tue Sep 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- automated CPAN update

* Wed Apr 02 2014 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- automated CPAN update

* Fri Jan 03 2014 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- automated CPAN update

* Wed Oct 16 2013 Igor Vlasenko <viy@altlinux.ru> 0.04-alt2
- build for Sisyphus (required for perl update)

* Fri Sep 06 2013 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- initial import by package builder

