%define real_name Mojolicious-Plugin-OAuth2-Server

Name: perl-%real_name
Version: 0.52
Release: alt1

Summary: Easier implementation of an OAuth2 Authorization Server / Resource Server with Mojolicious

License: %perl_license
Group: Development/Perl

URL: https://metacpan.org/release/%real_name
# Source-url: https://cpan.metacpan.org/authors/id/L/LE/LEEJO/%real_name-%version.tar.gz
Source: %real_name-%version.tar

Patch0: %name-%version-alt-hmac-min-key.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-perl rpm-build-licenses
BuildRequires: perl-devel perl-Mojolicious perl-Net-OAuth2-AuthorizationServer
BuildRequires: perl-Mojo-JWT perl-Test-Deep perl-Test-Exception

%description
A Mojolicious plugin that implements an OAuth2 Authorization Server and
Resource Server. Wraps Net::OAuth2::AuthorizationServer to expose authorization
code, implicit, password, and client_credentials grant flows through
Mojolicious routes, with hooks for JWT support, custom login flows, and
configurable token TTLs.

%prep
%setup -q -n %real_name-%version
%patch0 -p1

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes
%perl_vendor_privlib/Mojolicious/Plugin/OAuth2*

%changelog
* Mon Jul 27 2026 Vitaly Lipatov <lav@altlinux.ru> 0.52-alt1
- initial build for Sisyphus
