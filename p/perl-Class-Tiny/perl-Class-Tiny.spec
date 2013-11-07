%define _unpackaged_files_terminate_build 1
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(File/Spec/Functions.pm) perl(IO/Handle.pm) perl(IPC/Open3.pm) perl(List/Util.pm) perl(Test/FailWarnings.pm) perl(Test/More.pm) perl(base.pm) perl(subs.pm)
# END SourceDeps(oneline)
%define module_version 0.012
%define module_name Class-Tiny
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.012
Release: alt1
Summary: Minimalist class construction
Group: Development/Perl
License: apache
URL: https://github.com/dagolden/Class-Tiny

Source: http://www.cpan.org/authors/id/D/DA/DAGOLDEN/Class-Tiny-%{version}.tar.gz
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
%doc LICENSE README Changes
%perl_vendor_privlib/C*

%changelog
* Wed Nov 06 2013 Igor Vlasenko <viy@altlinux.ru> 0.012-alt1
- automated CPAN update

* Sat Sep 28 2013 Igor Vlasenko <viy@altlinux.ru> 0.011-alt1
- automated CPAN update

* Tue Sep 24 2013 Igor Vlasenko <viy@altlinux.ru> 0.010-alt1
- regenerated from template by package builder

* Tue Sep 17 2013 Igor Vlasenko <viy@altlinux.ru> 0.008-alt1
- initial import by package builder

