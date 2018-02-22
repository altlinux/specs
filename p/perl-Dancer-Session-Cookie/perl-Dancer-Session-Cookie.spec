BuildRequires: perl(Module/Build.pm)
Name: perl-Dancer-Session-Cookie
Version: 0.29
Release: alt1

Summary: Encrypted cookie-based session backend for Dancer
Group: Development/Perl
License: perl

Url: %CPAN Dancer-Session-Cookie
Source: %name-%version.tar

BuildArch: noarch
BuildRequires: perl-Crypt-CBC perl-devel perl-Test-Exception perl-Dancer perl-String-CRC32 perl-Test-NoWarnings perl-Crypt-Rijndael perl-YAML perl(Session/Storage/Secure.pm) perl(Time/Duration/Parse.pm) perl(Plack/Test.pm) perl(Test/Requires.pm)

%description
%summary

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README.mkdn LICENSE CONTRIBUTORS
%perl_vendor_privlib/Dancer/Session/Cookie*
%doc Changes README*

%changelog
* Thu Feb 22 2018 Igor Vlasenko <viy@altlinux.ru> 0.29-alt1
- automated CPAN update

* Thu Oct 15 2015 Igor Vlasenko <viy@altlinux.ru> 0.27-alt1
- automated CPAN update

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 0.25-alt1
- automated CPAN update

* Tue Jun 24 2014 Igor Vlasenko <viy@altlinux.ru> 0.22-alt1
- automated CPAN update

* Mon Nov 26 2012 Vladimir Lettiev <crux@altlinux.ru> 0.15-alt1
- initial build for ALTLinux

