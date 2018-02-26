%define module_name Module-Signature

Name: perl-%module_name
Version: 0.68
Release: alt1

Packager: Victor Forsiuk <force@altlinux.org>

Summary: %module_name module for perl
License: CC0 1.0
Group: Development/Perl

Url: %CPAN %module_name
Source: http://www.cpan.org/authors/id/F/FL/FLORA/Module-Signature-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Mon Jun 21 2010
BuildRequires: gnupg perl-Crypt-Blowfish perl-Crypt-DES_EDE3 perl-Crypt-OpenPGP perl-Digest-SHA perl-Math-BigInt-GMP perl-Module-Install perl(IPC/Run.pm)

# automatically added during perl 5.8 -> 5.12 upgrade.
# perl-podlators is required for pod2man conversion.
BuildRequires: perl-podlators

%description
Module::Signature, a module to check and create SIGNATURE files for CPAN distributions.

%prep
%setup -n %module_name-%version

%build
# Running _all_ tests successfully for our package build is tricky:
#
# Due to ".perl.req" file generation in ALT standard perl modules build
# process signature test will fail complaining about
# "MISMATCHED content between MANIFEST and distribution files!"
#
# So, we instruct our standard build macros to not run tests, then fix
# problem and run tests explicitly:
%def_without test
%perl_vendor_build INSTALLMAN1DIR=%_man1dir
# Need to set this environment variable to enable signature test
export TEST_SIGNATURE=1
mv .perl.req ../
%make test
mv ../.perl.req .

%install
%perl_vendor_install

%files
%_bindir/*
%perl_vendor_privlib/Module*
%_man1dir/*

%changelog
* Thu Sep 29 2011 Igor Vlasenko <viy@altlinux.ru> 0.68-alt1
- automated CPAN update

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.66-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Mon Sep 13 2010 Victor Forsiuk <force@altlinux.org> 0.66-alt1
- 0.66

* Mon Jun 21 2010 Victor Forsiuk <force@altlinux.org> 0.64-alt1
- 0.64

* Tue Dec 01 2009 Victor Forsyuk <force@altlinux.org> 0.61-alt1
- 0.61
- License change from MIT to CC0 (Creative Commons Zero).

* Tue Jul 03 2007 Victor Forsyuk <force@altlinux.org> 0.55-alt1
- Initial build.
