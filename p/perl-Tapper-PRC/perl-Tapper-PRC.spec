%define _unpackaged_files_terminate_build 1
BuildRequires: perl(File/Slurp.pm) perl(Proc/Killfam.pm)
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-devel perl-podlators perl(Hash/Merge.pm)
# END SourceDeps(oneline)
BuildRequires: perl(File/Slurp.pm)
%define upstream_name    Tapper-PRC
%define upstream_version 5.0.2

Name:       perl-%{upstream_name}
Version:    5.0.2
Release:    alt1

Summary:    Control running test programs
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source:    http://www.cpan.org/authors/id/T/TA/TAPPER/Tapper-PRC-%{version}.tar.gz

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
BuildRequires: perl(Log/Log4perl.pm)
BuildRequires: perl(Moose.pm)
BuildRequires: perl(MooseX/Log/Log4perl.pm)
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
BuildRequires: perl(strict.pm)
BuildRequires: perl(warnings.pm)
BuildArch:  noarch
Source44: import.info

%description
Tapper - Program run control for test program automation.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor

%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes LICENSE META.json META.yml  README
%perl_vendor_privlib/*
%_bindir/tapper*
%_man1dir/tapper*

%changelog
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

