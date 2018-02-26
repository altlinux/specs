Name: perl-Module-Install-XSUtil
Version: 0.42
Release: alt1
Summary: Module::Install::XSUtil - utility functions for XS modules

Group: Development/Perl
License: Perl
Url: %CPAN Module-Install-XSUtil

BuildArch: noarch
Source: %name-%version.tar
BuildRequires: perl-devel perl-Module-Install perl-B-Hooks-OP-Annotation

%description
Module::Install::XSUtil provides a set of utilities to setup
distributions which include or depend on XS module.

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Module/Install/XSUtil.pm
%doc Changes README 

%changelog
* Fri Dec 02 2011 Vladimir Lettiev <crux@altlinux.ru> 0.42-alt1
- New version 0.42

* Thu Sep 22 2011 Igor Vlasenko <viy@altlinux.ru> 0.39-alt1
- automated CPAN update

* Thu Feb 17 2011 Vladimir Lettiev <crux@altlinux.ru> 0.36-alt1
- initial build
