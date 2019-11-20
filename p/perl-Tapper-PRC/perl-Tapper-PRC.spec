# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Test/EOL.pm) perl(Test/Pod.pm) perl-podlators
# END SourceDeps(oneline)
BuildRequires: perl(File/Slurp.pm)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define upstream_name    Tapper-PRC
%define upstream_version 5.0.4

%{?perl_default_filter}

Name:       perl-%{upstream_name}
Version:    %{upstream_version}
Release:    alt1_1

Summary:    Control running test programs
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://metacpan.org/release/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Tapper/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Cwd.pm)
BuildRequires: perl(Data/Dumper.pm)
BuildRequires: perl(English.pm)
BuildRequires: perl(ExtUtils/MakeMaker.pm)
BuildRequires: perl(File/Basename.pm)
BuildRequires: perl(File/Copy.pm)
BuildRequires: perl(File/Temp.pm)
BuildRequires: perl(IO/Handle.pm)
BuildRequires: perl(IO/Socket/INET.pm)
BuildRequires: perl(IPC/Open3.pm)
BuildRequires: perl(IPC/Run.pm)
BuildRequires: perl(Log/Log4perl.pm)
BuildRequires: perl(Minion.pm)
BuildRequires: perl(Moose.pm)
BuildRequires: perl(MooseX/Log/Log4perl.pm)
BuildRequires: perl(Proc/Killfam.pm)
BuildRequires: perl(Proc/ProcessTable.pm)
BuildRequires: perl(Sys/Hostname.pm)
BuildRequires: perl(Tapper/Base.pm)
BuildRequires: perl(Tapper/Config.pm)
BuildRequires: perl(Tapper/Installer/Base.pm)
BuildRequires: perl(Tapper/Remote/Config.pm)
BuildRequires: perl(Tapper/Remote/Net.pm)
BuildRequires: perl(Test/Deep.pm)
BuildRequires: perl(Test/MockModule.pm)
BuildRequires: perl(Test/More.pm)
BuildRequires: perl(Try/Tiny.pm)
BuildRequires: perl(URI/Escape.pm)
BuildRequires: perl(YAML.pm)
BuildRequires: perl(YAML/Syck.pm)
BuildRequires: perl(constant.pm)
BuildRequires: perl(strict.pm)
BuildRequires: perl(warnings.pm)
BuildArch:  noarch
Source44: import.info

%description
Tapper - Program run control for test program automation.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor

%make_build

%check
%__make test

%install
%makeinstall_std

%files
%doc Changes LICENSE META.json META.yml  README
%{_mandir}/man1/*
%{perl_vendor_privlib}/*
%{_bindir}/tapper-automatic-test.pl
%{_bindir}/tapper-client
%{_bindir}/tapper-client-no-fork
%{_bindir}/tapper-minion-worker

%changelog
* Wed Nov 20 2019 Igor Vlasenko <viy@altlinux.ru> 5.0.4-alt1_1
- update by mgaimport

* Thu Nov 07 2019 Igor Vlasenko <viy@altlinux.ru> 5.0.4-alt1
- automated CPAN update

* Tue Oct 30 2018 Igor Vlasenko <viy@altlinux.ru> 5.0.3-alt1_1
- update by mgaimport

* Thu Sep 20 2018 Igor Vlasenko <viy@altlinux.ru> 5.0.3-alt1
- automated CPAN update

* Sat Feb 03 2018 Igor Vlasenko <viy@altlinux.ru> 5.0.2-alt1_1
- update by mgaimport

* Thu Nov 17 2016 Igor Vlasenko <viy@altlinux.ru> 5.0.2-alt1
- automated CPAN update

* Thu Apr 07 2016 Igor Vlasenko <viy@altlinux.ru> 5.0.1-alt1
- automated CPAN update

* Mon Mar 21 2016 Igor Vlasenko <viy@altlinux.ru> 5.0.0-alt1
- automated CPAN update

* Wed Feb 17 2016 Igor Vlasenko <viy@altlinux.ru> 4.1.2-alt1_7
- update by mgaimport

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 4.1.2-alt1_6
- update by mgaimport

* Tue Oct 07 2014 Igor Vlasenko <viy@altlinux.ru> 4.1.2-alt1_4
- update by mgaimport

* Mon Oct 21 2013 Igor Vlasenko <viy@altlinux.ru> 4.1.2-alt1_3
- update by mgaimport

* Wed Aug 07 2013 Igor Vlasenko <viy@altlinux.ru> 4.1.2-alt1_2
- update by mgaimport

* Sat Jul 27 2013 Igor Vlasenko <viy@altlinux.ru> 4.1.2-alt1
- automated CPAN update

* Mon Dec 10 2012 Igor Vlasenko <viy@altlinux.ru> 4.1.0-alt1_2
- mageia import by cas@ requiest

