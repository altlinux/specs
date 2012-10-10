Name: perl-Devel-PatchPerl
Version: 0.76
Release: alt1

Summary: Patch perl source a la Devel::PPPort's buildperl.pl
Group: Development/Perl
License: perl

Url: %CPAN Devel-PatchPerl
Source: %name-%version.tar

BuildArch: noarch
BuildRequires: perl-Module-Pluggable perl-File-pushd perl-devel perl-IPC-Cmd

%description
%summary

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Devel/PatchPerl*
%doc Changes LICENSE README

%changelog
* Wed Oct 10 2012 Vladimir Lettiev <crux@altlinux.ru> 0.76-alt1
- initial build for ALTLinux

