Name: perl-Plack-Middleware-ETag
Version: 0.03
Release: alt1

Summary: Adds automatically an ETag header
Group: Development/Perl
License: perl

Url: %CPAN Plack-Middleware-ETag
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildArch: noarch
BuildRequires: perl-parent perl-devel perl-Plack perl-HTTP-Message perl-Digest-SHA

%description
%summary

%prep
%setup -q
%patch -p1

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Plack/Middleware/ETag*
%doc Changes README

%changelog
* Mon Nov 26 2012 Vladimir Lettiev <crux@altlinux.ru> 0.03-alt1
- initial build for ALTLinux

