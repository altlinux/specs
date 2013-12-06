Name: perl-Devel-CallChecker
Version: 0.006
Release: alt1

Summary: custom op checking attached to subroutines
Group: Development/Perl
License: perl

Url: %CPAN Devel-CallChecker
Source: %name-%version.tar

BuildRequires: perl(parent.pm) perl-devel perl(DynaLoader/Functions.pm) perl(Module/Build.pm) perl(ExtUtils/CBuilder.pm)

%description
%summary

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_autolib/Devel/CallChecker*
%perl_vendor_archlib/Devel/CallChecker*
%doc Changes README

%changelog
* Fri Dec 06 2013 Vladimir Lettiev <crux@altlinux.ru> 0.006-alt1
- initial build for ALTLinux

