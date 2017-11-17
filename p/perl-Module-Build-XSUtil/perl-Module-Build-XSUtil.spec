%define _unpackaged_files_terminate_build 1
%define module_name Module-Build-XSUtil
# BEGIN SourceDeps(oneline):
BuildRequires: perl(CPAN/Meta.pm) perl(CPAN/Meta/Prereqs.pm) perl(Config.pm) perl(Devel/CheckCompiler.pm) perl(Devel/PPPort.pm) perl(Exporter.pm) perl(ExtUtils/CBuilder.pm) perl(File/Basename.pm) perl(File/Path.pm) perl(Module/Build.pm) perl(Test/More.pm) perl(XSLoader.pm) perl(parent.pm) perl(File/Copy/Recursive.pm) perl(Cwd/Guard.pm) perl(Capture/Tiny.pm) perl(Module/Build/Tiny.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.18
Release: alt1.1
Summary: A Module::Build class for building XS modules
Group: Development/Perl
License: perl
URL: https://github.com/hideo55/Module-Build-XSUtil

Source0: http://www.cpan.org/authors/id/H/HI/HIDEAKIO/%{module_name}-%{version}.tar.gz
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
%doc README.md LICENSE Changes
%perl_vendor_privlib/M*

%changelog
* Fri Nov 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.18-alt1.1
- automated CPAN update

* Wed Nov 08 2017 Igor Vlasenko <viy@altlinux.ru> 0.18-alt1
- automated CPAN update

* Wed Nov 01 2017 Igor Vlasenko <viy@altlinux.ru> 0.17-alt1
- automated CPAN update

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1
- automated CPAN update

* Fri May 22 2015 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1
- automated CPAN update

* Tue Aug 19 2014 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1
- automated CPAN update

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

