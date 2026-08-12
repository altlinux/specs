%define real_name Net-OAuth2-AuthorizationServer

Name: perl-%real_name
Version: 0.28
Release: alt1

Summary: Easier implementation of an OAuth2 Authorization Server

License: %perl_license
Group: Development/Perl

URL: https://metacpan.org/release/%real_name
# Source-url: https://cpan.metacpan.org/authors/id/L/LE/LEEJO/%real_name-%version.tar.gz
Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-perl rpm-build-licenses
BuildRequires: perl-devel perl-Moo perl-Type-Tiny perl-CryptX perl-Crypt-JWT
BuildRequires: perl-Try-Tiny perl-Test-Most perl-Test-Exception

%description
Easier implementation of an OAuth2 Authorization Server / Resource Server with
Mojolicious. Provides grants for authorization_code, implicit, password, and
client_credentials flows.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes
%perl_vendor_privlib/Net/OAuth2/AuthorizationServer*

%changelog
* Mon Jul 27 2026 Vitaly Lipatov <lav@altlinux.ru> 0.28-alt1
- initial build for Sisyphus
