%define module_version 1.02
%define module_name Log-Report-Optional
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(List/Util.pm) perl(String/Print.pm) perl(Test/More.pm) perl(base.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators
BuildRequires: perl-Encode-CN perl-Encode-JP perl-Encode-KR perl-Encode-TW

Name: perl-%module_name
Version: 1.02
Release: alt1
Summary: Log::Report in the lightest form
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source: http://www.cpan.org/authors/id/M/MA/MARKOV/Log-Report-Optional-%{version}.tar.gz
BuildArch: noarch

%description
%summary

%prep
%setup -n %{module_name}-%{module_version}
[ %version = 1.02 ] && rm t/21messages.t

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc ChangeLog README
%perl_vendor_privlib/L*

%changelog
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

