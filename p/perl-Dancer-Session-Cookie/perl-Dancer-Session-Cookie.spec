BuildRequires: perl(Module/Build.pm)
Name: perl-Dancer-Session-Cookie
Version: 0.25
Release: alt1

Summary: Encrypted cookie-based session backend for Dancer
Group: Development/Perl
License: perl

Url: %CPAN Dancer-Session-Cookie
Source: %name-%version.tar

BuildArch: noarch
BuildRequires: perl-Crypt-CBC perl-devel perl-Test-Exception perl-Dancer perl-String-CRC32 perl-Test-NoWarnings perl-Crypt-Rijndael perl-YAML perl(Session/Storage/Secure.pm) perl(Time/Duration/Parse.pm)

%description
%summary

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Dancer/Session/Cookie*
%doc Changes README

%changelog
* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 0.25-alt1
- automated CPAN update

* Tue Jun 24 2014 Igor Vlasenko <viy@altlinux.ru> 0.22-alt1
- automated CPAN update

* Mon Nov 26 2012 Vladimir Lettiev <crux@altlinux.ru> 0.15-alt1
- initial build for ALTLinux

