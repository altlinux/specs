## SPEC file for Perl module Config::MVP::Slicer

%define real_name Config-MVP-Slicer

Name: perl-Config-MVP-Slicer
Version: 0.302
Release: alt3

Summary: Perl module to extract embedded plugin config from parent config

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/dist/Config-MVP-Slicer/

Packager: Nikolay A. Fetisov <naf@altlinux.org>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Thu May 04 2017
# optimized out: perl perl-Class-Load perl-Data-OptList perl-Devel-GlobalDestruction perl-Devel-OverloadInfo perl-Eval-Closure perl-IPC-Run3 perl-MRO-Compat perl-Module-Implementation perl-Module-Runtime perl-Package-DeprecationManager perl-Package-Stash perl-Package-Stash-XS perl-Params-Util perl-Probe-Perl perl-Sub-Exporter perl-Sub-Exporter-Progressive perl-Sub-Identify perl-Sub-Install perl-Sub-Name perl-Test-Fatal perl-Try-Tiny perl-devel perl-parent python-base python-modules python3
BuildRequires: perl-Encode perl-Moose perl-Test-Script

%description
Perl module Config::MVP::Slicer can be used to extract embedded
configurations for other plugins out of larger (parent)
configurations.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Config/MVP/Slicer*

%changelog
* Thu May 04 2017 Nikolay A. Fetisov <naf@altlinux.org> 0.302-alt3
- Initial build for ALT Linux Sisyphus
