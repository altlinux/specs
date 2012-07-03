Name: perl-Debug-Client
Version: 0.20
Release: alt1
Summary: Debug::Client - client for the standard perl debugger

Group: Development/Perl
License: Perl
Url: %CPAN Debug-Client

BuildArch: noarch
Source: %name-%version.tar
BuildRequires: perl-devel perl-pod perl-Test-Deep perl-Term-ReadLine-Gnu perl-File-HomeDir perl-PadWalker perl-Test-Class

%description
%summary

%prep
%setup -q
# fixing test failure
sed -i 's/Term::ReadLine::Perl/Term::ReadLine::Gnu/' t/01-Debug-Client.t

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Debug/Client*
%doc Changes

%changelog
* Tue Apr 10 2012 Vladimir Lettiev <crux@altlinux.ru> 0.20-alt1
- New version 0.20

* Tue Dec 06 2011 Vladimir Lettiev <crux@altlinux.ru> 0.16-alt1
- New version 0.16

* Fri Jan 29 2010 Vladimir Lettiev <crux@altlinux.ru> 0.11-alt1
- initial build
