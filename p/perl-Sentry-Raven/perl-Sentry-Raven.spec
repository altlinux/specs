%define real_name Sentry-Raven

Name: perl-%real_name
Version: 1.14
Release: alt1

Summary: A perl sentry client

License: MIT
Group: Development/Perl

URL: https://metacpan.org/release/%real_name
# Source-url: https://cpan.metacpan.org/authors/id/Q/QR/QRRY/%real_name-%version.tar.gz
Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-perl rpm-build-licenses
BuildRequires: perl-devel
# Runtime requires (also needed at build/test time, as the module loads them).
BuildRequires: perl-Data-Dump
BuildRequires: perl-Devel-StackTrace
BuildRequires: perl-File-Slurp
BuildRequires: perl-HTTP-Message
BuildRequires: perl-JSON-XS
BuildRequires: perl-LWP-Protocol-https
BuildRequires: perl-libwww
BuildRequires: perl-Moo
BuildRequires: perl-MooX-Types-MooseLike
BuildRequires: perl-URI
BuildRequires: perl-UUID-Tiny
# Test requirements.
BuildRequires: perl-Test-LWP-UserAgent
BuildRequires: perl-Test-Warn

%description
Sentry::Raven is a Perl client for Sentry (https://sentry.io). It supports
sending events with stack traces, user and HTTP request context, breadcrumbs,
tagging, and structured logging of exceptions.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Sentry*

%changelog
* Mon Jul 27 2026 Vitaly Lipatov <lav@altlinux.ru> 1.14-alt1
- initial build for Sisyphus
