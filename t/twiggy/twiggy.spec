Name: twiggy
Version: 0.1010
Release: alt1
Summary: Twiggy - AnyEvent HTTP server for PSGI (like Thin)

Group: Development/Perl
License: Perl
Url: %CPAN Twiggy

BuildArch: noarch
Source: %name-%version.tar
BuildRequires: perl-Test-TCP perl-devel perl-Plack perl-Try-Tiny perl-Test-Requires perl-AnyEvent perl-HTTP-Message perl-Module-Install-AuthorTests perl-Module-Install-ReadmeFromPod perl-Module-Install-Repository perl-Server-Starter

%description
%summary

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%_bindir/%name
%perl_vendor_privlib/Twiggy*
%perl_vendor_privlib/Plack/Handler/Twiggy.pm
%perl_vendor_privlib/AnyEvent/Server/PSGI.pm
%doc Changes README 

%changelog
* Sat Jul 30 2011 Vladimir Lettiev <crux@altlinux.ru> 0.1010-alt1
- initial build
