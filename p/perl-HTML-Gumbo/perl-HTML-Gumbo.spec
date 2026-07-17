%define _unpackaged_files_terminate_build 1
%define module_name HTML-Gumbo

Name: perl-%module_name
Version: 0.20
Release: alt1

Summary: HTML5 parser based on gumbo C library

License: GPL-1.0+ or Artistic-1.0
Group: Development/Perl
URL: %CPAN %module_name
# Source-url: https://cpan.metacpan.org/authors/id/B/BP/BPS/%module_name-%version.tar.gz
Source: %name-%version.tar

# Uses system libgumbo via pkg-config (patched Build.PL).
Patch: %name-use-system-libgumbo.patch

BuildRequires(pre): rpm-build-perl
BuildRequires: perl-devel perl-Module-Build
BuildRequires: libgumbo-devel

%description
HTML::Gumbo is an HTML5 parser based on the gumbo C library
(https://github.com/google/gumbo-parser). It is a Perl XS wrapper around
the pure C99 conformant HTML5 parsing algorithm implementation.

%prep
%setup -q -n %module_name-%version
%patch -p1

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes LICENSE
%perl_vendor_archlib/HTML/Gumbo.pm
%perl_vendor_autolib/HTML/Gumbo/

%changelog
* Thu Jul 16 2026 Vitaly Lipatov <lav@altlinux.ru> 0.20-alt1
- initial build for ALT Sisyphus

