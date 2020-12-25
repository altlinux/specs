%define _unpackaged_files_terminate_build 1
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Any/Moose.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(FindBin.pm) perl(Moose.pm) perl(Test/More.pm) perl(Moo.pm)
# END SourceDeps(oneline)
%define module_name Date-HolidayParser
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.43
Release: alt1
Summary: Parser for .holiday-files
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://www.cpan.org/authors/id/Z/ZE/ZERODOGG/%{module_name}-%{version}.tar.gz
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
%doc README Changes COPYING.gpl COPYING.artistic
%perl_vendor_privlib/D*

%changelog
* Fri Dec 25 2020 Igor Vlasenko <viy@altlinux.ru> 0.43-alt1
- automated CPAN update

* Wed Apr 02 2014 Igor Vlasenko <viy@altlinux.ru> 0.41-alt2
- moved as dayplanner dependency

* Thu Sep 19 2013 Igor Vlasenko <viy@altlinux.ru> 0.41-alt1
- initial import by package builder

