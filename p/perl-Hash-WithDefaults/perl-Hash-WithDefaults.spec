## SPEC file for Perl module CGI::Ex

%define real_name Hash-WithDefaults

Name: perl-Hash-WithDefaults
Version: 0.05
Release: alt1

Summary: class for hashes with key-casing requirements supporting defaults

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/dist/Hash-WithDefaults/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar

BuildArch: noarch

AutoReqProv: perl, yes
BuildPreReq: rpm-build-licenses

# Automatically added by buildreq on Tue Oct 11 2011
# optimized out: perl-Devel-Symdump perl-Encode perl-Pod-Coverage perl-Pod-Escapes perl-Pod-Parser perl-Pod-Simple perl-YAML-Tiny perl-devel perl-podlators
BuildRequires: perl-Module-Build perl-Test-Pod perl-Test-Pod-Coverage

%description
Perl module Hash::WithDefaults implements hashes that support "defaults".
That is you may specify several more hashes in which the data will be
looked up in case it is not found in the current hash.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Hash/WithDefaults*

%changelog
* Tue Oct 11 2011 Nikolay A. Fetisov <naf@altlinux.ru> 0.05-alt1
- Initial build for ALT Linux Sisyphus
