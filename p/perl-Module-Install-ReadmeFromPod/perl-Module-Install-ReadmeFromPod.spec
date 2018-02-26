Name: perl-Module-Install-ReadmeFromPod
Version: 0.18
Release: alt1

Summary: Module::Install extension to automatically convert POD to a README
Group: Development/Perl
License: Perl

Url: %CPAN Module-Install-ReadmeFromPod
Source: %name-%version.tar

BuildArch: noarch
BuildRequires: perl-devel perl-Module-Install perl-Capture-Tiny

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
* Thu Apr 12 2012 Vladimir Lettiev <crux@altlinux.ru> 0.18-alt1
- 0.18

* Thu Feb 10 2011 Vladimir Lettiev <crux@altlinux.ru> 0.12-alt1
- New version 0.12

* Mon Aug 30 2010 Vladimir Lettiev <crux@altlinux.ru> 0.08-alt1
- initial build
