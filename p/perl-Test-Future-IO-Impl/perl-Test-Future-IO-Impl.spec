## SPEC file for Perl module Test::Future::IO::Impl

%define real_name Test-Future-IO-Impl

%define _unpackaged_files_terminate_build 1

Name: perl-Test-Future-IO-Impl
Version: 0.14
Release: alt2

Summary: acceptance tests for Future::IO implementations

License: %perl_license
Group: Development/Perl

URL: https://metacpan.org/release/Test-Future-IO-Impl

Packager: Nikolay A. Fetisov <naf@altlinux.org>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Sun Aug 06 2023
# optimized out: libgpg-error perl perl-CPAN-Meta perl-CPAN-Meta-Requirements perl-CPAN-Meta-YAML perl-Encode perl-Importer perl-JSON-PP perl-MIME-Charset perl-Module-Metadata perl-Parse-CPAN-Meta perl-Perl-OSType perl-Pod-Escapes perl-Pod-Simple perl-Term-Size-Any perl-Term-Size-Perl perl-Term-Table perl-TermReadKey perl-Unicode-LineBreak perl-devel perl-parent perl-podlators python-modules python2-base python3-base sh4
BuildRequires: perl-HTML-Parser perl-Module-Build perl-Test-Pod perl-Test2-Suite

%description
Perl module Test::Future::IO::Impl contains a collection
of acceptance tests for implementations of Future::IO.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Test/Future/IO/Impl*

%changelog
* Sun Aug 06 2023 Nikolay A. Fetisov <naf@altlinux.org> 0.14-alt2
- Bump release to override autoimports package

* Sun Aug 06 2023 Nikolay A. Fetisov <naf@altlinux.org> 0.14-alt1
- Initial build for ALT Linux Sisyphus
