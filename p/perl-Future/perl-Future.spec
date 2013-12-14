Name: perl-Future
Version: 0.20
Release: alt1

Summary: represent an operation awaiting completion
Group: Development/Perl
License: perl

Url: %CPAN Future
Source: %name-%version.tar

BuildArch: noarch
BuildRequires: perl-devel perl(Module/Build.pm) perl(Test/Refcount.pm) perl(Test/Fatal.pm) perl(Test/Identity.pm)

%description
%summary

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Future*
%doc Changes LICENSE README

%changelog
* Sat Dec 14 2013 Vladimir Lettiev <crux@altlinux.ru> 0.20-alt1
- initial build for ALTLinux

