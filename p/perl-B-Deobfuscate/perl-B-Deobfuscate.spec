## SPEC file for Perl module B::Deobfuscate

%define real_name B-Deobfuscate

Name: perl-B-Deobfuscate
Version: 0.20
Release: alt2

Summary: deobfuscate Perl source code

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/dist/B-Deobfuscate/

Packager: Nikolay A. Fetisov <naf@altlinux.org>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Fri Mar 09 2018
# optimized out: perl perl-CPAN-Meta-Requirements perl-Encode perl-JSON-PP perl-Parse-CPAN-Meta perl-devel perl-parent python-base python-modules python3 python3-base python3-module-mpl_toolkits python3-module-zope ruby ruby-stdlibs
BuildRequires: perl-B-Keywords perl-CPAN-Meta perl-IPC-Run perl-YAML

%description
Perl module B::Deobfuscate is a backend module for the Perl
compiler that generates perl source code, based on the
internal compiled structure that perl itself creates after
parsing a program. It adds symbol renaming functions to the
B::Deparse module. An obfuscated program is already parsed
and interpreted correctly by the B::Deparse program.
Unfortunately, if the obfuscation involved variable renaming
then the resulting program also has obfuscated symbols.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/B/Deobfuscate*
#%%perl_vendor_archlib/B/Deobfuscate*
#%%perl_vendor_autolib/B/Deobfuscate*

%changelog
* Fri Mar 09 2018 Nikolay A. Fetisov <naf@altlinux.org> 0.20-alt2
- Initial build for ALT Linux Sisyphus
