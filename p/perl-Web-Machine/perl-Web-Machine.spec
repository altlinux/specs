%define _unpackaged_files_terminate_build 1
%define dist Web-Machine

Name: perl-%dist
Version: 0.17
Release: alt1

Summary: A Perl port of Webmachine
License: GPL-1.0-or-later OR Artistic-1.0-Perl
Group: Development/Perl
URL: https://metacpan.org/release/%dist

# Source-url: https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/%dist-%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-devel
BuildRequires: perl-HTTP-Headers-ActionPack perl-IO-Handle-Util
BuildRequires: perl-HTTP-Message perl-Hash-MultiValue perl-Module-Runtime
BuildRequires: perl-Plack perl-Sub-Exporter perl-Try-Tiny
BuildRequires: perl-Locale-Maketext perl-Net-HTTP
BuildRequires: perl-Test-FailWarnings perl-Test-Fatal

%description
Web::Machine provides a Perl port of Webmachine, which is a system for
building RESTful web applications based on the HTTP protocol. It
implements the HTTP state machine (FSM) described in the "Webmachine
flowchart", handling content negotiation, conditional requests, caching
and other HTTP features automatically.

%prep
%setup

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes INSTALL CONTRIBUTING.md
%doc examples
%perl_vendor_privlib/Web/*

%changelog
* Thu Jul 16 2026 Vitaly Lipatov <lav@altlinux.ru> 0.17-alt1
- initial build for ALT Sisyphus

