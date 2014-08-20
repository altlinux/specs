# BEGIN SourceDeps(oneline):
BuildRequires: perl(Config.pm) perl(ExtUtils/MakeMaker.pm) perl(Module/Build.pm) perl(Test/More.pm) perl(parent.pm)
# END SourceDeps(oneline)
%define module_version 0.02
%define module_name Devel-CheckBin
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.02
Release: alt2
Summary: check that a command is available
Group: Development/Perl
License: perl
URL: https://github.com/tokuhirom/Devel-CheckBin

Source0: http://cpan.org.ua/authors/id/T/TO/TOKUHIROM/%module_name-%module_version.tar.gz
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
* Wed Aug 20 2014 Igor Vlasenko <viy@altlinux.ru> 0.02-alt2
- moved to Sysiphus as dependency

* Fri Sep 06 2013 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- initial import by package builder

