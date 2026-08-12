%define real_name Auth-GoogleAuth

Name: perl-%real_name
Version: 1.10
Release: alt1

Summary: Google Authenticator (TOTP/HOTP) abstraction

License: Artistic-2.0
Group: Development/Perl

URL: https://metacpan.org/release/%real_name
# Source-url: https://cpan.metacpan.org/authors/id/G/GR/GRYPHON/%real_name-%version.tar.gz
Source: %real_name-%version.tar
Patch0: %real_name-%version-alt-optional-deps.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-perl rpm-build-licenses
BuildRequires: perl-devel perl-Convert-Base32 perl-Class-Accessor perl-CryptX perl-Digest-HMAC perl-URI perl-Test2-Suite

# Crypt::PRNG (perl-CryptX) and URI::Escape (perl-URI) are loaded on demand by
# Patch0, so they are optional features -- drop their auto-generated runtime
# Requires. They stay as BuildRequires because the test suite exercises them.
%filter_from_requires /Crypt\/PRNG/d
%filter_from_requires /URI\/Escape/d

%description
Auth::GoogleAuth is a Google Authenticator (two-factor authentication) module
that generates TOTP and HOTP codes compatible with the Google Authenticator
app and compatible RFC 6238 / RFC 4226 clients.

%prep
%setup -q -n %real_name-%version
%patch0 -p1

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes
%perl_vendor_privlib/Auth*

%changelog
* Mon Jul 27 2026 Vitaly Lipatov <lav@altlinux.ru> 1.10-alt1
- initial build for Sisyphus
