%define real_name URI-git

Name: perl-%real_name
Version: 0.02
Release: alt1

Summary: git URI scheme

License: %perl_license
Group: Development/Perl

URL: https://metacpan.org/release/%real_name

# Source-url: https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/%real_name-%version.tar.gz
Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-perl rpm-build-licenses
BuildRequires: perl-devel perl-URI

%description
URI::git adds support for the git:// and git+ssh:// URI schemes to the URI
class hierarchy. It is used by Alien::Build::Plugin::Fetch::Git.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes
%perl_vendor_privlib/URI/git.pm

%changelog
* Mon Jul 27 2026 Vitaly Lipatov <lav@altlinux.ru> 0.02-alt1
- initial build for Sisyphus
