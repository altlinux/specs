Name: perl-B-Flags
Version: 0.06
Release: alt1

Summary: B::Flags - Friendlier flags for B
License: Perl
Group: Development/Perl

URL: %CPAN B-Flags
# Cloned from git git://github.com/rurban/b-flags.git
Source: %name-%version.tar

BuildRequires: perl-devel

%description
%summary

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes
%perl_vendor_archlib/B/Flags.pm
%perl_vendor_autolib/B/Flags

%changelog
* Mon Apr 09 2012 Vladimir Lettiev <crux@altlinux.ru> 0.06-alt1
- Initial release for ALTLinux Sisyphus

