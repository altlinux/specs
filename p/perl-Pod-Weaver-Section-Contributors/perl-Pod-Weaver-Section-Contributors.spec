## SPEC file for Perl module Pod::Weaver::Section::Contributors

%define real_name Pod-Weaver-Section-Contributors

Name: perl-Pod-Weaver-Section-Contributors
Version: 0.009
Release: alt2

Summary: Pod:Weaver section listing contributors

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/dist/Pod-Weaver-Section-Contributors/

Packager: Nikolay A. Fetisov <naf@altlinux.org>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Sun Jan 22 2017
# optimized out: perl perl-Encode perl-List-MoreUtils perl-Moose perl-Pod-Elemental perl-devel python-base python-modules python3-base
BuildRequires: perl-Pod-Weaver

%description
Perl module Pod::Weaver::Section::Contributors provides a section
for Pod:Weaver that adds a listing of the documents contributors.
It expects a contributors input parameter to be an arrayref of
strings.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Pod/Weaver/Section/Contributors*

%changelog
* Sun Jan 22 2017 Nikolay A. Fetisov <naf@altlinux.org> 0.009-alt2
- Initial build for ALT Linux Sisyphus
