## SPEC file for Perl module Sub::Exporter::GlobExporter

Name: perl-Sub-Exporter-GlobExporter
Version: 0.002
Release: alt1

Summary: export shared globs with Sub::Exporter collectors  

License: %perl_license
Group: Development/Perl
URL: http://search.cpan.org/dist/Sub-Exporter-GlobExporter/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>
BuildArch: noarch

%define real_name Sub-Exporter-GlobExporter
Source: %real_name-%version.tar

AutoReqProv: perl, yes
BuildRequires(pre): rpm-build-licenses perl-devel

# Automatically added by buildreq on Sat Jan 28 2012
# optimized out: perl-Data-OptList perl-Params-Util perl-Sub-Install
BuildRequires: perl-Sub-Exporter perl-devel

%description
Perl module Sub::Exporter::GlobExporter provides a way to export
shared globs with Sub::Exporter collectors.

%prep
%setup  -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Sub/Exporter/GlobExporter*

%changelog
* Sat Jan 28 2012 Nikolay A. Fetisov <naf@altlinux.ru> 0.002-alt1
- Initial build for ALT Linux Sisyphus

