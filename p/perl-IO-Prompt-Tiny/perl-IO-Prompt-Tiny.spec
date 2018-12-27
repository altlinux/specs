# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define upstream_name    IO-Prompt-Tiny
%define upstream_version 0.003

%{?perl_default_filter}

Name:       perl-%{upstream_name}
Version:    %{upstream_version}
Release:    alt2_4

Summary:    Prompt for user input with a default option
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/IO/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Capture/Tiny.pm)
BuildRequires: perl(Carp.pm)
BuildRequires: perl(Exporter.pm)
BuildRequires: perl(ExtUtils/MakeMaker.pm)
BuildRequires: perl(File/Spec.pm)
BuildRequires: perl(File/Temp.pm)
BuildRequires: perl(Test/More.pm)
BuildRequires: perl(strict.pm)
BuildRequires: perl(warnings.pm)
BuildArch:  noarch
Source44: import.info

%description
This is an extremely simple prompting module, based on the extremely simple
prompt offered by the ExtUtils::MakeMaker manpage.In many cases, that's all
you need and this module gives it to you without all the overhead of
ExtUtils::MakeMaker just to prompt for input.

It doesn't do any validation, coloring, menus, timeouts, or any of the
wild, crazy, cool stuff that other prompting modules do. It just prompts
with a default. That's it!

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes LICENSE META.json META.yml  README
%{perl_vendor_privlib}/*

%changelog
* Thu Dec 27 2018 Igor Vlasenko <viy@altlinux.ru> 0.003-alt2_4
- to Sisyphus as perl-POE-Component-SSLify dependency

* Thu Oct 04 2018 Igor Vlasenko <viy@altlinux.ru> 0.003-alt1_4
- update by mgaimport

* Wed Jul 27 2016 Igor Vlasenko <viy@altlinux.ru> 0.003-alt1_3
- update by mgaimport

* Sun Feb 21 2016 Igor Vlasenko <viy@altlinux.ru> 0.003-alt1_2
- update by mgaimport

* Tue Oct 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.003-alt1_1
- update by mgaimport

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 0.002-alt2_4
- update by mgaimport

* Tue Oct 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.002-alt2_3
- update by mgaimport

* Tue Sep 02 2014 Cronbuild Service <cronbuild@altlinux.org> 0.002-alt2_2
- rebuild to get rid of unmets

* Tue Oct 29 2013 Igor Vlasenko <viy@altlinux.ru> 0.002-alt1_2
- mga update

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.002-alt1_1
- mgaimport update

* Thu Jul 25 2013 Igor Vlasenko <viy@altlinux.ru> 0.001-alt1_1
- converted for ALT Linux by srpmconvert tools

