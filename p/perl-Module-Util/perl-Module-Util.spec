%define m_distro Module-Util
Name: perl-Module-Util
Version: 1.07
Release: alt2
Summary: Module::Util - Module name tools and transformations

Packager: Vladimir Lettiev <crux@altlinux.ru>

Group: Development/Perl
License: Perl
Url: http://search.cpan.org/~mattlaw/Module-Util/

BuildArch: noarch
Source: %m_distro-%version.tar
BuildRequires: perl-Module-Build perl-podlators

%description
%summary

%prep
%setup -q -n %m_distro-%version

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
* Mon Nov 29 2010 Vladimir Lettiev <crux@altlinux.ru> 1.07-alt2
- fixed generation of man1 pages

* Tue Aug 24 2010 Vladimir Lettiev <crux@altlinux.ru> 1.07-alt1
- initial build
