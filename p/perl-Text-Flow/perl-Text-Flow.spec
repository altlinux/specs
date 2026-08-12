%define real_name Text-Flow

Name: perl-%real_name
Version: 0.01
Release: alt1

Summary: Flexible text flowing and word wrapping for not just ASCII output

License: %perl_license
Group: Development/Perl

URL: https://metacpan.org/release/%real_name
# Source-url: https://cpan.metacpan.org/authors/id/S/ST/STEVAN/%real_name-%version.tar.gz
Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-perl rpm-build-licenses
BuildRequires: perl-devel perl-Moose perl-Module-Build perl-Test-Exception perl-Test-LongString

%description
Text::Flow provides flexible text flowing and word wrapping that handles
non-ASCII output correctly. It is used by layout/rendering code that needs
to wrap text while respecting character widths beyond simple byte counts.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes
%perl_vendor_privlib/Text/Flow*

%changelog
* Tue Jul 28 2026 Vitaly Lipatov <lav@altlinux.ru> 0.01-alt1
- initial build for Sisyphus
