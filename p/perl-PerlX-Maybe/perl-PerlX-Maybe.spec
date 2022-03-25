%define _unpackaged_files_terminate_build 1
%define module_name PerlX-Maybe
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(Test/More.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.202
Release: alt1
Summary: return a pair only if they are both defined
Group: Development/Perl
License: perl
URL: https://metacpan.org/release/PerlX-Maybe

Source0: http://www.cpan.org/authors/id/T/TO/TOBYINK/%{module_name}-%{version}.tar.gz
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
%doc README COPYRIGHT Changes CREDITS
%perl_vendor_privlib/S*
%perl_vendor_privlib/P*

%changelog
* Fri Mar 25 2022 Igor Vlasenko <viy@altlinux.org> 1.202-alt1
- automated CPAN update

* Fri Dec 07 2018 Igor Vlasenko <viy@altlinux.ru> 1.201-alt1
- automated CPAN update

* Wed Oct 24 2018 Igor Vlasenko <viy@altlinux.ru> 1.200-alt1
- automated CPAN update

* Sun Mar 11 2018 Igor Vlasenko <viy@altlinux.ru> 1.001-alt2
- to Sisyphus as perl-Dancer-Session-Cookie dep

* Wed Oct 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.001-alt1
- regenerated from template by package builder

* Wed Sep 04 2013 Igor Vlasenko <viy@altlinux.ru> 1.000-alt1
- initial import by package builder

