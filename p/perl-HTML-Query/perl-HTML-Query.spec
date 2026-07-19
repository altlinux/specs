%define _unpackaged_files_terminate_build 1
%define module_name HTML-Query

Name: perl-%module_name
Version: 0.09
Release: alt1

Summary: Perform jQuery-like queries on HTML::Element trees
License: GPL-1.0-or-later OR Artistic-1.0-clause
Group: Development/Perl
URL: %CPAN %module_name
# Source-url: https://cpan.metacpan.org/authors/id/K/KA/KAMELKEV/%module_name-%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-perl
BuildRequires: perl-devel perl-Badger perl-HTML-Tree

%description
HTML::Query is a concise and powerful tool for performing jQuery-like
queries on HTML::Element trees, allowing you to select elements using
CSS-style selectors.

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README
%perl_vendor_privlib/HTML/Query.pm

%changelog
* Sun Jul 19 2026 Vitaly Lipatov <lav@altlinux.ru> 0.09-alt1
- initial build for ALT Sisyphus
