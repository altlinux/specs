%define _unpackaged_files_terminate_build 1
# tests require external formatters (w3m/lynx/elinks/zen) and X11 DISPLAY
%def_without test
%define module_name HTML-FormatExternal

Name: perl-%module_name
Version: 26
Release: alt1

Summary: HTML to text formatting using external programs

License: GPL-3.0-or-later
Group: Development/Perl
URL: %CPAN %module_name
# Source-url: https://cpan.metacpan.org/authors/id/K/KR/KRYDE/%module_name-%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-perl
BuildRequires: perl-devel perl-constant-defer perl-IPC-Run perl-URI

%description
HTML::FormatExternal is a pure-Perl module for converting HTML to text
using external programs: elinks, html2text, links, lynx, netrik, vilistextum,
w3m or zen. It runs the chosen formatter as a separate process and feeds
the HTML input to it.

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/HTML/FormatExternal.pm
%perl_vendor_privlib/HTML/FormatText/

%changelog
* Thu Jul 16 2026 Vitaly Lipatov <lav@altlinux.ru> 26-alt1
- initial build for ALT Sisyphus

