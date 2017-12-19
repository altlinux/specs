%define _unpackaged_files_terminate_build 1
%define module_name File-Slurper
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Benchmark.pm) perl(Carp.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(File/Slurp.pm) perl(File/Spec/Functions.pm) perl(File/Temp.pm) perl(Test/More.pm) perl(Unicode/UTF8.pm) perl(constant.pm) perl(strict.pm) perl(warnings.pm) perl(Test/Warnings.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.011
Release: alt1
Summary: A simple, sane and efficient file slurper
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://www.cpan.org/authors/id/L/LE/LEONT/%{module_name}-%{version}.tar.gz
BuildArch: noarch

%description
From summary: %summary

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README LICENSE
%perl_vendor_privlib/F*

%changelog
* Tue Dec 19 2017 Igor Vlasenko <viy@altlinux.ru> 0.011-alt1
- automated CPAN update

* Tue Sep 26 2017 Igor Vlasenko <viy@altlinux.ru> 0.010-alt1
- automated CPAN update

* Tue Sep 20 2016 Igor Vlasenko <viy@altlinux.ru> 0.009-alt1
- automated CPAN update

* Wed Oct 14 2015 Igor Vlasenko <viy@altlinux.ru> 0.008-alt1
- regenerated from template by package builder

* Tue Feb 10 2015 Igor Vlasenko <viy@altlinux.ru> 0.004-alt1
- regenerated from template by package builder

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.002-alt1
- initial import by package builder

