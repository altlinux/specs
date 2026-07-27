%define real_name Alien-Build-Plugin-Download-GitHub

Name: perl-%real_name
Version: 0.10
Release: alt1

Summary: Alien::Build plugin to download the latest asset from a GitHub repo

License: %perl_license
Group: Development/Perl

URL: https://metacpan.org/release/%real_name

# Source-url: https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/%real_name-%version.tar.gz
Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-perl rpm-build-licenses
BuildRequires: perl-devel perl-Alien-Build
BuildRequires: perl-Capture-Tiny perl-Test2-Suite
BuildRequires: perl-URI perl-HTTP-Tiny

%description
Alien::Build::Plugin::Download::GitHub is an Alien::Build plugin that downloads
the latest GitHub release asset for a project. It is a build-time dependency of
perl-Alien-FFI, whose alienfile loads this plugin.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes
%perl_vendor_privlib/Alien*

%changelog
* Sun Jul 26 2026 Vitaly Lipatov <lav@altlinux.ru> 0.10-alt1
- initial build for Sisyphus
