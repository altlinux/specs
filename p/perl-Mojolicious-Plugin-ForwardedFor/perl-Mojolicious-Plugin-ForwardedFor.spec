%define real_name Mojolicious-Plugin-ForwardedFor

Name: perl-%real_name
Version: 0.002
Release: alt1

Summary: Retrieve the remote address from X-Forwarded-For

License: Artistic-2.0
Group: Development/Perl

URL: https://metacpan.org/release/%real_name
# Source-url: https://cpan.metacpan.org/authors/id/D/DB/DBOOK/%real_name-%version.tar.gz
Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-perl rpm-build-licenses
BuildRequires: perl-devel perl-Mojolicious perl-Module-Build-Tiny

%description
Mojolicious::Plugin::ForwardedFor retrieves the remote address of a client
from the X-Forwarded-For header, useful when running behind a reverse proxy.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes
%perl_vendor_privlib/Mojolicious/Plugin/ForwardedFor*

%changelog
* Mon Jul 27 2026 Vitaly Lipatov <lav@altlinux.ru> 0.002-alt1
- initial build for Sisyphus
