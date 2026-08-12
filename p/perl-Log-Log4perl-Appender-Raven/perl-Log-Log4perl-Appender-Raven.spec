%define real_name Log-Log4perl-Appender-Raven

Name: perl-%real_name
Version: 0.006
Release: alt1

Summary: Send log events to a Sentry account from Log::Log4perl

License: %perl_license
Group: Development/Perl

URL: https://metacpan.org/release/%real_name
# Source-url: https://cpan.metacpan.org/authors/id/J/JE/JETEVE/%real_name-%version.tar.gz
Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-perl rpm-build-licenses
BuildRequires: perl-devel
# Runtime requires (also needed at build/test time, as the module loads them).
BuildRequires: perl-Devel-StackTrace
BuildRequires: perl-Log-Log4perl
BuildRequires: perl-Moose
BuildRequires: perl-Scope-Guard
BuildRequires: perl-Sentry-Raven
BuildRequires: perl-Text-Template
# Test requirements.
BuildRequires: perl-Log-Any
BuildRequires: perl-Log-Any-Adapter-Log4perl
BuildRequires: perl-Test-Fatal

%description
Log::Log4perl::Appender::Raven is a Log::Log4perl appender that sends log
events to a Sentry (https://sentry.io) account using the Sentry::Raven
module. It supports stack traces, user and HTTP request context, and
templating of event messages.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README.md
%perl_vendor_privlib/Log/Log4perl/Appender/Raven*

%changelog
* Mon Jul 27 2026 Vitaly Lipatov <lav@altlinux.ru> 0.006-alt1
- initial build for Sisyphus

