%define module_version 0.1.1
%define module_name Authen-ModAuthPubTkt
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators perl-base perl-IPC-Run3 perl-Test-Pod perl-Test-Pod-Coverage openssl

Name: perl-%module_name
Version: %module_version
Release: alt1
Summary: Generate Tickets (Signed HTTP Cookies) for mod_auth_pubtkt protected websites
Group: Development/Perl
License: Perl
Url: %CPAN %module_name

Source0: https://cpan.metacpan.org/authors/id/A/AG/AGORDON/%module_name-%module_version.tar.gz
BuildArch: noarch

%description
%summary.

%prep
%setup -n %module_name-%module_version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/A*
%_bindir/mod_auth_pubtkt.pl

%changelog
* Mon May 23 2022 Andrew A. Vasilyev <andy@altlinux.org> 0.1.1-alt1
- initial build for ALT


