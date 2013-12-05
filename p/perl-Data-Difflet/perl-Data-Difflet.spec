%define _unpackaged_files_terminate_build 1
%define module_version 0.10
%define module_name Data-Difflet
# BEGIN SourceDeps(oneline):
BuildRequires: perl(CPAN/Meta.pm) perl(CPAN/Meta/Prereqs.pm) perl(Module/Build.pm) perl(Term/ANSIColor.pm) perl(Test/Deep.pm) perl(Test/More.pm) perl(autodie.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.10
Release: alt1
Summary: Ultra special pretty cute diff generator Mark II
Group: Development/Perl
License: perl
URL: https://github.com/tokuhirom/Data-Difflet

Source: http://www.cpan.org/authors/id/T/TO/TOKUHIROM/Data-Difflet-%{version}.tar.gz
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
%doc README.md Changes LICENSE
%perl_vendor_privlib/T*
%perl_vendor_privlib/D*

%changelog
* Thu Dec 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1
- automated CPAN update

* Sun Oct 06 2013 Igor Vlasenko <viy@altlinux.ru> 0.09-alt2
- regenerated from template by package builder

* Fri Sep 06 2013 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1
- initial import by package builder

