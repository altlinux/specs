## SPEC file for Perl module Devel::SimpleTrace

%define real_name Devel-SimpleTrace

Name: perl-Devel-SimpleTrace
Version: 0.08
Release: alt3

Summary: Perl module to die using stack traces

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/dist/Devel-SimpleTrace/

Packager: Nikolay A. Fetisov <naf@altlinux.org>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Sun Jan 22 2017
# optimized out: perl perl-CPAN-Meta perl-CPAN-Meta-Requirements perl-CPAN-Meta-YAML perl-Devel-Symdump perl-Encode perl-JSON-PP perl-Module-Metadata perl-Parse-CPAN-Meta perl-Perl-OSType perl-Pod-Coverage perl-Pod-Escapes perl-Pod-Parser perl-Pod-Simple perl-devel perl-parent perl-podlators python-base python-modules python3-base
BuildRequires: perl-HTML-Parser perl-Module-Build perl-Test-Pod perl-Test-Pod-Coverage perl-Test-Portability-Files

%description
Perl module Devel::SimpleTrace can be used to more easily spot
the place where a program or a module generates errors. Its
use is extremely simple, reduced to just useing it.

This is achieved by modifying the functions warn() and die()
in order to replace the standard messages by complete stack
traces that precisely indicates how and where the error or
warning occurred. Other than this, their use should stay
unchanged, even when using die() inside eval().

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Devel/SimpleTrace*

%changelog
* Sun Jan 22 2017 Nikolay A. Fetisov <naf@altlinux.org> 0.08-alt3
- Initial build for ALT Linux Sisyphus
