# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(CPAN.pm) perl(Carp.pm) perl(Config.pm) perl(Cwd.pm) perl(File/Basename.pm) perl(File/Spec.pm) perl(FileHandle.pm) perl(LWP/Simple.pm) perl(Module/Build.pm) perl(Module/Signature.pm) perl(Net/FTP.pm) perl(Socket.pm) perl(YAML.pm) perl(subs.pm) perl-podlators
# END SourceDeps(oneline)
%define upstream_name    Alien-SeleniumRC
%define upstream_version 2.95

%{?perl_default_filter}

Name:       perl-%{upstream_name}
Version:    %{upstream_version}
Release:    alt1_3

Summary:    Packaging up SeleniumRC java server
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Alien/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(ExtUtils/MakeMaker.pm)
BuildRequires: perl(Test/More.pm)
BuildArch:  noarch
Source44: import.info

%description
The Selenium RC home page is at the http://openqa.org/selenium-rc manpage

Selenium Remote Control is a test tool that allows you to write automated
web application UI tests in any programming language against any HTTP
website using any mainstream JavaScript-enabled browser.

Selenium Remote Control provides a Selenium Server, which can automatically
start/stop/control any supported browser. It works by using Selenium Core,
a pure-HTML+JS library that performs automated tasks in JavaScript.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
%makeinstall_std

%files
%doc Changes  README SIGNATURE
%{perl_vendor_privlib}/*
/usr/bin/selenium-rc

%changelog
* Wed Jul 27 2016 Igor Vlasenko <viy@altlinux.ru> 2.95-alt1_3
- update by mgaimport

* Tue Mar 29 2016 Igor Vlasenko <viy@altlinux.ru> 2.95-alt1_2
- update by mgaimport

* Mon Sep 28 2015 Igor Vlasenko <viy@altlinux.ru> 2.95-alt1_1
- update by mgaimport

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 2.93-alt1_4
- update by mgaimport

* Tue Oct 07 2014 Igor Vlasenko <viy@altlinux.ru> 2.93-alt1_3
- update by mgaimport

* Mon Oct 21 2013 Igor Vlasenko <viy@altlinux.ru> 2.93-alt1_2
- update by mgaimport

* Wed Aug 07 2013 Igor Vlasenko <viy@altlinux.ru> 2.93-alt1_1
- build for Sisyphus

* Thu Jul 25 2013 Igor Vlasenko <viy@altlinux.ru> 2.92-alt1_1
- converted for ALT Linux by srpmconvert tools

