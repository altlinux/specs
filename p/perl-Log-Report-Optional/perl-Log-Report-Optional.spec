%define _unpackaged_files_terminate_build 1
%define module_name Log-Report-Optional
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(List/Util.pm) perl(String/Print.pm) perl(Test/More.pm) perl(base.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators
BuildRequires: perl-Encode-CN perl-Encode-JP perl-Encode-KR perl-Encode-TW

Name: perl-%module_name
Version: 1.04
Release: alt1
Summary: Log::Report in the lightest form
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://www.cpan.org/authors/id/M/MA/MARKOV/%{module_name}-%{version}.tar.gz
BuildArch: noarch

%description
%summary

%prep
%setup -q -n %{module_name}-%{version}
[ %version = 1.04 ] && rm t/21messages.t

%build
export NPROCS=1
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc ChangeLog README
%perl_vendor_privlib/L*

%changelog
* Wed Dec 20 2017 Igor Vlasenko <viy@altlinux.ru> 1.04-alt1
- automated CPAN update

* Wed Apr 20 2016 Igor Vlasenko <viy@altlinux.ru> 1.02-alt1
- automated CPAN update

* Mon Jun 23 2014 Igor Vlasenko <viy@altlinux.ru> 1.01-alt2
- finished bootstrap perl-Log-Report update
- re-enabled test

* Mon Jun 23 2014 Igor Vlasenko <viy@altlinux.ru> 1.01-alt1
- regenerated from template by package builder

* Mon Jun 23 2014 Igor Vlasenko <viy@altlinux.ru> 1.00-alt2
- moved to Sisyphus

* Fri Mar 07 2014 Igor Vlasenko <viy@altlinux.ru> 1.00-alt1
- initial import by package builder

