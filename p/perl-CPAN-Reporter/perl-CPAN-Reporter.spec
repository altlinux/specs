%define _unpackaged_files_terminate_build 1
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Module/Build.pm) perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define upstream_name    CPAN-Reporter
%define upstream_version 1.2018

Name:       perl-%{upstream_name}
Version:    1.2019
Release:    alt1

Summary:    Adds CPAN Testers reporting to CPAN.pm
License:    Apache License
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/authors/id/G/GA/GARU/%{upstream_name}-%{version}.tar.gz

BuildRequires: perl(Archive/Tar.pm)
BuildRequires: perl(CPAN.pm)
BuildRequires: perl(CPAN/Version.pm)
BuildRequires: perl(Capture/Tiny.pm)
BuildRequires: perl(Carp.pm)
BuildRequires: perl(Config/Tiny.pm)
BuildRequires: perl(Data/Dumper.pm)
BuildRequires: perl(Devel/Autoflush.pm)
BuildRequires: perl(Exporter.pm)
BuildRequires: perl(ExtUtils/MakeMaker.pm)
BuildRequires: perl(Fcntl.pm)
BuildRequires: perl(File/Basename.pm)
BuildRequires: perl(File/Copy/Recursive.pm)
BuildRequires: perl(File/Find.pm)
BuildRequires: perl(File/Glob.pm)
BuildRequires: perl(File/HomeDir.pm)
BuildRequires: perl(File/Path.pm)
BuildRequires: perl(File/Spec.pm)
BuildRequires: perl(File/Spec/Functions.pm)
BuildRequires: perl(File/Temp.pm)
BuildRequires: perl(File/pushd.pm)
BuildRequires: perl(IO/CaptureOutput.pm)
BuildRequires: perl(IO/File.pm)
BuildRequires: perl(IPC/Cmd.pm)
BuildRequires: perl(List/Util.pm)
BuildRequires: perl(Parse/CPAN/Meta.pm)
BuildRequires: perl(Probe/Perl.pm)
BuildRequires: perl(Test/Harness.pm)
BuildRequires: perl(Test/More.pm)
BuildRequires: perl(Test/Reporter.pm)
BuildRequires: perl(constant.pm)
BuildRequires: perl(strict.pm)
BuildRequires: perl(vars.pm)
BuildRequires: perl(version.pm)
BuildRequires: perl(warnings.pm)
BuildArch:  noarch
Source44: import.info

%description
The CPAN Testers project captures and analyses detailed results from
building and testing CPAN distributions on multiple operating systems and
multiple versions of Perl. This provides valuable feedback to module
authors and potential users to identify bugs or platform compatibility
issues and improves the overall quality and value of CPAN.

One way individuals can contribute is to send a report for each module that
they test or install. CPAN::Reporter is an add-on for the CPAN.pm module to
send the results of building and testing modules to the CPAN Testers
project. Full support for CPAN::Reporter is available in CPAN.pm as of
version 1.92.

%prep
%setup -q -n %{upstream_name}-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test

%install
%makeinstall_std

%files
%doc Changes META.json META.yml README examples Todo
%{perl_vendor_privlib}/*


%changelog
* Sun May 21 2023 Igor Vlasenko <viy@altlinux.org> 1.2019-alt1
- automated CPAN update

* Wed Mar 13 2019 Igor Vlasenko <viy@altlinux.ru> 1.2018-alt2_3
- to Sisyphus as perl-CPAN dep

* Thu Oct 04 2018 Igor Vlasenko <viy@altlinux.ru> 1.2018-alt1_3
- update by mgaimport

* Fri Oct 13 2017 Igor Vlasenko <viy@altlinux.ru> 1.2018-alt1_2
- update by mgaimport

* Mon Sep 25 2017 Igor Vlasenko <viy@altlinux.ru> 1.2018-alt1_1
- update by mgaimport

* Wed Jul 27 2016 Igor Vlasenko <viy@altlinux.ru> 1.2015-alt1_3
- update by mgaimport

* Sun Feb 21 2016 Igor Vlasenko <viy@altlinux.ru> 1.2015-alt1_2
- update by mgaimport

* Tue Oct 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.2015-alt1_1
- update by mgaimport

* Fri Dec 19 2014 Igor Vlasenko <viy@altlinux.ru> 1.2011-alt2_5
- update by mgaimport

* Tue Oct 07 2014 Igor Vlasenko <viy@altlinux.ru> 1.2011-alt2_4
- update by mgaimport

* Tue Sep 02 2014 Cronbuild Service <cronbuild@altlinux.org> 1.2011-alt2_1
- rebuild to get rid of unmets

* Tue Apr 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.2011-alt1_1
- update by mgaimport

* Mon Oct 21 2013 Igor Vlasenko <viy@altlinux.ru> 1.2010-alt2_2
- mga update

* Fri Sep 13 2013 Cronbuild Service <cronbuild@altlinux.org> 1.2010-alt2_1
- rebuild to get rid of unmets

* Wed Aug 07 2013 Igor Vlasenko <viy@altlinux.ru> 1.2010-alt1_1
- mgaimport update

* Thu Jul 25 2013 Igor Vlasenko <viy@altlinux.ru> 1.2006-alt1_1
- converted for ALT Linux by srpmconvert tools

