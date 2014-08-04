%define _unpackaged_files_terminate_build 1
%define module_version 0.13
%define module_name Module-Build-XSUtil
# BEGIN SourceDeps(oneline):
BuildRequires: perl(CPAN/Meta.pm) perl(CPAN/Meta/Prereqs.pm) perl(Config.pm) perl(Devel/CheckCompiler.pm) perl(Devel/PPPort.pm) perl(Exporter.pm) perl(ExtUtils/CBuilder.pm) perl(File/Basename.pm) perl(File/Path.pm) perl(Module/Build.pm) perl(Test/More.pm) perl(XSLoader.pm) perl(parent.pm) perl(File/Copy/Recursive.pm) perl(Cwd/Guard.pm) perl(Capture/Tiny.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.13
Release: alt1
Summary: A Module::Build class for building XS modules
Group: Development/Perl
License: perl
URL: https://github.com/hideo55/Module-Build-XSUtil

Source: http://www.cpan.org/authors/id/H/HI/HIDEAKIO/Module-Build-XSUtil-%{version}.tar.gz
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
%doc README.md LICENSE Changes
%perl_vendor_privlib/M*

%changelog
* Mon Aug 04 2014 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1
- automated CPAN update

* Mon May 19 2014 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1
- automated CPAN update

* Fri May 02 2014 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1
- automated CPAN update

* Thu Mar 06 2014 Igor Vlasenko <viy@altlinux.ru> 0.06-alt2
- moved to Sisyphus as perl update dependency

* Tue Jan 14 2014 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- regenerated from template by package builder

* Tue Nov 26 2013 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- regenerated from template by package builder

* Mon Sep 09 2013 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- initial import by package builder

