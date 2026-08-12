%define real_name Test2-Tools-URL

Name: perl-%real_name
Version: 0.07
Release: alt1

Summary: Tools for comparing URL strings in Test2

License: %perl_license
Group: Development/Perl

URL: https://metacpan.org/release/%real_name

# Source-url: https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/%real_name-%version.tar.gz
Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-perl rpm-build-licenses
BuildRequires: perl-devel perl-Test2-Suite perl-URI

%description
Test2::Tools::URL provides Test2 comparison tools for testing URL strings,
building on Test2::Compare and URI.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes LICENSE
%perl_vendor_privlib/Test2/Tools/URL.pm

%changelog
* Mon Jul 27 2026 Vitaly Lipatov <lav@altlinux.ru> 0.07-alt1
- initial build for Sisyphus
