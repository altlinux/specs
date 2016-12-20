Name: perl-Config-Identity
Version: 0.0019
Release: alt1

Summary: Load (and optionally decrypt via GnuPG) user/pass identity information 
Group: Development/Perl
License: perl

Url: %CPAN Config-Identity
Source: %name-%version.tar

BuildArch: noarch
BuildRequires: perl(File/HomeDir.pm) perl(IPC/Run.pm) perl-devel perl(Test/Most.pm) perl(File/Which.pm)

%description
%summary

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Config/Identity*
%doc Changes README

%changelog
* Tue Dec 20 2016 Igor Vlasenko <viy@altlinux.ru> 0.0019-alt1
- automated CPAN update

* Mon May 12 2014 Vladimir Lettiev <crux@altlinux.ru> 0.0018-alt1
- initial build for ALTLinux

