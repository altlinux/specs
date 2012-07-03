%define module Module-Starter-PBP

Name: perl-Module-Starter-PBP
Version: 0.0.3
Release: alt1

Summary: Module::Starter::PBP - Create a module as recommended in "Perl Best Practices"

License: Artistic
Group: Development/Perl
Url: %CPAN %module

Packager: Michael Bochkaryov <misha@altlinux.ru>

BuildArch: noarch
Source: %module.tar

# Automatically added by buildreq on Tue Aug 30 2011
# optimized out: perl-Devel-Symdump perl-Encode perl-Pod-Coverage perl-Pod-Escapes perl-Pod-Parser perl-Pod-Simple perl-YAML-Tiny perl-devel perl-podlators
BuildRequires: perl-Module-Build perl-Module-Starter perl-Test-Pod perl-Test-Pod-Coverage

%description
This module implements a simple approach to creating modules and their support
files, based on the Module::Starter approach. Module::Starter needs to be
installed before this module can be used.

When used as a Module::Starter plugin, this module allows you to specify a
simple directory of templates which are filled in with module-specific
information, and thereafter form the basis of your new module.

The default templates that this module initially provides are based on the
recommendations in the book "Perl Best Practices".

%prep
%setup -n Module-Starter-PBP

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Module/*

%changelog
* Tue Aug 30 2011 Michael Bochkaryov <misha@altlinux.ru> 0.0.3-alt1
- initial build for ALT Linux Sisyphus

