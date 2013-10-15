Name: perl-Text-TestBase
Version: 0.12
Release: alt1

Summary: Parser for Test::Base format
Group: Development/Perl
License: perl

Url: %CPAN Text-TestBase
Source: %name-%version.tar

BuildArch: noarch
BuildRequires: perl(Test/Requires.pm) perl(parent.pm) perl(Class/Accessor/Lite.pm) perl-devel perl(CPAN/Meta.pm) perl(Module/Build.pm) perl(CPAN/Meta/Prereqs.pm)

%description
%summary

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Text/TestBase*
%perl_vendor_privlib/Data/Section/TestBase.pm
%perl_vendor_privlib/Test/Base/Less.pm
%doc Changes LICENSE README.md

%changelog
* Tue Oct 15 2013 Vladimir Lettiev <crux@altlinux.ru> 0.12-alt1
- initial build for ALTLinux

