%define dist Module-Util
Name: perl-Module-Util
Version: 1.08
Release: alt1

Summary: Module::Util - Module name tools and transformations
License: Perl
Group: Development/Perl

Url: %CPAN %dist
Source: %dist-%version.tar.gz

BuildRequires: perl-Module-Build perl-podlators
BuildArch: noarch

%description
%summary

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build --install_path bindoc=%_man1dir

%install
%perl_vendor_install

%files
%_bindir/pm_which
%_man1dir/pm_which.1*
%perl_vendor_privlib/Module/Util*
%doc Changes README 

%changelog
* Sat Sep 29 2012 Vladimir Lettiev <crux@altlinux.ru> 1.08-alt1
- 1.07 -> 1.08
- built as plain srpm

* Mon Nov 29 2010 Vladimir Lettiev <crux@altlinux.ru> 1.07-alt2
- fixed generation of man1 pages

* Tue Aug 24 2010 Vladimir Lettiev <crux@altlinux.ru> 1.07-alt1
- initial build
