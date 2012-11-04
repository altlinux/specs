## SPEC file for Perl module Test::Prereq

%define real_name Test-Prereq

Name: perl-Test-Prereq
Version: 1.037
Release: alt1

Summary: Check if Makefile.PL has the right pre-requisites

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/dist/Test-Prereq/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar
Patch0: %real_name-1.037-alt-fix_pod_encoding.patch

BuildArch: noarch

AutoReqProv: perl, yes
BuildPreReq: rpm-build-licenses

# Automatically added by buildreq on Sun Nov 04 2012
# optimized out: perl-CPAN-Meta perl-CPAN-Meta-Requirements perl-CPAN-Meta-YAML perl-Devel-Symdump perl-Encode perl-JSON-PP perl-Module-CoreList perl-Module-Metadata perl-Parse-CPAN-Meta perl-Perl-OSType perl-Pod-Coverage perl-Pod-Escapes perl-Pod-Parser perl-Pod-Simple perl-devel perl-podlators
BuildRequires: perl-HTML-Parser perl-Module-Build perl-Module-Info perl-Test-Manifest perl-Test-Pod perl-Test-Pod-Coverage

%description
Perl module Test::Prereq checks if Makefile.PL has the right
pre-requisites.


%prep
%setup -q -n %real_name-%version
%patch0

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Test/Prereq*

%changelog
* Sun Nov 04 2012 Nikolay A. Fetisov <naf@altlinux.ru> 1.037-alt1
- Initial build for ALT Linux Sisyphus
