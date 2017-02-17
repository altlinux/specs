Name: perl-Module-Install-ReadmeFromPod
Version: 0.28
Release: alt1

Summary: Module::Install extension to automatically convert POD to a README
Group: Development/Perl
License: Perl

Url: %CPAN Module-Install-ReadmeFromPod
Source: %name-%version.tar

BuildArch: noarch
BuildRequires: perl-devel perl-Module-Install perl-Capture-Tiny perl(IO/All.pm) perl(Pod/Markdown.pm) perl(Test/InDistDir.pm)

%description
Module::Install::ReadmeFromPod is a Module::Install extension that
generates a "README" file automatically from an indicated file
containing POD, whenever the author runs "Makefile.PL".

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Module/Install/ReadmeFromPod*
%doc LICENSE Changes README

%changelog
* Fri Feb 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.28-alt1
- automated CPAN update

* Thu May 26 2016 Igor Vlasenko <viy@altlinux.ru> 0.26-alt1
- automated CPAN update

* Tue Oct 15 2013 Igor Vlasenko <viy@altlinux.ru> 0.22-alt1
- new version 0.22

* Thu Apr 12 2012 Vladimir Lettiev <crux@altlinux.ru> 0.18-alt1
- 0.18

* Thu Feb 10 2011 Vladimir Lettiev <crux@altlinux.ru> 0.12-alt1
- New version 0.12

* Mon Aug 30 2010 Vladimir Lettiev <crux@altlinux.ru> 0.08-alt1
- initial build
