# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-devel perl-podlators
# END SourceDeps(oneline)
%define upstream_name    Tapper-TestSuite-HWTrack
%define upstream_version 4.1.1

Name:       perl-%{upstream_name}
Version:    %{upstream_version}
Release:    alt1_6

Summary:    Report hardware meta information
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Tapper/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(ExtUtils/MakeMaker.pm)
BuildRequires: perl(File/ShareDir.pm)
BuildRequires: perl(File/Temp.pm)
BuildRequires: perl(IO/Select.pm)
BuildRequires: perl(IO/Socket/INET.pm)
BuildRequires: perl(Log/Log4perl.pm)
BuildRequires: perl(Moose.pm)
BuildRequires: perl(Sys/Hostname.pm)
BuildRequires: perl(Tapper/Base.pm)
BuildRequires: perl(Test/More.pm)
BuildRequires: perl(XML/Simple.pm)
BuildRequires: perl(YAML.pm)
BuildRequires: perl(aliased.pm)
BuildArch:  noarch
Source44: import.info

%description
HWTrack calls the tool lshw, parses its input and sends it to the report
framework.

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
/usr/bin/tapper-testsuite-hwtrack
/usr/share/man/man1/tapper-testsuite-hwtrack.1*

%changelog
* Wed Feb 17 2016 Igor Vlasenko <viy@altlinux.ru> 4.1.1-alt1_6
- update by mgaimport

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 4.1.1-alt1_5
- update by mgaimport

* Mon Oct 21 2013 Igor Vlasenko <viy@altlinux.ru> 4.1.1-alt1_3
- update by mgaimport

* Wed Aug 07 2013 Igor Vlasenko <viy@altlinux.ru> 4.1.1-alt1_2
- update by mgaimport

* Sat Jul 27 2013 Igor Vlasenko <viy@altlinux.ru> 4.1.1-alt1
- automated CPAN update

* Mon Dec 10 2012 Igor Vlasenko <viy@altlinux.ru>  4.1.0-alt1_2
- mageia import by cas@ requiest

