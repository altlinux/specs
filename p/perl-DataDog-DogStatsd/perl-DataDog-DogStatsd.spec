%define real_name DataDog-DogStatsd

Name: perl-%real_name
Version: 0.07
Release: alt1

Summary: A Perl client for DogStatsd

License: %perl_license
Group: Development/Perl

URL: https://metacpan.org/release/%real_name
# Source-url: https://cpan.metacpan.org/authors/id/B/BI/BINARY/%real_name-%version.tar.gz
Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-perl rpm-build-licenses
BuildRequires: perl-devel

%description
DataDog::DogStatsd is a Perl client for DogStatsd, a metrics aggregation
service provided by Datadog.

%prep
%setup -q -n %real_name-%version
# t/00-check-deps.t is a meta-test that just re-checks prerequisites via
# Test::CheckDeps (a test-infra module, not a runtime dep). RPM BuildRequires
# already enforce prereqs; drop the redundant meta-test.
rm -v t/00-check-deps.t

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes
%perl_vendor_privlib/DataDog*

%changelog
* Mon Jul 27 2026 Vitaly Lipatov <lav@altlinux.ru> 0.07-alt1
- initial build for Sisyphus
