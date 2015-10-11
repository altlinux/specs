%define _unpackaged_files_terminate_build 1
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Config.pm) perl(ExtUtils/MakeMaker.pm) perl(Module/Build.pm) perl(Test/More.pm) perl(parent.pm)
# END SourceDeps(oneline)
%define module_version 0.04
%define module_name Devel-CheckBin
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.04
Release: alt1
Summary: check that a command is available
Group: Development/Perl
License: perl
URL: https://github.com/tokuhirom/Devel-CheckBin

Source: http://www.cpan.org/authors/id/T/TO/TOKUHIROM/Devel-CheckBin-%{version}.tar.gz
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
%doc LICENSE README.md Changes
%perl_vendor_privlib/D*

%changelog
* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- automated CPAN update

* Fri May 22 2015 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- automated CPAN update

* Wed Aug 20 2014 Igor Vlasenko <viy@altlinux.ru> 0.02-alt2
- moved to Sysiphus as dependency

* Fri Sep 06 2013 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- initial import by package builder

