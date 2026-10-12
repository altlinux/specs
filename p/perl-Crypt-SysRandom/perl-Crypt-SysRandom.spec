%define _unpackaged_files_terminate_build 1
%define dist Crypt-SysRandom
Name: perl-%dist
Version: 0.007
Release: alt1

Summary: Perl interface to system randomness

License: %perl_license
Group: Development/Perl
Url: %CPAN %dist

# Source-url: http://www.cpan.org/authors/id/L/LE/LEONT/%dist-%version.tar.gz
Source: %dist-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-perl rpm-build-licenses
BuildRequires: perl-devel perl(Test/More.pm)

%description
This module uses whatever interface is available to procure
cryptographically random data from the system.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Crypt/SysRandom.pm

%changelog
* Mon Oct 12 2026 Vitaly Lipatov <lav@altlinux.ru> 0.007-alt1
- initial build for Sisyphus
