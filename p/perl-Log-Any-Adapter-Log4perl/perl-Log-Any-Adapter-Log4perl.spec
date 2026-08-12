%define real_name Log-Any-Adapter-Log4perl

Name: perl-%real_name
Version: 0.09
Release: alt1

Summary: Log::Any adapter for Log::Log4perl

License: %perl_license
Group: Development/Perl

URL: https://metacpan.org/release/%real_name
# Source-url: https://cpan.metacpan.org/authors/id/P/PR/PREACTION/%real_name-%version.tar.gz
Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-perl rpm-build-licenses
BuildRequires: perl-devel
# Runtime requires (also needed at build/test time, as the module loads them).
BuildRequires: perl-Log-Any
BuildRequires: perl-Log-Log4perl

%description
Log::Any::Adapter::Log4perl forwards Log::Any log messages to Log::Log4perl,
letting applications that use Log::Any route their log output through the
Log::Log4perl logging framework (appenders, layouts, thresholds, etc.).

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes
%perl_vendor_privlib/Log/Any/Adapter/Log4perl*

%changelog
* Mon Jul 27 2026 Vitaly Lipatov <lav@altlinux.ru> 0.09-alt1
- initial build for Sisyphus
