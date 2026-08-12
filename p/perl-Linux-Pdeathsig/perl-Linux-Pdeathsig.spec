%define real_name Linux-Pdeathsig

Name: perl-%real_name
Version: 0.10
Release: alt1

Summary: Perl interface to request a signal on parent death

License: %perl_license
Group: Development/Perl

URL: https://metacpan.org/release/%real_name
# Source-url: https://cpan.metacpan.org/authors/id/Z/ZE/ZEROHP/%real_name-%version.tar.gz
Source: %real_name-%version.tar

BuildRequires(pre): rpm-build-perl rpm-build-licenses
BuildRequires: perl-devel

%description
Linux::Pdeathsig provides an interface to the PR_SET_PDEATHSIG flag of
the prctl(2) system call, allowing a process to request a signal on
parent death.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes
%perl_vendor_archlib/Linux/Pdeathsig*
%perl_vendor_archlib/auto/Linux/Pdeathsig

%changelog
* Mon Jul 27 2026 Vitaly Lipatov <lav@altlinux.ru> 0.10-alt1
- initial build for Sisyphus

