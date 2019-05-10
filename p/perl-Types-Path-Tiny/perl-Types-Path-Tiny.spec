## SPEC file for Perl module Types::Path::Tiny

%define real_name Types-Path-Tiny

Name: perl-Types-Path-Tiny
Version: 0.006
Release: alt1

Summary: Path::Tiny types and coercions for Moose and Mo

License: %asl 2.0
Group: Development/Perl

URL: https://metacpan.org/release/Types-Path-Tiny

Packager: Nikolay A. Fetisov <naf@altlinux.org>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Fri May 10 2019
# optimized out: gem-power-assert perl perl-CPAN-Meta-Requirements perl-Encode perl-Exporter-Tiny perl-JSON-PP perl-Parse-CPAN-Meta perl-Path-Tiny perl-devel perl-parent python-base python-modules python3 python3-base python3-dev ruby ruby-coderay ruby-method_source ruby-pry ruby-rake ruby-rdoc ruby-stdlibs sh4
BuildRequires: perl-CPAN-Meta perl-File-pushd perl-Ref-Util-XS perl-Type-Tiny

%description
Perl module Types::Path::Tiny provides Path::Tiny types for
Moose, Moo, etc.
It handles two important types of coercion:
- coercing objects with overloaded stringification
- coercing to absolute paths
It also can check to ensure that files or directories exist.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Types/Path/Tiny*

%changelog
* Fri May 10 2019 Nikolay A. Fetisov <naf@altlinux.org> 0.006-alt1
- Initial build for ALT Linux Sisyphus
