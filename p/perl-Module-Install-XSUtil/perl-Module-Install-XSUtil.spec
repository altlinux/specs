Name: perl-Module-Install-XSUtil
Version: 0.45
Release: alt1

Summary: Module::Install::XSUtil - utility functions for XS modules
License: Perl
Group: Development/Perl

Url: %CPAN Module-Install-XSUtil
# Cloned from git://github.com/gfx/Perl-Module-Install-XSUtil.git
Source: %name-%version.tar

BuildArch: noarch
BuildRequires: perl-devel perl-Module-Install perl-B-Hooks-OP-Annotation perl-Module-Install-Repository

%description
Module::Install::XSUtil provides a set of utilities to setup
distributions which include or depend on XS module.

%prep
%setup -q
# skip authors tests
sed -i "/author_tests/d" Makefile.PL

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Module/Install/XSUtil.pm
%doc Changes README 

%changelog
* Sat Jun 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.45-alt1
- automated CPAN update

* Thu Aug 29 2013 Vladimir Lettiev <crux@altlinux.ru> 0.44-alt1
- 0.43 -> 0.44

* Sat Sep 29 2012 Vladimir Lettiev <crux@altlinux.ru> 0.43-alt1
- 0.42 -> 0.43
- sources cloned from upstream git

* Fri Dec 02 2011 Vladimir Lettiev <crux@altlinux.ru> 0.42-alt1
- New version 0.42

* Thu Sep 22 2011 Igor Vlasenko <viy@altlinux.ru> 0.39-alt1
- automated CPAN update

* Thu Feb 17 2011 Vladimir Lettiev <crux@altlinux.ru> 0.36-alt1
- initial build
