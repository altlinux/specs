%define real_name MojoX-Log-Log4perl

Name: perl-%real_name
Version: 0.12
Release: alt1

Summary: Log::Log4perl logging for Mojo/Mojolicious

License: %perl_license
Group: Development/Perl

URL: https://metacpan.org/release/%real_name

# Source-url: https://cpan.metacpan.org/authors/id/G/GA/GARU/%real_name-%version.tar.gz
Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-perl rpm-build-licenses
BuildRequires: perl-devel perl-Mojolicious perl-Log-Log4perl

%description
MojoX::Log::Log4perl provides Log::Log4perl logging for Mojo/Mojolicious
applications.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes
%perl_vendor_privlib/MojoX*

%changelog
* Sun Jul 26 2026 Vitaly Lipatov <lav@altlinux.ru> 0.12-alt1
- initial build for Sisyphus
