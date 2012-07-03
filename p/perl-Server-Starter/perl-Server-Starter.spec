Name: perl-Server-Starter
Version: 0.11
Release: alt1
Summary: Server::Starter - a superdaemon for hot-deploying server programs

Group: Development/Perl
License: Perl
Url: %CPAN Server-Starter

BuildArch: noarch
Source: %name-%version.tar
BuildRequires: perl-Test-TCP perl-Proc-Wait3 perl-Scope-Guard perl-List-MoreUtils perl-Module-Install

%description
%summary

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%_bindir/start_server
%perl_vendor_privlib/Server/Starter*
%doc Changes README 

%changelog
* Sat Jul 30 2011 Vladimir Lettiev <crux@altlinux.ru> 0.11-alt1
- initial build
