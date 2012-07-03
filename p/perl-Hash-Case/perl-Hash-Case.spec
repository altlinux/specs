## SPEC file for Perl module Hash::Case

%define real_name Hash-Case

Name: perl-Hash-Case
Version: 1.01
Release: alt1

Summary: base class for hashes with key-casing requirements

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/dist/Hash-Case/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar

BuildArch: noarch

AutoReqProv: perl, yes
BuildPreReq: rpm-build-licenses

# Automatically added by buildreq on Tue Oct 11 2011
# optimized out: perl-Encode perl-Pod-Escapes perl-Pod-Simple perl-devel
BuildRequires: perl-Log-Report perl-Test-Pod

%description
Perl module Hash::Case is the base class for various classes
which tie special treatment for the casing of keys.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README ChangeLog
%perl_vendor_privlib/Hash/Case*

%changelog
* Tue Oct 11 2011 Nikolay A. Fetisov <naf@altlinux.ru> 1.01-alt1
- Initial build for ALT Linux Sisyphus
