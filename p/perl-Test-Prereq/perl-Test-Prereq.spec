## SPEC file for Perl module Test::Prereq

%define real_name Test-Prereq

Name: perl-Test-Prereq
Version: 1.038
Release: alt1

Summary: Check if Makefile.PL has the right pre-requisites

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/dist/Test-Prereq/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar

BuildArch: noarch

AutoReqProv: perl, yes
BuildPreReq: rpm-build-licenses

# Automatically added by buildreq on Sun Aug 31 2014
# optimized out: perl-Devel-Symdump perl-Encode perl-Module-Build perl-Module-CoreList perl-Module-Metadata perl-Perl-OSType perl-Pod-Coverage perl-Pod-Escapes perl-Pod-Parser perl-Pod-Simple perl-devel
BuildRequires: perl-Module-Info perl-Test-Manifest perl-Test-Pod perl-Test-Pod-Coverage perl-unicore

%description
Perl module Test::Prereq checks if Makefile.PL has the right
pre-requisites.


%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Test/Prereq*

%changelog
* Sun Aug 31 2014 Nikolay A. Fetisov <naf@altlinux.ru> 1.038-alt1
- New version

* Mon Apr 22 2013 Nikolay A. Fetisov <naf@altlinux.ru> 1.037-alt3
- Fix build with new Module::CoreList

* Sun Apr 14 2013 Nikolay A. Fetisov <naf@altlinux.ru> 1.037-alt2
- Fix build with Perl 5.16.3

* Sun Nov 04 2012 Nikolay A. Fetisov <naf@altlinux.ru> 1.037-alt1
- Initial build for ALT Linux Sisyphus
