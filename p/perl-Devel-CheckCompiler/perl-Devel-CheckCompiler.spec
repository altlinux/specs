%define _unpackaged_files_terminate_build 1
# BEGIN SourceDeps(oneline):
BuildRequires: perl(CPAN/Meta.pm) perl(CPAN/Meta/Prereqs.pm) perl(Exporter.pm) perl(ExtUtils/CBuilder.pm) perl(File/Temp.pm) perl(Module/Build/Tiny.pm) perl(Test/More.pm) perl(Test/Requires.pm) perl(parent.pm)
# END SourceDeps(oneline)
%define module_version 0.07
%define module_name Devel-CheckCompiler
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.07
Release: alt1
Summary: Check the compiler's availability
Group: Development/Perl
License: perl
URL: https://github.com/tokuhirom/Devel-CheckCompiler

Source: http://www.cpan.org/authors/id/S/SY/SYOHEX/Devel-CheckCompiler-%{version}.tar.gz
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
%perl_vendor_privlib/D*

%changelog
* Sat Nov 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- automated CPAN update

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- automated CPAN update

* Thu Mar 06 2014 Igor Vlasenko <viy@altlinux.ru> 0.05-alt2
- moved to Sisyphus as perl update dependency

* Fri Dec 06 2013 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- regenerated from template by package builder

* Mon Oct 07 2013 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- regenerated from template by package builder

* Fri Sep 06 2013 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- initial import by package builder

