Name: perl-Stream-Buffered
Version: 0.02
Release: alt1

Summary: temporary buffer to save bytes
Group: Development/Perl
License: perl

Url: %CPAN Stream-Buffered
Source: %name-%version.tar

BuildArch: noarch
BuildRequires: perl-devel perl-Module-Install perl-Module-Install-ReadmeFromPod perl-Module-Install-Repository

%description
%summary

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Stream/Buffered*
%doc Changes README

%changelog
* Fri Dec 14 2012 Vladimir Lettiev <crux@altlinux.ru> 0.02-alt1
- initial build for ALTLinux

