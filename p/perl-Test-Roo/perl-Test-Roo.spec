%define real_name Test-Roo

Name: perl-%real_name
Version: 1.004
Release: alt1

Summary: Composable, reusable tests with roles and Moo

License: Apache-2.0
Group: Development/Perl

URL: https://metacpan.org/release/%real_name

# Source-url: https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/%real_name-%version.tar.gz
Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-perl rpm-build-licenses
BuildRequires: perl-devel perl-Moo perl-MooX-Types-MooseLike perl-Sub-Install perl-strictures perl-Capture-Tiny perl-Math-BigInt

%description
Test::Roo provides composable, reusable tests with roles and Moo.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes
%perl_vendor_privlib/Test*

%changelog
* Sun Jul 26 2026 Vitaly Lipatov <lav@altlinux.ru> 1.004-alt1
- initial build for Sisyphus
