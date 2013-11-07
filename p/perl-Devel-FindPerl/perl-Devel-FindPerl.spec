# BEGIN SourceDeps(oneline):
BuildRequires: perl(Capture/Tiny.pm) perl(Config.pm) perl(Exporter.pm) perl(ExtUtils/Config.pm) perl(ExtUtils/MakeMaker.pm) perl(File/Spec/Functions.pm) perl(IPC/Open2.pm) perl(Test/More.pm)
# END SourceDeps(oneline)
%define module_version 0.008
%define module_name Devel-FindPerl
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.008
Release: alt1
Summary: Find the path to your perl
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source: http://www.cpan.org/authors/id/L/LE/LEONT/Devel-FindPerl-%{version}.tar.gz
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
%doc README LICENSE Changes
%perl_vendor_privlib/D*

%changelog
* Wed Nov 06 2013 Igor Vlasenko <viy@altlinux.ru> 0.008-alt1
- automated CPAN update

* Fri Oct 25 2013 Igor Vlasenko <viy@altlinux.ru> 0.007-alt1
- automated CPAN update

* Tue Oct 01 2013 Igor Vlasenko <viy@altlinux.ru> 0.006-alt2
- regenerated from template by package builder

* Fri Sep 06 2013 Igor Vlasenko <viy@altlinux.ru> 0.006-alt1
- initial import by package builder

