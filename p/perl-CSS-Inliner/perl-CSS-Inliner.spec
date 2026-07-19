%define _unpackaged_files_terminate_build 1
%define module_name CSS-Inliner

Name: perl-%module_name
Version: 4027
Release: alt1

Summary: Library for converting CSS style blocks to inline styles
License: GPL-1.0-or-later OR Artistic-1.0-clause
Group: Development/Perl
URL: %CPAN %module_name
# Source-url: https://cpan.metacpan.org/authors/id/K/KA/KAMELKEV/%module_name-%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-perl
BuildRequires: perl-devel perl-HTML-Query perl-HTML-Tree perl-libwww perl-URI perl-Test-Pod perl-unicore

%description
CSS::Inliner is a library for converting CSS <style> blocks into inline
styles on the HTML elements they target. This is primarily useful for
preparing HTML emails, where many clients ignore <style> blocks.

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README
%perl_vendor_privlib/CSS/Inliner.pm
%perl_vendor_privlib/CSS/Inliner/

%changelog
* Sun Jul 19 2026 Vitaly Lipatov <lav@altlinux.ru> 4027-alt1
- initial build for ALT Sisyphus
