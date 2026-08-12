%define real_name Alien-Build-Git

Name: perl-%real_name
Version: 0.10
Release: alt1

Summary: Alien::Build tools for interacting with git

License: %perl_license
Group: Development/Perl

URL: https://metacpan.org/release/%real_name

# Source-url: https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/%real_name-%version.tar.gz
Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-perl rpm-build-licenses
BuildRequires: perl-devel perl-Alien-Build
BuildRequires: perl-File-Which perl-Capture-Tiny
BuildRequires: perl-PerlX-Maybe perl-Path-Tiny perl-File-chdir
BuildRequires: perl-URI perl-URI-git
BuildRequires: perl-Test2-Tools-URL
BuildRequires: git

%description
Alien::Build::Git provides Alien::Build plugins (Download::Git and Fetch::Git)
and the Alien::git helper for interacting with git in alienfiles. These were
split out of the core Alien-Build distribution.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes
%perl_vendor_privlib/Alien/Build/Git.pm
%perl_vendor_privlib/Alien/Build/Plugin/Download/Git.pm
%perl_vendor_privlib/Alien/Build/Plugin/Fetch/Git.pm
%perl_vendor_privlib/Alien/git.pm

%changelog
* Mon Jul 27 2026 Vitaly Lipatov <lav@altlinux.ru> 0.10-alt1
- initial build for Sisyphus
