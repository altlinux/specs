%define dist HTTP-Headers-ActionPack

Name: perl-%dist
Version: 0.10
Release: alt1

Summary: HTTP Action, Adventure and Excitement

License: GPL-1.0-or-later OR Artistic-1.0-Perl
Group: Development/Perl
URL: https://metacpan.org/release/%dist

# Source-url: https://cpan.metacpan.org/authors/id/R/RR/RRWO/%dist-%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-devel

# Build/test dependencies (non-core modules from META.yml)
BuildRequires: perl-HTTP-Message perl-Module-Runtime perl-Sub-Exporter
BuildRequires: perl-Time-Piece perl-URI perl-Test-Fatal perl-Test-Timer perl-Test-Warnings

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
* Tue Oct 27 2026 Vitaly Lipatov <lav@altlinux.ru> 0.10-alt1
- new version 0.10
- added BuildRequires: perl-Test-Timer for upstream tests.
- fixes:
  + CVE-2026-113877: match Accept-Language ranges as literals.

* Fri Jul 17 2026 Vitaly Lipatov <lav@altlinux.ru> 0.09-alt1
- initial build for ALT Sisyphus

