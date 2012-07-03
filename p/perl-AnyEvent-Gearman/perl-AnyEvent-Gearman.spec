Name: perl-AnyEvent-Gearman
Version: 0.09
Release: alt1
Summary: AnyEvent::Gearman - Asynchronous Gearman client/worker module for AnyEvent applications

Group: Development/Perl
License: Perl
Url: %CPAN AnyEvent-Gearman

BuildArch: noarch
Source: %name-%version.tar
BuildRequires: perl-devel perl-Module-Install perl-Module-Install-AuthorTests perl-Module-Install-Repository perl-Test-Base perl-Test-Deep perl-Any-Moose perl-Object-Container perl-AnyEvent perl-Object-Event perl-Test-TCP perl-Test-Exception perl-Mouse perl-MouseX-Foreign perl-Moose

%description
%summary

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/AnyEvent/Gearman*
%doc LICENSE Changes README 

%changelog
* Fri Aug 12 2011 Vladimir Lettiev <crux@altlinux.ru> 0.09-alt1
- initial build
