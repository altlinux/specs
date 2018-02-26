%define dist Module-Install-Repository
Name: perl-%dist
Version: 0.06
Release: alt3

Summary: Automatically sets repository URL from svn/svk/Git checkout
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Tue Nov 15 2011 (-bi)
BuildRequires: perl-Filter perl-Module-Install

%description
Module::Install::Repository is a Module::Install plugin to
automatically figure out repository URL and set it via repository()
which then will be added to resources under META.yml.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Module*

%changelog
* Tue Nov 15 2011 Alexey Tourbin <at@altlinux.ru> 0.06-alt3
- rebuilt as plain src.rpm

* Fri Feb 25 2011 Vladimir Lettiev <crux@altlinux.ru> 0.06-alt2
- fixed build

* Tue Mar 23 2010 Alexey Tourbin <at@altlinux.ru> 0.06-alt1
- initial revision
