%define dist HTTP-Headers-ActionPack

Name: perl-%dist
Version: 0.09
Release: alt1

Summary: HTTP Action, Adventure and Excitement

License: GPL-1.0-or-later OR Artistic-1.0-Perl
Group: Development/Perl
URL: https://metacpan.org/release/%dist

# Source-url: https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/%dist-%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-devel

# Build/test dependencies (non-core modules from META.yml)
BuildRequires: perl-HTTP-Message perl-Module-Runtime perl-Sub-Exporter
BuildRequires: perl-Time-Piece perl-URI perl-Test-Fatal perl-Test-Warnings

%description
HTTP::Headers::ActionPack provides a set of objects representing HTTP
headers with specific handling for content negotiation, MIME types,
character sets, languages, dates, authorization, authentication info,
link headers and more.

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README.md Changes LICENSE
%perl_vendor_privlib/HTTP/Headers/ActionPack/
%perl_vendor_privlib/HTTP/Headers/ActionPack.pm

%changelog
* Fri Jul 17 2026 Vitaly Lipatov <lav@altlinux.ru> 0.09-alt1
- initial build for ALT Sisyphus

