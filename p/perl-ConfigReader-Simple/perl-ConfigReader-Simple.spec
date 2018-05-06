# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define upstream_name    ConfigReader-Simple
%define upstream_version 1.293

%{?perl_default_filter}

Name:       perl-%{upstream_name}
Version:    %{upstream_version}
Release:    alt1_1

License:    GPL+ or Artistic
Group:      Development/Perl
Summary:    Read simple configuration file formats
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/ConfigReader/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Carp.pm)
BuildRequires: perl(Data/Dumper.pm)
BuildRequires: perl(ExtUtils/MakeMaker.pm)
BuildRequires: perl(File/Spec.pm)
BuildRequires: perl(File/Spec/Functions.pm)
BuildRequires: perl(Test/More.pm)
BuildRequires: perl(Test/Output.pm)
BuildRequires: perl(Test/Warn.pm)
BuildRequires: perl(strict.pm)
BuildRequires: perl(subs.pm)
BuildRequires: perl(vars.pm)
BuildRequires: perl(warnings.pm)
BuildArch:  noarch
Source44: import.info

%description
'ConfigReader::Simple' reads and parses simple configuration files. It is
designed to be smaller and simpler than the 'ConfigReader' module and is
more suited to simple configuration files. 

The configuration file format
    The configuration file uses a line-oriented format, meaning that the
    directives do not have containers. The values can be split across lines
    with a continuation character, but for the most part everything ends up
    on the same line.

    The first group of non-whitespace characters is the "directive", or the
    name of the configuration item. The linear whitespace after that
    separates the directive from the "value", which is the rest of the
    line, including any other whitespace.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes LICENSE META.json META.yml  eg examples
%{perl_vendor_privlib}/*

%changelog
* Sun May 06 2018 Igor Vlasenko <viy@altlinux.ru> 1.293-alt1_1
- update by mgaimport

* Wed May 02 2018 Igor Vlasenko <viy@altlinux.ru> 1.293-alt1
- automated CPAN update

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.291-alt1_1
- update by mgaimport

* Sun Dec 18 2016 Igor Vlasenko <viy@altlinux.ru> 1.291-alt1
- automated CPAN update

* Wed Jul 27 2016 Igor Vlasenko <viy@altlinux.ru> 1.29-alt1_6
- update by mgaimport

* Wed Feb 17 2016 Igor Vlasenko <viy@altlinux.ru> 1.29-alt1_5
- update by mgaimport

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 1.29-alt1_4
- update by mgaimport

* Tue Oct 07 2014 Igor Vlasenko <viy@altlinux.ru> 1.29-alt1_2
- update by mgaimport

* Fri Aug 29 2014 Igor Vlasenko <viy@altlinux.ru> 1.29-alt1_1
- update by mgaimport

* Tue Aug 05 2014 Igor Vlasenko <viy@altlinux.ru> 1.28-alt2_4
- moved to Sysiphus as dependency

* Mon Oct 21 2013 Igor Vlasenko <viy@altlinux.ru> 1.28-alt1_4
- mga update

* Wed Aug 07 2013 Igor Vlasenko <viy@altlinux.ru> 1.28-alt1_3
- mgaimport update

* Thu Jul 25 2013 Igor Vlasenko <viy@altlinux.ru> 1.28-alt1_2
- converted for ALT Linux by srpmconvert tools

